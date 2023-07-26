# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PyQt5.QtWidgets import QApplication,QLineEdit, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem, QComboBox
from PyQt5.QtCore import QSize, Qt
from PyQt5.Qt import QMainWindow, QVBoxLayout, QWidget, QLabel, QAction, Qt, QMessageBox, QApplication

class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        self.setWindowTitle('Отчет')
        self.setMinimumWidth(765)
        self.setMinimumHeight(620)
        self.tableWidget3 = QtWidgets.QTableWidget(self)
        self.tableWidget3.setGeometry(QtCore.QRect(10, 10, 548, 604))
        self.tableWidget3.setRowCount(20)
        self.tableWidget3.setColumnCount(7)
        self.tableWidget3.horizontalHeader().hide()
        self.tableWidget3.verticalHeader().hide()
        self.tableWidget3.setItem(0, 0, QTableWidgetItem("№"))
        self.tableWidget3.setItem(0, 3, QTableWidgetItem("1"))
        self.tableWidget3.setItem(0, 4, QTableWidgetItem("2"))
        self.tableWidget3.setItem(0, 5, QTableWidgetItem("3"))
        self.tableWidget3.setItem(0, 6, QTableWidgetItem("4"))
        self.tableWidget3.setItem(0, 7, QTableWidgetItem("5"))
        self.tableWidget3.setItem(1, 3, QTableWidgetItem("SSJ-100   "))
        self.tableWidget3.setItem(1, 4, QTableWidgetItem("Airbus A310"))
        self.tableWidget3.setItem(1, 5, QTableWidgetItem("ИЛ-96М"))
        self.tableWidget3.setItem(1, 6, QTableWidgetItem("Airbus A320"))
        #self.tableWidget3.setItem(1, 7, QTableWidgetItem("Boeing-737"))
        self.tableWidget3.setItem(2, 3, QTableWidgetItem("1"))
        self.tableWidget3.setItem(2, 4, QTableWidgetItem("1"))
        self.tableWidget3.setItem(2, 5, QTableWidgetItem("1"))
        self.tableWidget3.setItem(2, 6, QTableWidgetItem("2"))
        #self.tableWidget3.setItem(2, 7, QTableWidgetItem("1"))
        #self.tableWidget3.setItem(0, 1, QTableWidgetItem("Состояние эксплуатации"))
        #self.tableWidget3.setItem(0, 2, QTableWidgetItem("Усл. обозн."))
        self.tableWidget3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget3.setSpan(4,0,20,1)
        self.tableWidget3.setSpan(4,1,9,1)
        pic = QtGui.QPixmap("data/22.bmp")
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setPixmap(pic)
        self.tableWidget3.setCellWidget(4, 0, self.label2)
        self.tableWidget3.setItem(4, 0, QTableWidgetItem("0"))
        pic = QtGui.QPixmap("data/23.bmp")
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setPixmap(pic)
        self.tableWidget3.setCellWidget(4, 1, self.label2)
        self.tableWidget3.setItem(4, 1, QTableWidgetItem("0"))
        pic = QtGui.QPixmap("data/24.bmp")
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setPixmap(pic)
        self.tableWidget3.setCellWidget(13, 1, self.label2)
        self.tableWidget3.setItem(13, 1, QTableWidgetItem("0"))
        self.tableWidget3.setSpan(13,1,20,1)
        self.tableWidget3.setSpan(0,0,1,3)
        self.tableWidget3.setItem(4, 2, QTableWidgetItem("Всего исправных самолетов"))
        self.tableWidget3.setItem(5, 2, QTableWidgetItem("Время в рейсе"))
        self.tableWidget3.setItem(6, 2, QTableWidgetItem("Обеспечение вылета"))
        self.tableWidget3.setItem(7, 2, QTableWidgetItem("В резерве"))
        self.tableWidget3.setItem(8, 2, QTableWidgetItem("Простой по метео - условиям и запретам"))
        self.tableWidget3.setItem(9, 2, QTableWidgetItem("Исправные, не совершающие полётов"))
        self.tableWidget3.setItem(10, 2, QTableWidgetItem("На техническом обслуживании"))
        self.tableWidget3.setItem(11, 2, QTableWidgetItem("В ремонте"))
        self.tableWidget3.setItem(12, 2, QTableWidgetItem("Ожидание ремонта"))
        self.tableWidget3.setItem(13, 2, QTableWidgetItem("Восстановление после повреждения"))
        self.tableWidget3.setItem(14, 2, QTableWidgetItem("Отсутствие запасных частей"))
        self.tableWidget3.setItem(15, 2, QTableWidgetItem("Отсутствие двигателей"))
        self.tableWidget3.setItem(16, 2, QTableWidgetItem("Доработки по бюллетеням"))
        self.tableWidget3.setItem(17, 2, QTableWidgetItem("Рекламация промышленности"))
        self.tableWidget3.setItem(18, 2, QTableWidgetItem("Рекламация ремонтным заводом"))
        self.tableWidget3.setItem(19, 2, QTableWidgetItem("Ожидание списания"))
        self.tableWidget3.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        
        #self.tableWidget3.setItem(20, 2, QTableWidgetItem(""))
        
        self.tableWidget3.resizeColumnsToContents()
        self.tableWidget3.setSpan(1,0,1,3)
        self.tableWidget3.setItem(1, 0, QTableWidgetItem("Тип самолета"))
        self.tableWidget3.setSpan(2,0,1,3)
        self.tableWidget3.setItem(2, 0, QTableWidgetItem("Количество самолетов"))
        self.tableWidget3.setSpan(3,0,1,3)
        self.tableWidget3.setItem(3, 0, QTableWidgetItem("Календарный фонд времемни самолето-час"))
        for j in range(8):
            if j == 1 or j==2:
                p = 0
            elif j == 7:
                p = 0
            else:
                self.tableWidget3.item(0, j).setBackground(QtGui.QColor(219,235,255))
                self.tableWidget3.item(1, j).setBackground(QtGui.QColor(219,235,255))
                self.tableWidget3.item(2, 0).setBackground(QtGui.QColor(219,235,255))
                self.tableWidget3.item(3, 0).setBackground(QtGui.QColor(219,235,255))
                self.tableWidget3.item(13, 1).setBackground(QtGui.QColor(219,235,255))
                self.tableWidget3.item(4, 0).setBackground(QtGui.QColor(219,235,255))
                self.tableWidget3.item(4, 1).setBackground(QtGui.QColor(219,235,255))
        for j in range(21):
            if j>=4 and j<20:
                self.tableWidget3.item(j, 2).setBackground(QtGui.QColor(219,235,255))
        #############
        self.groupBox2 = QtWidgets.QGroupBox(self)
        self.groupBox2.setGeometry(QtCore.QRect(565, 0, 200, 160))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.groupBox2.setFont(font)
        self.groupBox2.setMouseTracking(False)
        self.groupBox2.setAcceptDrops(False)
        self.groupBox2.setAutoFillBackground(False)
        self.groupBox2.setFlat(False)
        self.groupBox2.setCheckable(False)
        self.groupBox2.setTitle("Настройки")
        self.qlabel2 = QLabel(self.groupBox2)
        self.qlabel2.move(10,30)
        self.qlabel2.setText('Месяц:')
        self.combo2 = QComboBox(self.groupBox2)
        self.combo2.addItem("Январь")
        self.combo2.addItem("Февраль")
        self.combo2.addItem("Март")
        self.combo2.addItem("Апрель")
        self.combo2.addItem("Май")
        self.combo2.addItem("Июнь")
        self.combo2.addItem("Июль")
        self.combo2.addItem("Август")
        self.combo2.addItem("Сентябрь")
        self.combo2.addItem("Октябрь")
        self.combo2.addItem("Ноябрь")
        self.combo2.addItem("Декабрь")
        self.combo2.move(80, 30)
        self.qlabel3 = QLabel(self.groupBox2)
        self.qlabel3.move(10,60)
        self.qlabel3.setText('Год:')
        self.line = QLineEdit(self.groupBox2)
        self.line.move(41, 60)
        self.pushButton = QtWidgets.QPushButton(self.groupBox2)
        self.pushButton.setGeometry(QtCore.QRect(10, 100, 169, 31))
        self.pushButton.clicked.connect(self.tab)
        self.pushButton.setText('ПРОСМОТР')


        
    def tab(self):
        year=self.line.text()
        mmm = str(self.combo2.currentIndex()+1)
        #samin = self.combo.currentIndex()+1
        try:
            dvsegoall = 0
            dvsisprall = 0
            dvpolall = 0
            dobspall = 0
            dmeteoall = 0
            drezrvall = 0
            disneisall = 0
            dvsneisprall = 0
            dustrnall = 0
            dozhoball = 0
            dobslall = 0
            dozhperall = 0
            dperall = 0
            dnochall = 0
            dvremntall = 0
            dozhrall = 0
            dvossprall = 0
            dotszpall = 0
            dotsdvall = 0
            ddorbulall = 0
            drekprall = 0
            drekremzall = 0
            dozhspall = 0
            for samin in range(5):
                vsegoall = 0
                vsisprall = 0
                vpolall = 0
                obspall = 0
                meteoall = 0
                rezrvall = 0
                isneisall = 0
                vsneisprall = 0
                ustrnall = 0
                ozhoball = 0
                obslall = 0
                ozhperall = 0
                perall = 0
                nochall = 0
                vremntall = 0
                ozhrall = 0
                vossprall = 0
                otszpall = 0
                otsdvall = 0
                dorbulall = 0
                rekprall = 0
                rekremzall = 0
                ozhspall = 0
                samin = samin+1
                for i in range(31):
                    #try:
                        i = i+1
                        ii = i
                        if i<10:
                            dddd = "0"+str(i)
                        with open("base/"+dddd+"-0"+mmm+"-"+year, 'r') as f:
                        #with open("base/22-09-2021", 'r') as f:
                            text = f.read().split("\n")
                            #.replace("\n", " ")
                        vsego = 0
                        sp = text[samin].split(' ')
                        ###########
                        for i in sp:
                            if i!='0' and i!='':
                                vsego+=1
                        vsegoall += vsego
                        vsego = str((vsego*10)//60)+"ч. "+str((vsego*10)%60)+"м."
                        #######
                        vsispr = 0
                        for i in sp:
                            if i=='1' or i=='2'or i=='3'or i=='4'or i=='5':
                                vsispr+=1
                        vsisprall += vsispr
                        vsispr = str((vsispr*10)//60)+"ч. "+str((vsispr*10)%60)+"м."
                        #######
                        vpol = 0
                        for i in sp:
                            if i=='1':
                                vpol+=1
                        vpolall += vpol
                        vpol = str((vpol*10)//60)+"ч. "+str((vpol*10)%60)+"м."
                        #######
                        obsp = 0
                        for i in sp:
                            if i=='2':
                                obsp+=1
                        obspall += obsp
                        obsp = str((obsp*10)//60)+"ч. "+str((obsp*10)%60)+"м."
                        #######
                        meteo = 0
                        for i in sp:
                            if i=='3':
                                meteo+=1
                        meteoall += meteo
                        meteo = str((meteo*10)//60)+"ч. "+str((meteo*10)%60)+"м."
                        #######
                        rezrv = 0
                        for i in sp:
                            if i=='4':
                                rezrv+=1
                        rezrvall += rezrv
                        rezrv = str((rezrv*10)//60)+"ч. "+str((rezrv*10)%60)+"м."
                        #######
                        isneis = 0
                        for i in sp:
                            if i=='5':
                                isneis+=1
                        isneisall += isneis
                        isneis = str((isneis*10)//60)+"ч. "+str((isneis*10)%60)+"м."
                        #######
                        vsneispr = 0
                        for i in sp:
                            if i!='1' and i!='2'and  i!='3'and  i!='4'and  i!='5'and  i!='0'and i!='':
                                vsneispr+=1
                        vsneispr = str((vsneispr*10)//60)+"ч. "+str((vsneispr*10)%60)+"м."
                        #######
                        ustrn = 0
                        for i in sp:
                            if i=='6':
                                ustrn+=1
                        ustrn = str((ustrn*10)//60)+"ч. "+str((ustrn*10)%60)+"м."
                        #######
                        ozhob = 0
                        for i in sp:
                            if i=='7':
                                ozhob+=1
                        ozhob= str((ozhob*10)//60)+"ч. "+str((ozhob*10)%60)+"м."
                        #######
                        obsl = 0
                        for i in sp:
                            if i=='8':
                                obsl+=1
                        obsl = str((obsl*10)//60)+"ч. "+str((obsl*10)%60)+"м."
                        #######
                        ozhper = 0
                        for i in sp:
                            if i=='9':
                                ozhper+=1
                        ozhper = str((ozhper*10)//60)+"ч. "+str((ozhper*10)%60)+"м."
                        #######
                        per = 0
                        for i in sp:
                            if i=='10':
                                per+=1
                        perall += per
                        per = str((per*10)//60)+"ч. "+str((per*10)%60)+"м."
                        #######
                        noch = 0
                        for i in sp:
                            if i=='11':
                                noch+=1
                        noch = str((noch*10)//60)+"ч. "+str((noch*10)%60)+"м."
                        #######
                        ozhr = 0
                        for i in sp:
                            if i=='12':
                                ozhr+=1
                        ozhrall += ozhr
                        ozhr = str((ozhr*10)//60)+"ч. "+str((ozhr*10)%60)+"м."
                        #######
                        vremnt = 0
                        for i in sp:
                            if i=='13':
                                vremnt+=1
                        vremntall += vremnt
                        vremnt = str((vremnt*10)//60)+"ч. "+str((vremnt*10)%60)+"м."
                        #######
                        otszp = 0
                        for i in sp:
                            if i=='14':
                                otszp+=1
                        otszpall += otszp
                        otszp = str((otszp*10)//60)+"ч. "+str((otszp*10)%60)+"м."
                        #######
                        otsdv = 0
                        for i in sp:
                            if i=='15':
                                otsdv+=1
                        otsdvall += otsdv
                        otsdv = str((otsdv*10)//60)+"ч. "+str((otsdv*10)%60)+"м."
                        #######
                        dorbul = 0
                        for i in sp:
                            if i=='16':
                                dorbul+=1
                        dorbulall += dorbul
                        dorbul = str((dorbul*10)//60)+"ч. "+str((dorbul*10)%60)+"м."
                        #######
                        rekpr = 0
                        for i in sp:
                            if i=='17':
                                rekpr+=1
                        rekprall += rekpr
                        rekpr = str((rekpr*10)//60)+"ч. "+str((rekpr*10)%60)+"м."
                        #######
                        rekremz = 0
                        for i in sp:
                            if i=='18':
                                rekremz+=1
                        rekremzall += rekremz
                        rekremz = str((rekremz*10)//60)+"ч. "+str((rekremz*10)%60)+"м."
                        #######
                        rasspr = 0
                        for i in sp:
                            if i=='19':
                                rasspr+=1
                        rasspr = str((rasspr*10)//60)+"ч. "+str((rasspr*10)%60)+"м."
                        #######
                        vosspr = 0
                        for i in sp:
                            if i=='20':
                                vosspr+=1
                        vossprall += vosspr
                        vosspr = str((vosspr*10)//60)+"ч. "+str((vosspr*10)%60)+"м."
                        #######
                        ozhsp = 0
                        for i in sp:
                            if i=='21':
                                ozhsp+=1
                        ozhspall += ozhsp
                        ozhsp = str((ozhsp*10)//60)+"ч. "+str((ozhsp*10)%60)+"м."
                        kispr = '0' ###надо формулу чел!!!!!!!
                        kisp = '0'
                        #self.tableWidget2.resizeColumnsToContents()
                    #except:
                        #p = 0
                print(samin)
                if samin >= 4:
                    dvsegoall += vsegoall
                    print(dvsegoall)
                    dvsisprall += vsisprall
                    dvpolall += vpolall
                    dobspall += obspall
                    dmeteoall += meteoall
                    drezrvall += rezrvall
                    disneisall += isneisall
                    dvsneisprall += vsneisprall
                    dustrnall += ustrnall
                    dozhoball += ozhoball
                    dobslall += obslall
                    dozhperall += ozhperall
                    dperall += perall
                    dnochall += nochall
                    dvremntall += vremntall
                    dozhrall += ozhrall
                    dvossprall += vossprall
                    dotszpall += otszpall
                    dotsdvall += otsdvall
                    ddorbulall += dorbulall
                    drekprall += rekprall
                    drekremzall += rekremzall
                    dozhspall += ozhspall
                gg = 2+samin
                vsegoall = str((vsegoall*10)//60)+"ч. "+str((vsegoall*10)%60)+"м."
                vsisprall = str((vsisprall*10)//60)+"ч. "+str((vsisprall*10)%60)+"м."
                vpolall = str((vpolall*10)//60)+"ч. "+str((vpolall*10)%60)+"м."
                obspall = str((obspall*10)//60)+"ч. "+str((obspall*10)%60)+"м."
                meteoall = str((meteoall*10)//60)+"ч. "+str((meteoall*10)%60)+"м."
                rezrvall = str((rezrvall*10)//60)+"ч. "+str((rezrvall*10)%60)+"м."
                isneisall = str((isneisall*10)//60)+"ч. "+str((isneisall*10)%60)+"м."
                vsneisprall = str((vsneisprall*10)//60)+"ч. "+str((vsneisprall*10)%60)+"м."
                ustrnall = str((ustrnall*10)//60)+"ч. "+str((ustrnall*10)%60)+"м."
                ozhoball = str((ozhoball*10)//60)+"ч. "+str((ozhoball*10)%60)+"м."
                obslall = str((obslall*10)//60)+"ч. "+str((obslall*10)%60)+"м."
                ozhperall = str((ozhperall*10)//60)+"ч. "+str((ozhperall*10)%60)+"м."
                perall = str((perall*10)//60)+"ч. "+str((perall*10)%60)+"м."
                nochall = str((nochall*10)//60)+"ч. "+str((nochall*10)%60)+"м."
                vremntall = str((vremntall*10)//60)+"ч. "+str((vremntall*10)%60)+"м."
                ozhrall = str((ozhrall*10)//60)+"ч. "+str((ozhrall*10)%60)+"м."
                vossprall = str((vossprall*10)//60)+"ч. "+str((vossprall*10)%60)+"м."
                otszpall = str((otszpall*10)//60)+"ч. "+str((otszpall*10)%60)+"м."
                otsdvall = str((otsdvall*10)//60)+"ч. "+str((otsdvall*10)%60)+"м."
                dorbulall = str((dorbulall*10)//60)+"ч. "+str((dorbulall*10)%60)+"м."
                rekprall = str((rekprall*10)//60)+"ч. "+str((rekprall*10)%60)+"м."
                rekremzall = str((rekremzall*10)//60)+"ч. "+str((rekremzall*10)%60)+"м."
                ozhspall = str((ozhspall*10)//60)+"ч. "+str((ozhspall*10)%60)+"м."
                self.tableWidget3.setItem(3, gg, QTableWidgetItem(vsegoall))
                self.tableWidget3.setItem(4, gg, QTableWidgetItem(vsisprall))
                self.tableWidget3.setItem(5, gg, QTableWidgetItem(vpolall))
                self.tableWidget3.setItem(6, gg, QTableWidgetItem(obspall))
                self.tableWidget3.setItem(7, gg, QTableWidgetItem(meteoall))
                self.tableWidget3.setItem(8, gg, QTableWidgetItem(rezrvall))
                self.tableWidget3.setItem(9, gg, QTableWidgetItem(isneisall))
                self.tableWidget3.setItem(10, gg, QTableWidgetItem(vsneisprall))
                self.tableWidget3.setItem(11, gg, QTableWidgetItem(ustrnall))
                self.tableWidget3.setItem(12, gg, QTableWidgetItem(obslall))
                self.tableWidget3.setItem(13, gg, QTableWidgetItem(ozhperall))
                self.tableWidget3.setItem(14, gg, QTableWidgetItem(perall))
                self.tableWidget3.setItem(15, gg, QTableWidgetItem(nochall))
                self.tableWidget3.setItem(16, gg, QTableWidgetItem(vremntall))
                self.tableWidget3.setItem(17, gg, QTableWidgetItem(ozhrall))
                self.tableWidget3.setItem(18, gg, QTableWidgetItem(otszpall))
                self.tableWidget3.setItem(19, gg, QTableWidgetItem(otsdvall))
                self.tableWidget3.setItem(20, gg, QTableWidgetItem(dorbulall))
                self.tableWidget3.setItem(21, gg, QTableWidgetItem(rekprall))
                self.tableWidget3.setItem(22, gg, QTableWidgetItem(rekremzall))
                self.tableWidget3.setItem(23, gg, QTableWidgetItem(ozhspall))
                if samin >= 4:
                    ddvsegoall = str((dvsegoall*10)//60)+"ч. "+str((dvsegoall*10)%60)+"м."
                    ddvsisprall = str((dvsisprall*10)//60)+"ч. "+str((dvsisprall*10)%60)+"м."
                    ddvpolall = str((dvpolall*10)//60)+"ч. "+str((dvpolall*10)%60)+"м."
                    ddobspall = str((dobspall*10)//60)+"ч. "+str((dobspall*10)%60)+"м."
                    ddmeteoall = str((dmeteoall*10)//60)+"ч. "+str((dmeteoall*10)%60)+"м."
                    ddrezrvall = str((drezrvall*10)//60)+"ч. "+str((drezrvall*10)%60)+"м."
                    ddisneisall = str((disneisall*10)//60)+"ч. "+str((disneisall*10)%60)+"м."
                    ddvsneisprall = str((dvsneisprall*10)//60)+"ч. "+str((dvsneisprall*10)%60)+"м."
                    ddustrnall = str((dustrnall*10)//60)+"ч. "+str((dustrnall*10)%60)+"м."
                    ddozhoball = str((dozhoball*10)//60)+"ч. "+str((dozhoball*10)%60)+"м."
                    ddobslall = str((dobslall*10)//60)+"ч. "+str((dobslall*10)%60)+"м."
                    ddozhperall = str((dozhperall*10)//60)+"ч. "+str((dozhperall*10)%60)+"м."
                    ddperall = str((dperall*10)//60)+"ч. "+str((dperall*10)%60)+"м."
                    ddnochall = str((dnochall*10)//60)+"ч. "+str((dnochall*10)%60)+"м."
                    ddvremntall = str((dvremntall*10)//60)+"ч. "+str((dvremntall*10)%60)+"м."
                    ddozhrall = str((dozhrall*10)//60)+"ч. "+str((dozhrall*10)%60)+"м."
                    ddvossprall = str((dvossprall*10)//60)+"ч. "+str((dvossprall*10)%60)+"м."
                    ddotszpall = str((dotszpall*10)//60)+"ч. "+str((dotszpall*10)%60)+"м."
                    ddotsdvall = str((dotsdvall*10)//60)+"ч. "+str((dotsdvall*10)%60)+"м."
                    dddorbulall = str((ddorbulall*10)//60)+"ч. "+str((ddorbulall*10)%60)+"м."
                    ddrekprall = str((drekprall*10)//60)+"ч. "+str((drekprall*10)%60)+"м."
                    ddrekremzall = str((drekremzall*10)//60)+"ч. "+str((drekremzall*10)%60)+"м."
                    ddozhspall = str((dozhspall*10)//60)+"ч. "+str((dozhspall*10)%60)+"м."
                    self.tableWidget3.setItem(3, 6, QTableWidgetItem(ddvsegoall))
                    self.tableWidget3.setItem(4, 6, QTableWidgetItem(ddvsisprall))
                    self.tableWidget3.setItem(5, 6, QTableWidgetItem(ddvpolall))
                    self.tableWidget3.setItem(6, 6, QTableWidgetItem(ddobspall))
                    self.tableWidget3.setItem(7, 6, QTableWidgetItem(ddmeteoall))
                    self.tableWidget3.setItem(8, 6, QTableWidgetItem(ddrezrvall))
                    self.tableWidget3.setItem(9, 6, QTableWidgetItem(ddisneisall))
                    self.tableWidget3.setItem(10, 6, QTableWidgetItem(ddvsneisprall))
                    self.tableWidget3.setItem(11, 6, QTableWidgetItem(ddustrnall))
                    self.tableWidget3.setItem(12, 6, QTableWidgetItem(ddobslall))
                    self.tableWidget3.setItem(13, 6, QTableWidgetItem(ddozhperall))
                    self.tableWidget3.setItem(14, 6, QTableWidgetItem(ddperall))
                    self.tableWidget3.setItem(15, 6, QTableWidgetItem(ddnochall))
                    self.tableWidget3.setItem(16, 6, QTableWidgetItem(ddvremntall))
                    self.tableWidget3.setItem(17, 6, QTableWidgetItem(ddozhrall))
                    self.tableWidget3.setItem(18, 6, QTableWidgetItem(ddotszpall))
                    self.tableWidget3.setItem(19, 6, QTableWidgetItem(ddotsdvall))
                    self.tableWidget3.setItem(20, 6, QTableWidgetItem(dddorbulall))
                    self.tableWidget3.setItem(21, 6, QTableWidgetItem(ddrekprall))
                    self.tableWidget3.setItem(22, 6, QTableWidgetItem(ddrekremzall))
                    self.tableWidget3.setItem(23, 6, QTableWidgetItem(ddozhspall))
        except ValueError:
            QMessageBox.about(self, "Ошибка", "Ошибка данных!")
            

class Window1(QWidget):
    def __init__(self):
        super(Window1, self).__init__()
        self.setWindowTitle('Табель учета исправности и использования самолетов')
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)
        #self.button = QPushButton(self)
        #self.button.setText('Ok')
        #self.button.show()
        self.tableWidget2 = QtWidgets.QTableWidget(self)
        self.tableWidget2.setGeometry(QtCore.QRect(10, 10, 501, 591))
        self.tableWidget2.setRowCount(27)
        self.tableWidget2.setColumnCount(34)
        self.tableWidget2.horizontalHeader().hide()
        self.tableWidget2.verticalHeader().hide()
        self.tableWidget2.setItem(0, 0, QTableWidgetItem("№"))
        self.tableWidget2.setItem(0, 1, QTableWidgetItem("Состояние эксплуатации"))
        self.tableWidget2.setItem(0, 2, QTableWidgetItem("Усл. обозн."))
        self.tableWidget2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        """
        for j in range(35):
            if j>=2:
                if mint == 60:
                    mint = 0
                    hour+=1
                    self.tableWidget.setItem(0, j, QTableWidgetItem("      "+str(hour)+":"+str(mint)+"0   "))
                    mint += 10
                else:
                    self.tableWidget.setItem(0, j, QTableWidgetItem("      "+str(hour)+":"+str(mint)+"   "))
                    mint += 10
            self.tableWidget.item(0, j).setBackground(QtGui.QColor(219,235,255))
        """
        self.tableWidget2.setItem(25, 0, QTableWidgetItem(" "))
        self.tableWidget2.setItem(26, 0, QTableWidgetItem(" "))
        self.tableWidget2.setItem(1, 1, QTableWidgetItem("Всего самолёто - часов"))
        self.tableWidget2.setItem(2, 1, QTableWidgetItem("Всего исправных самолёто - часов"))
        self.tableWidget2.setItem(3, 1, QTableWidgetItem("Время в рейсе"))
        self.tableWidget2.setItem(4, 1, QTableWidgetItem("Обеспечение рейса"))
        self.tableWidget2.setItem(5, 1, QTableWidgetItem("Простой по метео - условиям и запретам"))
        self.tableWidget2.setItem(6, 1, QTableWidgetItem("В резерве"))
        self.tableWidget2.setItem(7, 1, QTableWidgetItem("Исправные - неиспользованные"))
        self.tableWidget2.setItem(8, 1, QTableWidgetItem("Всего неисправных самолёто - часов"))
        self.tableWidget2.setItem(9, 1, QTableWidgetItem("Устранение неисправностей при Ф-А"))
        self.tableWidget2.setItem(10, 1, QTableWidgetItem("Ожидание обслуживания по Ф-Б"))
        self.tableWidget2.setItem(11, 1, QTableWidgetItem("Обслуживание по Ф-Б"))
        self.tableWidget2.setItem(12, 1, QTableWidgetItem("Ожидание периодического Т.О."))
        self.tableWidget2.setItem(13, 1, QTableWidgetItem("Периодическое Т.О."))
        self.tableWidget2.setItem(14, 1, QTableWidgetItem("Ночные и межсменные простои Т.О."))
        self.tableWidget2.setItem(15, 1, QTableWidgetItem("Ожидание ремонта"))
        self.tableWidget2.setItem(16, 1, QTableWidgetItem("В ремонте"))
        self.tableWidget2.setItem(17, 1, QTableWidgetItem("Отсутствие запасных частей"))
        self.tableWidget2.setItem(18, 1, QTableWidgetItem("Отсутствие двигателей"))
        self.tableWidget2.setItem(19, 1, QTableWidgetItem("Доработки по бюллетеням"))
        self.tableWidget2.setItem(20, 1, QTableWidgetItem("Рекламация промышленности"))
        self.tableWidget2.setItem(21, 1, QTableWidgetItem("Рекламация ремонтным заводом"))
        self.tableWidget2.setItem(22, 1, QTableWidgetItem("Расследование проишествий"))
        self.tableWidget2.setItem(23, 1, QTableWidgetItem("Восстановление после проишествий"))
        self.tableWidget2.setItem(24, 1, QTableWidgetItem("Ожидание списания"))
        self.tableWidget2.setItem(25, 1, QTableWidgetItem("Процент исправности"))
        self.tableWidget2.setItem(26, 1, QTableWidgetItem("Процент использования"))
        
        self.tableWidget2.setItem(1, 2, QTableWidgetItem("Ф"))
        self.tableWidget2.setItem(2, 2, QTableWidgetItem("И"))
        self.tableWidget2.setItem(3, 2, QTableWidgetItem("К"))
        self.tableWidget2.setItem(4, 2, QTableWidgetItem("Е"))
        self.tableWidget2.setItem(5, 2, QTableWidgetItem("М"))
        self.tableWidget2.setItem(6, 2, QTableWidgetItem("Г"))
        self.tableWidget2.setItem(7, 2, QTableWidgetItem("А"))
        self.tableWidget2.setItem(8, 2, QTableWidgetItem("Н"))
        self.tableWidget2.setItem(9, 2, QTableWidgetItem("У"))
        self.tableWidget2.setItem(10, 2, QTableWidgetItem("Об"))
        self.tableWidget2.setItem(11, 2, QTableWidgetItem("Тб"))
        self.tableWidget2.setItem(12, 2, QTableWidgetItem("Оп"))
        self.tableWidget2.setItem(13, 2, QTableWidgetItem("Тп"))
        self.tableWidget2.setItem(14, 2, QTableWidgetItem("Ш"))
        self.tableWidget2.setItem(15, 2, QTableWidgetItem("Ор"))
        self.tableWidget2.setItem(16, 2, QTableWidgetItem("Р"))
        self.tableWidget2.setItem(17, 2, QTableWidgetItem("З"))
        self.tableWidget2.setItem(18, 2, QTableWidgetItem("Дв"))
        self.tableWidget2.setItem(19, 2, QTableWidgetItem("Д"))
        self.tableWidget2.setItem(20, 2, QTableWidgetItem("Ж"))
        self.tableWidget2.setItem(21, 2, QTableWidgetItem("Жр"))
        self.tableWidget2.setItem(22, 2, QTableWidgetItem("Л"))
        self.tableWidget2.setItem(23, 2, QTableWidgetItem("В"))
        self.tableWidget2.setItem(24, 2, QTableWidgetItem("С"))
        self.tableWidget2.setItem(25, 2, QTableWidgetItem("Киспр"))
        self.tableWidget2.setItem(26, 2, QTableWidgetItem("Кисп"))
        #self.tableWidget2.setItem(0, 34, QTableWidgetItem("Итого за месяц"))
        self.tableWidget2.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        nn = 1
        for j in range(34):
            if j >= 1 and j<25:
                self.tableWidget2.setItem(j, 0, QTableWidgetItem(str(j)))
            if j<27:
                self.tableWidget2.item(j, 0).setBackground(QtGui.QColor(219,235,255))
                self.tableWidget2.item(j, 1).setBackground(QtGui.QColor(219,235,255))
                self.tableWidget2.item(j, 2).setBackground(QtGui.QColor(219,235,255))
            if j >=3 and j<34:
                self.tableWidget2.setItem(0, j, QTableWidgetItem(str(nn)))
                nn+=1
            self.tableWidget2.item(0, j).setBackground(QtGui.QColor(219,235,255))
        self.tableWidget2.resizeColumnsToContents()
        ##############################
        self.groupBox2 = QtWidgets.QGroupBox(self)
        self.groupBox2.setGeometry(QtCore.QRect(520, 1, 271, 221))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.groupBox2.setFont(font)
        self.groupBox2.setMouseTracking(False)
        self.groupBox2.setAcceptDrops(False)
        self.groupBox2.setAutoFillBackground(False)
        self.groupBox2.setFlat(False)
        self.groupBox2.setCheckable(False)
        self.groupBox2.setTitle("Настройки")
        self.combo = QComboBox(self.groupBox2)
        self.combo.addItem("SSJ-100")
        self.combo.addItem("Airbus A310")
        self.combo.addItem("ИЛ-96М")
        self.combo.addItem("Airbus A320")
        self.combo.addItem("Boeing-737")
        self.qlabel = QLabel(self.groupBox2)
        self.qlabel.move(10,37)
        self.qlabel.setText('Самолет:')
        self.qlabel2 = QLabel(self.groupBox2)
        self.qlabel2.move(10,77)
        self.qlabel2.setText('Месяц:')
        self.combo2 = QComboBox(self.groupBox2)
        self.combo2.addItem("Январь")
        self.combo2.addItem("Февраль")
        self.combo2.addItem("Март")
        self.combo2.addItem("Апрель")
        self.combo2.addItem("Май")
        self.combo2.addItem("Июнь")
        self.combo2.addItem("Июль")
        self.combo2.addItem("Август")
        self.combo2.addItem("Сентябрь")
        self.combo2.addItem("Октябрь")
        self.combo2.addItem("Ноябрь")
        self.combo2.addItem("Декабрь")
        self.combo.move(110, 35)
        self.combo2.move(80, 77)
        self.qlabel3 = QLabel(self.groupBox2)
        self.qlabel3.move(10,125)
        self.qlabel3.setText('Год:')
        self.line = QLineEdit(self.groupBox2)
        self.line.move(65, 127)
        self.pushButton = QtWidgets.QPushButton(self.groupBox2)
        self.pushButton.setGeometry(QtCore.QRect(10, 180, 231, 31))
        self.pushButton.clicked.connect(self.tab)
        self.pushButton.setText('ПРОСМОТР')
    def tab(self):
        year=self.line.text()
        mmm = str(self.combo2.currentIndex()+1)
        samin = self.combo.currentIndex()+1
        chty = (self.combo2.currentIndex()+1)%2
        if chty == 0:
            msx = 31
        else:
            msx = 30
        if mmm == 2:
            msx = 28
        try:
            for i in range(msx):
                xhasi = 0
                i = i+1
                ii = i
                if i<10:
                    dddd = "0"+str(i)
                with open("base/"+dddd+"-0"+mmm+"-"+year, 'r') as f:
                #with open("base/22-09-2021", 'r') as f:
                    text = f.read().split("\n")
                    #.replace("\n", " ")
                vsego = 0
                sp = text[samin].split(' ')
                ###########
                for i in sp:
                    if i!='0' and i!='':
                        vsego+=1
                vsego = str((vsego*10)//60)+"ч. "+str((vsego*10)%60)+"м."
                #######
                vsispr = 0
                for i in sp:
                    if i=='1' or i=='2'or i=='3'or i=='4'or i=='5':
                        vsispr+=1
                vsispr = str((vsispr*10)//60)+"ч. "+str((vsispr*10)%60)+"м."
                #######
                vpol = 0
                for i in sp:
                    if i=='1':
                        vpol+=1
                fgpol = vpol
                vpol = str((vpol*10)//60)+"ч. "+str((vpol*10)%60)+"м."
                #######
                obsp = 0
                for i in sp:
                    if i=='2':
                        obsp+=1
                xhasi =+ obsp
                obsp = str((obsp*10)//60)+"ч. "+str((obsp*10)%60)+"м."
                #######
                meteo = 0
                for i in sp:
                    if i=='3':
                        meteo+=1
                xhasi =+ meteo
                meteo = str((meteo*10)//60)+"ч. "+str((meteo*10)%60)+"м."
                #######
                rezrv = 0
                for i in sp:
                    if i=='4':
                        rezrv+=1
                xhasi =+ rezrv
                rezrv = str((rezrv*10)//60)+"ч. "+str((rezrv*10)%60)+"м."
                #######
                isneis = 0
                for i in sp:
                    if i=='5':
                        isneis+=1
                xhasi =+ isneis
                isneis = str((isneis*10)//60)+"ч. "+str((isneis*10)%60)+"м."
                #######
                vsneispr = 0
                for i in sp:
                    if i!='1' and i!='2'and  i!='3'and  i!='4'and  i!='5'and  i!='0'and i!='':
                        vsneispr+=1
                vsneispr = str((vsneispr*10)//60)+"ч. "+str((vsneispr*10)%60)+"м."
                #######
                ustrn = 0
                for i in sp:
                    if i=='6':
                        ustrn+=1
                ustrn = str((ustrn*10)//60)+"ч. "+str((ustrn*10)%60)+"м."
                #######
                ozhob = 0
                for i in sp:
                    if i=='7':
                        ozhob+=1
                ozhob= str((ozhob*10)//60)+"ч. "+str((ozhob*10)%60)+"м."
                #######
                obsl = 0
                for i in sp:
                    if i=='8':
                        obsl+=1
                obsl = str((obsl*10)//60)+"ч. "+str((obsl*10)%60)+"м."
                #######
                ozhper = 0
                for i in sp:
                    if i=='9':
                        ozhper+=1
                kozh = ozhper
                ozhper = str((ozhper*10)//60)+"ч. "+str((ozhper*10)%60)+"м."
                #######
                per = 0
                for i in sp:
                    if i=='10':
                        per+=1
                per = str((per*10)//60)+"ч. "+str((per*10)%60)+"м."
                #######
                noch = 0
                for i in sp:
                    if i=='11':
                        noch+=1
                noch = str((noch*10)//60)+"ч. "+str((noch*10)%60)+"м."
                #######
                ozhr = 0
                for i in sp:
                    if i=='12':
                        ozhr+=1
                ozhr = str((ozhr*10)//60)+"ч. "+str((ozhr*10)%60)+"м."
                #######
                vremnt = 0
                for i in sp:
                    if i=='13':
                        vremnt+=1
                vremnt = str((vremnt*10)//60)+"ч. "+str((vremnt*10)%60)+"м."
                #######
                otszp = 0
                for i in sp:
                    if i=='14':
                        otszp+=1
                otszp = str((otszp*10)//60)+"ч. "+str((otszp*10)%60)+"м."
                #######
                otsdv = 0
                for i in sp:
                    if i=='15':
                        otsdv+=1
                otsdv = str((otsdv*10)//60)+"ч. "+str((otsdv*10)%60)+"м."
                #######
                dorbul = 0
                for i in sp:
                    if i=='16':
                        dorbul+=1
                dorbul = str((dorbul*10)//60)+"ч. "+str((dorbul*10)%60)+"м."
                #######
                rekpr = 0
                for i in sp:
                    if i=='17':
                        rekpr+=1
                rekpr = str((rekpr*10)//60)+"ч. "+str((rekpr*10)%60)+"м."
                #######
                rekremz = 0
                for i in sp:
                    if i=='18':
                        rekremz+=1
                rekremz = str((rekremz*10)//60)+"ч. "+str((rekremz*10)%60)+"м."
                #######
                rasspr = 0
                for i in sp:
                    if i=='19':
                        rasspr+=1
                rasspr = str((rasspr*10)//60)+"ч. "+str((rasspr*10)%60)+"м."
                #######
                vosspr = 0
                for i in sp:
                    if i=='20':
                        vosspr+=1
                vosspr = str((vosspr*10)//60)+"ч. "+str((vosspr*10)%60)+"м."
                #######
                ozhsp = 0
                for i in sp:
                    if i=='21':
                        ozhsp+=1
                ozhsp = str((ozhsp*10)//60)+"ч. "+str((ozhsp*10)%60)+"м."
                xhasi = xhasi*10
                fgpol = fgpol*10
                kpi = xhasi/fgpol
                kispr = (720-(kozh*10))/720 ###надо формулу чел!!!!!!!
                kisp = (720*kispr-fgpol*kpi)/720
                self.tableWidget2.setItem(1, 2+ii, QTableWidgetItem(vsego))
                self.tableWidget2.setItem(2, 2+ii, QTableWidgetItem(vsispr))
                self.tableWidget2.setItem(3, 2+ii, QTableWidgetItem(vpol))
                self.tableWidget2.setItem(4, 2+ii, QTableWidgetItem(obsp))
                self.tableWidget2.setItem(5, 2+ii, QTableWidgetItem(meteo))
                self.tableWidget2.setItem(6, 2+ii, QTableWidgetItem(rezrv))
                self.tableWidget2.setItem(7, 2+ii, QTableWidgetItem(isneis))
                self.tableWidget2.setItem(8, 2+ii, QTableWidgetItem(vsneispr))
                self.tableWidget2.setItem(9, 2+ii, QTableWidgetItem(ustrn))
                self.tableWidget2.setItem(10, 2+ii, QTableWidgetItem(ozhob))
                self.tableWidget2.setItem(11, 2+ii, QTableWidgetItem(obsl))
                self.tableWidget2.setItem(12, 2+ii, QTableWidgetItem(ozhper))
                self.tableWidget2.setItem(13, 2+ii, QTableWidgetItem(per))
                self.tableWidget2.setItem(14, 2+ii, QTableWidgetItem(noch))
                self.tableWidget2.setItem(15, 2+ii, QTableWidgetItem(ozhr))
                self.tableWidget2.setItem(16, 2+ii, QTableWidgetItem(vremnt))
                self.tableWidget2.setItem(17, 2+ii, QTableWidgetItem(otszp))
                self.tableWidget2.setItem(18, 2+ii, QTableWidgetItem(otsdv))
                self.tableWidget2.setItem(19, 2+ii, QTableWidgetItem(dorbul))
                self.tableWidget2.setItem(20, 2+ii, QTableWidgetItem(rekpr))
                self.tableWidget2.setItem(21, 2+ii, QTableWidgetItem(rekremz))
                self.tableWidget2.setItem(22, 2+ii, QTableWidgetItem(rasspr))
                self.tableWidget2.setItem(23, 2+ii, QTableWidgetItem(vosspr))
                self.tableWidget2.setItem(24, 2+ii, QTableWidgetItem(ozhsp))
                self.tableWidget2.setItem(25, 2+ii, QTableWidgetItem(str(round(kispr,2))[2:]+'%'))#[-1:]
                self.tableWidget2.setItem(26, 2+ii, QTableWidgetItem(str(round(kisp,2))[2:]+'%'))
                self.tableWidget2.resizeColumnsToContents()
        except:
            QMessageBox.about(self, "Ошибка", "Ошибка данных!")
            
                    
        

class Ui_MainWindow(object):
    def show_window_1(self):
        self.w1 = Window1()
        self.w1.show()

    def show_window_2(self):
        self.w2 = Window2()
        self.w2.show()
###ФУНКЦИИ КОНТЕКСТНОГО МЕНЮ
    def daction1(self):
        for index in self.tableWidget.selectedIndexes():
            pic = QtGui.QPixmap("data/1.bmp")
            self.label = QtWidgets.QLabel(MainWindow)
            self.label.setPixmap(pic)
            self.tableWidget.setCellWidget(index.row(),index.column(), self.label)
            self.tableWidget.setItem(index.row(),index.column(), QTableWidgetItem("1"))
    def daction2(self):
        for index in self.tableWidget.selectedIndexes():
            pic = QtGui.QPixmap("data/2.bmp")
            self.label = QtWidgets.QLabel(MainWindow)
            self.label.setPixmap(pic)
            self.tableWidget.setCellWidget(index.row(),index.column(), self.label)
            self.tableWidget.setItem(index.row(),index.column(), QTableWidgetItem("2"))
    def daction3(self):
        for index in self.tableWidget.selectedIndexes():
            pic = QtGui.QPixmap("data/3.bmp")
            self.label = QtWidgets.QLabel(MainWindow)
            self.label.setPixmap(pic)
            self.tableWidget.setCellWidget(index.row(),index.column(), self.label)
            self.tableWidget.setItem(index.row(),index.column(), QTableWidgetItem("3"))
    def daction4(self):
        for index in self.tableWidget.selectedIndexes():
            pic = QtGui.QPixmap("data/4.bmp")
            self.label = QtWidgets.QLabel(MainWindow)
            self.label.setPixmap(pic)
            self.tableWidget.setCellWidget(index.row(),index.column(), self.label)
            self.tableWidget.setItem(index.row(),index.column(), QTableWidgetItem("4"))
    def daction5(self):
        for index in self.tableWidget.selectedIndexes():
            pic = QtGui.QPixmap("data/5.bmp")
            self.label = QtWidgets.QLabel(MainWindow)
            self.label.setPixmap(pic)
            self.tableWidget.setCellWidget(index.row(),index.column(), self.label)
            self.tableWidget.setItem(index.row(),index.column(), QTableWidgetItem("5"))
    def daction6(self):
        for index in self.tableWidget.selectedIndexes():
            pic = QtGui.QPixmap("data/6.bmp")
            self.label = QtWidgets.QLabel(MainWindow)
            self.label.setPixmap(pic)
            self.tableWidget.setCellWidget(index.row(),index.column(), self.label)
            self.tableWidget.setItem(index.row(),index.column(), QTableWidgetItem("6"))
    def daction7(self):
        for index in self.tableWidget.selectedIndexes():
            pic = QtGui.QPixmap("data/7.bmp")
            self.label = QtWidgets.QLabel(MainWindow)
            self.label.setPixmap(pic)
            self.tableWidget.setCellWidget(index.row(),index.column(), self.label)
            self.tableWidget.setItem(index.row(),index.column(), QTableWidgetItem("7"))
    def daction8(self):
        for index in self.tableWidget.selectedIndexes():
            pic = QtGui.QPixmap("data/8.bmp")
            self.label = QtWidgets.QLabel(MainWindow)
            self.label.setPixmap(pic)
            self.tableWidget.setCellWidget(index.row(),index.column(), self.label)
            self.tableWidget.setItem(index.row(),index.column(), QTableWidgetItem("8"))
    def daction9(self):
        for index in self.tableWidget.selectedIndexes():
            pic = QtGui.QPixmap("data/9.bmp")
            self.label = QtWidgets.QLabel(MainWindow)
            self.label.setPixmap(pic)
            self.tableWidget.setCellWidget(index.row(),index.column(), self.label)
            self.tableWidget.setItem(index.row(),index.column(), QTableWidgetItem("9"))
    def daction10(self):
        for index in self.tableWidget.selectedIndexes():
            pic = QtGui.QPixmap("data/10.bmp")
            self.label = QtWidgets.QLabel(MainWindow)
            self.label.setPixmap(pic)
            self.tableWidget.setCellWidget(index.row(),index.column(), self.label)
            self.tableWidget.setItem(index.row(),index.column(), QTableWidgetItem("10"))
    def daction11(self):
        for index in self.tableWidget.selectedIndexes():
            pic = QtGui.QPixmap("data/11.bmp")
            self.label = QtWidgets.QLabel(MainWindow)
            self.label.setPixmap(pic)
            self.tableWidget.setCellWidget(index.row(),index.column(), self.label)
            self.tableWidget.setItem(index.row(),index.column(), QTableWidgetItem("11"))
    def daction12(self):
        for index in self.tableWidget.selectedIndexes():
            pic = QtGui.QPixmap("data/12.bmp")
            self.label = QtWidgets.QLabel(MainWindow)
            self.label.setPixmap(pic)
            self.tableWidget.setCellWidget(index.row(),index.column(), self.label)
            self.tableWidget.setItem(index.row(),index.column(), QTableWidgetItem("12"))
    def daction13(self):
        for index in self.tableWidget.selectedIndexes():
            pic = QtGui.QPixmap("data/13.bmp")
            self.label = QtWidgets.QLabel(MainWindow)
            self.label.setPixmap(pic)
            self.tableWidget.setCellWidget(index.row(),index.column(), self.label)
            self.tableWidget.setItem(index.row(),index.column(), QTableWidgetItem("13"))
    def daction14(self):
        for index in self.tableWidget.selectedIndexes():
            pic = QtGui.QPixmap("data/14.bmp")
            self.label = QtWidgets.QLabel(MainWindow)
            self.label.setPixmap(pic)
            self.tableWidget.setCellWidget(index.row(),index.column(), self.label)
            self.tableWidget.setItem(index.row(),index.column(), QTableWidgetItem("14"))
    def daction15(self):
        for index in self.tableWidget.selectedIndexes():
            pic = QtGui.QPixmap("data/15.bmp")
            self.label = QtWidgets.QLabel(MainWindow)
            self.label.setPixmap(pic)
            self.tableWidget.setCellWidget(index.row(),index.column(), self.label)
            self.tableWidget.setItem(index.row(),index.column(), QTableWidgetItem("15"))
    def daction16(self):
        for index in self.tableWidget.selectedIndexes():
            pic = QtGui.QPixmap("data/16.bmp")
            self.label = QtWidgets.QLabel(MainWindow)
            self.label.setPixmap(pic)
            self.tableWidget.setCellWidget(index.row(),index.column(), self.label)
            self.tableWidget.setItem(index.row(),index.column(), QTableWidgetItem("16"))
    def daction17(self):
        for index in self.tableWidget.selectedIndexes():
            pic = QtGui.QPixmap("data/17.bmp")
            self.label = QtWidgets.QLabel(MainWindow)
            self.label.setPixmap(pic)
            self.tableWidget.setCellWidget(index.row(),index.column(), self.label)
            self.tableWidget.setItem(index.row(),index.column(), QTableWidgetItem("17"))
    def daction18(self):
        for index in self.tableWidget.selectedIndexes():
            pic = QtGui.QPixmap("data/18.bmp")
            self.label = QtWidgets.QLabel(MainWindow)
            self.label.setPixmap(pic)
            self.tableWidget.setCellWidget(index.row(),index.column(), self.label)
            self.tableWidget.setItem(index.row(),index.column(), QTableWidgetItem("18"))
    def daction19(self):
        for index in self.tableWidget.selectedIndexes():
            pic = QtGui.QPixmap("data/19.bmp")
            self.label = QtWidgets.QLabel(MainWindow)
            self.label.setPixmap(pic)
            self.tableWidget.setCellWidget(index.row(),index.column(), self.label)
            self.tableWidget.setItem(index.row(),index.column(), QTableWidgetItem("19"))
    def daction20(self):
        for index in self.tableWidget.selectedIndexes():
            pic = QtGui.QPixmap("data/20.bmp")
            self.label = QtWidgets.QLabel(MainWindow)
            self.label.setPixmap(pic)
            self.tableWidget.setCellWidget(index.row(),index.column(), self.label)
            self.tableWidget.setItem(index.row(),index.column(), QTableWidgetItem("20"))
    def daction21(self):
        for index in self.tableWidget.selectedIndexes():
            pic = QtGui.QPixmap("data/21.bmp")
            self.label = QtWidgets.QLabel(MainWindow)
            self.label.setPixmap(pic)
            self.tableWidget.setCellWidget(index.row(),index.column(), self.label)
            self.tableWidget.setItem(index.row(),index.column(), QTableWidgetItem("21"))

    def savegr(self):
        name = self.calendarWidget.selectedDate().toString("dd-MM-yyyy")
        with open("base/"+name, 'w', encoding='UTF-8') as out_file:
            for row in range(self.tableWidget.rowCount()):
                for column in range(self.tableWidget.columnCount()):
                    if row == 0 or column == 0 or column ==1:
                        p = 0
                    else:
                        item = self.tableWidget.item(row, column)
                        print(item.text() if item else "0", end=' ', file=out_file)
                        #print(' ', file=out_file)
                print('', file=out_file)

    def gruz(self):
        name = self.calendarWidget.selectedDate().toString("dd-MM-yyyy")
        num = 0
        with open("base/"+name, 'r') as f:
            text = f.read().replace("\n", " ").split()
            #print(text)
        for row in range(self.tableWidget.rowCount()):
                for column in range(self.tableWidget.columnCount()):
                    if row == 0 or column == 0 or column ==1:
                        p = 0
                    else:
                        pic = QtGui.QPixmap("data/"+text[num]+".bmp")
                        self.label = QtWidgets.QLabel(MainWindow)
                        self.label.setPixmap(pic)
                        self.tableWidget.setCellWidget(row,column, self.label)
                        self.tableWidget.setItem(row,column, QTableWidgetItem(text[num]))
                        num+=1
    def och(self):
        for row in range(self.tableWidget.rowCount()):
                for column in range(self.tableWidget.columnCount()):
                    if row == 0 or column == 0 or column ==1:
                        p = 0
                    else:
                        pic = QtGui.QPixmap("data/0.bmp")
                        self.label = QtWidgets.QLabel(MainWindow)
                        self.label.setPixmap(pic)
                        self.tableWidget.setCellWidget(row,column, self.label)
                        self.tableWidget.setItem(row,column, QTableWidgetItem("0"))
 
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 519)
        font = QtGui.QFont()
        font.setUnderline(False)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ИОТЭАТ МОЛОКО и СЕРКАН/sam.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 520, 519))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("data/fno.jpg"))
        self.label_4.setScaledContents(True)
        #мега супер пупер таблица
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 501, 191))
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(146)
        self.tableWidget.horizontalHeader().hide()
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("ТИП САМОЛЕТА"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("БОРТОВОЙ №"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("SSJ-100"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("43214"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Airbus A310"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("43206"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("ИЛ-96М"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("22814"))
        self.tableWidget.setItem(4, 0, QTableWidgetItem("Airbus A320"))
        self.tableWidget.setItem(4, 1, QTableWidgetItem("14888"))
        self.tableWidget.setItem(5, 0, QTableWidgetItem("Airbus A320"))
        self.tableWidget.setItem(5, 1, QTableWidgetItem("43612"))
        self.tableWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.action1 = QAction("В рейсе(К)", MainWindow)
        self.action2 = QAction("Обеспечение рейса(Е)", MainWindow)
        self.action3 = QAction("Задержки по метео условиям и запретам(М)", MainWindow)
        self.action4 = QAction("В резерве(Г)", MainWindow)
        self.action5 = QAction("Исправный - неиспользуемый(А)", MainWindow)
        self.action6 = QAction("Устранение неиспр. при оперативном ТО(У)", MainWindow)
        self.action7 = QAction("Ожидание ТО по Ф-Б(Об)", MainWindow)
        self.action8 = QAction("ТО по Ф-Б(Тб)", MainWindow)
        self.action9 = QAction("Ожидание переодического ТО(Оп)", MainWindow)
        self.action10 = QAction("ТО по переодическим формам(Тп)", MainWindow)
        self.action11 = QAction("Межсменные или ночные перерывы(Ш)", MainWindow)
        self.action12 = QAction("Ожидание ремонта(Ор)", MainWindow)
        self.action13 = QAction("В ремонте(Р)", MainWindow)
        self.action14 = QAction("Отсутствие запчастей(З)", MainWindow)
        self.action15 = QAction("Отсутствие двигателей(Дв)", MainWindow)
        self.action16 = QAction("Доработки по бюллютеням(Д)", MainWindow)
        self.action17 = QAction("Рекламация промышленности(Ж)", MainWindow)
        self.action18 = QAction("Рекламация ремзаводом(Жр)", MainWindow)
        self.action19 = QAction("Расследование летных происшествий(Л)", MainWindow)
        self.action20 = QAction("Восстановление самолета(В)", MainWindow)
        self.action21 = QAction("Ожидание списания(С)", MainWindow)
        self.tableWidget.addAction(self.action1)
        self.tableWidget.addAction(self.action2)
        self.tableWidget.addAction(self.action3)
        self.tableWidget.addAction(self.action4)
        self.tableWidget.addAction(self.action5)
        self.tableWidget.addAction(self.action6)
        self.tableWidget.addAction(self.action7)
        self.tableWidget.addAction(self.action8)
        self.tableWidget.addAction(self.action9)
        self.tableWidget.addAction(self.action10)
        self.tableWidget.addAction(self.action11)
        self.tableWidget.addAction(self.action12)
        self.tableWidget.addAction(self.action13)
        self.tableWidget.addAction(self.action14)
        self.tableWidget.addAction(self.action15)
        self.tableWidget.addAction(self.action16)
        self.tableWidget.addAction(self.action17)
        self.tableWidget.addAction(self.action18)
        self.tableWidget.addAction(self.action19)
        self.tableWidget.addAction(self.action20)
        self.tableWidget.addAction(self.action21)
        self.action1.triggered.connect(self.daction1)
        self.action2.triggered.connect(self.daction2)
        self.action3.triggered.connect(self.daction3)
        self.action4.triggered.connect(self.daction4)
        self.action5.triggered.connect(self.daction5)
        self.action6.triggered.connect(self.daction6)
        self.action7.triggered.connect(self.daction7)
        self.action8.triggered.connect(self.daction8)
        self.action9.triggered.connect(self.daction9)
        self.action10.triggered.connect(self.daction10)
        self.action11.triggered.connect(self.daction11)
        self.action12.triggered.connect(self.daction12)
        self.action13.triggered.connect(self.daction13)
        self.action14.triggered.connect(self.daction14)
        self.action15.triggered.connect(self.daction15)
        self.action16.triggered.connect(self.daction16)
        self.action17.triggered.connect(self.daction17)
        self.action18.triggered.connect(self.daction18)
        self.action19.triggered.connect(self.daction19)
        self.action20.triggered.connect(self.daction20)
        self.action21.triggered.connect(self.daction21)
        hour = 0
        mint = 10
        for j in range(146):
            if j>=2:
                if mint == 60:
                    mint = 0
                    hour+=1
                    self.tableWidget.setItem(0, j, QTableWidgetItem("      "+str(hour)+":"+str(mint)+"0   "))
                    mint += 10
                else:
                    self.tableWidget.setItem(0, j, QTableWidgetItem("      "+str(hour)+":"+str(mint)+"   "))
                    mint += 10
            self.tableWidget.item(0, j).setBackground(QtGui.QColor(219,235,255))
        for j in range(6):
            self.tableWidget.item(j, 0).setBackground(QtGui.QColor(219,235,255))
            self.tableWidget.item(j, 1).setBackground(QtGui.QColor(219,235,255))
        self.tableWidget.resizeColumnsToContents()
        #############
            
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 210, 251, 141))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setMouseTracking(False)
        self.groupBox.setAcceptDrops(False)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 30, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setUnderline(False)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 65, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setUnderline(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 100, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setUnderline(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(23, 32, 28, 28))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("data/babl.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(24, 64, 28, 28))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("data/kovid.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(24, 102, 28, 28))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("data/jopa.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 350, 191, 141))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setMouseTracking(False)
        self.groupBox_2.setAcceptDrops(False)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 30, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setUnderline(False)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_4.setAutoRepeat(False)
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setDefault(True)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 65, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setUnderline(False)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setDefault(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 100, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setUnderline(False)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setDefault(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(27, 33, 25, 25))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("data/1f4d5.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(28, 68, 27, 25))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("data/kybok.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(30, 104, 24, 24))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("data/274c.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(270, 210, 241, 141))
        self.calendarWidget.setObjectName("calendarWidget")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(210, 360, 301, 131))
        '''
        self.label_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Plain)
        '''
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("data/plane-2.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setWordWrap(False)
        self.label_7.setOpenExternalLinks(False)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setWindowIcon(QtGui.QIcon('data/sam.png'))


        self.pushButton_6.clicked.connect(sys.exit)
        self.pushButton.clicked.connect(self.savegr)
        self.pushButton_2.clicked.connect(self.gruz)
        self.pushButton_3.clicked.connect(self.och)

    
    def openDialog(self):
#       pass
        dialog = ClssDialog(self)
        dialog.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DM"))
        self.groupBox.setTitle(_translate("MainWindow", "Действия"))
        self.pushButton.setText(_translate("MainWindow", "     Сохранение графика"))
        self.pushButton_2.setText(_translate("MainWindow", "   Загрузка графика"))
        self.pushButton_3.setText(_translate("MainWindow", "   Очистка графика"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Переход"))
        self.pushButton_4.setText(_translate("MainWindow", "Табель"))
        self.pushButton_5.setText(_translate("MainWindow", "Отчёт"))
        self.pushButton_6.setText(_translate("MainWindow", "Выход"))
        self.pushButton_4.clicked.connect(self.show_window_1)
        self.pushButton_5.clicked.connect(self.show_window_2)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

