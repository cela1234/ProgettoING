# -*- coding: utf-8 -*-
from datetime import datetime

import mysql
# Form implementation generated from reading ui file 'F:\Users\framo\Desktop\ProgettoING-master\form_ui\GestionePrenotazioni.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from .aggiungiModificaPrenotazione import Ui_AggiungiModificaPrenotazione
from db_connection import get_connection

class Ui_GestionePrenotazioni(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1252, 599)
        Dialog.setStyleSheet("background-color: rgb(159, 197, 248);")
        self.lbl_titolo_gest_pren = QtWidgets.QLabel(Dialog)
        self.lbl_titolo_gest_pren.setGeometry(QtCore.QRect(10, 10, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(18)
        self.lbl_titolo_gest_pren.setFont(font)
        self.lbl_titolo_gest_pren.setObjectName("lbl_titolo_gest_pren")
        self.twPrenotazioni = QtWidgets.QTableWidget(Dialog)
        self.twPrenotazioni.setGeometry(QtCore.QRect(440, 80, 602, 471))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.twPrenotazioni.setFont(font)
        self.twPrenotazioni.setStyleSheet("background-color: rgb(240, 236, 95);")
        self.twPrenotazioni.setObjectName("twPrenotazioni")
        self.twPrenotazioni.setColumnCount(6)
        self.twPrenotazioni.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twPrenotazioni.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twPrenotazioni.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twPrenotazioni.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.twPrenotazioni.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.twPrenotazioni.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.twPrenotazioni.setHorizontalHeaderItem(5, item)
        self.bt_modifica_prenot = QtWidgets.QPushButton(Dialog)
        self.bt_modifica_prenot.setGeometry(QtCore.QRect(1070, 160, 161, 81))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.bt_modifica_prenot.setFont(font)
        self.bt_modifica_prenot.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.bt_modifica_prenot.setObjectName("bt_modifica_prenot")
        self.bt_elimina_prenot = QtWidgets.QPushButton(Dialog)
        self.bt_elimina_prenot.setGeometry(QtCore.QRect(1070, 400, 161, 81))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.bt_elimina_prenot.setFont(font)
        self.bt_elimina_prenot.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.bt_elimina_prenot.setObjectName("bt_elimina_prenot")
        self.bt_aggiung_prenot = QtWidgets.QPushButton(Dialog)
        self.bt_aggiung_prenot.setGeometry(QtCore.QRect(1070, 280, 161, 81))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.bt_aggiung_prenot.setFont(font)
        self.bt_aggiung_prenot.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.bt_aggiung_prenot.setObjectName("bt_aggiung_prenot")
        self.calendario_gest_prenot = QtWidgets.QCalendarWidget(Dialog)
        self.calendario_gest_prenot.setGeometry(QtCore.QRect(10, 120, 411, 431))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setBold(False)
        font.setWeight(50)
        self.calendario_gest_prenot.setFont(font)
        self.calendario_gest_prenot.setStyleSheet("background-color: rgb(240, 236, 95);")
        self.calendario_gest_prenot.setObjectName("calendario_gest_prenot")
        self.tbCerca = QtWidgets.QLineEdit(Dialog)
        self.tbCerca.setGeometry(QtCore.QRect(10, 80, 141, 22))
        self.tbCerca.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tbCerca.setObjectName("tbCerca")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(180, 80, 241, 20))
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        ########
        self.calendario_gest_prenot.selectionChanged.connect(self.aggiornaPrenotazioni)
        self.bt_aggiung_prenot.clicked.connect(self.apriDialogoAggiungiPrenotazione)
        self.bt_modifica_prenot.clicked.connect(self.apriDialogoModificaPrenotazione)
        self.bt_elimina_prenot.clicked.connect(self.bt_elimina_prenot_clicked)
        self.tbCerca.textChanged.connect(self.aggiornaPrenotazioni)
        self.checkBox.stateChanged.connect(self.aggiornaPrenotazioni)
        self.aggiornaPrenotazioni()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lbl_titolo_gest_pren.setText(_translate("Dialog", "Gestione Prenotazioni"))
        item = self.twPrenotazioni.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Nome Cliente"))
        item = self.twPrenotazioni.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Tavolo"))
        item = self.twPrenotazioni.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Sala"))
        item = self.twPrenotazioni.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Orario"))
        item = self.twPrenotazioni.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "N° Coperti"))
        item = self.twPrenotazioni.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Codice"))
        self.bt_modifica_prenot.setText(_translate("Dialog", "Modifica Prenotazione"))
        self.bt_elimina_prenot.setText(_translate("Dialog", "Elimina Prenotazione"))
        self.bt_aggiung_prenot.setText(_translate("Dialog", "Aggiungi Prenotazione"))
        self.tbCerca.setPlaceholderText(_translate("Dialog", "Cerca per nome"))
        self.checkBox.setText(_translate("Dialog", "Cerca in tutte le date future"))

    def aggiornaPrenotazioni(self):
        data_selezionata = self.calendario_gest_prenot.selectedDate().toString("yyyy-MM-dd")
        cerca_text = self.tbCerca.text()
        cerca_tutte_date = self.checkBox.isChecked()

        # Connessione al database
        db = None
        cursor = None

        try:
            db = get_connection()
            cursor = db.cursor()

            # Esegui la query per ottenere le prenotazioni per la data selezionata
            if cerca_tutte_date:
                query = """
                        SELECT p.nome, t.numero, t.sala, TIME(p.Dataeoraprenotazione), p.numeroPersone, p.ID
                        FROM Prenotazione p
                        JOIN Tavolo t ON p.IDTavolo = t.ID
                        WHERE p.nome LIKE %s AND DATE(p.Dataeoraprenotazione) >= %s
                        ORDER BY TIME(p.Dataeoraprenotazione)
                        """
                cursor.execute(query, (f"%{cerca_text}%", data_selezionata))
            else:
                query = """
                        SELECT p.nome, t.numero, t.sala, TIME(p.Dataeoraprenotazione), p.numeroPersone, p.ID
                        FROM Prenotazione p
                        JOIN Tavolo t ON p.IDTavolo = t.ID
                        WHERE p.nome LIKE %s AND DATE(p.Dataeoraprenotazione) = %s
                        ORDER BY TIME(p.Dataeoraprenotazione)
                        """
                cursor.execute(query, (f"%{cerca_text}%", data_selezionata))

            result = cursor.fetchall()

            # Pulisci la tabella prima di aggiungere nuove righe
            self.twPrenotazioni.setRowCount(0)

            # Aggiungi i dati alla tabella
            for row_number, row_data in enumerate(result):
                self.twPrenotazioni.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.twPrenotazioni.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        except mysql.connector.Error as err:
            print(f"Errore: {err}")
        finally:
            # Chiudi la connessione al database
            if cursor:
                cursor.close()
            if db:
                db.close()


    def apriDialogoAggiungiPrenotazione(self):
        dialog = QDialog()
        ui = Ui_AggiungiModificaPrenotazione()
        ui.setupUi(dialog,-1,self)
        ui.btAggiungiModifica.setText("Aggiungi Prenotazione")
        ora_attuale = datetime.now()
        orario = ora_attuale.strftime("%H:%M:%S")

        # Formatta la data e l'ora in una stringa
        data_ora_string = f"{self.calendario_gest_prenot.selectedDate().toString('yyyy-MM-dd')} {orario}"

        # Imposta la data e l'ora nel QDateTimeEdit
        ui.dtDataEOra.setDateTime(QtCore.QDateTime.fromString(data_ora_string, "yyyy-MM-dd HH:mm:ss"))

        dialog.exec_()
        self.aggiornaPrenotazioni()

    def apriDialogoModificaPrenotazione(self):
        selected_row = self.twPrenotazioni.currentRow()
        if selected_row == -1:
            QMessageBox.warning(None, "Errore", "Seleziona una prenotazione da modificare")
            return

        # Ottieni i dati della prenotazione selezionata
        id_prenotazione = self.twPrenotazioni.item(selected_row, 5).text()
        nome_prenotazione = self.twPrenotazioni.item(selected_row, 0).text()
        numero_tavolo = self.twPrenotazioni.item(selected_row, 1).text()
        sala = self.twPrenotazioni.item(selected_row, 2).text()
        orario = self.twPrenotazioni.item(selected_row, 3).text()
        numero_persone = self.twPrenotazioni.item(selected_row, 4).text()

        dialog = QDialog()
        ui = Ui_AggiungiModificaPrenotazione()
        ui.setupUi(dialog, id_prenotazione,self)
        ui.btAggiungiModifica.setText("Modifica Prenotazione")

        # Carica i dati della prenotazione nel dialogo
        ui.tbNomePrenotazione.setText(nome_prenotazione)
        ui.cbNumeroTavolo.setCurrentText(numero_tavolo)
        ui.cbSala.setCurrentText(sala)
        ui.dtDataEOra.setDateTime( QtCore.QDateTime.fromString(f"{self.calendario_gest_prenot.selectedDate().toString("yyyy-MM-dd")} {orario}", "yyyy-MM-dd HH:mm:ss"))
        ui.nudNumeroPersone.setValue(int(numero_persone))

        dialog.exec_()

    def bt_elimina_prenot_clicked(self):
        selected_row = self.twPrenotazioni.currentRow()
        if selected_row == -1:
            QMessageBox.warning(None, "Errore", "Seleziona una prenotazione da eliminare")
            return

        # Ottieni l'ID della prenotazione selezionata
        id_prenotazione = self.twPrenotazioni.item(selected_row, 5).text()

        # Connessione al database
        db = None
        cursor = None

        try:
            db = get_connection()
            cursor = db.cursor()

            # Esegui la query per eliminare la prenotazione
            query = "DELETE FROM Prenotazione WHERE ID = %s"
            cursor.execute(query, (id_prenotazione,))
            db.commit()

            # Aggiorna la visualizzazione delle prenotazioni
            self.aggiornaPrenotazioni()

            QMessageBox.information(None, "Successo", "Prenotazione eliminata con successo")
        except mysql.connector.Error as err:
            QMessageBox.critical(None, "Errore", f"Errore del database: {err}")
        finally:
            # Chiudi la connessione al database
            if cursor:
                cursor.close()
            if db:
                db.close()
            self.aggiornaPrenotazioni()

    def filtraTabella(self):
        ricerca = self.tbCerca.text().lower()
        for row in range(self.twPrenotazioni.rowCount()):
            item = self.twPrenotazioni.item(row, 1)  # Colonna "Nome"
            if item:
                # Confronta il testo dell'elemento con il testo di ricerca
                if ricerca in item.text().lower():
                    self.twPrenotazioni.setRowHidden(row, False)
                else:
                    self.twPrenotazioni.setRowHidden(row, True)
