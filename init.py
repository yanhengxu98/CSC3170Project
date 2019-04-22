from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from PyQt5.QtSql import QSqlDatabase, QsqlTableModel

import sys
import pymysql
from datetime import datetime

from database_project import Ui_Form


class MyMainwindow(QMainWindow, Ui_Form):

    def __init__(self, parent=None):
        super(MyMainwindow, self).__init__(parent)
        self.setupUi(self)
        self.dateEdit.setDate(QDate.currentDate())

        self.connection = pymysql.connect(host='127.0.0.1', user='root', password='232323Xyh!', db='LGUAirline', port=3306,
                                          charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.connection.cursor()
        self.prefix = "select FlightDATE,FlightCode,TakeoffTime,EstArrTime,DepApFCC,ArrApFCC from flight where DepApFCC = 'SZX'"
        query_order = self.prefix
        self.cursor.execute(query_order)
        k = 0
        for attribute in self.cursor:
            print("------", attribute)
            w = 0
            for j in attribute:
                # 这里是将int类型转成string类型，方便后面文本设置
                instance = attribute[j]
                if type(instance) == int:
                    newItem = QTableWidgetItem(str(instance))
                else:
                    newItem = QTableWidgetItem(instance)
                # 根据循环标签一次对table中的格子进行设置
                self.tableWidget.setItem(k, w, newItem)
                w += 1
            k += 1

        self.pushButton.clicked.connect(self.query_flight)
        self.pushButton.clicked.connect(self.query_crew)

    def query_flight(self):
        self.tableWidget.clearContents()  # 每一次查询时清除表格中信息
        searchdate = self.dateEdit.dateTime().toString("yyyy-MM-dd")
        dep = self.comboBox.currentText()[-4:-1]
        arr = self.comboBox_2.currentText()[-4:-1]

        self.prefix = "select FlightDATE,FlightCode,TakeoffTime,EstArrTime,DepApFCC,ArrApFCC from flight where DepApFCC = '%s' and ArrApFCC = '%s'" % (dep, arr)
        query_order = self.prefix
        self.cursor.execute(query_order)
        k = 0
        for attribute in self.cursor:
            print("------", attribute)
            w = 0
            for j in attribute:
                # 这里是将int类型转成string类型，方便后面文本设置
                instance = attribute[j]
                if type(instance) == int:
                    newItem = QTableWidgetItem(str(instance))
                else:
                    newItem = QTableWidgetItem(instance)
                # 根据循环标签一次对table中的格子进行设置
                self.tableWidget.setItem(k, w, newItem)
                w += 1
            k += 1

    def query_crew(self):
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MyMainwindow()
    ui.show()
    sys.exit(app.exec_())


