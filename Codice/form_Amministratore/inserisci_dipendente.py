# -*- coding: utf-8 -*-
import mysql
# Form implementation generated from reading ui file 'F:\Users\framo\Desktop\ProgettoING-master\form_ui\inserisci_dipendente.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from db_connection import get_connection


class Ui_formInserisciDipendente(object):

    formAttuale=None
    def setupUi(self, formInserisciDipendente):
        self.formAttuale=formInserisciDipendente
        formInserisciDipendente.setObjectName("formInserisciDipendente")
        formInserisciDipendente.resize(322, 226)
        formInserisciDipendente.setStyleSheet("background-color: rgb(159, 197, 248)")
        self.tbnome = QtWidgets.QLineEdit(formInserisciDipendente)
        self.tbnome.setGeometry(QtCore.QRect(120, 30, 141, 22))
        self.tbnome.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tbnome.setObjectName("tbnome")
        self.label = QtWidgets.QLabel(formInserisciDipendente)
        self.label.setGeometry(QtCore.QRect(30, 30, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(formInserisciDipendente)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 55, 16))
        self.label_2.setObjectName("label_2")
        self.cbRuolo = QtWidgets.QComboBox(formInserisciDipendente)
        self.cbRuolo.setGeometry(QtCore.QRect(120, 75, 141, 22))
        self.cbRuolo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbRuolo.setObjectName("cbRuolo")
        self.cbRuolo.addItem("")
        self.cbRuolo.addItem("")
        self.btConferma = QtWidgets.QPushButton(formInserisciDipendente)
        self.btConferma.setGeometry(QtCore.QRect(110, 145, 101, 41))
        self.btConferma.setStyleSheet("background-color: rgb(132, 224, 142);")
        self.btConferma.setObjectName("btConferma")

        self.retranslateUi(formInserisciDipendente)
        QtCore.QMetaObject.connectSlotsByName(formInserisciDipendente)
        #############################################
        self.btConferma.clicked.connect(self.inserisci_dipendente)

    def retranslateUi(self, formInserisciDipendente):
        _translate = QtCore.QCoreApplication.translate
        formInserisciDipendente.setWindowTitle(_translate("formInserisciDipendente", "Inserisci dipendente"))
        self.label.setText(_translate("formInserisciDipendente", "Nome"))
        self.label_2.setText(_translate("formInserisciDipendente", "Ruolo"))
        self.cbRuolo.setItemText(0, _translate("formInserisciDipendente", "cameriere"))
        self.cbRuolo.setItemText(1, _translate("formInserisciDipendente", "cuoco"))
        self.btConferma.setText(_translate("formInserisciDipendente", "Conferma"))

    def inserisci_dipendente(self):
        nome = self.tbnome.text()
        ruolo = self.cbRuolo.currentText()

        if not nome or not ruolo:
            QtWidgets.QMessageBox.warning(None, "Errore", "Compila tutti i campi!")
            return

        try:
            myconn  = get_connection()
            cursor = myconn.cursor()
            query = "INSERT INTO dipendente (cognomenome, ruolo) VALUES (%s, %s)"
            cursor.execute(query, (nome, ruolo))
            myconn.commit()
            cursor.close()
            myconn.close()
            self.formAttuale.close()
        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(None, "Errore", f"Errore durante l'inserimento: {err}")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formInserisciDipendente = QtWidgets.QDialog()
    ui = Ui_formInserisciDipendente()
    ui.setupUi(formInserisciDipendente)
    formInserisciDipendente.show()
    sys.exit(app.exec_())