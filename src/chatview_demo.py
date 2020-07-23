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


app = QtWidgets.QApplication(sys.argv)

chatview = ChatView()
chatview.show()

app.exec_()
