
from PyQt5.QtWidgets import *
import sys
import pandas #as pd
from difflib import SequenceMatcher

from appwindow3 import Ui_MainWindow

class main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.actionOpen_File_1.triggered.connect(self.open_file1)
        self.actionOpen_File_2.triggered.connect(self.open_file2)
        self.btfile1.clicked.connect(self.full_similiar_same1)
        self.btfile2.clicked.connect(self.full_similiar_same2)
        self.btfull.clicked.connect(self.full_similiar)
        self.btless.clicked.connect(self.part_similiar)
        self.btlooklike.clicked.connect(self.less_similiar)
    csv1 = None
    def open_file1(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)

        global csv1
        csv1 = fileName
        if fileName:
            print(type(fileName))

    csv2 = None
    def open_file2(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)

        global csv2
        csv2 = fileName
        if fileName:
            print(type(fileName))


    def full_similiar(self):
        df1 = pandas.read_csv(csv1)
        df2 = pandas.read_csv(csv2)
        df1['name'] = df1['name'].str.replace('\d+', '')
        df2['name'] = df2['name'].str.replace('\d+', '')

        for index1, row1 in df1.iterrows():
            for index2, row2 in df2.iterrows():
                match = SequenceMatcher(None, row1['name'], row2['name'])
                result = int(match.ratio() * 100)

                if result >= 95 and result <= 100:
                    print("File -1 - index ->", index1 + 2, "- ", row1[
                        'name'], " equal ", "  " + " File -2 - index ->", index2 + 2, "- ", row2['name']
                        )

    def part_similiar(self):
        df1 = pandas.read_csv(csv1)
        df2 = pandas.read_csv(csv2)
        df1['name'] = df1['name'].str.replace('\d+', '')
        df2['name'] = df2['name'].str.replace('\d+', '')

        for index1, row1 in df1.iterrows():
            for index2, row2 in df2.iterrows():
                match = SequenceMatcher(None, row1['name'], row2['name'])
                result = int(match.ratio() * 100)

                if result >= 65 and result < 80:
                    print("File -1 - index ->", index1 + 2, "- ", row1[
                        'name'], " partiall like ", "  " + " File -2 - index ->", index2 + 2, "- ", row2['name']
                          )


    def less_similiar(self):
        df1 = pandas.read_csv(csv1)
        df2 = pandas.read_csv(csv2)
        df1['name'] = df1['name'].str.replace('\d+', '')
        df2['name'] = df2['name'].str.replace('\d+', '')

        for index1, row1 in df1.iterrows():
            for index2, row2 in df2.iterrows():
                match = SequenceMatcher(None, row1['name'], row2['name'])
                result = int(match.ratio() * 100)

                if result >= 80 and result <= 90:
                    print("File -1 - index ->", index1 + 2, "- ", row1[
                        'name'], " looks like ", "  " + " File -2 - index ->", index2 + 2, "- ", row2['name']
                        )

    def full_similiar_same1(self):
        print("###################################")
        df1 = pandas.read_csv(csv1)
        df1['name'] = df1['name'].str.replace('\d+', '')
        df1['check'] = df1['name'].duplicated(keep=False)
        total = ''
        for index1, row1 in df1.iterrows():
            if row1['check'] == True:
                index = index1 + 2
                result = row1['name'] + "   " + str(index)+ "\n"

                total += result
        print(total)
        print("done")
        print("###################################")


    def full_similiar_same2(self):
        print("###################################")
        df2 = pandas.read_csv(csv2)
        df2['name'] = df2['name'].str.replace('\d+', '')
        df2['check'] = df2['name'].duplicated(keep=False)
        total = ''
        for index1, row2 in df2.iterrows():
            if row2['check'] == True:
                index= index1 + 2
                result = row2['name']+ "   "+str(index)+"\n"
                total += result
        print(total)
        print("done")
        print("###################################")


app    = QApplication(sys.argv)
window = main()
window.show()
app.exec_()
