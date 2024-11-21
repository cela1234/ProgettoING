# -*- coding: utf-8 -*-
import mysql
from PyQt5 import QtCore, QtGui, QtWidgets
from db_connection import get_connection


class Ui_AggiungiUtente(object):
    formAttuale = None

    def setupUi(self, AggiungiUtente):
        self.formAttuale = AggiungiUtente
        AggiungiUtente.setObjectName("AggiungiUtente")
        AggiungiUtente.resize(346, 320)
        AggiungiUtente.setStyleSheet("background-color: rgb(159, 197, 248)")

        # Campi per Username e Password
        self.tbUsername = QtWidgets.QLineEdit(AggiungiUtente)
        self.tbUsername.setGeometry(QtCore.QRect(150, 37, 141, 22))
        self.tbUsername.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tbUsername.setObjectName("tbUsername")

        self.tbPassword = QtWidgets.QLineEdit(AggiungiUtente)
        self.tbPassword.setGeometry(QtCore.QRect(150, 95, 141, 22))
        self.tbPassword.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tbPassword.setObjectName("tbPassword")

        # Etichette per Username e Password
        self.label = QtWidgets.QLabel(AggiungiUtente)
        self.label.setGeometry(QtCore.QRect(20, 40, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(AggiungiUtente)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        # ComboBox per la selezione del ruolo
        self.cbRuolo = QtWidgets.QComboBox(AggiungiUtente)
        self.cbRuolo.setGeometry(QtCore.QRect(150, 150, 141, 22))
        self.cbRuolo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbRuolo.setObjectName("cbRuolo")
        self.cbRuolo.addItems(["admin", "cameriere", "cuoco"])

        # Etichetta per il ruolo
        self.label_3 = QtWidgets.QLabel(AggiungiUtente)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        # Bottone Conferma
        self.btConferma = QtWidgets.QPushButton(AggiungiUtente)
        self.btConferma.setGeometry(QtCore.QRect(120, 220, 111, 41))
        self.btConferma.setStyleSheet("background-color: rgb(132, 224, 142)")
        self.btConferma.setObjectName("btConferma")

        self.retranslateUi(AggiungiUtente)
        QtCore.QMetaObject.connectSlotsByName(AggiungiUtente)

        # Collegamento bottone
        self.btConferma.clicked.connect(self.btConfermaClicked)

    def retranslateUi(self, AggiungiUtente):
        _translate = QtCore.QCoreApplication.translate
        AggiungiUtente.setWindowTitle(_translate("AggiungiUtente", "Aggiungi Utente"))
        self.label.setText(_translate("AggiungiUtente", "Username"))
        self.label_2.setText(_translate("AggiungiUtente", "Password"))
        self.label_3.setText(_translate("AggiungiUtente", "Ruolo"))
        self.btConferma.setText(_translate("AggiungiUtente", "Conferma"))

    def btConfermaClicked(self):
        username = self.tbUsername.text()
        password = self.tbPassword.text()
        ruolo = self.cbRuolo.currentText()

        if not username or not password:
            QtWidgets.QMessageBox.warning(None, "Errore", "Compila tutti i campi!")
            return

        try:
            myconn = get_connection()
            cursor = myconn.cursor()
            # Verifica se l'utente esiste già
            cursor.execute("SELECT * FROM account WHERE username = %s", (username,))
            result = cursor.fetchone()
            if result:
                QtWidgets.QMessageBox.warning(None, "Errore", "Username già esistente!")
                return

            # Inserisci nuovo utente
            query = "INSERT INTO account (username, pwd, ruolo) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, password, ruolo))
            myconn.commit()

        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(None, "Errore", f"Errore durante l'inserimento: {err}")
        finally:
            cursor.close()
            myconn.close()
            self.formAttuale.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AggiungiUtente = QtWidgets.QDialog()
    ui = Ui_AggiungiUtente()
    ui.setupUi(AggiungiUtente)
    AggiungiUtente.show()
    sys.exit(app.exec_())
