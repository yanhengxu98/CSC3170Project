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
        # self.dateEdit.setDate(QDate.currentDate())

        self.connection = pymysql.connect(host='10.20.5.31', user='root', password='root', db='LGUAirline', port=3306,
                                          charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.connection.cursor()
        self.passengernum.setValidator(QIntValidator(0, 500))
        self.newPassengerNum.setValidator(QIntValidator(0, 500))
        self.newFlightCode.setValidator(QIntValidator(1000, 10000))
        self.planeAge.setValidator(QIntValidator(0, 50))

        self.show_flight_table()
        # self.cursor.execute('SELECT * FROM flight')
        # k = 0
        # for attribute in self.cursor:
        #     print("------", attribute)
        #     w = 0
        #     for j in attribute:
        #         print(j)
        #         instance = attribute[j]
        #         if type(instance) == int:
        #             newItem = QTableWidgetItem(str(instance))
        #         else:
        #             newItem = QTableWidgetItem(instance)
        #         if j == 'FlightCode':
        #             self.tableWidget_6.setItem(k, 0, newItem)
        #         if j == 'PlaneRegiNum':
        #             self.tableWidget_6.setItem(k, 1, newItem)
        #         if j == 'FlightDATE':
        #             self.tableWidget_6.setItem(k, 2, newItem)
        #         if j == 'TakeoffTime':
        #             self.tableWidget_6.setItem(k, 3, newItem)
        #         if j == 'DepApFCC':
        #             self.tableWidget_6.setItem(k, 4, newItem)
        #         if j == 'EstArrTime':
        #             self.tableWidget_6.setItem(k, 5, newItem)
        #         if j == 'ArrApFCC':
        #             self.tableWidget_6.setItem(k, 6, newItem)
        #         if j == 'CapID':
        #             self.tableWidget_6.setItem(k, 7, newItem)
        #         if j == 'PassengerNum':
        #             self.tableWidget_6.setItem(k, 8, newItem)
        #         w += 1
        #     k += 1

        # self.prefix = "select f.FlightCode, f.TakeoffTime, f.EstArrTime, f.DepApFCC, f.ArrApFCC, p.ModelID " \
        #               "from flight f, Plane p " \
        #               "where f.DepApFCC = 'SZX' and f.PlaneRegiNum = p.RegiNum"
        # query_order = self.prefix
        # self.cursor.execute(query_order)  # run sql order
        # k = 0
        # for attribute in self.cursor:
        #     print("------", attribute)
        #     w = 0
        #     for j in attribute:
        #         # 这里是将int类型转成string类型，方便后面文本设置
        #         instance = attribute[j]
        #         if type(instance) == int:
        #             newItem = QTableWidgetItem(str(instance))
        #         else:
        #             newItem = QTableWidgetItem(instance)
        #         # 根据循环标签一次对table中的格子进行设置
        #         self.tableWidget.setItem(k, w, newItem)
        #         w += 1
        #     k += 1

        self.searchFlight.clicked.connect(self.query_flight)
        self.searchStaff.clicked.connect(self.query_staff)
        self.searchPlane.clicked.connect(self.query_plane)
        self.searchAirport.clicked.connect(self.query_airport)
        self.insertFlight.clicked.connect(self.insert_flight)
        self.deleteFlight.clicked.connect(self.delete_flight)




    def closeEvent(self, event):

        reply = QMessageBox.question(self,
                                     'LGUAirline',
                                     "Are you sure to quit？",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
            self.connection.close()
        else:
            event.ignore()

    def query_flight(self):
        self.tableWidget.clearContents()  # 每一次查询时清除表格中信息
        searchdate = self.dateEdit.dateTime().toString("yyyy-MM-dd")
        if self.comboBox.currentText() != 'Wherever' and self.comboBox_2.currentText() != 'Wherever':
            dep = self.comboBox.currentText()[-4:-1]
            arr = self.comboBox_2.currentText()[-4:-1]
            self.prefix3 = "where f.DepApFcc = '%s' and f.ArrApFcc = '%s' and f.PlaneRegiNum = p.RegiNum and f.FlightDATE = '%s' " % (dep, arr, searchdate)
        elif self.comboBox.currentText() != 'Wherever':
            dep = self.comboBox.currentText()[-4:-1]
            self.prefix3 = "where f.DepApFcc = '%s' and f.PlaneRegiNum = p.RegiNum and f.FlightDATE = '%s' " % (dep, searchdate)
        elif self.comboBox_2.currentText() != 'Wherever':
            arr = self.comboBox_2.currentText()[-4:-1]
            self.prefix3 = "where f.ArrApFcc = '%s' and f.PlaneRegiNum = p.RegiNum and f.FlightDATE = '%s' " % (arr, searchdate)
        else:
            self.prefix3 = "where f.PlaneRegiNum = p.RegiNum and f.FlightDATE = '%s' " % searchdate

        self.prefix1 = "select f.FlightCode, f.TakeoffTime, f.EstArrTime, f.DepApFCC, f.ArrApFCC, p.ModelID "
        self.prefix2 = "from flight f, Plane p "

        if self.planemode.isChecked():
            planemode = self.planeselect.currentText()
            self.prefix3 = self.prefix3 + "and p.ModelID = '%s' " % planemode

        if self.directflight.isChecked():
            self.prefix3 = self.prefix3 + "and f.StopByFCC is NULL "

        if self.planeage.isChecked():
            self.prefix3 = self.prefix3 + "and p.age <= 3 "

        if self.passenger.isChecked() and self.passengernum.text() != '':
            passengernum = int(self.passengernum.text())
            self.prefix3 = self.prefix3 + "and f.PassengerNum <= %d " % passengernum

        # passenger number check

        query_order = self.prefix1 + self.prefix2 + self.prefix3
        print(query_order)
        self.cursor.execute(query_order)

        if self.cursor.rowcount == 0:
            info = QMessageBox.about(self, "Information", "This query does not return any result.")
            print(info)

        k = 0
        for attribute in self.cursor:
            print("------", attribute)
            w = 0
            for j in attribute:
                print(j)
                # 这里是将int类型转成string类型，方便后面文本设置
                instance = attribute[j]
                if type(instance) == int:
                    newItem = QTableWidgetItem(str(instance))
                else:
                    newItem = QTableWidgetItem(instance)
                # 根据循环标签一次对table中的格子进行设置
                if j=='FlightCode':
                    self.tableWidget.setItem(k, 0, newItem)
                if j=='TakeoffTime':
                    self.tableWidget.setItem(k, 1, newItem)
                if j=='EstArrTime':
                    self.tableWidget.setItem(k, 2, newItem)
                if j=='DepApFCC':
                    self.tableWidget.setItem(k, 3, newItem)
                if j=='ArrApFCC':
                    self.tableWidget.setItem(k, 4, newItem)
                if j=='ModelID':
                    self.tableWidget.setItem(k, 5, newItem)
                    # btn = QPushButton(self.tableWidget)
                    # btn.setText('Click')
                    # self.tableWidget.setCellWidget(k, 6, btn)
                w += 1
            k += 1

    def query_staff(self):
        self.tableWidget_2.clearContents()  # 每一次查询时清除表格中信息
        occupation = self.comboBox_3.currentText()
        level = self.comboBox_4.currentText()
        name = self.lineEdit.text()
        staff_id = self.lineEdit_2.text()
        if occupation=='Cabin Crew':
            self.prefix1 = "select c.StaffID, c.FirstName, c.LastName, c.CrewLevel, c.PhoneNum, c.Salary "
            self.prefix2 = "from CABINCREW c "
            self.prefix3 = "where c.CrewLevel = '%s' " % level
            if len(name)>0:
                self.prefix3+="and  c.FirstName = '%s'" % name
            if len(staff_id)>0:
                self.prefix3+="and  c.StaffID = '%s'" % staff_id
        if occupation=='Pilot':
            self.prefix1 = "select p.PilotID, p.FirstName, p.LastName, p.PilotLevel, p.PhoneNum, p.Salary "
            self.prefix2 = "from PILOT p "
            self.prefix3 = "where p.PilotLevel = '%s' " % level
            if len(name)>0:
                self.prefix3+="and  p.FirstName = '%s'" % name
            if len(staff_id)>0:
                self.prefix3+="and  p.PilotID = '%s'" % staff_id
        if occupation=='Maintainer':
            self.prefix1 = "select m.MTStaffID, m.FirstName, m.LastName, m.MTLevel, m.PhoneNum, m.Salary "
            self.prefix2 = "from MAINTAINER m "
            self.prefix3 = "where m.MTLevel = '%s' " % level
            if len(name)>0:
                self.prefix3+="and  m.FirstName = '%s'" % name
            if len(staff_id)>0:
                self.prefix3+="and  m.MTStaffID = '%s'" % staff_id
        query_order = self.prefix1 + self.prefix2 + self.prefix3
        self.cursor.execute(query_order)
        k = 0
        for attribute in self.cursor:
            print("------", attribute)
            w = 0
            for j in attribute:
                print(j)
                instance = attribute[j]
                if type(instance) == int:
                    newItem = QTableWidgetItem(str(instance))
                else:
                    newItem = QTableWidgetItem(instance)
                if j == 'PilotID' or j == 'StaffID' or j == 'MTStaffID':
                    self.tableWidget_2.setItem(k, 0, newItem)
                if j == 'FirstName':
                    self.tableWidget_2.setItem(k, 1, newItem)
                if j == 'LastName':
                    self.tableWidget_2.setItem(k, 2, newItem)
                if j == 'PilotLevel' or j == 'CrewLevel' or j == 'MTLevel':
                    self.tableWidget_2.setItem(k, 3, newItem)
                if j == 'PhoneNum':
                    self.tableWidget_2.setItem(k, 4, newItem)
                w += 1
            k += 1
        print((occupation))
        print(level)
        print(len(name))
        print(staff_id)

    def query_airport(self):
        self.tableWidget_3.clearContents()
        if self.comboBox_6.currentText() != "All":
            airport = self.comboBox_6.currentText()[-4:-1]
            self.prefix3 = "where a.FCCCode= '%s'" % airport
        else:
            self.prefix3 = ''

        self.prefix1 = "select a.FCCCode, a.AirLevel, a.FlightCap, a.AirportName "
        self.prefix2 = "from AIRPORT a "

        query_order = self.prefix1 + self.prefix2 + self.prefix3
        self.cursor.execute(query_order)
        k = 0
        for attribute in self.cursor:
            print("------", attribute)
            w = 0
            for j in attribute:
                print(j)
                instance = attribute[j]
                if type(instance) == int:
                    newItem = QTableWidgetItem(str(instance))
                else:
                    newItem = QTableWidgetItem(instance)
                if j == 'FCCCode':
                    self.tableWidget_3.setItem(k, 0, newItem)
                if j == 'AirportName':
                    self.tableWidget_3.setItem(k, 1, newItem)
                if j == 'AirLevel':
                    self.tableWidget_3.setItem(k, 2, newItem)
                if j == 'FlightCap':
                    self.tableWidget_3.setItem(k, 3, newItem)
                w += 1
            k += 1

    def query_plane(self):
        self.planeTable.clearContents()
        regnum = self.planeRegNum.currentText()
        print(regnum)
        age = self.planeAge.text()
        print(age)
        modelid = self.planeModelID.currentText()
        print(modelid)
        query = "SELECT p.RegiNum, p.Age, p.ModelID, m.MaxCapacity, m.MaxMileage, m.MinAirLevel from plane p, planemodel m where p.ModelID = m.ModelID "
        if regnum != '':
            query += "and p.RegiNum = '%s' " % regnum
        if age != '':
            query += "and p.Age = '%s' " % age
        if modelid != '':
            query += "and p.ModelID = '%s' " % modelid
        print(query)
        self.cursor.execute(query)
        k = 0
        for attribute in self.cursor:
            w = 0
            for j in attribute:
                instance = attribute[j]
                if type(instance) == int:
                    newItem = QTableWidgetItem(str(instance))
                else:
                    newItem = QTableWidgetItem(instance)
                if j == 'RegiNum':
                    self.planeTable.setItem(k, 0, newItem)
                if j == 'Age':
                    self.planeTable.setItem(k, 1, newItem)
                if j == 'ModelID':
                    self.planeTable.setItem(k, 2, newItem)
                if j == 'MaxCapacity':
                    self.planeTable.setItem(k, 3, newItem)
                if j == 'MaxMileage':
                    self.planeTable.setItem(k, 4, newItem)
                if j == 'MinAirLevel':
                    self.planeTable.setItem(k, 5, newItem)
                w += 1
            k += 1

    def insert_flight(self):
        insert = "INSERT INTO FLIGHT VALUES ("
        flightID = self.newDate.dateTime().toString("MMdd") + 'LG' + self.newFlightCode.text()
        insert += "'%s', " % flightID
        date = self.newDate.dateTime().toString("yyyy-MM-dd")
        insert += "'%s', " % date
        code = self.newFlightCode.text()
        insert += "'LG%s', " % code
        pilot = self.newPilotID.currentText()
        insert += "'%s', " % pilot
        passnum = self.newPassengerNum.text()
        insert += "'%s', " % passnum
        deptime = self.newDepTime.time().toString("HH:mm:ss")
        insert += "'%s', " % deptime
        arrtime = self.newArrTime.time().toString("HH:mm:ss")
        insert += "'%s', " % arrtime
        depFCC = self.newDepFCCCode.currentText()[-4:-1]
        insert += "'%s', " % depFCC
        stpFCC = self.newStpFCCCode.currentText()
        if stpFCC=="":
            insert += "NULL, "
        else:
            insert += "'%s', " % stpFCC[-4:-1]
        arrFCC = self.newArrFCCCode.currentText()[-4:-1]
        insert += "'%s', " % arrFCC


        regnum = self.newRegNum.currentText()
        insert += "'%s')" % regnum
        print(insert)
        try:
            self.cursor.execute(insert)
            self.show_flight_table()
            self.connection.commit()
        except:
            info = QMessageBox.about(self, "Warning", "Duplicate Flight ID and date.")
            print(info)



    def delete_flight(self):
        index = self.tableWidget_6.selectionModel().currentIndex()
        row = index.row()
        item = self.tableWidget_6.itemFromIndex(index)
        flightid = self.tableWidget_6.item(row,2).text()[-5:-3] + self.tableWidget_6.item(row,2).text()[-2:] + self.tableWidget_6.item(row,0).text()
        delete1 = "DELETE FROM ONDUTY WHERE FlightID = '%s' " % flightid
        delete2 = "DELETE FROM COPILOT WHERE FlightID = '%s' " % flightid
        delete3 = "DELETE FROM flight WHERE FlightID = '%s' " % flightid
        print(delete1, delete2, delete3)
        self.cursor.execute(delete1)
        self.cursor.execute(delete2)
        self.cursor.execute(delete3)
        self.show_flight_table()
        self.connection.commit()

    def show_flight_table(self):
        self.tableWidget_6.clearContents()
        self.cursor.execute('SELECT * FROM flight')
        k = 0
        for attribute in self.cursor:
            w = 0
            for j in attribute:
                instance = attribute[j]
                if type(instance) == int:
                    newItem = QTableWidgetItem(str(instance))
                else:
                    newItem = QTableWidgetItem(instance)
                if j == 'FlightCode':
                    self.tableWidget_6.setItem(k, 0, newItem)
                if j == 'PlaneRegiNum':
                    self.tableWidget_6.setItem(k, 1, newItem)
                if j == 'FlightDATE':
                    self.tableWidget_6.setItem(k, 2, newItem)
                if j == 'TakeoffTime':
                    self.tableWidget_6.setItem(k, 3, newItem)
                if j == 'DepApFCC':
                    self.tableWidget_6.setItem(k, 4, newItem)
                if j == 'StopByFCC':
                    self.tableWidget_6.setItem(k, 5, newItem)
                if j == 'EstArrTime':
                    self.tableWidget_6.setItem(k, 6, newItem)
                if j == 'ArrApFCC':
                    self.tableWidget_6.setItem(k, 7, newItem)
                if j == 'CapID':
                    self.tableWidget_6.setItem(k, 8, newItem)
                if j == 'PassengerNum':
                    self.tableWidget_6.setItem(k, 9, newItem)
                w += 1
            k += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MyMainwindow()
    ui.show()
    sys.exit(app.exec_())


