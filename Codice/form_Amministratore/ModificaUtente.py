# -*- coding: utf-8 -*-
import mysql
# Form implementation generated from reading ui file 'F:\Users\framo\Desktop\ProgettoING-master\form_ui\ModificaUtente.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from db_connection import get_connection

class Ui_ModificaUtente(object):
    formAttuale=None
    def setupUi(self, ModificaUtente):
        self.formAttuale=ModificaUtente
        ModificaUtente.setObjectName("ModificaUtente")
        ModificaUtente.resize(346, 282)
        ModificaUtente.setStyleSheet("background-color: rgb(159, 197, 248)")
        self.tbUsername = QtWidgets.QLineEdit(ModificaUtente)
        self.tbUsername.setGeometry(QtCore.QRect(150, 37, 141, 22))
        self.tbUsername.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tbUsername.setObjectName("tbUsername")
        self.tbUsername.setEnabled(False)
        self.tbPassword = QtWidgets.QLineEdit(ModificaUtente)
        self.tbPassword.setGeometry(QtCore.QRect(150, 95, 141, 22))
        self.tbPassword.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tbPassword.setObjectName("tbPassword")
        self.label = QtWidgets.QLabel(ModificaUtente)
        self.label.setGeometry(QtCore.QRect(20, 40, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ModificaUtente)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btConferma = QtWidgets.QPushButton(ModificaUtente)
        self.btConferma.setGeometry(QtCore.QRect(120, 180, 111, 41))
        self.btConferma.setStyleSheet("background-color: rgb(132, 224, 142)")
        self.btConferma.setObjectName("btConferma")

        self.retranslateUi(ModificaUtente)
        QtCore.QMetaObject.connectSlotsByName(ModificaUtente)
        ##################################
        self.btConferma.clicked.connect(self.btConfermaClicked)

    def retranslateUi(self, ModificaUtente):
        _translate = QtCore.QCoreApplication.translate
        ModificaUtente.setWindowTitle(_translate("ModificaUtente", "Modifica Utente"))
        self.label.setText(_translate("ModificaUtente", "Username"))
        self.label_2.setText(_translate("ModificaUtente", "Password"))
        self.btConferma.setText(_translate("ModificaUtente", "Conferma"))

    def btConfermaClicked(self):
        username = self.tbUsername.text()
        new_password = self.tbPassword.text()

        if not username or not new_password:
            QtWidgets.QMessageBox.warning(None, "Errore", "Compila tutti i campi!")
            return

        try:
            myconn = get_connection()
            cursor = myconn.cursor()
            query = "UPDATE account SET pwd = %s WHERE username = %s"
            cursor.execute(query, (new_password, username))
            myconn.commit()


        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(None, "Errore", f"Errore durante la modifica: {err}")
        finally:
            cursor.close()
            myconn.close()
            self.formAttuale.close()
