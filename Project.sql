drop database LGUAirline;
CREATE DATABASE LGUAirline;
USE LGUAirline;

CREATE TABLE PLANEMODEL
( 	ModelID VARCHAR(7) NOT NULL,
	MaxCapacity Integer NOT NULL,
	MaxMileage Integer NOT NULL,
    MinAirLevel CHAR(2) NOT NULL,
	PRIMARY KEY(ModelID)
);

CREATE TABLE AIRPORT
(	FCCCode CHAR(3) NOT NULL,
	AirLevel CHAR(2) NOT NULL,
    FlightCap Integer NOT NULL,
    AirportName VARCHAR(100) Unique NOT NULL,
    PRIMARY KEY(FCCCode)
);

CREATE TABLE CABINCREW
(	StaffID CHAR(4) NOT NULL,
	Salary Integer NOT NULL,
    WeeklyWorkingHours Integer NOT NULL,
    CrewLevel VARCHAR(15) NOT NULL,
    PhoneNum CHAR(11) Unique NOT NULL,
    FirstName VARCHAR(20) NOT NULL,
    LastName VARCHAR(20) NOT NULL,
    PRIMARY KEY(StaffID)
);

CREATE TABLE PILOT
(	PilotID CHAR(4) NOT NULL,
	FlightHour Integer NOT NULL,
    WeeklyWorkingHours Integer NOT NULL,
	Salary Integer NOT NULL,
    PilotLevel VARCHAR(15) NOT NULL,
    PhoneNum CHAR(11) Unique NOT NULL,
    FirstName VARCHAR(20) NOT NULL,
    LastName VARCHAR(20) NOT NULL,
    ExpModelID VARCHAR(7) NOT NULL,
    PRIMARY KEY (PilotID),
    FOREIGN KEY (ExpModelID) REFERENCES PLANEMODEL(ModelID)
);

CREATE TABLE MAINTAINER
(	MTStaffID CHAR(4) NOT NULL,
	Salary Integer NOT NULL,	
    WeeklyWorkingHours Integer NOT NULL,
    MTLevel VARCHAR(15) NOT NULL,
    PhoneNum CHAR(11) Unique NOT NULL,
    FirstName VARCHAR(20) NOT NULL,
    LastName VARCHAR(20) NOT NULL,
    PRIMARY KEY (MTStaffID)
);

CREATE TABLE PLANE
(	RegiNum CHAR(6) NOT NULL,
	Age Integer NOT NULL,
    ModelID VARCHAR(7) NOT NULL,
    PRIMARY KEY (RegiNum),
    FOREIGN KEY (ModelID) REFERENCES PLANEMODEL(ModelID)
);

CREATE TABLE FLIGHT
(	FlightID VARCHAR(10) NOT NULL,
	FlightDATE CHAR(10) NOT NULL,
    FlightCode VARCHAR(6) NOT NULL,
    CapID CHAR(4) NOT NULL,
    PassengerNum Integer NOT NULL,
    TakeoffTime CHAR(8) NOT NULL,
    EstArrTime CHAR(8) NOT NULL,
    DepApFCC CHAR(3) NOT NULL,
    StopByFCC CHAR(3),
    ArrApFCC CHAR(3) NOT NULL,
    PlaneRegiNum CHAR(6) NOT NULL,
    PRIMARY KEY (FlightID),
    Foreign KEY (DepApFCC) References AIRPORT(FCCCode),
    Foreign KEY (ArrApFCC) References AIRPORT(FCCCode),
    Foreign KEY (PlaneRegiNum) References PLANE(RegiNum),
    foreign key (CapID) References PILOT(PilotID)
);
    
CREATE TABLE CoPilot
(	PliotID CHAR(4) NOT NULL,
	FlightID VARCHAR(10) NOT NULL,
    PRIMARY KEY (PliotID, FlightID),
    Foreign KEY (PliotID) References PILOT(PilotID),
    Foreign KEY (FlightID) References FLIGHT(FlightID)
);

CREATE TABLE MAINTAIN
(	MTStaffID CHAR(4) NOT NULL,
    PlaneRegiNum CHAR(6) NOT NULL,
	Foreign KEY (MTStaffID) References MAINTAINER(MTStaffID),
    Foreign KEY (PlaneRegiNum) References PLANE(RegiNum)
);

CREATE TABLE ONDUTY
(	StaffID CHAR(4) NOT NULL,
	FlightID VARCHAR(10) NOT NULL,
    PRIMARY KEY (StaffID, FlightID),
    Foreign KEY (StaffID) References CABINCREW(StaffID),
    Foreign KEY (FlightID) References FLIGHT(FlightID)
);

INSERT INTO AIRPORT VALUES ('SZX','4F','7','Shenzhen Baoan International Airport');
INSERT INTO AIRPORT VALUES ('PVG','4F','9','Shanghai Pudong International Airport');
INSERT INTO AIRPORT VALUES ('SHA','4E','5','Shanghai Hongqiao International Airport');
INSERT INTO AIRPORT VALUES ('HGH','4F','6','Hangzhou Xiaoshan International Airport');
INSERT INTO AIRPORT VALUES ('PEK','4F','11','Beijing Capital International Airport');
INSERT INTO AIRPORT VALUES ('WUH','4F','8','Wuhan Tianhe International Airport');
INSERT INTO AIRPORT VALUES ('XIY','4F','3',"Xi'an Xianyang International Airport");
INSERT INTO AIRPORT VALUES ('CTU','4F','4',"Chengdu Shuangliu International Airport");
INSERT INTO AIRPORT VALUES ('CAN','4F','4',"Guangzhou Baiyun International Airport");
INSERT INTO AIRPORT VALUES ('KHN','4E','3',"Nanchang Changbei International Airport");

INSERT INTO PLANEMODEL VALUES ('737-800','189','5370',"4C");
INSERT INTO PLANEMODEL VALUES ('A321','220','5600',"4C");

INSERT INTO CABINCREW VALUES ('C001', '3000', '35', 'F1', '13712345678', 'Yu', 'Chen');
INSERT INTO CABINCREW VALUES ('C002', '3500', '39', 'F2', '13723456789', 'Hao', 'Chen');
INSERT INTO CABINCREW VALUES ('C003', '3600', '40', 'F2', '13823456789', 'Erba', 'Da');
INSERT INTO CABINCREW VALUES ('C004', '2900', '40', 'F1', '13923456789', 'Kun', 'Xin');
INSERT INTO CABINCREW VALUES ('C005', '4000', '41', 'F4', '13223456789', 'Yuechen', 'Gao');
INSERT INTO CABINCREW VALUES ('C006', '3800', '39', 'F3', '13934567890', 'Xi', 'Zhu');
INSERT INTO CABINCREW VALUES ('C007', '3000', '35', 'F1', '13512345678', 'Ertu', 'Hu');
INSERT INTO CABINCREW VALUES ('C008', '3500', '39', 'F2', '13623456789', 'Ziao', 'Wang');
INSERT INTO CABINCREW VALUES ('C009', '3600', '40', 'F2', '13323456789', 'Si', 'Li');
INSERT INTO CABINCREW VALUES ('C010', '2900', '40', 'F1', '13423456789', 'San', 'Zhang');
INSERT INTO CABINCREW VALUES ('C011', '4000', '41', 'F4', '13523456789', 'Han', 'Wang');
INSERT INTO CABINCREW VALUES ('C012', '3800', '39', 'F3', '13634567890', 'Shimin', 'Li');
INSERT INTO CABINCREW VALUES ('C013', '4000', '41', 'F4', '13223456769', 'Zheng', 'Yin');
INSERT INTO CABINCREW VALUES ('C014', '3800', '39', 'F3', '13934567850', 'Bang', 'Liu');
INSERT INTO CABINCREW VALUES ('C015', '3000', '35', 'F1', '13512345698', 'Yu', 'Xiang');
INSERT INTO CABINCREW VALUES ('C016', '3500', '39', 'F2', '13623456719', 'Yuanzhang', 'Zhu');

INSERT INTO PILOT VALUES ('P001', '10000', '40', '8600', 'F1', '18023456789', 'Yihua', 'Lu', '737-800');
INSERT INTO PILOT VALUES ('P002', '8000', '40', '7500', 'F1', '18123456789', 'Jiagen', 'Li', 'A321');
INSERT INTO PILOT VALUES ('P003', '10000', '40', '8600', 'F2', '18143456789', 'Qiangdong', 'Liu', '737-800');
INSERT INTO PILOT VALUES ('P004', '8000', '40', '7500', 'F2', '18923456789', 'Yun', 'Ma', 'A321');
INSERT INTO PILOT VALUES ('P005', '4000', '41', '6400', 'F3', '18084686111', 'Rulin', 'Liu', '737-800');
INSERT INTO PILOT VALUES ('P006', '3000', '39', '5300', 'F3', '18134567890', 'Yao', 'Xu', 'A321');
INSERT INTO PILOT VALUES ('P007', '4000', '41', '6400', 'F4', '18084686101', 'Yangsheng', 'Xu', '737-800');
INSERT INTO PILOT VALUES ('P008', '3000', '39', '5300', 'F4', '18134567800', 'Zhiquan', 'Luo', 'A321');

INSERT INTO MAINTAINER VALUES ('M001', '4000', '50', 'F1', '18012312349', 'Haoxiang', 'Lin');
INSERT INTO MAINTAINER VALUES ('M002', '4500', '45', 'F2', '18032312949', 'Shujie', 'Wang');

INSERT INTO PLANE VALUES ('B-5165', '2', '737-800');
INSERT INTO PLANE VALUES ('B-5332', '1', '737-800');
INSERT INTO PLANE VALUES ('B-6312', '3', 'A321');
INSERT INTO PLANE VALUES ('B-6443', '1', 'A321');
INSERT INTO PLANE VALUES ('B-2165', '10', '737-800');
INSERT INTO PLANE VALUES ('B-2178', '9', '737-800');
INSERT INTO PLANE VALUES ('B-5552', '6', 'A321');
INSERT INTO PLANE VALUES ('B-5983', '5', 'A321');

INSERT INTO FLIGHT VALUES ('0422LG9101', '2019-04-22', 'LG9101', 'P001', '160', '07:30:00', '10:40:00', 'SZX', NULL, 'PEK', 'B-5332');
INSERT INTO FLIGHT VALUES ('0422LG9104', '2019-04-22', 'LG9102', 'P001', '173', '14:25:00', '17:40:00', 'PEK', NULL, 'SZX', 'B-5332');
INSERT INTO FLIGHT VALUES ('0422LG9509', '2019-04-22', 'LG9509', 'P002', '180', '11:05:00', '16:10:00', 'SZX', 'KHN', 'PVG', 'B-6312');
INSERT INTO FLIGHT VALUES ('0422LG9510', '2019-04-22', 'LG9510', 'P002', '203', '18:10:00', '22:40:00', 'PVG', 'KHN', 'SZX', 'B-6312');
INSERT INTO FLIGHT VALUES ('0422LG9407', '2019-04-22', 'LG9407', 'P003', '143', '15:55:00', '18:25:00', 'SZX', NULL, 'CTU', 'B-5165');
INSERT INTO FLIGHT VALUES ('0422LG9408', '2019-04-22', 'LG9408', 'P003', '131', '19:55:00', '22:20:00', 'CTU', NULL, 'SZX', 'B-5165');
INSERT INTO FLIGHT VALUES ('0422LG9401', '2019-04-22', 'LG9401', 'P004', '174', '08:10:00', '10:45:00', 'SZX', NULL, 'CTU', 'B-6443');
INSERT INTO FLIGHT VALUES ('0422LG9402', '2019-04-22', 'LG9402', 'P004', '190', '12:25:00', '14:50:00', 'CTU', NULL, 'SZX', 'B-6443');

INSERT INTO FLIGHT VALUES ('0423LG9101', '2019-04-23', 'LG9101', 'P001', '161', '07:30:00', '10:40:00', 'SZX', NULL, 'PEK', 'B-5332');
INSERT INTO FLIGHT VALUES ('0423LG9104', '2019-04-23', 'LG9102', 'P001', '174', '14:25:00', '17:40:00', 'PEK', NULL, 'SZX', 'B-5332');
INSERT INTO FLIGHT VALUES ('0423LG9509', '2019-04-23', 'LG9509', 'P002', '192', '11:05:00', '16:10:00', 'SZX', 'KHN', 'PVG', 'B-6312');
INSERT INTO FLIGHT VALUES ('0423LG9510', '2019-04-23', 'LG9510', 'P002', '188', '18:10:00', '22:40:00', 'PVG', 'KHN', 'SZX', 'B-6312');
INSERT INTO FLIGHT VALUES ('0423LG9407', '2019-04-23', 'LG9407', 'P003', '147', '15:55:00', '18:25:00', 'SZX', NULL, 'CTU', 'B-5165');
INSERT INTO FLIGHT VALUES ('0423LG9408', '2019-04-23', 'LG9408', 'P003', '135', '19:55:00', '22:20:00', 'CTU', NULL, 'SZX', 'B-5165');
INSERT INTO FLIGHT VALUES ('0423LG9401', '2019-04-23', 'LG9401', 'P004', '175', '08:10:00', '10:45:00', 'SZX', NULL, 'CTU', 'B-6443');
INSERT INTO FLIGHT VALUES ('0423LG9402', '2019-04-23', 'LG9402', 'P004', '199', '12:25:00', '14:50:00', 'CTU', NULL, 'SZX', 'B-6443');

INSERT INTO CoPilot VALUES ('P005', '0422LG9509');
INSERT INTO CoPilot VALUES ('P005', '0422LG9510');
INSERT INTO CoPilot VALUES ('P006', '0422LG9101');
INSERT INTO CoPilot VALUES ('P006', '0422LG9104');
INSERT INTO CoPilot VALUES ('P007', '0422LG9407');
INSERT INTO CoPilot VALUES ('P007', '0422LG9408');
INSERT INTO CoPilot VALUES ('P008', '0422LG9401');
INSERT INTO CoPilot VALUES ('P008', '0422LG9402');

INSERT INTO CoPilot VALUES ('P005', '0423LG9509');
INSERT INTO CoPilot VALUES ('P005', '0423LG9510');
INSERT INTO CoPilot VALUES ('P006', '0423LG9101');
INSERT INTO CoPilot VALUES ('P006', '0423LG9104');
INSERT INTO CoPilot VALUES ('P007', '0423LG9407');
INSERT INTO CoPilot VALUES ('P007', '0423LG9408');
INSERT INTO CoPilot VALUES ('P008', '0423LG9401');
INSERT INTO CoPilot VALUES ('P008', '0423LG9402');

INSERT INTO MAINTAIN VALUES ('M001', 'B-6312');
INSERT INTO MAINTAIN VALUES ('M002', 'B-6312');
INSERT INTO MAINTAIN VALUES ('M001', 'B-5332');
INSERT INTO MAINTAIN VALUES ('M001', 'B-6443');
INSERT INTO MAINTAIN VALUES ('M002', 'B-5165');
INSERT INTO MAINTAIN VALUES ('M001', 'B-5165');

INSERT INTO ONDUTY VALUES ('C001', '0422LG9101');
INSERT INTO ONDUTY VALUES ('C002', '0422LG9101');
INSERT INTO ONDUTY VALUES ('C003', '0422LG9101');
INSERT INTO ONDUTY VALUES ('C004', '0422LG9101');
INSERT INTO ONDUTY VALUES ('C001', '0422LG9104');
INSERT INTO ONDUTY VALUES ('C002', '0422LG9104');
INSERT INTO ONDUTY VALUES ('C003', '0422LG9104');
INSERT INTO ONDUTY VALUES ('C004', '0422LG9104');
INSERT INTO ONDUTY VALUES ('C008', '0422LG9509');
INSERT INTO ONDUTY VALUES ('C009', '0422LG9509');
INSERT INTO ONDUTY VALUES ('C010', '0422LG9509');
INSERT INTO ONDUTY VALUES ('C011', '0422LG9509');
INSERT INTO ONDUTY VALUES ('C008', '0422LG9510');
INSERT INTO ONDUTY VALUES ('C009', '0422LG9510');
INSERT INTO ONDUTY VALUES ('C010', '0422LG9510');
INSERT INTO ONDUTY VALUES ('C011', '0422LG9510');

INSERT INTO ONDUTY VALUES ('C005', '0423LG9101');
INSERT INTO ONDUTY VALUES ('C006', '0423LG9101');
INSERT INTO ONDUTY VALUES ('C007', '0423LG9101');
INSERT INTO ONDUTY VALUES ('C012', '0423LG9101');
INSERT INTO ONDUTY VALUES ('C013', '0423LG9104');
INSERT INTO ONDUTY VALUES ('C014', '0423LG9104');
INSERT INTO ONDUTY VALUES ('C015', '0423LG9104');
INSERT INTO ONDUTY VALUES ('C016', '0423LG9104');
INSERT INTO ONDUTY VALUES ('C005', '0423LG9509');
INSERT INTO ONDUTY VALUES ('C006', '0423LG9509');
INSERT INTO ONDUTY VALUES ('C007', '0423LG9509');
INSERT INTO ONDUTY VALUES ('C012', '0423LG9509');
INSERT INTO ONDUTY VALUES ('C005', '0423LG9510');
INSERT INTO ONDUTY VALUES ('C006', '0423LG9510');
INSERT INTO ONDUTY VALUES ('C007', '0423LG9510');
INSERT INTO ONDUTY VALUES ('C012', '0423LG9510');

INSERT INTO ONDUTY VALUES ('C001', '0423LG9407');
INSERT INTO ONDUTY VALUES ('C002', '0423LG9407');
INSERT INTO ONDUTY VALUES ('C003', '0423LG9407');
INSERT INTO ONDUTY VALUES ('C004', '0423LG9407');
INSERT INTO ONDUTY VALUES ('C001', '0423LG9408');
INSERT INTO ONDUTY VALUES ('C002', '0423LG9408');
INSERT INTO ONDUTY VALUES ('C003', '0423LG9408');
INSERT INTO ONDUTY VALUES ('C004', '0423LG9408');
INSERT INTO ONDUTY VALUES ('C008', '0423LG9401');
INSERT INTO ONDUTY VALUES ('C009', '0423LG9401');
INSERT INTO ONDUTY VALUES ('C010', '0423LG9401');
INSERT INTO ONDUTY VALUES ('C011', '0423LG9401');
INSERT INTO ONDUTY VALUES ('C008', '0423LG9402');
INSERT INTO ONDUTY VALUES ('C009', '0423LG9402');
INSERT INTO ONDUTY VALUES ('C010', '0423LG9402');
INSERT INTO ONDUTY VALUES ('C011', '0423LG9402');

INSERT INTO ONDUTY VALUES ('C005', '0422LG9407');
INSERT INTO ONDUTY VALUES ('C006', '0422LG9407');
INSERT INTO ONDUTY VALUES ('C007', '0422LG9407');
INSERT INTO ONDUTY VALUES ('C012', '0422LG9407');
INSERT INTO ONDUTY VALUES ('C013', '0422LG9408');
INSERT INTO ONDUTY VALUES ('C014', '0422LG9408');
INSERT INTO ONDUTY VALUES ('C015', '0422LG9408');
INSERT INTO ONDUTY VALUES ('C016', '0422LG9408');
INSERT INTO ONDUTY VALUES ('C005', '0422LG9401');
INSERT INTO ONDUTY VALUES ('C006', '0422LG9401');
INSERT INTO ONDUTY VALUES ('C007', '0422LG9401');
INSERT INTO ONDUTY VALUES ('C012', '0422LG9401');
INSERT INTO ONDUTY VALUES ('C013', '0422LG9402');
INSERT INTO ONDUTY VALUES ('C014', '0422LG9402');
INSERT INTO ONDUTY VALUES ('C015', '0422LG9402');
INSERT INTO ONDUTY VALUES ('C016', '0422LG9402');


