# -*- coding: utf-8 -*-
import sqlite3
from collections import defaultdict

import mysql
# Form implementation generated from reading ui file 'F:\Users\framo\Desktop\ProgettoING-master\form_ui\Lista_comande.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollArea, QListWidget, QPushButton, QListWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from collections import defaultdict
from db_connection import get_connection
from form_Cuoco.ElementoOrdine import ElementoOrdine
from form_Cuoco.Ordinazione import Ordinazione


class Ui_formListaComande(object):
    FormListaComande=None
    def setupUi(self, formListaComande):
        self.FormListaComande=formListaComande
        formListaComande.setObjectName("formListaComande")
        formListaComande.resize(1132, 632)
        formListaComande.setStyleSheet("background-color: rgb(159, 197, 248);")
        self.label_titolo_lista_ordini = QtWidgets.QLabel(formListaComande)
        self.label_titolo_lista_ordini.setGeometry(QtCore.QRect(20, 0, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_titolo_lista_ordini.setFont(font)
        self.label_titolo_lista_ordini.setObjectName("label_titolo_lista_ordini")
        self.label_data = QtWidgets.QLabel(formListaComande)
        self.label_data.setGeometry(QtCore.QRect(930, 20, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_data.setFont(font)
        self.label_data.setObjectName("label_data")
        self.scrollAreaComande = QtWidgets.QScrollArea(formListaComande)
        self.scrollAreaComande.setGeometry(QtCore.QRect(20, 80, 1091, 541))
        self.scrollAreaComande.setWidgetResizable(True)
        self.scrollAreaComande.setObjectName("scrollAreaComande")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1089, 539))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaComande.setWidget(self.scrollAreaWidgetContents)
        self.scrollAreaComande.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # Nasconde la barra di scorrimento orizzontale
        self.label = QtWidgets.QLabel(formListaComande)
        self.label.setGeometry(QtCore.QRect(20, 55, 391, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(formListaComande)

        self.aggiornaGeneraComande()
        QtCore.QMetaObject.connectSlotsByName(formListaComande)

    def retranslateUi(self, formListaComande):
        _translate = QtCore.QCoreApplication.translate
        formListaComande.setWindowTitle(_translate("formListaComande", "Lista comande"))
        self.label_titolo_lista_ordini.setText(_translate("formListaComande", "Lista Ordinazoni:"))
        self.label_data.setText(_translate("formListaComande", "Mercoledi 01/03/2024"))
        self.label.setText(_translate("formListaComande", "Tocca il post-it per confermare la preparazione dell\'ordine"))

    def aggiornaGeneraComande(self):
        # Elimina tutti i bottoni creati precedentemente
        for widget in self.FormListaComande.findChildren(QtWidgets.QListWidget):
            widget.deleteLater()
        try:
            db_connection = get_connection()
            cursor = db_connection.cursor()

            # Esecuzione della query per le ordinazioni
            query = "SELECT ID, IDTavolo, completato, sequenzaCorrente FROM ordinazione WHERE completato = 0"
            cursor.execute(query)
            ordinazioni = cursor.fetchall()

            # Creazione della lista di oggetti Ordinazione
            lista_ordinazioni = []
            for ordinazione in ordinazioni:
                id, id_tavolo, completato, sequenza_corrente = ordinazione
                ord = Ordinazione(id, id_tavolo, completato, sequenza_corrente)
                ord.elementi_ordine = []
                lista_ordinazioni.append(ord)

            # Esecuzione della query per gli elementi ordine
            id_ordinazioni = tuple([ord.ID for ord in lista_ordinazioni])
            if id_ordinazioni:
                # Se la tupla contiene solo un elemento, cambia il formato
                if len(id_ordinazioni) == 1:
                    query = f"SELECT ID, idOrdinazione, idProdotto, completato, sequenza FROM elementoordine WHERE idOrdinazione = {id_ordinazioni[0]}"
                else:
                    query = f"SELECT ID, idOrdinazione, idProdotto, completato, sequenza FROM elementoordine WHERE idOrdinazione IN {id_ordinazioni}"
                cursor.execute(query)
                elementi_ordine = cursor.fetchall()

                # Creazione della lista di oggetti ElementoOrdine e assegnazione alle rispettive ordinazioni
                for elemento in elementi_ordine:
                    id, id_ordinazione, id_prodotto, completato, sequenza = elemento
                    for ord in lista_ordinazioni:
                        if ord.ID == id_ordinazione and ord.sequenzaCorrente == sequenza:
                            elem = ElementoOrdine(id, id_ordinazione, id_prodotto, completato, sequenza)
                            ord.elementi_ordine.append(elem)

            # Chiudere la connessione al database
            db_connection.close()

            # Debug: Stampa le ordinazioni e i relativi elementi ordine
            for ord in lista_ordinazioni:
                print(f"Ordine ID: {ord.ID}, Tavolo: {ord.ID_tavolo}, Sequenza Corrente: {ord.sequenzaCorrente}")
                for elem in ord.elementi_ordine:
                    print(
                        f"  Elemento Ordine ID: {elem.ID}, Prodotto ID: {elem.ID_prodotto}, Completato: {elem.completato}, Sequenza: {elem.sequenza}")


            # Popolazione dell'interfaccia con le ordinazioni
            self.popolaInterfaccia(lista_ordinazioni)

        except Exception as e:
            print(f"Errore durante l'accesso al database: {e}")
        finally:
            # Chiusura della connessione al database
            if 'db_connection' in locals() and db_connection.is_connected():
                db_connection.close()

    def popolaInterfaccia(self, lista_ordinazioni):
        total_width = 0
        row_height = 0
        current_row_y = 20
        row_spacing = 10
        scroll_width = self.scrollAreaComande.width()

        for ordinazione in lista_ordinazioni:
            # Comprehension di generatori che verifica se ogni elemento non è completato
            elementi_non_completati = (not elemento.completato for elemento in ordinazione.elementi_ordine)

            # Utilizzare la funzione any per verificare se ci sono elementi non completati
            if any(elementi_non_completati):
                # Creazione della QListWidget per rappresentare l'ordinazione
                list_widget = QListWidget(self.scrollAreaWidgetContents)

                # Impostazione dello stile personalizzato per il post-it
                list_widget.setStyleSheet("background-color: yellow; border: 1px solid black; border-radius: 5px;")

                # Aggiunta dell'id del tavolo come elemento della lista
                tavolo_item = QListWidgetItem(f"ID Tavolo: {ordinazione.ID_tavolo}", list_widget)
                tavolo_item.setFont(QtGui.QFont("Arial", 12))
                tavolo_item.setTextAlignment(Qt.AlignCenter)

                # Aggregazione degli elementi per idProdotto
                prodotti = defaultdict(int)
                for elemento in ordinazione.elementi_ordine:
                    if not elemento.completato:
                        prodotti[elemento.ID_prodotto] += 1
                # Aggiunta di tutti gli elementi di quell'ordine come sotto-elementi della lista
                for id_prodotto, quantita in prodotti.items():
                    nome_prodotto = self.daIDaNomeProdotto(id_prodotto)
                    elemento_item = QListWidgetItem(f"{nome_prodotto} x{quantita}", list_widget)
                    list_widget.addItem(elemento_item)

                # Impostazione dell'evento di click per visualizzare il popup
                list_widget.clicked.connect(lambda state, lw=list_widget, ord=ordinazione: self.lwClicked(ord, lw))

                # Calcolo della larghezza del rettangolo corrente
                list_widget_width = list_widget.sizeHint().width()

                # Se la larghezza totale della riga più la larghezza del rettangolo corrente supera la larghezza della scrollArea,
                # passa alla riga successiva
                if total_width + list_widget_width > scroll_width:
                    current_row_y += row_height + row_spacing
                    total_width = 0
                    row_height = 0

                # Posizionamento del rettangolo corrente
                list_widget.setGeometry(QtCore.QRect(20 + total_width, current_row_y, list_widget_width, 170))

                # Aggiornamento della larghezza totale e dell'altezza della riga corrente
                total_width += list_widget_width + row_spacing
                row_height = max(row_height, list_widget.sizeHint().height())
                list_widget.setVisible(True)

        # Aggiornamento della dimensione della scrollArea
        content_height = current_row_y + row_height + row_spacing
        self.scrollAreaWidgetContents.setFixedSize(scroll_width, content_height)


    def lwClicked(self, ordinazione, list_widget):
        popup = QMessageBox()
        popup.setWindowTitle("Conferma completamento")
        popup.setText(f"Vuoi impostare questi elementi come completati per l'ordinazione {ordinazione.ID}?")
        popup.setIcon(QMessageBox.Question)
        popup.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        popup.setDefaultButton(QMessageBox.No)

        # Se l'utente conferma, imposto gli elementi ordine come completati nel database
        if popup.exec_() == QMessageBox.Yes:
            self.impostaElementiCompletati(ordinazione)


    def impostaElementiCompletati(self, ordinazione):
        try:
            db_connection = get_connection()
            cursor = db_connection.cursor()

            # Imposta completato=True per tutti gli elementi ordine dell'ordinazione
            query = f"UPDATE elementoordine SET completato = TRUE WHERE idOrdinazione = {ordinazione.ID} AND Sequenza = {ordinazione.sequenzaCorrente}"
            cursor.execute(query)
            db_connection.commit()

            # Aggiorna l'interfaccia
            self.aggiornaGeneraComande()
        except Exception as e:
            print(f"Errore durante l'accesso al database: {e}")
        finally:
            # Chiusura della connessione al database
            if 'db_connection' in locals() and db_connection.is_connected():
                db_connection.close()

    def daIDaNomeProdotto(self,id_prodotto):
        try:
            db_connection = get_connection()
            cursor = db_connection.cursor()

            # Esecuzione della query per trovare il nome del prodotto
            query = f"SELECT nome FROM prodottomenu WHERE ID = {id_prodotto}"
            cursor.execute(query)
            nome_prodotto = cursor.fetchone()[0]  # Ottieni il nome del prodotto dalla prima colonna

            # Chiudere la connessione al database
            db_connection.close()

            return nome_prodotto
        except Exception as e:
            print(f"Errore durante l'accesso al database: {e}")
            return None
        finally:
            # Chiusura della connessione al database
            if 'db_connection' in locals() and db_connection.is_connected():
                db_connection.close()
