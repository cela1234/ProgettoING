import unittest
from unittest.mock import patch, MagicMock
from Metodi_Gestione_Tavoli import aggiorna_stato_tavolo, ottieni_prenotazioni, ottieni_ordinazioni_non_completate, aggiorna_stato_tavoli
from datetime import datetime, timedelta

class TestMetodiGestioneTavoli(unittest.TestCase):

    @patch('mysql.connector.connect')
    def test_aggiorna_stato_tavolo(self, mock_connect):
        mock_db = MagicMock()
        mock_connect.return_value = mock_db

        # Chiama la funzione
        aggiorna_stato_tavolo(1, 'libero')

        # Verifica che la query SQL sia stata chiamata correttamente
        mock_cursor = mock_db.cursor.return_value
        mock_cursor.execute.assert_called_with("UPDATE tavolo SET stato = %s WHERE id = %s", ('libero', 1))
        mock_db.commit.assert_called()

    @patch('mysql.connector.connect')
    def test_ottieni_prenotazioni(self, mock_connect):
        mock_db = MagicMock()
        mock_connect.return_value = mock_db
        mock_cursor = mock_db.cursor.return_value
        # Simula un risultato di fetchall come lista di tuple con tutte le colonne
        mock_cursor.fetchall.return_value = [
            (1, 1, 'Rossi', 4, datetime.now())
            # Tupla con id, idTavolo, Nome, NumeroPersone, DataEOraPrenotazione
        ]

        result = ottieni_prenotazioni()
        self.assertEqual(len(result), 1)
        # Verifica che la prima tupla contenga l'idTavolo corretto
        self.assertEqual(result[0][1], 1)  # Verifica che il secondo elemento della tupla sia l'idTavolo
        self.assertEqual(result[0][2], 'Rossi')  # Verifica che il terzo elemento sia il nome


    @patch('mysql.connector.connect')
    @patch('Metodi_Gestione_Tavoli.ottieni_prenotazioni')
    @patch('Metodi_Gestione_Tavoli.ottieni_ordinazioni_non_completate')
    @patch('Metodi_Gestione_Tavoli.aggiorna_stato_tavolo')
    def test_aggiorna_stato_tavoli(self, mock_aggiorna_stato_tavolo, mock_ottieni_ordinazioni, mock_ottieni_prenotazioni, mock_connect):
        # Simula l'ora attuale
        ora_attuale = datetime.now()

        # Mock delle prenotazioni (una prenotazione entro 2 ore, una fuori)
        mock_ottieni_prenotazioni.return_value = [
            {"idTavolo": 1, "DataEOraPrenotazione": ora_attuale + timedelta(hours=1)},  # Prenotazione valida
            {"idTavolo": 2, "DataEOraPrenotazione": ora_attuale + timedelta(hours=3)}  # Prenotazione fuori intervallo
        ]

        # Mock delle ordinazioni non completate
        mock_ottieni_ordinazioni.return_value = [
            {"idTavolo": 3, "completato": 0}  # Ordinazione non completata
        ]

        # Simula i tavoli presenti nel database
        mock_db = MagicMock()
        mock_connect.return_value = mock_db
        mock_cursor = mock_db.cursor.return_value
        mock_cursor.fetchall.return_value = [
            {"id": 1},  # Tavolo con prenotazione valida
            {"id": 2},  # Tavolo con prenotazione fuori intervallo
            {"id": 3},  # Tavolo con ordinazione non completata
            {"id": 4}  # Tavolo libero
        ]

        aggiorna_stato_tavoli()

        # Verifica che il tavolo 1 sia stato aggiornato a "prenotato"
        mock_aggiorna_stato_tavolo.assert_any_call(1, 'prenotato')

        # Verifica che il tavolo 3 sia stato aggiornato a "occupato"
        mock_aggiorna_stato_tavolo.assert_any_call(3, 'occupato')

        # Verifica che il tavolo 4 sia stato aggiornato a "libero"
        mock_aggiorna_stato_tavolo.assert_any_call(4, 'libero')

        # Verifica che il tavolo 2 non sia stato aggiornato (prenotazione fuori intervallo)
        self.assertNotIn((2, 'prenotato'), mock_aggiorna_stato_tavolo.call_args_list)

    @patch('mysql.connector.connect')
    def test_ottieni_ordinazioni_non_completate(self, mock_connect):
        mock_db = MagicMock()
        mock_connect.return_value = mock_db
        mock_cursor = mock_db.cursor.return_value

        # Dati simulati: ordinazioni nel database (alcune completate, alcune no)
        ordinazioni_db = [
            {"id": 1, "idTavolo": 1, "completato": 0, "sequenzaCorrente": 2},  # Ordinazione non completata
            {"id": 3, "idTavolo": 3, "completato": 1, "sequenzaCorrente": 4},  # Ordinazione completata
            {"id": 4, "idTavolo": 4, "completato": 1, "sequenzaCorrente": 5},  # Ordinazione completata
            {"id": 2, "idTavolo": 2, "completato": 0, "sequenzaCorrente": 3},  # Ordinazione non completata
            {"id": 5, "idTavolo": 5, "completato": 1, "sequenzaCorrente": 6}  # Ordinazione completata
        ]

        # Funzione per simulare l'esecuzione della query
        def execute_query(query):
            if query == "SELECT * FROM ordinazione WHERE completato = 0":
                # Restituisci solo le ordinazioni non completate
                mock_cursor.fetchall.return_value = [
                    ordinazione for ordinazione in ordinazioni_db if ordinazione["completato"] == 0
                ]
            else:
                mock_cursor.fetchall.return_value = []

        # Mock della funzione execute per simulare la query
        mock_cursor.execute.side_effect = execute_query

        # Esegui il metodo da testare
        result = ottieni_ordinazioni_non_completate()

        # Verifica che il risultato contenga solo le ordinazioni non completate (2 ordinazioni)
        self.assertEqual(len(result), 2)

        # Verifica che i dati delle ordinazioni non completate siano corretti
        self.assertEqual(result[0]["id"], 1)  # Verifica l'id della prima ordinazione non completata
        self.assertEqual(result[0]["idTavolo"], 1)
        self.assertEqual(result[0]["completato"], 0)
        self.assertEqual(result[0]["sequenzaCorrente"], 2)

        self.assertEqual(result[1]["id"], 2)  # Verifica l'id della seconda ordinazione non completata
        self.assertEqual(result[1]["idTavolo"], 2)
        self.assertEqual(result[1]["completato"], 0)
        self.assertEqual(result[1]["sequenzaCorrente"], 3)

if __name__ == '__main__':
    unittest.main()