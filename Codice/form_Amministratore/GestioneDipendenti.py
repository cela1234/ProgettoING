import mysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from db_connection import get_connection

from .inserisci_dipendente import Ui_formInserisciDipendente


class Ui_formGestioneDipendenti(object):
    def setupUi(self, formGestioneDipendenti):
        formGestioneDipendenti.setObjectName("formGestioneDipendenti")
        formGestioneDipendenti.resize(708, 547)
        formGestioneDipendenti.setStyleSheet("background-color: rgb(159, 197, 248);")
        self.twDipendenti = QtWidgets.QTableWidget(formGestioneDipendenti)
        self.twDipendenti.setGeometry(QtCore.QRect(10, 100, 511, 421))
        self.twDipendenti.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.twDipendenti.setFont(font)
        self.twDipendenti.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.twDipendenti.setObjectName("twDipendenti")
        self.twDipendenti.setColumnCount(3)
        self.twDipendenti.setColumnWidth(0, 9)
        self.twDipendenti.setColumnWidth(1, 280)
        self.twDipendenti.setColumnWidth(2, 155)
        self.twDipendenti.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twDipendenti.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twDipendenti.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twDipendenti.setHorizontalHeaderItem(2, item)
        self.line_sopra = QtWidgets.QFrame(formGestioneDipendenti)
        self.line_sopra.setGeometry(QtCore.QRect(-10, 50, 791, 16))
        self.line_sopra.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_sopra.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_sopra.setObjectName("line_sopra")
        self.lbl_titolo_gtd = QtWidgets.QLabel(formGestioneDipendenti)
        self.lbl_titolo_gtd.setGeometry(QtCore.QRect(10, 10, 551, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(18)
        self.lbl_titolo_gtd.setFont(font)
        self.lbl_titolo_gtd.setObjectName("lbl_titolo_gtd")
        self.btNuovoDipendente = QtWidgets.QPushButton(formGestioneDipendenti)
        self.btNuovoDipendente.setGeometry(QtCore.QRect(550, 100, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.btNuovoDipendente.setFont(font)
        self.btNuovoDipendente.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.btNuovoDipendente.setObjectName("btNuovoDipendente")
        self.btEliminaDipendente = QtWidgets.QPushButton(formGestioneDipendenti)
        self.btEliminaDipendente.setGeometry(QtCore.QRect(550, 200, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.btEliminaDipendente.setFont(font)
        self.btEliminaDipendente.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.btEliminaDipendente.setObjectName("btEliminaDipendente")


        self.retranslateUi(formGestioneDipendenti)
        QtCore.QMetaObject.connectSlotsByName(formGestioneDipendenti)

        # Collegare i pulsanti ai rispettivi metodi
        self.popolaTwDipendenti()
        self.btNuovoDipendente.clicked.connect(self.btNuovoDipendenteClicked)
        self.btEliminaDipendente.clicked.connect(self.btEliminaDipendenteClicked)

    def retranslateUi(self, formGestioneDipendenti):
        _translate = QtCore.QCoreApplication.translate
        formGestioneDipendenti.setWindowTitle(_translate("formGestioneDipendenti", "Gestione Dipendenti"))
        item = self.twDipendenti.horizontalHeaderItem(0)
        item.setText(_translate("formGestioneDipendenti", "ID"))
        item = self.twDipendenti.horizontalHeaderItem(1)
        item.setText(_translate("formGestioneDipendenti", "Nome"))
        item = self.twDipendenti.horizontalHeaderItem(2)
        item.setText(_translate("formGestioneDipendenti", "Ruolo"))
        self.lbl_titolo_gtd.setText(_translate("formGestioneDipendenti", "Gestione Dipendenti "))
        self.btNuovoDipendente.setText(_translate("formGestioneDipendenti", "Nuovo Dipendente"))
        self.btEliminaDipendente.setText(_translate("formGestioneDipendenti", "Elimina Dipendente"))

    def btNuovoDipendenteClicked(self):
        dialog = QDialog()
        ui = Ui_formInserisciDipendente()
        ui.setupUi(dialog)
        dialog.exec_()
        self.popolaTwDipendenti()

    def btEliminaDipendenteClicked(self):
        selected_row = self.twDipendenti.currentRow()
        if selected_row >= 0:
            id_dipendente = self.twDipendenti.item(selected_row, 0).text()
            try:

                # Ora puoi utilizzare la connessione così:
                myconn = get_connection()
                cursor = myconn.cursor()
                query = "DELETE FROM dipendente WHERE ID = %s"
                cursor.execute(query, (id_dipendente,))
                myconn.commit()
                cursor.close()
                myconn.close()
                QMessageBox.information(None, "Successo", "Dipendente eliminato con successo!")
                self.popolaTwDipendenti()
            except mysql.connector.Error as err:
                QMessageBox.critical(None, "Errore", f"Errore durante l'eliminazione: {err}")
        else:
            QMessageBox.warning(None, "Errore", "Seleziona un dipendente da eliminare!")

    def popolaTwDipendenti(self):
        try:

            myconn = get_connection()

            cursor = myconn.cursor()
            cursor.execute("SELECT ID, cognomenome, ruolo FROM dipendente")
            results = cursor.fetchall()

            # Imposta il numero di righe e colonne della tabella
            self.twDipendenti.setRowCount(len(results))
            self.twDipendenti.setColumnCount(3)
            self.twDipendenti.setHorizontalHeaderLabels(['ID', 'Nome', 'Ruolo'])

            # Popola la tabella con i dati del database
            for row_index, row_data in enumerate(results):
                for column_index, data in enumerate(row_data):
                    self.twDipendenti.setItem(row_index, column_index, QtWidgets.QTableWidgetItem(str(data)))

            # Chiudere il cursore e la connessione al database
            cursor.close()
            myconn.close()

        except mysql.connector.Error as err:
            print(f"Errore durante l'accesso al database: {err}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formGestioneDipendenti = QtWidgets.QDialog()
    ui = Ui_formGestioneDipendenti()
    ui.setupUi(formGestioneDipendenti)
    formGestioneDipendenti.show()
    sys.exit(app.exec_())
