from PyQt5 import QtWidgets
import sys
from ImageEditor import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)
MainWindows = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindows)
MainWindows.show()
sys.exit(app.exec_())

