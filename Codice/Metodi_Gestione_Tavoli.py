import mysql.connector
from datetime import datetime, timedelta
from db_connection import get_connection



# Funzione per aggiornare lo stato del tavolo
def aggiorna_stato_tavolo(id_tavolo, nuovo_stato):
    try:
        # Connessione al database
        myconn = get_connection()
        cursor = myconn.cursor()
        query = "UPDATE tavolo SET stato = %s WHERE id = %s"
        cursor.execute(query, (nuovo_stato, id_tavolo))
        myconn.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Errore durante l'aggiornamento dello stato del tavolo {id_tavolo}: {err}")
    finally:
        # Chiudere la connessione al database
        myconn.close()


# Funzione per ottenere tutte le prenotazioni
def ottieni_prenotazioni():
    try:
        # Connessione al database
        myconn = get_connection()
        cursor = myconn.cursor(dictionary=True)
        query = "SELECT * FROM prenotazione"
        cursor.execute(query)
        prenotazioni = cursor.fetchall()
        cursor.close()
        return prenotazioni
    except mysql.connector.Error as err:
        print(f"Errore durante l'ottenimento delle prenotazioni: {err}")
        return []
    finally:
        # Chiudere la connessione al database
        myconn.close()


# Funzione per ottenere tutte le ordinazioni non completate
def ottieni_ordinazioni_non_completate():
    try:
        # Connessione al database
        myconn = get_connection()
        cursor = myconn.cursor(dictionary=True)
        query = "SELECT * FROM ordinazione WHERE completato = 0"
        cursor.execute(query)
        ordinazioni = cursor.fetchall()
        cursor.close()
        return ordinazioni
    except mysql.connector.Error as err:
        print(f"Errore durante l'ottenimento delle ordinazioni non completate: {err}")
        return []
    finally:
        # Chiudere la connessione al database
        myconn.close()


# Funzione per aggiornare lo stato dei tavoli
def aggiorna_stato_tavoli():
    prenotazioni = ottieni_prenotazioni()
    ordinazioni_non_completate = ottieni_ordinazioni_non_completate()

    ora_attuale = datetime.now()
    intervallo_2_ore = timedelta(hours=2)

    tavoli_con_prenotazioni = set()
    tavoli_con_ordinazioni_non_completate = set()

    # Controlla le prenotazioni
    for prenotazione in prenotazioni:
        if 'DataEOraPrenotazione' in prenotazione and 'idTavolo' in prenotazione:
            data_prenotazione = prenotazione['DataEOraPrenotazione']
            id_tavolo = prenotazione['idTavolo']

            if ora_attuale <= data_prenotazione < ora_attuale + intervallo_2_ore:
                aggiorna_stato_tavolo(id_tavolo, 'prenotato')
                tavoli_con_prenotazioni.add(id_tavolo)
        else:
            print(f"Errore: Chiave mancante nella prenotazione: {prenotazione}")

    # Controlla le ordinazioni non completate
    for ordinazione in ordinazioni_non_completate:
        if 'idTavolo' in ordinazione:
            id_tavolo = ordinazione['idTavolo']
            aggiorna_stato_tavolo(id_tavolo, 'occupato')
            tavoli_con_ordinazioni_non_completate.add(id_tavolo)
        else:
            print(f"Errore: Chiave mancante nell'ordinazione: {ordinazione}")

    # Imposta i tavoli a "libero" se non ci sono prenotazioni entro 2 ore e non ci sono ordinazioni non completate
    try:
        # Connessione al database
        myconn = get_connection()
        cursor = myconn.cursor(dictionary=True)
        query_tavoli = "SELECT id FROM tavolo"
        cursor.execute(query_tavoli)
        tavoli = cursor.fetchall()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Errore durante l'ottenimento dei tavoli: {err}")
        return
    finally:
        # Chiudere la connessione al database
        myconn.close()

    for tavolo in tavoli:
        id_tavolo = tavolo['id']
        if id_tavolo not in tavoli_con_prenotazioni and id_tavolo not in tavoli_con_ordinazioni_non_completate:
            aggiorna_stato_tavolo(id_tavolo, 'libero')


