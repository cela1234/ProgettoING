# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DettaglioProdotto.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

import classi.GestoriDB.GestoreProdottiMenu as GestoreDBMenu
from PyQt5.QtSql import QSqlQueryModel

class Ui_DettaglioProdotto(object):
    def setupUi(self, DettaglioProdotto, idProdotto):
        self.idProdotto = idProdotto
        DettaglioProdotto.setObjectName("DettaglioProdotto")
        DettaglioProdotto.resize(443, 461)
        DettaglioProdotto.setStyleSheet("background-color: rgb(159, 197, 248);")
        self.formLayout = QtWidgets.QFormLayout(DettaglioProdotto)
        self.formLayout.setObjectName("formLayout")
        self.lbNome = QtWidgets.QLabel(DettaglioProdotto)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.lbNome.setFont(font)
        self.lbNome.setText("")
        self.lbNome.setObjectName("lbNome")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lbNome)
        self.label_2 = QtWidgets.QLabel(DettaglioProdotto)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lbCategoria = QtWidgets.QLabel(DettaglioProdotto)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.lbCategoria.setFont(font)
        self.lbCategoria.setText("")
        self.lbCategoria.setObjectName("lbCategoria")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lbCategoria)
        self.lbPrezzo = QtWidgets.QLabel(DettaglioProdotto)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.lbPrezzo.setFont(font)
        self.lbPrezzo.setText("")
        self.lbPrezzo.setObjectName("lbPrezzo")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lbPrezzo)
        self.label_5 = QtWidgets.QLabel(DettaglioProdotto)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.tableIngredienti = QtWidgets.QTableWidget(DettaglioProdotto)
        self.tableIngredienti.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableIngredienti.setObjectName("tableIngredienti")
        self.tableIngredienti.setColumnCount(0)
        self.tableIngredienti.setRowCount(0)
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.tableIngredienti)
        self.label_4 = QtWidgets.QLabel(DettaglioProdotto)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label = QtWidgets.QLabel(DettaglioProdotto)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_3 = QtWidgets.QLabel(DettaglioProdotto)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txtDescrizione = QtWidgets.QTextBrowser(DettaglioProdotto)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.txtDescrizione.setFont(font)
        self.txtDescrizione.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtDescrizione.setObjectName("txtDescrizione")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.txtDescrizione)
        self.tableIngredienti.setColumnCount(5)
        self.tableIngredienti.verticalHeader().setVisible(False)
        self.tableIngredienti.setHorizontalHeaderLabels(["Nome", "Quantità", "Piccante", "Vegano", "Intolleranze"])
        self.retranslateUi(DettaglioProdotto)
        QtCore.QMetaObject.connectSlotsByName(DettaglioProdotto)
        self.inserisciDati()

    def retranslateUi(self, DettaglioProdotto):
        _translate = QtCore.QCoreApplication.translate
        DettaglioProdotto.setWindowTitle(_translate("DettaglioProdotto", "Dettaglio prodotto"))
        self.label_2.setText(_translate("DettaglioProdotto", "Categoria:"))
        self.label_5.setText(_translate("DettaglioProdotto", "Ingredienti:"))
        self.label_4.setText(_translate("DettaglioProdotto", "Prezzo:"))
        self.label.setText(_translate("DettaglioProdotto", "Nome:"))
        self.label_3.setText(_translate("DettaglioProdotto", "Descrizione:"))
        self.txtDescrizione.setHtml(_translate("DettaglioProdotto", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Georgia\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p></body></html>"))

    def inserisciDati(self):
        DatiProdotto = GestoreDBMenu.ottieniProdottoSpecifico(self.idProdotto)
        DatiIngredienti = GestoreDBMenu.ottieniIngredientiProdotto(self.idProdotto)
        self.lbNome.setText(str(DatiProdotto[0][1]))
        self.lbPrezzo.setText("€"+str(DatiProdotto[0][4]))
        self.lbCategoria.setText(str(DatiProdotto[0][3]))
        self.txtDescrizione.setText(str(DatiProdotto[0][2]))
        for row_number, row_data in enumerate(DatiIngredienti):
            print(row_number)
            self.tableIngredienti.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                print(f"{data}, {column_number}")
                if column_number == 2 or column_number == 3:
                    if data == 0:
                        self.tableIngredienti.setItem(row_number, column_number, QTableWidgetItem("No"))
                    else:
                        self.tableIngredienti.setItem(row_number, column_number, QTableWidgetItem("Si"))
                else:
                    self.tableIngredienti.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.tableIngredienti.resizeColumnsToContents()
