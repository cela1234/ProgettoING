# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuAmministratore.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import Resources.icons

class Ui_formAmministratore(object):
    def setupUi(self, formAmministratore):
        formAmministratore.setObjectName("formAmministratore")
        formAmministratore.resize(971, 522)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 197, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 226, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 98, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 131, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 197, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 226, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 197, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 226, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 98, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 131, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 197, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 226, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 98, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 197, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 226, 251))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 98, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 131, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 98, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 98, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 197, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 197, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 197, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        formAmministratore.setPalette(palette)
        self.btAnalisiDati = QtWidgets.QPushButton(formAmministratore)
        self.btAnalisiDati.setGeometry(QtCore.QRect(330, 160, 311, 131))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btAnalisiDati.setFont(font)
        self.btAnalisiDati.setStyleSheet("\n"
"background-color: rgb(245, 243, 201);")
        self.btAnalisiDati.setObjectName("btAnalisiDati")
        self.btMagazzino = QtWidgets.QPushButton(formAmministratore)
        self.btMagazzino.setGeometry(QtCore.QRect(10, 10, 311, 131))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(245, 243, 201))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 243, 201))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 243, 201))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 243, 201))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 243, 201))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 243, 201))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 243, 201))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 243, 201))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 243, 201))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btMagazzino.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.btMagazzino.setFont(font)
        self.btMagazzino.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.btMagazzino.setObjectName("btMagazzino")
        self.btOrdinazioni = QtWidgets.QPushButton(formAmministratore)
        self.btOrdinazioni.setGeometry(QtCore.QRect(10, 160, 311, 131))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btOrdinazioni.setFont(font)
        self.btOrdinazioni.setStyleSheet("\n"
"background-color: rgb(245, 243, 201);")
        self.btOrdinazioni.setObjectName("btOrdinazioni")
        self.btUtenti = QtWidgets.QPushButton(formAmministratore)
        self.btUtenti.setGeometry(QtCore.QRect(500, 300, 311, 131))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btUtenti.setFont(font)
        self.btUtenti.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.btUtenti.setObjectName("btUtenti")
        self.btDipendenti = QtWidgets.QPushButton(formAmministratore)
        self.btDipendenti.setGeometry(QtCore.QRect(180, 300, 311, 131))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.btDipendenti.setFont(font)
        self.btDipendenti.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.btDipendenti.setObjectName("btDipendenti")
        self.btMenu = QtWidgets.QPushButton(formAmministratore)
        self.btMenu.setGeometry(QtCore.QRect(330, 10, 311, 131))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(245, 243, 201))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 243, 201))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 243, 201))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 243, 201))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 243, 201))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 243, 201))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 243, 201))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 243, 201))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 243, 201))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btMenu.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.btMenu.setFont(font)
        self.btMenu.setAutoFillBackground(False)
        self.btMenu.setStyleSheet("\n"
"background-color: rgb(245, 243, 201);")
        self.btMenu.setObjectName("btMenu")
        self.btPrenotazioni = QtWidgets.QPushButton(formAmministratore)
        self.btPrenotazioni.setGeometry(QtCore.QRect(650, 10, 311, 131))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.btPrenotazioni.setFont(font)
        self.btPrenotazioni.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.btPrenotazioni.setObjectName("btPrenotazioni")
        self.btFatture = QtWidgets.QPushButton(formAmministratore)
        self.btFatture.setGeometry(QtCore.QRect(650, 160, 311, 131))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btFatture.setFont(font)
        self.btFatture.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.btFatture.setObjectName("btFatture")
        self.widgetLogout = QtWidgets.QWidget(formAmministratore)
        self.widgetLogout.setGeometry(QtCore.QRect(10, 450, 61, 61))
        self.widgetLogout.setStyleSheet("image: url(:/icone/Icons/log-out.svg);")
        self.widgetLogout.setObjectName("widgetLogout")
        self.btLogout = QtWidgets.QPushButton(formAmministratore)
        self.btLogout.setGeometry(QtCore.QRect(80, 460, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btLogout.setFont(font)
        self.btLogout.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.btLogout.setObjectName("btLogout")
        self.line = QtWidgets.QFrame(formAmministratore)
        self.line.setGeometry(QtCore.QRect(0, 430, 971, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btAnalisiDati.raise_()
        self.btOrdinazioni.raise_()
        self.btUtenti.raise_()
        self.btDipendenti.raise_()
        self.btMenu.raise_()
        self.btPrenotazioni.raise_()
        self.btFatture.raise_()
        self.widgetLogout.raise_()
        self.btLogout.raise_()
        self.line.raise_()
        self.btMagazzino.raise_()

        self.btMagazzino.clicked.connect(self.btMagazzinoClicked)


        self.retranslateUi(formAmministratore)
        QtCore.QMetaObject.connectSlotsByName(formAmministratore)

    def retranslateUi(self, formAmministratore):
        _translate = QtCore.QCoreApplication.translate
        formAmministratore.setWindowTitle(_translate("formAmministratore", "Schermata principale amminstratore - Il Giardino"))
        self.btAnalisiDati.setText(_translate("formAmministratore", "Analisi dei dati"))
        self.btMagazzino.setText(_translate("formAmministratore", "Gestione del magazzino"))
        self.btOrdinazioni.setText(_translate("formAmministratore", "Gestione delle ordinazioni"))
        self.btUtenti.setText(_translate("formAmministratore", "Gestione degli utenti"))
        self.btDipendenti.setText(_translate("formAmministratore", "Gestione dei \ndipendenti - turni"))
        self.btMenu.setText(_translate("formAmministratore", "Gestione del Menu"))
        self.btPrenotazioni.setText(_translate("formAmministratore", "Gestione delle prenotazioni"))
        self.btFatture.setText(_translate("formAmministratore", "Gestione delle fatture"))
        self.btLogout.setText(_translate("formAmministratore", "Log Out"))


    def btMagazzinoClicked(self):
        import formGestioneMagazzino
        self.formGestioneMagazzino = QtWidgets.QDialog()
        self.uiMagazzino = formGestioneMagazzino.Ui_formMagazzino()
        self.uiMagazzino.setupUi(self.formGestioneMagazzino, formAmm)
        self.formGestioneMagazzino.show()
        formAmm.hide()
        



if __name__ == "__main__":
            import sys
            app = QtWidgets.QApplication(sys.argv)
            formAmm = QtWidgets.QDialog()
            ui = Ui_formAmministratore()
            ui.setupUi(formAmm)
            formAmm.show()
            sys.exit(app.exec_())

