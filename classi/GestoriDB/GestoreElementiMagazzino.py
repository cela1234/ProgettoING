import mysql
import mysql.connector
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "alessio"
DB_DATABASE = "mydbristorante"
DB_PORT = 3360
def ottieniElementiTabellaMagazzino():
    try:
        myconn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            passwd = DB_PASSWORD,
            database = DB_DATABASE,
            port = DB_PORT
        )
        cursor = myconn.cursor()
        query = """select elementomagazzino.id, nome, prezzo, quantita, scadenza, fornitore
        from elementomagazzino inner join nomeelemento
        on elementomagazzino.idNomeElemento = nomeelemento.id"""
        cursor.execute(query)
        elementiMagazzino = cursor.fetchall()
        return elementiMagazzino
    except mysql.connector.Error as err:
        print(f"Errore durante l'ottenimento delle informazioni: {err}")
        return[]
    finally:
        myconn.close()

def eseguiQuery(query): #eseguiQuery è per le query che fanno modifiche al database ma non restituiscono niente
    try:
        myconn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            passwd = DB_PASSWORD,
            database = DB_DATABASE,
            port = DB_PORT
        )
        cursor = myconn.cursor()
        cursor.execute(query)
        myconn.commit()
        return "corretto"
    except mysql.connector.Error as err:
        print(f"Errore durante l'esecuzione del comando: {err}")
        return err
    finally:
        myconn.close()

def eseguiQuerySELECT(query):
    try:
        myconn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            passwd=DB_PASSWORD,
            database=DB_DATABASE,
            port=DB_PORT
        )
        cursor = myconn.cursor()
        cursor.execute(query)
        risultato = cursor.fetchall()
        return risultato
    except mysql.connector.Error as err:
        print(f"Errore durante l'esecuzione della query: {err}")
        return []
    finally:
        myconn.close()
def ottieniNomiElementiCUelementoMagazzino():  #metodo ridondante ma lo faccio perchè rimane più chiaro
    query = "SELECT id, nome FROM nomeelemento"
    result = eseguiQuerySELECT(query)
    return result

def ottieniNomiElementiGestioneNomi():
    query = "SELECT id, nome, vegano, piccante, intolleranze from nomeelemento"
    result = eseguiQuerySELECT(query)
    return result

