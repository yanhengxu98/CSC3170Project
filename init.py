from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from PyQt5.QtSql import QSqlDatabase, QsqlTableModel

import sys
import pymysql

from database_project import Ui_Form


class MyMainwindow(QMainWindow, Ui_Form):

    def __init__(self, parent = None):
        super(MyMainwindow, self).__init__(parent)
        self.setupUi(self)

        self.connection = pymysql.connect(host='10.26.1.10', user='root', password='root', db='LGUAirline', port=3306,
                                          charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.connection.cursor()
        self.prefix = "select FlightDATE,FlightCode,TakeoffTime,EstArrTime,DepApFCC,ArrApFCC from flight where DepApFCC = SZX"
        query_order = self.prefix
        self.cursor.execute(query_order)
        k = 0
        for i in self.cursor:
            print("------", i)
            w = 0
            for j in i:
                # 这里是将int类型转成string类型，方便后面文本设置
                if type(j) == int:
                    newItem = QtWidget.QTableWidgetItem(str(j))

                else:
                    newItem = QtWidget.QTableWidgetItem(j)
                # 根据循环标签一次对table中的格子进行设置
                self.tableWidget.setItem(k, w, newItem)
                w += 1
            k += 1

    # def query(self):


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MyMainwindow()
    ui.show()
    sys.exit(app.exec_())


