import sys
from PyQt5 import QtWidgets, Qt

app = QtWidgets.QApplication(sys.argv)

widget = QtWidgets.QWidget()
main_layout = QtWidgets.QVBoxLayout()
widget.setLayout(main_layout)
listbox = QtWidgets.QListWidget(widget)
listbox.addItems([f"item{i:0=2}" for i in range(1, 21)])
main_layout.addWidget(listbox)

sub_layout = QtWidgets.QHBoxLayout()
main_layout.addLayout(sub_layout)

entry = QtWidgets.QLineEdit(widget)
sub_layout.addWidget(entry)
send_button = QtWidgets.QPushButton("send", widget)
sub_layout.addWidget(send_button)

widget.show()

app.exec_()
