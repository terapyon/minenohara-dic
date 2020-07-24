import sys
from PyQt5 import Qt, QtWidgets, QtWebSockets, QtGui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize()
        self.initialize_menue()

    def initialize(self):
        self.chat = ChatWidget(self)
        self.setCentralWidget(self.chat)

    def initialize_menue(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(QtWidgets.qApp.quit)
        quit_action.setShortcuts(QtGui.QKeySequence.Quit)


class ChatWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.initialize()
        # self.ws.textMessageReceived.connect(self.on_text_recived)

    def initialize(self):
        self.messages = QtWidgets.QListWidget(self)
        self.results = QtWidgets.QListWidget(self)
        self.input = QtWidgets.QLineEdit(self)
        self.send = QtWidgets.QPushButton("Send", self)
        self.send.clicked.connect(self.on_send)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.messages)
        self.main_layout.addWidget(self.results)
        self.sub_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.sub_layout)
        self.sub_layout.addWidget(self.input)
        self.sub_layout.addWidget(self.send)
        self.setLayout(self.main_layout)

    # def on_text_recived(self, message):
    #     self.messages.addItem(message)

    def on_send(self, *args, **kwargs):
        inline_text = self.input.text()
        self.messages.addItem(inline_text)
        # inline_button = QtWidgets.QPushButton(inline_text, self)
        # self.messages.addItem(inline_button)

        # self.ws.sendTextMessage(inline_text)
        self.input.setText("")
        self.remove_messages()

    def remove_messages(self):
        pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()


if __name__ == "__main__":
    main()
