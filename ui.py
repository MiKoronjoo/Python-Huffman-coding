# -*- coding: utf-8 -*-

# Huffman coding UI
# Copyright (C) 2019  Hassan Abbasi
# Email: hassan.abbp@gmail.com

from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess

DRAW_TREE = 2
INPUT_FILE = 'Input.txt'
ZIP_FILE = 'Zip.txt'
HUFFMAN_FILE = 'Huffman.txt'


def run_coding():
    output = subprocess.getoutput('python3 coding.py %s %s' % (INPUT_FILE, DRAW_TREE))
    ui.log(output)


def run_decoding():
    output = subprocess.getoutput('python3 decoding.py %s %s' % (ZIP_FILE, HUFFMAN_FILE))
    ui.log(output)


def click_on_check_box(dt_code):
    global DRAW_TREE
    DRAW_TREE = dt_code


def input_new_text(text):
    global INPUT_FILE
    INPUT_FILE = text


def zip_new_text(text):
    global ZIP_FILE
    ZIP_FILE = text


def huffman_new_text(text):
    global HUFFMAN_FILE
    HUFFMAN_FILE = text


class Ui_MainWindow(object):
    def log(self, text: str):
        self.logger.setText(text)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(372, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.inputText.setGeometry(QtCore.QRect(20, 100, 131, 25))
        self.inputText.setObjectName("inputText")
        self.inputText.setText(INPUT_FILE)
        self.zipText = QtWidgets.QLineEdit(self.centralwidget)
        self.zipText.setGeometry(QtCore.QRect(22, 290, 131, 25))
        self.zipText.setObjectName("zipText")
        self.zipText.setText(ZIP_FILE)
        self.huffmanText = QtWidgets.QLineEdit(self.centralwidget)
        self.huffmanText.setGeometry(QtCore.QRect(22, 380, 131, 25))
        self.huffmanText.setObjectName("huffmanText")
        self.huffmanText.setText(HUFFMAN_FILE)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 71, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 260, 61, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 350, 131, 20))
        self.label_3.setObjectName("label_3")
        self.zipButton = QtWidgets.QPushButton(self.centralwidget)
        self.zipButton.setGeometry(QtCore.QRect(238, 100, 111, 25))
        self.zipButton.setObjectName("zipButton")
        self.unzipButton = QtWidgets.QPushButton(self.centralwidget)
        self.unzipButton.setGeometry(QtCore.QRect(238, 330, 111, 25))
        self.unzipButton.setObjectName("unzipButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 200, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.logger = QtWidgets.QTextBrowser(self.centralwidget)
        self.logger.setGeometry(QtCore.QRect(15, 470, 341, 81))
        self.logger.setObjectName("logger")
        self.drawTreeCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.drawTreeCheckBox.setGeometry(QtCore.QRect(240, 70, 92, 23))
        self.drawTreeCheckBox.setChecked(True)
        self.drawTreeCheckBox.setObjectName("drawTreeCheckBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 372, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.zipButton.clicked.connect(run_coding)
        self.unzipButton.clicked.connect(run_decoding)
        self.drawTreeCheckBox.stateChanged['int'].connect(click_on_check_box)
        self.inputText.textChanged.connect(input_new_text)
        self.zipText.textChanged.connect(zip_new_text)
        self.huffmanText.textChanged.connect(huffman_new_text)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Huffman Coding"))
        self.label.setText(_translate("MainWindow", "Input file:"))
        self.label_2.setText(_translate("MainWindow", "Zip file:"))
        self.label_3.setText(_translate("MainWindow", "Huffman code file:"))
        self.zipButton.setText(_translate("MainWindow", "Zip"))
        self.unzipButton.setText(_translate("MainWindow", "Unzip"))
        self.label_4.setText(_translate("MainWindow", "📥 Coding"))
        self.label_5.setText(_translate("MainWindow", "📤 Decoding"))
        self.drawTreeCheckBox.setText(_translate("MainWindow", "Draw tree"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
