import sys
from PyQt5 import QtWidgets, Qt

app = QtWidgets.QApplication(sys.argv)


# button = QtWidgets.QPushButton("Hello")
# button.clicked.connect(lambda: print("Hello2"))
# button.clicked.connect(Qt.qApp.quit)
# button.show()

# lineedit = QtWidgets.QLineEdit()
# lineedit.setText("Hello, World!")
# lineedit.show()

linewidget = QtWidgets.QListWidget()
linewidget.addItems([f"item{i:0=2}" for i in range(1, 10)])
linewidget.show()

app.exec_()
