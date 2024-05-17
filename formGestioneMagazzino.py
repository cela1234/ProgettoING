# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gestioneMagazzino.ui'
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

import Resources.icons

class Ui_formMagazzino(object):
    def setupUi(self, formMagazzino):
        formMagazzino.setObjectName("Dialog")
        formMagazzino.resize(782, 660)
        formMagazzino.setStyleSheet("background-color: rgb(159, 197, 248);")
        self.tableMagazzino = QtWidgets.QTableWidget(formMagazzino)
        self.tableMagazzino.setGeometry(QtCore.QRect(10, 10, 520, 571))
        self.tableMagazzino.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableMagazzino.setObjectName("tableMagazzino")
        self.tableMagazzino.setRowCount(0)
        self.tableMagazzino.setColumnCount(9)
        self.btIndietro = QtWidgets.QPushButton(formMagazzino)
        self.btIndietro.setGeometry(QtCore.QRect(10, 600, 51, 51))
        self.btIndietro.setStyleSheet("\n"
"image: url(:/icone/Icons/arrow-left.svg);")
        self.btIndietro.setText("")
        self.btIndietro.setObjectName("btIndietro")
        self.line = QtWidgets.QFrame(formMagazzino)
        self.line.setGeometry(QtCore.QRect(0, 580, 771, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.txtCerca = QtWidgets.QLineEdit(formMagazzino)
        self.txtCerca.setGeometry(QtCore.QRect(540, 10, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.txtCerca.setFont(font)
        self.txtCerca.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtCerca.setText("")
        self.txtCerca.setObjectName("txtCerca")
        #self.btMostraDettaglio = QtWidgets.QPushButton(Dialog)
        #self.btMostraDettaglio.setGeometry(QtCore.QRect(540, 50, 231, 91))
        #font = QtGui.QFont()
        #font.setFamily("Georgia")
        #font.setPointSize(14)
        #self.btMostraDettaglio.setFont(font)
        #self.btMostraDettaglio.setStyleSheet("background-color: rgb(245, 243, 201);")
        #self.btMostraDettaglio.setObjectName("btMostraDettaglio")
        self.btInserisciElemento = QtWidgets.QPushButton(formMagazzino)
        self.btInserisciElemento.setGeometry(QtCore.QRect(540, 50, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.btInserisciElemento.setFont(font)
        self.btInserisciElemento.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.btInserisciElemento.setObjectName("btInserisciElemento")
        self.btModificaElemento = QtWidgets.QPushButton(formMagazzino)
        self.btModificaElemento.setGeometry(QtCore.QRect(540, 100, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.btModificaElemento.setFont(font)
        self.btModificaElemento.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.btModificaElemento.setObjectName("btModificaElemento")
        self.btRimuoviElemento = QtWidgets.QPushButton(formMagazzino)
        self.btRimuoviElemento.setGeometry(QtCore.QRect(540, 150, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.btRimuoviElemento.setFont(font)
        self.btRimuoviElemento.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.btRimuoviElemento.setObjectName("btRimuoviElemento")
        self.btRimuoviElemento.clicked.connect(self.btRimuoviClicked)
        self.tableMagazzino.setColumnCount(6)
        self.tableMagazzino.setHorizontalHeaderLabels(["id", "Nome", "Prezzo", "Quantità", "Data di scadenza", "Fornitore"])
        self.btVisualizzaTabellaNomi = QtWidgets.QPushButton(formMagazzino)
        self.btVisualizzaTabellaNomi.setGeometry(QtCore.QRect(540, 200, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.btVisualizzaTabellaNomi.setFont(font)
        self.btVisualizzaTabellaNomi.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.btVisualizzaTabellaNomi.setObjectName("btVisualizzaTabellaNomi")
        QtCore.QMetaObject.connectSlotsByName(formMagazzino)
        self.retranslateUi(formMagazzino)
        self.init_db()
        self.load_data_tabella()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Gestione magazzino - Admin"))
        self.txtCerca.setPlaceholderText(_translate("Dialog", "Cerca"))
        #self.btMostraDettaglio.setText(_translate("Dialog", "Mostra informazioni dell\'\n"
#"elemento selezionato"))
        self.btInserisciElemento.setText(_translate("Dialog", "Inserisci elemento"))
        self.btModificaElemento.setText(_translate("Dialog", "Modifica elemento"))
        self.btRimuoviElemento.setText(_translate("Dialog", "Elimina elemento"))
        self.btVisualizzaTabellaNomi.setText(_translate("Dialog", "Visualizza schermata\n dei nomi"))
        self.tableMagazzino.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)

    def init_db(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="alessio",
            database="mydbristorante"
        )
        self.model = QSqlQueryModel()
        self.cursor = self.db.cursor()

    def load_data_tabella(self):
        cur = self.cursor
        query = """select elementomagazzino.id, nome, prezzo, quantita, scadenza, fornitore
        from elementomagazzino inner join nomeelemento
        on elementomagazzino.idNomeElemento = nomeelemento.id"""
        cur.execute(query)
        result = cur.fetchall()
        self.tableMagazzino.setRowCount(0)
        for row_number, row_data in enumerate(result):
            print(row_number)
            self.tableMagazzino.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                print(f"{data}, {column_number}")
                if column_number == 2:
                    self.tableMagazzino.setItem(row_number, column_number, QTableWidgetItem("€"+str(data)))
                else:
                    self.tableMagazzino.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.tableMagazzino.resizeColumnsToContents()

    def btRimuoviClicked(self):
        selectedRow = self.tableMagazzino.currentRow()
        if selectedRow == -1:
            dlg = QMessageBox()
            dlg.setWindowTitle("Errore")
            dlg.setText("Non hai selezionato nessun elemento!")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.exec()
        else:
            dlg = QMessageBox()
            dlg.setWindowTitle("Eliminazione elemento magazzino")
            dlg.setText(f"Sicuro di voler eliminare l'elemento del magazzino con nome: {self.tableMagazzino.item(selectedRow, 1).text()} del fornitore {self.tableMagazzino.item(selectedRow, 5).text()}")
            cur = self.cursor
            dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dlg.setIcon(QMessageBox.Warning)
            button = dlg.exec()

            if button == QMessageBox.Yes:
                query = f"DELETE FROM elementomagazzino WHERE id = {self.tableMagazzino.item(selectedRow, 0).text()}"
                cur.execute(query)
                self.db.commit()
            self.load_data_tabella()




if __name__ == "__main__":
            import sys
            app = QtWidgets.QApplication(sys.argv)
            formGestioneMagazzino = QtWidgets.QDialog()
            ui = (Ui_formMagazzino())
            ui.setupUi(formGestioneMagazzino)
            formGestioneMagazzino.show()
            sys.exit(app.exec_())

