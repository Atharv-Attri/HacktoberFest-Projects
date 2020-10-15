# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'findBook.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pb1 = QtWidgets.QPushButton(Form)
        self.pb1.setObjectName("pb1")
        self.gridLayout.addWidget(self.pb1, 0, 3, 1, 1)
        self.l1 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.l1.setFont(font)
        self.l1.setObjectName("l1")
        self.gridLayout.addWidget(self.l1, 0, 0, 1, 1)
        self.t1 = QtWidgets.QLineEdit(Form)
        self.t1.setObjectName("t1")
        self.gridLayout.addWidget(self.t1, 0, 2, 1, 1)
        self.l2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.l2.setFont(font)
        self.l2.setObjectName("l2")
        self.gridLayout.addWidget(self.l2, 1, 0, 1, 1)
        self.l3 = QtWidgets.QLabel(Form)
        self.l3.setObjectName("l3")
        self.gridLayout.addWidget(self.l3, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setLineWidth(0)
        self.line.setMidLineWidth(20)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.l6 = QtWidgets.QLabel(Form)
        self.l6.setObjectName("l6")
        self.gridLayout_2.addWidget(self.l6, 1, 1, 1, 2)
        self.t2 = QtWidgets.QLineEdit(Form)
        self.t2.setObjectName("t2")
        self.gridLayout_2.addWidget(self.t2, 0, 2, 1, 1)
        self.pb2 = QtWidgets.QPushButton(Form)
        self.pb2.setObjectName("pb2")
        self.gridLayout_2.addWidget(self.pb2, 0, 3, 1, 1)
        self.l5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.l5.setFont(font)
        self.l5.setObjectName("l5")
        self.gridLayout_2.addWidget(self.l5, 1, 0, 1, 1)
        self.l4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.l4.setFont(font)
        self.l4.setObjectName("l4")
        self.gridLayout_2.addWidget(self.l4, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.pb1.pressed.connect(self.book_cost)
        self.pb2.pressed.connect(self.total_cost)

        self.cost=0
    

    def book_cost(self):
        import sqlite3
        db=sqlite3.connect("records.db")
        cur=db.cursor()
        text=self.t1.text()
        if (text):
            sql="SELECT price FROM Books WHERE title='"+text+"';"
            cur.execute(sql)
            result=cur.fetchone()
            if result:
                self.l3.setText("Rs. "+str(float(result[0])))
                self.cost=int(result[0])
            else:
                self.l3.setText("Book not found")

    def total_cost(self):
        num=self.t2.text()
        if (num):
            qty=int(num)
            self.l6.setText("Rs. "+str(float(self.cost*qty)))
        else:
            self.l6.setText("Enter the quantity please")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Find Book"))
        self.pb1.setText(_translate("Form", "Find Price"))
        self.l1.setText(_translate("Form", "   Book Title:      "))
        self.l2.setText(_translate("Form", "            Price:"))
        self.l3.setText(_translate("Form", " Rs. 0"))
        self.l6.setText(_translate("Form", "   Rs. 0"))
        self.pb2.setText(_translate("Form", "Find Total"))
        self.l5.setText(_translate("Form", "           Total:"))
        self.l4.setText(_translate("Form", "    Quantity:      "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
