import mysql
import mysql.connector
from db_connection import get_connection

def eseguiQuerySELECT(query):
    try:
        myconn = get_connection()
        cursor = myconn.cursor()
        cursor.execute(query)
        risultato = cursor.fetchall()
        return risultato
    except mysql.connector.Error as err:
        print(f"Errore durante l'esecuzione della query: {err}")
        return []
    finally:
        myconn.close()

def ottieniElementiTabellaProdottiMenu():
    try:
        myconn = get_connection()
        cursor = myconn.cursor()
        query = "Select id, nome, descrizione, prezzo, categoria from prodottomenu WHERE eliminato = 0"
        cursor.execute(query)
        elementiMagazzino = cursor.fetchall()
        return elementiMagazzino
    except mysql.connector.Error as err:
        print(f"Errore durante l'ottenimento delle informazioni: {err}")
        return[]
    finally:
        myconn.close()

def ottieniProdottoSpecifico(id):
    query = f"select id, nome, descrizione, categoria, prezzo from prodottomenu WHERE id = '{id}'"
    return eseguiQuerySELECT(query)

def ottieniIngredientiProdotto(id):
    query = f"select nomeelemento.nome, ingredienteprodotto.Quantita, nomeelemento.piccante, nomeelemento.vegano, nomeelemento.intolleranze FROM ingredienteprodotto INNER JOIN nomeelemento ON nomeelemento.id = ingredienteprodotto.idNomeElemento WHERE ingredienteprodotto.idProdotto = {id}"
    return eseguiQuerySELECT(query)

def eseguiQuery(query): #eseguiQuery è per le query che fanno modifiche al database ma non restituiscono niente
    try:
        myconn = get_connection()
        cursor = myconn.cursor()
        cursor.execute(query)
        myconn.commit()
        return "corretto"
    except mysql.connector.Error as err:
        print(f"Errore durante l'esecuzione del comando: {err}")
        return err
    finally:
        myconn.close()