#este bot spamea mensajes por medio de la pantalla, se necesita tener instalsdo los modulos de pyautogui
import pyautogui,time, keyboard
import sys
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.uic import *
from PyQt5.QtCore import Qt
import os

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Bot(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(resource_path("Bot.ui"), self)
        self.botonActivar.clicked.connect(self.activar)
        self.checkBoxImagen.clicked.connect(self.limpiar)
    def limpiar(self):
        self.textoInput.clear()
    def activar(self):
        if self.checkBoxImagen.isChecked():
            time.sleep(10)
            while True:
                pyautogui.hotkey('ctrl','v')
                time.sleep(0.5)
                pyautogui.press("enter")
                if keyboard.is_pressed("alt"):
                    break
        elif self.checkBoxTexto.isChecked():
            time.sleep(10)
            while True:
                s = self.textoInput.text()
                time.sleep(0.5)
                pyautogui.typewrite(str(s))
                pyautogui.press("enter")
                if keyboard.is_pressed("alt"):
                    break
#main
app = QApplication(sys.argv)
bot = Bot()
bot.show()
app.exec_()