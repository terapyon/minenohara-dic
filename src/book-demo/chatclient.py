import sys
from PyQt5 import Qt, QtWidgets, QtWebSockets, QtGui

WEBSOCKET_URL = "ws://127.0.0.1:8080/ws"


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ws = QtWebSockets.QWebSocket()
        self.initialize()
        self.initialize_menue()

    def initialize(self):
        self.chat = ChatWidget(self.ws, self)
        self.setCentralWidget(self.chat)
        self.chat.ws.stateChanged.connect(self.on_state_changed)

    def on_state_changed(self, state):
        if state == Qt.QAbstractSocket.ConnectedState:
            self.statusBar().showMessage("connected")
        else:
            self.statusBar().clearMessage()

    def initialize_menue(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        connect_action = file_menu.addAction("Connect")
        connect_action.triggered.connect(self.connect)
        connect_action.setShortcuts(QtGui.QKeySequence.Open)
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(QtWidgets.qApp.quit)
        quit_action.setShortcuts(QtGui.QKeySequence.Quit)

    def connect(self):
        url = self.ask_url(WEBSOCKET_URL)
        if not url:
            return
        self.chat.ws.open(Qt.QUrl(url))

    def ask_url(self, default):
        url, ok = QtWidgets.QInputDialog.getText(
            self, "chatserver", "Connection URL", text=default
        )
        if ok:
            return url


class ChatWidget(QtWidgets.QWidget):
    def __init__(self, ws, parent=None):
        super().__init__(parent=parent)
        self.initialize()
        self.ws = ws
        self.ws.textMessageReceived.connect(self.on_text_recived)

    def initialize(self):
        self.messages = QtWidgets.QListWidget(self)
        self.input = QtWidgets.QLineEdit(self)
        self.send = QtWidgets.QPushButton("Send", self)
        self.send.clicked.connect(self.on_send)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.messages)
        self.sub_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.sub_layout)
        self.sub_layout.addWidget(self.input)
        self.sub_layout.addWidget(self.send)
        self.setLayout(self.main_layout)

    def on_text_recived(self, message):
        self.messages.addItem(message)

    def on_send(self, *args, **kwargs):
        self.ws.sendTextMessage(self.input.text())
        self.input.setText("")


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()


if __name__ == "__main__":
    main()
