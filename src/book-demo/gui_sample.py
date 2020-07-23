import sys
from PyQt5 import QtWidgets, Qt


class ChatView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)
        listbox = QtWidgets.QListWidget(self)
        listbox.addItems([f"item{i:0=2}" for i in range(1, 21)])
        main_layout.addWidget(listbox)

        sub_layout = QtWidgets.QHBoxLayout()
        main_layout.addLayout(sub_layout)

        entry = QtWidgets.QLineEdit(self)
        sub_layout.addWidget(entry)
        send_button = QtWidgets.QPushButton("send", self)
        sub_layout.addWidget(send_button)


class MainWIndow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatview = ChatView(self)
        self.setup_menues()
        self.setCentralWidget(self.chatview)
        self.show_status_message("started")

    def setup_menues(self):
        menubar = self.menuBar()
        filemenu = menubar.addMenu("file")
        quitAction = filemenu.addAction("Quit")
        quitAction.triggered.connect(QtWidgets.qApp.quit)

    def show_status_message(self, message):
        statusbar = self.statusBar()
        statusbar.showMessage(message)


app = QtWidgets.QApplication(sys.argv)

main = MainWIndow()
main.show()

app.exec_()
