# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AggiungiProdottoMenù.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
import mysql.connector
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.uic import loadUi
from db_connection import get_connection


class Ui_Form(object):
    def setupUi(self, Form):
        self.FormAPM = Form
        self.conn = get_connection()
        Form.setObjectName("Form")
        Form.resize(663, 837)
        Form.setStyleSheet("background-color: rgb(159, 197, 248);")
        self.lbl_categoria = QtWidgets.QLabel(Form)
        self.lbl_categoria.setGeometry(QtCore.QRect(400, 180, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.lbl_categoria.setFont(font)
        self.lbl_categoria.setObjectName("lbl_categoria")
        self.lineEdit_nome = QtWidgets.QLineEdit(Form)
        self.lineEdit_nome.setGeometry(QtCore.QRect(10, 110, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.lineEdit_nome.setFont(font)
        self.lineEdit_nome.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.bt_aggiungi = QtWidgets.QPushButton(Form)
        self.bt_aggiungi.setGeometry(QtCore.QRect(440, 470, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.bt_aggiungi.setFont(font)
        self.bt_aggiungi.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.bt_aggiungi.setObjectName("bt_aggiungi")
        self.line_sopra2 = QtWidgets.QFrame(Form)
        self.line_sopra2.setGeometry(QtCore.QRect(0, 350, 681, 16))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.line_sopra2.setFont(font)
        self.line_sopra2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_sopra2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_sopra2.setObjectName("line_sopra2")
        self.lbl_nome = QtWidgets.QLabel(Form)
        self.lbl_nome.setGeometry(QtCore.QRect(20, 70, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.lbl_nome.setFont(font)
        self.lbl_nome.setObjectName("lbl_nome")
        self.line_sopra = QtWidgets.QFrame(Form)
        self.line_sopra.setGeometry(QtCore.QRect(0, 330, 691, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.line_sopra.setFont(font)
        self.line_sopra.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_sopra.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_sopra.setObjectName("line_sopra")
        self.lineEdit_info = QtWidgets.QLineEdit(Form)
        self.lineEdit_info.setGeometry(QtCore.QRect(10, 220, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.lineEdit_info.setFont(font)
        self.lineEdit_info.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.lineEdit_info.setObjectName("lineEdit_info")
        self.lbl_quantit = QtWidgets.QLabel(Form)
        self.lbl_quantit.setGeometry(QtCore.QRect(420, 410, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.lbl_quantit.setFont(font)
        self.lbl_quantit.setObjectName("lbl_quantit")
        self.tw_Ingredienti = QtWidgets.QTableWidget(Form)
        self.tw_Ingredienti.setGeometry(QtCore.QRect(20, 650, 621, 171))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.tw_Ingredienti.setFont(font)
        self.tw_Ingredienti.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.tw_Ingredienti.setObjectName("tw_Ingredienti")
        self.tw_Ingredienti.setColumnCount(5)
        self.tw_Ingredienti.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_Ingredienti.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_Ingredienti.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_Ingredienti.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_Ingredienti.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_Ingredienti.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_Ingredienti.setHorizontalHeaderItem(5, item)
        self.lbl_prezzo = QtWidgets.QLabel(Form)
        self.lbl_prezzo.setGeometry(QtCore.QRect(400, 70, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.lbl_prezzo.setFont(font)
        self.lbl_prezzo.setObjectName("lbl_prezzo")
        self.bt_elimina = QtWidgets.QPushButton(Form)
        self.bt_elimina.setGeometry(QtCore.QRect(440, 550, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(8)
        self.bt_elimina.setFont(font)
        self.bt_elimina.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.bt_elimina.setObjectName("bt_elimina")
        self.dsb_prezzo = QtWidgets.QDoubleSpinBox(Form)  # Modifica qui
        self.dsb_prezzo.setGeometry(QtCore.QRect(390, 110, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.dsb_prezzo.setFont(font)
        self.dsb_prezzo.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.dsb_prezzo.setObjectName("dsb_prezzo")
        self.dsb_prezzo.setDecimals(2)
        self.dsb_prezzo.setMaximum(9999.99)
        self.dsb_prezzo.setMinimum(0.00)
        self.comboBox_categoria = QtWidgets.QComboBox(Form)
        self.comboBox_categoria.setGeometry(QtCore.QRect(390, 220, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.comboBox_categoria.setFont(font)
        self.comboBox_categoria.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.comboBox_categoria.setObjectName("comboBox_categoria")

        # Add sample categories to the combo box
        self.comboBox_categoria.addItems(["Bevande", "Antipasti", "Primi", "Secondi", "Contorni", "Sushi", "Pizza", "Dolci", "Caffetteria"])
        self.lbl_altre_info = QtWidgets.QLabel(Form)
        self.lbl_altre_info.setGeometry(QtCore.QRect(20, 180, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.lbl_altre_info.setFont(font)
        self.lbl_altre_info.setObjectName("lbl_altre_info")
        self.lbl_titolo = QtWidgets.QLabel(Form)
        self.lbl_titolo.setGeometry(QtCore.QRect(20, 10, 671, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.lbl_titolo.setFont(font)
        self.lbl_titolo.setObjectName("lbl_titolo")
        self.bt_termina_aggiunta = QtWidgets.QPushButton(Form)
        self.bt_termina_aggiunta.setGeometry(QtCore.QRect(240, 270, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(8)
        self.bt_termina_aggiunta.setFont(font)
        self.bt_termina_aggiunta.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.bt_termina_aggiunta.setObjectName("bt_termina_aggiunta")
        self.tw_Ingredienti.raise_()
        self.lbl_categoria.raise_()
        self.lineEdit_nome.raise_()
        self.bt_aggiungi.raise_()
        self.line_sopra2.raise_()
        self.lbl_nome.raise_()
        self.line_sopra.raise_()
        self.lineEdit_info.raise_()
        self.lbl_quantit.raise_()
        self.lbl_prezzo.raise_()
        self.bt_elimina.raise_()
        self.dsb_prezzo.raise_()
        self.comboBox_categoria.raise_()
        self.lbl_altre_info.raise_()
        self.lbl_titolo.raise_()
        self.bt_termina_aggiunta.raise_()
        self.listWidget_nome_elemento = QtWidgets.QListWidget(Form)
        self.listWidget_nome_elemento.setGeometry(QtCore.QRect(20, 410, 321, 221))
        self.listWidget_nome_elemento.setStyleSheet("background-color: rgb(245, 243, 201);\n""")
        self.listWidget_nome_elemento.setObjectName("listWidget_nome_elemento")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox.setGeometry(QtCore.QRect(500, 390, 111, 51))
        self.doubleSpinBox.setStyleSheet("background-color: rgb(245, 243, 201);")
        self.doubleSpinBox.setObjectName("doubleSpinBox")

        self.doubleSpinBox.setDecimals(2)
        self.doubleSpinBox.setMinimum(0.1)
        self.doubleSpinBox.setMaximum(100.0)
        self.doubleSpinBox.setSingleStep(0.5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Connessione dei bottoni ai metodi
        self.bt_termina_aggiunta.clicked.connect(self.termina_agg)
        self.bt_aggiungi.clicked.connect(self.aggiungi_ingrediente)
        self.bt_elimina.clicked.connect(self.elimina_ingrediente)
        # Popola la QListWidget con i dati dal database
        self.popola_lista_elemento()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Aggiungi Prodotto"))
        self.lbl_categoria.setText(_translate("Form", "Categoria:"))
        self.bt_aggiungi.setText(_translate("Form", "Aggiungi Ingrediente"))
        self.lbl_nome.setText(_translate("Form", "Nome:"))
        self.lbl_quantit.setText(_translate("Form", "Quantità:"))
        item = self.tw_Ingredienti.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Ingrediente"))
        item = self.tw_Ingredienti.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Quantità"))
        item = self.tw_Ingredienti.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Intolleranze"))
        item = self.tw_Ingredienti.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Vegano"))
        item = self.tw_Ingredienti.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Piccante"))
        self.lbl_prezzo.setText(_translate("Form", "Prezzo:"))
        self.bt_elimina.setText(_translate("Form", "Elimina Ingrediente"))
        self.lbl_altre_info.setText(_translate("Form", "Altre informazioni:"))
        self.lbl_titolo.setText(_translate("Form", "Aggiungi un nuovo prodotto al menù"))
        self.bt_termina_aggiunta.setText(_translate("Form", "Termina aggiunta prodotto"))

    def termina_agg(self):
        # Recupera i dati del prodotto dai campi di input
        categoria = self.comboBox_categoria.currentText().strip()
        descrizione = self.lineEdit_info.text().strip()
        nome = self.lineEdit_nome.text().strip()
        prezzo = self.dsb_prezzo.value()  # Recupera il valore come float dal QDoubleSpinBox

        # Controlli per valori nulli o non validi
        if not categoria:
            QtWidgets.QMessageBox.warning(None, 'Errore', 'Il campo "Categoria" non può essere vuoto.')
            return
        if not descrizione:
            QtWidgets.QMessageBox.warning(None, 'Errore', 'Il campo "Descrizione" non può essere vuoto.')
            return
        if not nome:
            QtWidgets.QMessageBox.warning(None, 'Errore', 'Il campo "Nome" non può essere vuoto.')
            return
        if prezzo <= 0:
            QtWidgets.QMessageBox.warning(None, 'Errore', 'Il campo "Prezzo" deve essere maggiore di zero.')
            return

        try:
            connection = get_connection()

            if connection.is_connected():
                cursor = connection.cursor()

                # Inserisci il prodotto nella tabella prodottomenu
                query = """INSERT INTO prodottomenu (categoria, descrizione, nome, prezzo)
                           VALUES (%s, %s, %s, %s)"""
                record = (categoria, descrizione, nome, prezzo)
                cursor.execute(query, record)
                connection.commit()

                # Recupera l'ID del prodotto appena inserito
                prodotto_id = cursor.lastrowid

                # Itera attraverso la tabella degli ingredienti
                for row in range(self.tw_Ingredienti.rowCount()):
                    ingrediente_item = self.tw_Ingredienti.item(row, 0)
                    quantita_item = self.tw_Ingredienti.item(row, 1)

                    if ingrediente_item and quantita_item:
                        try:
                            # Estrarre ID e quantità dell'ingrediente
                            ingrediente_id = int(
                                ingrediente_item.text().split()[0])  # Supponendo che il formato sia "ID Nome"
                            quantita = float(quantita_item.text())

                            if quantita <= 0:
                                raise ValueError("La quantità deve essere maggiore di zero.")

                            # Inserisci i dati nella tabella ingredienteprodotto
                            query = """INSERT INTO ingredienteprodotto (IDNomeElemento, IDProdotto, Quantita)
                                       VALUES (%s, %s, %s)"""
                            record = (ingrediente_id, prodotto_id, quantita)
                            cursor.execute(query, record)
                        except ValueError as ve:
                            QtWidgets.QMessageBox.warning(None, 'Errore',
                                                          f'Errore nei dati dell\'ingrediente alla riga {row + 1}: {ve}')
                            return
                        except Exception as e:
                            QtWidgets.QMessageBox.critical(None, 'Errore',
                                                           f'Errore durante l\'inserimento dell\'ingrediente: {e}')
                            return

                connection.commit()
                QtWidgets.QMessageBox.information(None, 'Successo', 'Prodotto e ingredienti aggiunti con successo')

        except mysql.connector.Error as e:
            QtWidgets.QMessageBox.critical(None, 'Errore', f'Errore durante la connessione al database: {e}')

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                self.FormAPM.close()

    def popola_lista_elemento(self):  # Mi permette di popolare la lista con tutti gli ingredienti disponibili
        # Crea il cursore per eseguire query
        cursor = self.conn.cursor()

        try:
            # Query per selezionare le colonne 'id' e 'nome' dalla tabella 'nomeelemento'
            query = "SELECT id, nome FROM nomeelemento"
            cursor.execute(query)

            # Ottieni tutti i risultati dalla query
            result = cursor.fetchall()

            # Popola la QListWidget con i risultati della query
            for row in result:
                id_elemento = row[0]  # Assume che 'id' sia la prima colonna nella query
                nome_elemento = row[1]  # Assume che 'nome' sia la seconda colonna nella query
                elemento = f"{id_elemento} {nome_elemento}"
                self.listWidget_nome_elemento.addItem(elemento)

        except mysql.connector.Error as err:
            print(f"Errore durante l'esecuzione della query: {err}")

        finally:
            # Chiudi il cursore
            cursor.close()

    def aggiungi_ingrediente(self):
        # Ottieni l'elemento selezionato dalla listWidget
        selected_item = self.listWidget_nome_elemento.currentItem()

        # Ottieni il valore della spinBox
        quantity = self.doubleSpinBox.value()

        if selected_item and quantity > 0:
            # Nome dell'ingrediente selezionato
            ingrediente = selected_item.text()

            # Controlla se l'ingrediente è già presente nella tabella
            trovato = False
            for row in range(self.tw_Ingredienti.rowCount()):
                item = self.tw_Ingredienti.item(row, 0)
                if item and item.text() == ingrediente:
                    # Ingrediente trovato, aggiorna la quantità
                    quantità_corrente = float(self.tw_Ingredienti.item(row, 1).text())
                    nuova_quantità = quantità_corrente + quantity
                    self.tw_Ingredienti.setItem(row, 1, QTableWidgetItem(str(nuova_quantità)))
                    trovato = True
                    break

            if not trovato:
                # Query al database per ottenere il valore delle colonne 'intolleranze', 'piccante', e 'vegano'
                cursor = self.conn.cursor()
                try:
                    query = "SELECT intolleranze, vegano, piccante FROM nomeelemento WHERE nome = %s"
                    cursor.execute(query, (ingrediente,))
                    result = cursor.fetchone()
                    intolleranze = result[0] if result else ""
                    vegano = result[1] if result else ""
                    piccante = result[2] if result else ""

                except mysql.connector.Error as err:
                    print(f"Errore durante l'esecuzione della query: {err}")
                    intolleranze = ""
                    piccante = ""
                    vegano = ""

                finally:
                    cursor.close()

                # Inserisci i dati nella tabella tw_Ingredienti
                row_position = self.tw_Ingredienti.rowCount()
                self.tw_Ingredienti.insertRow(row_position)
                self.tw_Ingredienti.setItem(row_position, 0, QTableWidgetItem(ingrediente))
                self.tw_Ingredienti.setItem(row_position, 1, QTableWidgetItem(str(quantity)))
                self.tw_Ingredienti.setItem(row_position, 2, QTableWidgetItem(intolleranze))
                self.tw_Ingredienti.setItem(row_position, 3, QTableWidgetItem(vegano))
                self.tw_Ingredienti.setItem(row_position, 4, QTableWidgetItem(piccante))
        else:
            QMessageBox.warning(None, "Errore", "Seleziona un ingrediente e inserisci una quantità valida.")

    def elimina_ingrediente(self):  # permette di eliminare gli ingredienti dalla tabella
        # Ottieni la riga selezionata
        selected_row = self.tw_Ingredienti.currentRow()

        if selected_row != -1:
            # Rimuovi la riga selezionata
            self.tw_Ingredienti.removeRow(selected_row)
        else:
            QMessageBox.warning(None, "Errore", "Seleziona una riga da eliminare.")

    def closeEvent(self, event):
        # Chiudi la connessione al database quando l'applicazione viene chiusa
        if self.conn:
            self.conn.close()
        event.accept()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())