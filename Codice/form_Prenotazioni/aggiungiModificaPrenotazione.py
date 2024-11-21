# -*- coding: utf-8 -*-
import mysql
# Form implementation generated from reading ui file 'F:\Users\framo\Desktop\ProgettoING-master\form_ui\aggiungiModificaPrenotazione.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from db_connection import get_connection
from PyQt5.QtCore import QDateTime


class Ui_AggiungiModificaPrenotazione(object):
    idPrenotazione=None #se l'id è -1 sono in aggiunta, sennò in modifica
    formPadre=None
    def setupUi(self, Dialog,ID,padre):
        self.formPadre=padre
        self.idPrenotazione=ID
        Dialog.setObjectName("Dialog")
        Dialog.resize(490, 292)
        Dialog.setStyleSheet("background-color: rgb(159, 197, 248);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 121, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(290, 80, 101, 41))
        self.label_2.setObjectName("label_2")
        self.dtDataEOra = QtWidgets.QDateTimeEdit(Dialog)
        self.dtDataEOra.setGeometry(QtCore.QRect(100, 90, 131, 22))
        self.dtDataEOra.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dtDataEOra.setObjectName("dtDataEOra")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 71, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(290, 130, 91, 41))
        self.label_4.setObjectName("label_4")
        self.tbNomePrenotazione = QtWidgets.QLineEdit(Dialog)
        self.tbNomePrenotazione.setGeometry(QtCore.QRect(150, 40, 113, 22))
        self.tbNomePrenotazione.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tbNomePrenotazione.setObjectName("tbNomePrenotazione")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 31, 41))
        self.label_5.setObjectName("label_5")
        self.cbSala = QtWidgets.QComboBox(Dialog)
        self.cbSala.setGeometry(QtCore.QRect(100, 140, 171, 22))
        self.cbSala.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbSala.setObjectName("cbSala")
        self.cbSala.addItems(["pizzeria", "principale", "prive", "open space", "saletta"])
        self.cbNumeroTavolo = QtWidgets.QComboBox(Dialog)
        self.cbNumeroTavolo.setGeometry(QtCore.QRect(410, 140, 61, 22))
        self.cbNumeroTavolo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbNumeroTavolo.setObjectName("cbNumeroTavolo")
        self.nudNumeroPersone = QtWidgets.QSpinBox(Dialog)
        self.nudNumeroPersone.setGeometry(QtCore.QRect(410, 90, 61, 22))
        self.nudNumeroPersone.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nudNumeroPersone.setObjectName("nudNumeroPersone")
        self.btAggiungiModifica = QtWidgets.QPushButton(Dialog)
        self.btAggiungiModifica.setGeometry(QtCore.QRect(160, 220, 161, 41))
        self.btAggiungiModifica.setStyleSheet("background-color: rgb(132, 224, 142);")
        self.btAggiungiModifica.setObjectName("btAggiungiModifica")

        self.retranslateUi(Dialog)
        self.caricaTavoli()
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        ######
        self.cbSala.currentIndexChanged.connect(self.caricaTavoli)
        self.btAggiungiModifica.clicked.connect(self.aggiungiModificaPrenotazione)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Prenotazione"))
        self.label.setText(_translate("Dialog", "Nome prenotazione:"))
        self.label_2.setText(_translate("Dialog", "Numero persone:"))
        self.label_3.setText(_translate("Dialog", "Data e ora:"))
        self.label_4.setText(_translate("Dialog", "Numero tavolo:"))
        self.label_5.setText(_translate("Dialog", "Sala:"))
        self.btAggiungiModifica.setText(_translate("Dialog", "Aggiungi Prenotazione"))

    def aggiungiModificaPrenotazione(self):
        nome_prenotazione = self.tbNomePrenotazione.text()
        data_e_ora = self.dtDataEOra.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        numero_persone = self.nudNumeroPersone.value()
        sala = self.cbSala.currentText()
        numero_tavolo = self.cbNumeroTavolo.currentText()
        prenotazione_valida= self.controllaDisponibilita(sala, numero_tavolo, data_e_ora)
        if nome_prenotazione == "" or numero_persone == 0 or numero_tavolo == 0:
            QMessageBox.warning(None, "Errore", "Compila tutti i campi obbligatori")
            return
        if prenotazione_valida==False:
            QMessageBox.warning(None, "Errore", "Il tavolo è già prenotato in quella fascia oraria! (+/- 90 minuti)")
            return
        if(self.idPrenotazione==-1): #STO AGGIUNGENDO UNA PRENOTAZIONE
            try:
                connection = get_connection()
                cursor = connection.cursor()

                # Fetch the table ID based on the table number and sala
                cursor.execute("SELECT ID FROM Tavolo WHERE numero = %s AND sala = %s", (numero_tavolo, sala))
                tavolo_result = cursor.fetchone()
                if tavolo_result:
                    id_tavolo = tavolo_result[0]
                else:
                    QMessageBox.warning(None, "Errore", "Tavolo non trovato")
                    return

                query = """
                    INSERT INTO Prenotazione (IDTavolo, Dataeoraprenotazione, nome, numeroPersone)
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query, (id_tavolo, data_e_ora, nome_prenotazione, numero_persone))
                connection.commit()
                QMessageBox.information(None, "Successo", "Prenotazione aggiunta con successo")
            except mysql.connector.Error as err:
                QMessageBox.critical(None, "Errore", f"Errore del database: {err}")
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

        else: #sto modificando una prenotazione
            try:
                connection = get_connection()
                cursor = connection.cursor()

                # Trova l'ID del tavolo corrispondente al numero e alla sala selezionati
                cursor.execute("SELECT ID FROM Tavolo WHERE numero = %s AND sala = %s", (numero_tavolo, sala))
                tavolo_result = cursor.fetchone()
                if tavolo_result:
                    id_tavolo = tavolo_result[0]
                else:
                    QMessageBox.warning(None, "Errore", "Tavolo non trovato")
                    return

                # Aggiorna i dati della prenotazione nel database
                query = """
                        UPDATE Prenotazione
                        SET IDTavolo = %s, Dataeoraprenotazione = %s, nome = %s, numeroPersone = %s
                        WHERE ID = %s
                    """
                cursor.execute(query, (id_tavolo, data_e_ora, nome_prenotazione, numero_persone, self.idPrenotazione))
                connection.commit()
                QMessageBox.information(None, "Successo", "Prenotazione modificata con successo")
            except mysql.connector.Error as err:
                QMessageBox.critical(None, "Errore", f"Errore del database: {err}")
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
        self.formPadre.aggiornaPrenotazioni()

    def controllaDisponibilita(self, sala, numero, data_str):
        try:
            # Converte la stringa in oggetto QDateTime
            data = QDateTime.fromString(data_str, "yyyy-MM-dd HH:mm:ss")

            if not data.isValid():
                QMessageBox.critical(None, "Errore", "La data fornita non è valida")
                return False

            connection = get_connection()
            cursor = connection.cursor()

            # Trova l'ID del tavolo
            cursor.execute("SELECT ID FROM Tavolo WHERE numero = %s AND sala = %s", (numero, sala))
            tavolo_result = cursor.fetchone()

            if tavolo_result is None:
                # Tavolo non trovato
                return False

            id_tavolo = tavolo_result[0]

            # Calcola il range di tempo (un'ora e mezza prima e dopo la prenotazione)
            data_inizio = data.addSecs(-90 * 60)  # 90 minuti prima
            data_fine = data.addSecs(90 * 60)  # 90 minuti dopo

            # Confronta le prenotazioni per lo stesso tavolo
            query = """
                SELECT * FROM Prenotazione
                WHERE IDTavolo = %s 
                AND Dataeoraprenotazione BETWEEN %s AND %s
            """
            cursor.execute(query, (
            id_tavolo, data_inizio.toString("yyyy-MM-dd HH:mm:ss"), data_fine.toString("yyyy-MM-dd HH:mm:ss")))
            prenotazione_esistente = cursor.fetchone()

            # Se esiste una prenotazione nel range di tempo, restituisci False (non disponibile)
            if prenotazione_esistente:
                return False
            return True

        except mysql.connector.Error as err:
            QMessageBox.critical(None, "Errore", f"Errore del database: {err}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


    def caricaTavoli(self):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            sala = self.cbSala.currentText()

            # Fetch table numbers based on the selected sala
            cursor.execute("SELECT numero FROM Tavolo WHERE sala = %s", (sala,))
            tavoli = cursor.fetchall()

            self.cbNumeroTavolo.clear()
            for tavolo in tavoli:
                self.cbNumeroTavolo.addItem(str(tavolo[0]))

        except mysql.connector.Error as err:
            QMessageBox.critical(None, "Errore", f"Errore del database: {err}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()