# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gestioneMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql
import mysql.connector
from PyQt5.QtSql import QSqlQueryModel
from PyQt5.QtWidgets import QTableWidgetItem, QMainWindow, QPushButton, QMessageBox
import gestioneNomi
import formAggiungiModificaElementoMagazzino
from datetime import datetime, date
import classi.GestoriDB.GestoreProdottiMenu as GestoreDBMenu
import Resources.icons


class Ui_formGestioneMenu(object):
    def setupUi(self, formGestioneMenu):
        formGestioneMenu.setObjectName("formGestioneMenu")
        formGestioneMenu.resize(783, 570)
        formGestioneMenu.setStyleSheet("background-color: rgb(159, 197, 248);")
        self.tableProdotti = QtWidgets.QTableWidget(formGestioneMenu)
        self.tableProdotti.setGeometry(QtCore.QRect(10, 10, 521, 551))
        self.tableProdotti.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableProdotti.setObjectName("tableProdotti")
        self.tableProdotti.setColumnCount(0)
        self.tableProdotti.setRowCount(0)
        self.txtCerca = QtWidgets.QLineEdit(formGestioneMenu)
        self.txtCerca.setGeometry(QtCore.QRect(540, 10, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.txtCerca.setFont(font)
        self.txtCerca.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtCerca.setText("")
        self.txtCerca.setObjectName("txtCerca")
        self.btRefresh = QtWidgets.QPushButton(formGestioneMenu)
        self.btRefresh.setGeometry(QtCore.QRect(740, 10, 31, 31))
        self.btRefresh.setStyleSheet("image: url(:/icone/Icons/refresh-ccw.svg);")
        self.btRefresh.setText("")
        self.btRefresh.setObjectName("btRefresh")
        self.btMostraDettaglio = QtWidgets.QPushButton(formGestioneMenu)
        self.btMostraDettaglio.setGeometry(QtCore.QRect(540, 50, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.btMostraDettaglio.setFont(font)
        self.btMostraDettaglio.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.btMostraDettaglio.setObjectName("btMostraDettaglio")
        self.btInserisciProdotto = QtWidgets.QPushButton(formGestioneMenu)
        self.btInserisciProdotto.setGeometry(QtCore.QRect(540, 150, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.btInserisciProdotto.setFont(font)
        self.btInserisciProdotto.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.btInserisciProdotto.setObjectName("btInserisciProdotto")
        self.btModificaProdotto = QtWidgets.QPushButton(formGestioneMenu)
        self.btModificaProdotto.setGeometry(QtCore.QRect(540, 200, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.btModificaProdotto.setFont(font)
        self.btModificaProdotto.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.btModificaProdotto.setObjectName("btModificaProdotto")

        self.tableProdotti.setColumnCount(5)
        self.tableProdotti.verticalHeader().setVisible(False)
        self.tableProdotti.setHorizontalHeaderLabels(["id", "Nome", "Descrizione", "Prezzo", "Categoria"])
        self.btInserisciProdotto.clicked.connect(self.btInserisciProdottoClicked)
        self.btModificaProdotto.clicked.connect(self.btModificaProdottoClicked)
        self.btRefresh.clicked.connect(self.btRefreshClicked)
        self.txtCerca.textChanged.connect(self.txtCercaChanged)


        self.retranslateUi(formGestioneMenu)
        QtCore.QMetaObject.connectSlotsByName(formGestioneMenu)

        self.load_data_tabella()

    def retranslateUi(self, formGestioneMenu):
        _translate = QtCore.QCoreApplication.translate
        formGestioneMenu.setWindowTitle(_translate("formGestioneMenu", "GestioneMenu - Amministratore"))
        self.txtCerca.setPlaceholderText(_translate("formGestioneMenu", "Cerca"))
        self.btMostraDettaglio.setText(_translate("formGestioneMenu", "Mostra informazioni del\n"
"prodotto selezionato"))
        self.btInserisciProdotto.setText(_translate("formGestioneMenu", "Inserisci Prodotto"))
        self.btModificaProdotto.setText(_translate("formGestioneMenu", "Modifica Prodotto"))

    def load_data_tabella(self):
        self.txtCerca.setText("")
        result = GestoreDBMenu.ottieniElementiTabellaProdottiMenu()
        self.tableProdotti.setRowCount(0)
        for row_number, row_data in enumerate(result):
            print(row_number)
            self.tableProdotti.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                print(f"{data}, {column_number}")
                if column_number == 3:
                    self.tableProdotti.setItem(row_number, column_number, QTableWidgetItem("€" + str(data)))
                else:
                    self.tableProdotti.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.tableProdotti.resizeColumnsToContents()

    def btModificaProdottoClicked(self):
        pass

    def btInserisciProdottoClicked(self):
        pass

    def btRefreshClicked(self):
        self.load_data_tabella()

    def txtCercaChanged(self):
        ricerca = self.txtCerca.text().lower()
        for row in range(self.tableProdotti.rowCount()):
            item = self.tableProdotti.item(row, 1)  # Colonna "Nome"
            if item:
                # Confronta il testo dell'elemento con il testo di ricerca
                if ricerca in item.text().lower():
                    self.tableProdotti.setRowHidden(row, False)
                else:
                    self.tableProdotti.setRowHidden(row, True)

if __name__ == "__main__":
            import sys
            app = QtWidgets.QApplication(sys.argv)
            formGestioneMenu = QtWidgets.QDialog()
            ui = (Ui_formGestioneMenu())
            ui.setupUi(formGestioneMenu)
            formGestioneMenu.show()
            sys.exit(app.exec_())
