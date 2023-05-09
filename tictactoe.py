import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QLabel, QPushButton,QHBoxLayout,QVBoxLayout

class Game(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.setWindowTitle('TICTACTOE')
        self.setStyleSheet('background: #82E9ED')
        self.label=QLabel('Turn ❌')
        self.label.setFixedHeight
        self.label.setFixedWidth
        self.v_box=QVBoxLayout()
        self.s=0
        self.s1=0
        self.lis=[['btn1','btn2','btn3'],['btn4','btn5','btn6'],['btn7','btn8','btn9']]
        for i in range(3):
            self.h_box=QHBoxLayout()
            for j in range(3):
                self.lis[i][j]=QPushButton()
                self.lis[i][j].clicked.connect(self.PressButton)
                self.h_box.addWidget(self.lis[i][j])
                self.lis[i][j].setFixedHeight(60)
                self.lis[i][j].setFixedWidth(60)
            self.v_box.addLayout(self.h_box)
        self.v_box.addWidget(self.label)
        self.setLayout(self.v_box)
        
    def PressButton(self):
        self.s1+=1
        for i in range(3):
            for j in range(3):
                if self.sender()==self.lis[i][j]:
                    if self.s==0:
                        self.lis[i][j].setText('❌')
                        self.lis[i][j].setEnabled(False)
                        self.s=1
                        break
                    else:
                        self.lis[i][j].setText('⭕️')
                        self.lis[i][j].setEnabled(False)
                        self.s=0
                        break
        if self.s: self.label.setText('Turn ⭕️')
        else: self.label.setText('Turn ❌')
        
        if self.s1>4:
            n=self.isGameOverCheck()
            if n:
                for i in range(3):
                    for j in range(3):
                        self.lis[i][j].setEnabled(False)
                if n==2:
                    self.label.setText('⭕️ Win')
                else:
                    self.label.setText('❌ Win')
            elif self.s1==9:
                self.label.setText('Durrang')
                
    def isGameOverCheck(self):
        chek=0
        lis=list([0]*3 for i in range(3))
        lis2=list([0]*3 for i in range(3))
        for i in range(3):
            for j in range(3):
                lis[i][j]=self.lis[i][j].text()
                lis2[i][j]=self.lis[j][i].text()
                
        for i in range(3):
            if  lis[i]==['❌','❌','❌'] or lis2[i]==['❌','❌','❌']:
                chek=1
                break
            elif lis[i]==['⭕️','⭕️','⭕️'] or lis2[i]==['⭕️','⭕️','⭕️']:
                chek=2
                break
            
        if [lis[0][0],lis[1][1],lis[2][2]]==['❌','❌','❌'] or [lis[0][2],lis[1][1],lis[2][0]]==['❌','❌','❌']:
            chek=1
        elif [lis[0][0],lis[1][1],lis[2][2]]==['⭕️','⭕️','⭕️'] or [lis[0][2],lis[1][1],lis[2][0]]==['⭕️','⭕️','⭕️']:
            chek=2
            
        return chek
        
app=QApplication([0])
win=Game()
win.show()
app.exec_()
sys.exit()            
