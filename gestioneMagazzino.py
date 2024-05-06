# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gestioneMagazzino.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import Resources.icons

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(782, 660)
        Dialog.setStyleSheet("background-color: rgb(159, 197, 248);")
        self.tableMagazzino = QtWidgets.QTableView(Dialog)
        self.tableMagazzino.setGeometry(QtCore.QRect(10, 10, 511, 571))
        self.tableMagazzino.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableMagazzino.setObjectName("tableMagazzino")
        self.btIndietro = QtWidgets.QPushButton(Dialog)
        self.btIndietro.setGeometry(QtCore.QRect(10, 600, 51, 51))
        self.btIndietro.setStyleSheet("\n"
"image: url(:/icone/Icons/arrow-left.svg);")
        self.btIndietro.setText("")
        self.btIndietro.setObjectName("btIndietro")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 580, 771, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.txtCerca = QtWidgets.QLineEdit(Dialog)
        self.txtCerca.setGeometry(QtCore.QRect(540, 10, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.txtCerca.setFont(font)
        self.txtCerca.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtCerca.setText("")
        self.txtCerca.setObjectName("txtCerca")
        self.btMostraDettaglio = QtWidgets.QPushButton(Dialog)
        self.btMostraDettaglio.setGeometry(QtCore.QRect(540, 50, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.btMostraDettaglio.setFont(font)
        self.btMostraDettaglio.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.btMostraDettaglio.setObjectName("btMostraDettaglio")
        self.btInserisciElemento = QtWidgets.QPushButton(Dialog)
        self.btInserisciElemento.setGeometry(QtCore.QRect(540, 150, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.btInserisciElemento.setFont(font)
        self.btInserisciElemento.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.btInserisciElemento.setObjectName("btInserisciElemento")
        self.btModificaElemento = QtWidgets.QPushButton(Dialog)
        self.btModificaElemento.setGeometry(QtCore.QRect(540, 200, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.btModificaElemento.setFont(font)
        self.btModificaElemento.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.btModificaElemento.setObjectName("btModificaElemento")
        self.btRimuoviElemento = QtWidgets.QPushButton(Dialog)
        self.btRimuoviElemento.setGeometry(QtCore.QRect(540, 250, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.btRimuoviElemento.setFont(font)
        self.btRimuoviElemento.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.btRimuoviElemento.setObjectName("btRimuoviElemento")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Gestione magazzino - Admin"))
        self.txtCerca.setPlaceholderText(_translate("Dialog", "Cerca"))
        self.btMostraDettaglio.setText(_translate("Dialog", "Mostra informazioni dell\'\n"
"elemento selezionato"))
        self.btInserisciElemento.setText(_translate("Dialog", "Inserisci elemento"))
        self.btModificaElemento.setText(_translate("Dialog", "Modifica elemento"))
        self.btRimuoviElemento.setText(_translate("Dialog", "Elimina elemento"))
if __name__ == "__main__":
            import sys
            app = QtWidgets.QApplication(sys.argv)
            formGestioneMagazzino = QtWidgets.QDialog()
            ui = (Ui_Dialog())
            ui.setupUi(formGestioneMagazzino)
            formGestioneMagazzino.show()
            sys.exit(app.exec_())
