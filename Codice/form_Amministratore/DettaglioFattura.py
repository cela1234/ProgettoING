from PyQt5 import QtCore, QtGui, QtWidgets
from db_connection import get_connection
from PyQt5.QtWidgets import QMessageBox


class Ui_Dialog(object):

    def setupUi(self, idOrdinazione, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(460, 461)
        Dialog.setStyleSheet("background-color: rgb(159, 197, 248);")
        self.label_titolo_lista_ordini = QtWidgets.QLabel(Dialog)
        self.label_titolo_lista_ordini.setGeometry(QtCore.QRect(10, 0, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_titolo_lista_ordini.setFont(font)
        self.label_titolo_lista_ordini.setObjectName("label_titolo_lista_ordini")
        self.lblNumeroFattura = QtWidgets.QLabel(Dialog)
        self.lblNumeroFattura.setGeometry(QtCore.QRect(240, 0, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lblNumeroFattura.setFont(font)
        self.lblNumeroFattura.setText("")
        self.lblNumeroFattura.setObjectName("lblNumeroFattura")
        self.twProdotti = QtWidgets.QTableWidget(Dialog)
        self.twProdotti.setGeometry(QtCore.QRect(20, 70, 421, 371))
        self.twProdotti.setObjectName("twProdotti")
        self.twProdotti.setColumnCount(3)
        self.twProdotti.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twProdotti.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twProdotti.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twProdotti.setHorizontalHeaderItem(2, item)
        self.twProdotti.setStyleSheet("QTableWidget::item { background-color: white; }")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.caricaFattura(idOrdinazione)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dettaglio Fattura"))
        self.label_titolo_lista_ordini.setText(_translate("Dialog", f"Dettaglio fattura N. "))
        item = self.twProdotti.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Nome"))
        item = self.twProdotti.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Categoria"))
        item = self.twProdotti.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Prezzo"))

    def caricaFattura(self, idOrdinazione):
        db = None
        cursor = None

        try:
            db = get_connection()
            cursor = db.cursor()

            query = """
                SELECT pm.nome, pm.categoria, pm.prezzo
                FROM elementoordine eo
                JOIN prodottomenu pm ON eo.idProdotto = pm.id
                WHERE eo.idOrdinazione = %s
            """
            cursor.execute(query, (idOrdinazione,))
            prodotti = cursor.fetchall()

            self.twProdotti.setRowCount(len(prodotti))

            for row_num, row_data in enumerate(prodotti):
                self.twProdotti.setItem(row_num, 0, QtWidgets.QTableWidgetItem(row_data[0]))
                self.twProdotti.setItem(row_num, 1, QtWidgets.QTableWidgetItem(row_data[1]))
                self.twProdotti.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(row_data[2])))

        except mysql.connector.Error as err:
            QMessageBox.critical(None, "Errore", f"Errore: {err}")
        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(1, Dialog)  # Passa un idOrdinazione di esempio
    Dialog.show()
    sys.exit(app.exec_())
