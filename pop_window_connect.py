from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import pymysql

from popupwindow import Ui_Pop
from database_project import Ui_Form as Main


class DetailWindow(QMainWindow, Ui_Pop):

    def __init__(self, parent=None):
        super(DetailWindow, self).__init__(parent)
        self.setupUi(self)

        self.exit.clicked.connect(self.display_detail)

    def display_detail(self):
        print(Main.passengernum.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = DetailWindow()
    ui.show()
    sys.exit(app.exec_())