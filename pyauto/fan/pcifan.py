
import sys
import time
import re
import os
import datetime
from multiprocessing.context import Process
from threading import Thread



try:
    from PyQt5 import QtWidgets, QtCore
    from Ui_pcifan import *
    import pandas as pd
    import numpy as np
    import html_analysis as html_analysis
except ImportError as e:
    print('Lib missing:', e)
    exit()

path=r'./assets/'




class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.action_X.triggered.connect(QtCore.QCoreApplication.quit)
        self.actionFullScreen.triggered.connect(self.full_screen)

        self.action_A.triggered.connect(self.about)
        self.action_H.triggered.connect(self.get_help)

        self.actionLayoutWH.triggered.connect(self.printHW)

        self.columns=[]
        self.old_table={}
        self.tab_import('book')
        self.tab_import('reader')

        self.tableWidget_book.setColumnWidth(0,100)
        self.tableWidget_book.setColumnWidth(1,40)
        self.tableWidget_book.setColumnWidth(2,800)
        self.tableWidget_book.setColumnWidth(3,80)
        for i in range(4,7):
            self.tableWidget_book.setColumnWidth(i,40)

        self.bookButton_1.clicked.connect(lambda: self.tab_import('book'))
        self.bookButton_2.clicked.connect(lambda: self.tab_add(self.tableWidget_book))
        self.bookButton_3.clicked.connect(lambda: self.tab_del(self.tableWidget_book))
        self.bookButton_4.clicked.connect(lambda: self.tab_export(self.tableWidget_book,'books.csv'))
        self.readerButton_1.clicked.connect(lambda: self.tab_import('reader'))
        self.readerButton_2.clicked.connect(lambda: self.tab_add(self.tableWidget_reader))
        self.readerButton_3.clicked.connect(lambda: self.tab_del(self.tableWidget_reader))
        self.readerButton_4.clicked.connect(lambda: self.tab_export(self.tableWidget_reader,'readers.csv'))

        self.searching=False
        self.lineEdit_book_1.textChanged.connect(lambda: self.tab_search(self.tableWidget_book,'book'))
        self.lineEdit_reader_1.textChanged.connect(lambda: self.tab_search(self.tableWidget_reader,'reader'))

        self.lineEdit_reader_2.editingFinished.connect(self.borrow_book)
        self.lineEdit_reader_3.editingFinished.connect(self.return_book)

        self.magnetButton_1.clicked.connect(lambda:self.export_selected_magnet(self.tableWidget_book))

        self.bookButton_4.setEnabled(False)

        self.actionDebug_D.triggered.connect(lambda: self.set_table_titles(self.tableWidget_book,[]))


    def full_screen(self):
        if not self.isFullScreen():
            self.showFullScreen()
        else:
            self.showNormal()

    def printHW(self):
        print(f"Width * Height = {self.width()} * {self.height()}")

    def get_help(self):
        pass

    def about(self):
        QtWidgets.QMessageBox.information(self,'PCI fan','PCI fan\n\u00a9 PCI-Hyperbola 2021')

    def set_table(self,tab:QtWidgets.QTableWidget,df:pd.DataFrame):
        l1=len(df.index)
        tab.setRowCount(l1)
        for i in range(0, l1):
            li=list(df.iloc[i])
            for j in range(0, len(li)):
                tab.setItem(i, j, QtWidgets.QTableWidgetItem(str(li[j])))

    def get_table(self,tab:QtWidgets.QTableWidget):
        l1=tab.rowCount()
        l2=tab.columnCount()
        df=pd.DataFrame(np.zeros((l1,l2),dtype='U'))
        for i in range(0, l1):
            for j in range(0, l2):
                it=tab.item(i, j)
                if it is not None:
                    df.iloc[i,j]=it.text()
                else:
                    df.iloc[i, j] = ""
        return df

    def tab_export(self,tab:QtWidgets.QTableWidget,name='m1.csv',header=True,index=False,override=False):
        if override:
            path1=path+name
        else:
            path1=html_analysis.find_not_exist_name(path+name)

        self.get_table(tab).to_csv(path1, header=header, index=index)

    def tab_import(self,data='book',name='m1.csv'):
        self.old_table[data] = pd.read_csv(path + name)  
        self.columns = self.old_table[data].columns
        

        if data=='book':
            self.set_table_titles(self.tableWidget_book, self.columns)
            self.set_table(self.tableWidget_book, self.old_table[data])
        elif data=='reader':
            self.set_table_titles(self.tableWidget_reader, self.columns)
            self.set_table(self.tableWidget_reader, self.old_table[data])

    def tab_add(self,tab:QtWidgets.QTableWidget):
        tab.setRowCount(tab.rowCount()+1)

    def tab_del(self,tab:QtWidgets.QTableWidget):
        tab.removeRow(tab.currentRow())

    def tab_search(self,tab:QtWidgets.QTableWidget,data='book'):
        try:
            if data=='book':
                s1=self.lineEdit_book_1.text()
            elif data=='reader':
                s1 = self.lineEdit_reader_1.text()
            s2=s1.split(':')
            column1=int(s2[0])
            p = re.compile(s2[1])
        except Exception as ex:
            
            self.label_hint_1.setText('错误的正则表达式')
            self.set_table(tab,self.old_table[data])
            self.searching=False
            
            if data=='book':
                self.bookButton_4.setEnabled(True)
            elif data=='reader':
                self.readerButton_4.setEnabled(True)
            return
        self.label_hint_1.setText('提示')
        display_rows = []
        if not self.searching:
            self.old_table[data] = self.get_table(tab)
            self.searching=True
            
            if data=='book':
                self.bookButton_4.setEnabled(False)
            elif data=='reader':
                self.readerButton_4.setEnabled(False)
        if column1 in self.old_table[data].columns:
            li = list(self.old_table[data].loc[:,column1])
            for j in range(0, len(li)):
                if re.search(p,li[j]):
                    display_rows.append(j)
            self.set_table(tab,self.old_table[data].iloc[display_rows])

    def get_list_from_table(self,tab,column=0):
        r = []
        num = tab.rowCount()
        for i in range(0, num):
            if tab.item(i, column) is None:
                s=""
            else:
                s = tab.item(i, column).text()
            r.append(s)
        return r

    def borrow_book(self):
        book1=self.lineEdit_reader_2.text()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    def return_book(self):
        book1=self.lineEdit_reader_3.text()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    def set_table_titles(self,tab:QtWidgets.QTableWidget,columns):
        tab.setColumnCount(len(columns))
        for i in range(0,len(columns)):
            if tab.horizontalHeaderItem(i):
                tab.horizontalHeaderItem(i).setText(columns[i])
            else:
                tab.setHorizontalHeaderItem(i,QtWidgets.QTableWidgetItem(columns[i]))

    def export_selected_magnet(self,tab:QtWidgets.QTableWidget):
        
        
        
        
        
        
        
        

        k=-1
        magnet_list=[]
        magnet_column=8
        for item in tab.selectedItems():
            if item.row()>k:
                k = item.row()
                magnet_list.append(tab.item(k,magnet_column).text())
        html_analysis.write_txt(magnet_list)

    def the_last_function(self):
        pass


def start_process(target, args=()):
    p1 = Process(target=target, args=args)
    p1.start()



def run():
    import time

    start_time = time.time()

    app = QtWidgets.QApplication(sys.argv)
    u1 = MainWindow()
    u1.show()
    r = app.exec_()
    print(f"message loop ended with exit code {r}")
    print("运行时间: {} s".format(time.time() - start_time))
    return r


if __name__ == '__main__':

    exit(run())
