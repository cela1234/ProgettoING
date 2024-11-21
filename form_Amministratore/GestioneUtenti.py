# -*- coding: utf-8 -*-
import mysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from db_connection import get_connection
from .ModificaUtente import Ui_ModificaUtente
from .NuovoUtente import Ui_AggiungiUtente


class Ui_GestioneUtenti(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(469, 284)
        Dialog.setStyleSheet("background-color: rgb(159, 197, 248)")

        # TableWidget Utenti
        self.twUtenti = QtWidgets.QTableWidget(Dialog)
        self.twUtenti.setGeometry(QtCore.QRect(0, 0, 302, 281))
        self.twUtenti.setStyleSheet("background-color: rgb(245, 243, 201)")
        self.twUtenti.setObjectName("twUtenti")
        self.twUtenti.setColumnCount(3)
        self.twUtenti.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twUtenti.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twUtenti.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twUtenti.setHorizontalHeaderItem(2, item)
        self.twUtenti.setColumnWidth(0, 120)
        self.twUtenti.setColumnWidth(1, 120)
        self.twUtenti.setColumnWidth(2, 50)

        # Bottone Modifica Utente
        self.btModificaUtente = QtWidgets.QPushButton(Dialog)
        self.btModificaUtente.setGeometry(QtCore.QRect(330, 40, 111, 51))
        self.btModificaUtente.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.btModificaUtente.setObjectName("btModificaUtente")

        # Bottone Aggiungi Utente
        self.btAggiungiUtente = QtWidgets.QPushButton(Dialog)
        self.btAggiungiUtente.setGeometry(QtCore.QRect(330, 110, 111, 51))
        self.btAggiungiUtente.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.btAggiungiUtente.setObjectName("btAggiungiUtente")

        # Bottone Elimina Utente
        self.btEliminaUtente = QtWidgets.QPushButton(Dialog)
        self.btEliminaUtente.setGeometry(QtCore.QRect(330, 180, 111, 51))
        self.btEliminaUtente.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.btEliminaUtente.setObjectName("btEliminaUtente")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        ##################################
        # Connessione ai bottoni
        self.btModificaUtente.clicked.connect(self.btModificaUtenteClicked)
        self.btAggiungiUtente.clicked.connect(self.btAggiungiUtenteClicked)
        self.btEliminaUtente.clicked.connect(self.btEliminaUtenteClicked)

        # Popola la tabella degli utenti
        self.popolaTwUtenti()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Gestione Utenti"))
        item = self.twUtenti.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Username"))
        item = self.twUtenti.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Password"))
        item = self.twUtenti.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Ruolo"))
        self.btModificaUtente.setText(_translate("Dialog", "Modifica Utente"))
        self.btAggiungiUtente.setText(_translate("Dialog", "Aggiungi Utente"))
        self.btEliminaUtente.setText(_translate("Dialog", "Elimina Utente"))

    def btModificaUtenteClicked(self):
        selected_row = self.twUtenti.currentRow()
        if selected_row >= 0:
            username = self.twUtenti.item(selected_row, 0).text()
            dialog = QDialog()
            ui = Ui_ModificaUtente()
            ui.setupUi(dialog)
            ui.tbUsername.setText(username)
            dialog.exec_()
            self.popolaTwUtenti()
        else:
            QMessageBox.warning(self, "Attenzione", "Seleziona un utente da modificare.")

    def btAggiungiUtenteClicked(self):
        # Apri il file NuovoUtente.py per aggiungere un nuovo utente
        dialog = QDialog()
        ui = Ui_AggiungiUtente()
        ui.setupUi(dialog)
        dialog.exec_()
        self.popolaTwUtenti()

    def btEliminaUtenteClicked(self):
        selected_row = self.twUtenti.currentRow()
        if selected_row >= 0:
            username = self.twUtenti.item(selected_row, 0).text()
            risposta = QMessageBox.question(None, "Conferma Eliminazione",
                                            f"Sei sicuro di voler eliminare l'utente {username}?",
                                            QMessageBox.Yes | QMessageBox.No)
            if risposta == QMessageBox.Yes:
                try:
                    myconn = get_connection()
                    cursor = myconn.cursor()
                    cursor.execute("DELETE FROM account WHERE username = %s", (username,))
                    myconn.commit()
                    cursor.close()
                    myconn.close()
                    self.popolaTwUtenti()  # Aggiorna la tabella
                except mysql.connector.Error as err:
                    QMessageBox.critical(None, "Errore", f"Errore durante l'eliminazione: {err}")
        else:
            QMessageBox.warning(None, "Attenzione", "Seleziona un utente da eliminare.")

    def popolaTwUtenti(self):
        try:
            myconn = get_connection()
            cursor = myconn.cursor()
            cursor.execute("SELECT username, pwd, ruolo FROM account")
            results = cursor.fetchall()
            self.twUtenti.setRowCount(len(results))
            self.twUtenti.setColumnCount(3)
            self.twUtenti.setHorizontalHeaderLabels(['Username', 'Password', 'Ruolo'])
            for row_index, row_data in enumerate(results):
                for column_index, data in enumerate(row_data):
                    self.twUtenti.setItem(row_index, column_index, QtWidgets.QTableWidgetItem(str(data)))
            cursor.close()
            myconn.close()
        except mysql.connector.Error as err:
            print(f"Errore durante l'accesso al database: {err}")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_GestioneUtenti()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
