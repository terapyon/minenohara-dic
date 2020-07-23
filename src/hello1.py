import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
label = QtWidgets.QLabel("Hello")
label.show()
app.exec_()

