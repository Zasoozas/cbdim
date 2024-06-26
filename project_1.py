from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, \
    QHBoxLayout, QVBoxLayout, QLineEdit, QCheckBox, QTextEdit, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import wiki
import trans
from weath import get_weather
from random import randint

def choice_action_back():
    if button_back.text() == "Выход":
        exit()
    elif button_back.text() == "Назад":
        start_window()

def show_wiki():
    hello_text.hide()
    button_weather.hide()
    button_translator.hide()
    button_game.hide()
    button_back.setText("Назад")
    description_text.setText("Для поиска информации \nвведите запрос:")
    request.show()
    info.show()
    button_wiki.setText("Искать")

def start_window():
    description_text.setText("Для перехода к действию \nвведите запрос:")
    button_wiki.show()
    button_wiki.setText("Википедия")
    button_translator.show()
    button_translator.setText("Переводчик")
    button_weather.show()
    button_weather.setText("Погода")
    button_game.show()
    button_game.setText("Игра")
    request.clear()
    request.hide()
    info.clear()
    info.hide()
    button_back.setText("Выход")

def choice_action_wiki():
    if button_wiki.text() == "Википедия":
        show_wiki()
    elif request.text():
        info.setText(wiki.get_wiki(request.text()))

def show_translator():
    hello_text.hide()
    button_weather.hide()
    button_wiki.hide()
    button_game.hide()
    button_back.setText("Назад")
    description_text.setText("Для перевода \nвведите запрос:")
    request.show()
    info.show()
    button_translator.setText("Перевести")

def choice_action_trans():
    if button_translator.text() == "Переводчик":
        show_translator()
    elif request.text():
        info.setText(trans.translate_word(request.text()))

def show_weather():
    hello_text.hide()
    button_translator.hide()
    button_wiki.hide()
    button_game.hide()
    button_back.setText("Назад")
    description_text.setText("Для информации о погоде \nвведите запрос:")
    request.show()
    info.show()
    button_weather.setText("Узнать информацию")

def get_request_weath():
    if request.text():
        result = get_weather(request.text())
        info.setText(result)
def choice_action_weath():
    if button_weather.text() == "Погода":
        show_weather()
    elif button_weather.text() == "Узнать информацию":
        get_request_weath()

def show_game():
    global win_number
    hello_text.hide()
    button_weather.hide()
    button_wiki.hide()
    button_translator.hide()
    button_back.setText("Назад")
    description_text.setText("Отгадай число от 1 до 100:")
    request.show()
    info.show()
    button_game.setText("Предположить")
    win_number = randint(1, 100)

def get_request_game():
    if request.text():
        if int(request.text()) > win_number:
            info.insertPlainText("Много!\n")
        elif int(request.text()) < win_number:
            info.insertPlainText("Мало!\n")
        else:
            info.insertPlainText("Угадал!\nСледующая попытка\n")
            request.clear()
            show_game()

def choice_action_game():
    if button_game.text() == "Игра":
        show_game()
    elif button_game.text() == "Предположить":
        get_request_game()

app = QApplication([])
window = QWidget()
window.resize(450, 500)
window.setWindowTitle("Чат-бот")
window.setWindowIcon(QIcon("robot.png"))
window.setStyleSheet("background-color: #AA67D5; color: #FFFACD; font-family: fantasy, Verdana; font-size: 18px")
hello_text = QLabel("Приветствую! Я - чат-бот Dimometr!")
hello_text.setStyleSheet("font-size: 24px")
description_text = QLabel("Для выбора нажмите нужную кнопку!")
button_back = QPushButton("Выход")
button_wiki = QPushButton("Википедия")
button_translator = QPushButton("Переводчик")
button_weather = QPushButton("Погода")
button_game = QPushButton("Игра")
request = QLineEdit()
request.hide()
info = QTextEdit()
info.setReadOnly(True)
info.hide()


main_line = QVBoxLayout()
line_h1 = QHBoxLayout()
line_h2 = QHBoxLayout()
line_h3 = QHBoxLayout()
line_h1.addWidget(button_wiki)
line_h1.addWidget(button_translator)
line_h2.addWidget(button_weather)
line_h2.addWidget(button_game)
main_line.addWidget(hello_text, alignment=Qt.AlignmentFlag.AlignCenter)
main_line.addWidget(description_text, alignment=Qt.AlignmentFlag.AlignCenter)
main_line.addWidget(request, alignment=Qt.AlignmentFlag.AlignCenter)
main_line.addWidget(info, alignment=Qt.AlignmentFlag.AlignCenter)
main_line.addLayout(line_h1)
main_line.addLayout(line_h2)
main_line.addWidget(button_back)
window.setLayout(main_line)

button_back.clicked.connect(choice_action_back)
button_wiki.clicked.connect(choice_action_wiki)
button_translator.clicked.connect(choice_action_trans)
button_weather.clicked.connect(choice_action_weath)
button_game.clicked.connect(choice_action_game)


window.show()
app.exec()