# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formAggiungiModificaElementoMagazzino.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDoubleSpinBox
import mysql
import mysql.connector
from PyQt5.QtSql import QSqlQueryModel
import classi.GestoriDB.GestoreElementiMagazzino as GestoreDBMagazzino



class Ui_formCU_elementoMagazzino(object):
    def setupUi(self, formCU_elementoMagazzino):
        self.idToUpdate = -1
        self.fCUelementoMagazzino = formCU_elementoMagazzino
        formCU_elementoMagazzino.setObjectName("formCU_elementoMagazzino")
        formCU_elementoMagazzino.resize(291, 568)
        formCU_elementoMagazzino.setStyleSheet("background-color: rgb(159, 197, 248);")
        self.label = QtWidgets.QLabel(formCU_elementoMagazzino)
        self.label.setGeometry(QtCore.QRect(10, 20, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(formCU_elementoMagazzino)
        self.label_2.setGeometry(QtCore.QRect(10, 360, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(formCU_elementoMagazzino)
        self.label_3.setGeometry(QtCore.QRect(10, 400, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(formCU_elementoMagazzino)
        self.label_4.setGeometry(QtCore.QRect(10, 440, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(formCU_elementoMagazzino)
        self.label_5.setGeometry(QtCore.QRect(10, 480, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txtFornitore = QtWidgets.QLineEdit(formCU_elementoMagazzino)
        self.txtFornitore.setGeometry(QtCore.QRect(110, 470, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.txtFornitore.setFont(font)
        self.txtFornitore.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtFornitore.setText("")
        self.txtFornitore.setObjectName("txtFornitore")
        # self.txtQuantita = QtWidgets.QLineEdit(formCU_elementoMagazzino)
        # self.txtQuantita.setGeometry(QtCore.QRect(110, 390, 171, 31))
        # font = QtGui.QFont()
        # font.setFamily("Georgia")
        # font.setPointSize(14)
        # self.txtQuantita.setFont(font)
        # self.txtQuantita.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.txtQuantita.setText("")
        # self.txtQuantita.setObjectName("txtQuantita")
        # self.txtPrezzo = QtWidgets.QLineEdit(formCU_elementoMagazzino)
        # self.txtPrezzo.setGeometry(QtCore.QRect(110, 350, 171, 31))
        # font = QtGui.QFont()
        # font.setFamily("Georgia")
        # font.setPointSize(14)
        # self.txtPrezzo.setFont(font)
        # self.txtPrezzo.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.txtPrezzo.setText("")
        # self.txtPrezzo.setObjectName("txtPrezzo")
        self.dateEditScadenza = QtWidgets.QDateEdit(formCU_elementoMagazzino)
        self.dateEditScadenza.setGeometry(QtCore.QRect(110, 431, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.dateEditScadenza.setFont(font)
        self.dateEditScadenza.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEditScadenza.setObjectName("dateEditScadenza")
        self.btEsegui = QtWidgets.QPushButton(formCU_elementoMagazzino)
        self.btEsegui.setGeometry(QtCore.QRect(10, 510, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.btEsegui.setFont(font)
        self.btEsegui.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.btEsegui.setObjectName("btEsegui")
        self.listaNomi = QtWidgets.QListWidget(formCU_elementoMagazzino)
        self.listaNomi.setObjectName("listaNomi")
        self.listaNomi.setGeometry(QtCore.QRect(10, 50, 271, 291))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.listaNomi.setFont(font)
        self.listaNomi.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listaNomi.setViewMode(QtWidgets.QListView.ListMode)
        self.listaNomi.setObjectName("listWidget")
        self.btHelp = QtWidgets.QPushButton(formCU_elementoMagazzino)
        self.btHelp.setGeometry(QtCore.QRect(250, 10, 31, 31))
        self.btHelp.setStyleSheet("image: url(:/icone/Icons/help-circle.svg);")
        self.btHelp.setText("")
        self.btHelp.setObjectName("btHelp")
        self.btHelp.clicked.connect(self.btHelpClicked)
        self.numberQuantita = QDoubleSpinBox(formCU_elementoMagazzino)
        self.numberQuantita.setObjectName(u"numberQuantita")
        self.numberQuantita.setGeometry(QtCore.QRect(110, 390, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.numberQuantita.setFont(font)
        self.numberQuantita.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.numberPrezzo = QDoubleSpinBox(formCU_elementoMagazzino)
        self.numberPrezzo.setObjectName(u"numberPrezzo")
        self.numberPrezzo.setGeometry(QtCore.QRect(110, 350, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.numberPrezzo.setFont(font)
        self.numberPrezzo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.numberPrezzo.setMaximum(10000.00)
        self.numberQuantita.setMaximum(10000.00)
        self.btEsegui.clicked.connect(self.btEseguiClicked)

        self.load_data_list()
        self.retranslateUi(formCU_elementoMagazzino)
        QtCore.QMetaObject.connectSlotsByName(formCU_elementoMagazzino)

    def retranslateUi(self, formCU_elementoMagazzino):
        _translate = QtCore.QCoreApplication.translate
        formCU_elementoMagazzino.setWindowTitle(_translate("formCU_elementoMagazzino", "Dialog"))
        self.label.setText(_translate("formCU_elementoMagazzino", "Nome:"))
        self.label_2.setText(_translate("formCU_elementoMagazzino", "Prezzo:"))
        self.label_3.setText(_translate("formCU_elementoMagazzino", "Quantità:"))
        self.label_4.setText(_translate("formCU_elementoMagazzino", "Scadenza:"))
        self.label_5.setText(_translate("formCU_elementoMagazzino", "Fornitore:"))
        self.btEsegui.setText(_translate("formCU_elementoMagazzino", "Esegui operazione"))

    def btHelpClicked(self):
        dlg = QMessageBox()
        dlg.setWindowTitle("Info")
        dlg.setText("Se non vedi il nome che vuoi nella lista, devi prima aggiungerlo nella tabella dei nomi!")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(QMessageBox.Information)
        dlg.exec()


    def load_data_list(self):
        result = GestoreDBMagazzino.ottieniNomiElementiCUelementoMagazzino()
        self.listaIdNomi = []
        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                if column_number == 0:
                    self.listaIdNomi.append(str(data))
                else:
                    self.listaNomi.addItem(str(data))
        self.fCUelementoMagazzino.close()


    def btEseguiClicked(self):
        indiceNomeSelezionato = self.listaNomi.currentRow()
        Fornitore = self.txtFornitore.text().strip()
        quantita = self.numberQuantita.value()
        if indiceNomeSelezionato == -1:
            self.showErrorMessage("Non é possibile inserire un elemento senza aver selezionato un nome.")
            return
        if not Fornitore:
            self.showErrorMessage("Il campo 'Fornitore' non può essere vuoto.")
            return
        if quantita == 0:
            self.showErrorMessage("Il campo 'quantitá' non può essere 0.")
        dlg = QMessageBox()
        dlg.setWindowTitle("Conferma")
        dlg.setText("Sei sicuro di voler proseguire?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Warning)
        button = dlg.exec()
        if button == QMessageBox.Yes:
            idNomeElemento = int(self.listaIdNomi[indiceNomeSelezionato])
            Prezzo = float(self.numberPrezzo.text().replace(',', '.'))
            Quantita = float(self.numberQuantita.text().replace(',', '.'))
            DataDiScadenza = self.dateEditScadenza.date().toString('yyyy-MM-dd')

            if self.idToUpdate == -1:
                query = f"INSERT INTO elementomagazzino(idNomeElemento, Prezzo, Quantita, Scadenza, Fornitore) VALUES ({idNomeElemento}, {Prezzo}, {Quantita}, '{DataDiScadenza}', '{Fornitore}')"
                GestoreDBMagazzino.eseguiQuery(query)
                self.fCUelementoMagazzino.close()
            else:
                query = f"UPDATE elementomagazzino SET idNomeElemento = {idNomeElemento}, Prezzo = {Prezzo}, Quantita = {Quantita}, Scadenza = '{DataDiScadenza}', Fornitore = '{Fornitore}' WHERE id = {self.idToUpdate}"
                GestoreDBMagazzino.eseguiQuery(query)
                self.fCUelementoMagazzino.close()

    def showErrorMessage(self, message):
        dlg = QMessageBox()
        dlg.setWindowTitle("Errore")
        dlg.setText(message)
        dlg.setIcon(QMessageBox.Critical)
        dlg.exec()

