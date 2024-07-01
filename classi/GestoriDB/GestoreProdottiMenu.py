import mysql
import mysql.connector
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "alessio"
DB_DATABASE = "mydbristorante"
DB_PORT = 3360

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

def ottieniElementiTabellaProdottiMenu():
    try:
        myconn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            passwd = DB_PASSWORD,
            database = DB_DATABASE,
            port = DB_PORT
        )
        cursor = myconn.cursor()
        query = "Select id, nome, descrizione, prezzo, categoria from prodottomenu"
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