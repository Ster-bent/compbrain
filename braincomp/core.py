import mathgenerator as mg
from PySide6.QtWidgets import *
import sys
import random


#move some of the interface fucntions to a seperate file
#COLLECT BUG
class All(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Full Practice")
        global problem, solution
        problem, solution = mg.genById(random.randint(0,100))

        solution = list(solution)
        for i in range(len(solution)):
            if solution[i] == "$":
                solution[i] = ""
        solution = "".join(solution)

        self.nextButton = QPushButton("Next")
        self.nextButton.hide()
        self.nextButton.setFixedSize(175, 40)
        self.query = QLabel(problem)
        self.confirm = QLabel("")
        self.answer = QLineEdit()

        self.answer.textChanged.connect(self.collect)
        #change to a next button
        #add another query for correct and incorrect comments
        self.nextButton.clicked.connect(self.nextAll)
        self.answer.setFixedSize(175,40)
        self.query.setMaximumSize(300, 40)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.answer)
        self.layout.addWidget(self.query)
        self.layout.addWidget(self.nextButton)
        self.layout.addWidget(self.confirm)
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
    

    def collect(self):
        global solution
        text = str(self.answer.text())
        print(f"{text} and {solution}")
        if text == str(solution):
            self.confirm.setText("Correct")
            self.nextButton.show()
        else:
            self.confirm.setText(f"Wrong, Solution: {solution}")
    
    #BUG Some problems repeat, make more versatile
    def nextAll(self):
        global problem, solution
        problem, solution = mg.genById(random.randint(0,100))
        solution = list(solution)
        for i in range(len(solution)):
            if solution[i] == "$":
                solution[i] = ""
        solution = "".join(solution)

        self.nextButton.setText("Next")
        self.nextButton.hide()
        self.nextButton.setFixedSize(175, 40)
        self.query.setText(problem)
        self.answer.setText("")
        self.confirm.setText("")

class Algebra(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Algebra Practice")
        
        global algebra
        algebra = [mg.basic_algebra(), mg.combine_like_terms(),mg.complex_quadratic(),mg.distance_two_points()]
        global problem, solution
        problem, solution = algebra[random.randint(0,3)]

        solution = list(solution)
        for i in range(len(solution)):
            if solution[i] == "$":
                solution[i] = ""
        solution = "".join(solution)

        self.nextButton = QPushButton("Next")
        self.nextButton.hide()
        self.nextButton.setFixedSize(175, 40)
        self.query = QLabel(problem)
        self.confirm = QLabel("")
        self.answer = QLineEdit()

        self.answer.textChanged.connect(self.collect)
        #change to a next button
        #add another query for correct and incorrect comments
        self.nextButton.clicked.connect(self.nextAlge)
        self.answer.setFixedSize(175,40)
        self.query.setMaximumSize(300, 40)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.answer)
        self.layout.addWidget(self.query)
        self.layout.addWidget(self.nextButton)
        self.layout.addWidget(self.confirm)
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
    

    def collect(self):
        global solution
        text = str(self.answer.text())
        print(f"{text} and {solution}")
        if text == str(solution):
            self.confirm.setText("Correct")
            self.nextButton.show()
        else:
            self.confirm.setText(f"Wrong, Solution: {solution}")
    
    #BUG Some problems repeat, make more versatile
    def nextAlge(self):
        global algebra
        global problem, solution
        algebra = [mg.basic_algebra(), mg.combine_like_terms(),mg.complex_quadratic(),mg.distance_two_points()]
        problem, solution = algebra[random.randint(0,3)]
        solution = list(solution)
        for i in range(len(solution)):
            if solution[i] == "$":
                solution[i] = ""
        solution = "".join(solution)

        self.nextButton.setText("Next")
        self.nextButton.hide()
        self.nextButton.setFixedSize(175, 40)
        self.query.setText(problem)
        self.answer.setText("")
        self.confirm.setText("")

class Arithmetic(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Arithmetic Practice")
        
        global arithmetic
        arithmetic  = [mg.addition(), mg.subtraction(), mg.multiplication(), mg.division(), mg.divide_fractions(), mg.greatest_common_divisor()]
        global problem, solution
        problem, solution = arithmetic[random.randint(0,4)]

        solution = list(solution)
        for i in range(len(solution)):
            if solution[i] == "$":
                solution[i] = ""
        solution = "".join(solution)

        self.nextButton = QPushButton("Next")
        self.nextButton.hide()
        self.nextButton.setFixedSize(175, 40)
        self.query = QLabel(problem)
        self.confirm = QLabel("")
        self.answer = QLineEdit()

        self.answer.textChanged.connect(self.collect)
        #change to a next button
        #add another query for correct and incorrect comments
        self.nextButton.clicked.connect(self.nextArith)
        self.answer.setFixedSize(175,40)
        self.query.setMaximumSize(300, 40)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.answer)
        self.layout.addWidget(self.query)
        self.layout.addWidget(self.nextButton)
        self.layout.addWidget(self.confirm)
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
    

    def collect(self):
        global solution
        text = str(self.answer.text())
        print(f"{text} and {solution}")
        if text == str(solution):
            self.confirm.setText("Correct")
            self.nextButton.show()
        else:
            self.confirm.setText(f"Wrong, Solution: {solution}")
    
    #BUG Some problems repeat, make more versatile
    def nextArith(self):
        global arithmetic
        global problem, solution
        arithmetic = [mg.addition(), mg.subtraction(), mg.multiplication(), mg.division(), mg.divide_fractions(), mg.greatest_common_divisor()]
        problem, solution = arithmetic[random.randint(0,4)]
        solution = list(solution)
        for i in range(len(solution)):
            if solution[i] == "$":
                solution[i] = ""
        solution = "".join(solution)

        self.nextButton.setText("Next")
        self.nextButton.hide()
        self.nextButton.setFixedSize(175, 40)
        self.query.setText(problem)
        self.answer.setText("")
        self.confirm.setText("")
        
            
 

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BrainComp")

        self.modeselect = QComboBox()
        self.modeselect.setFixedSize(175, 40)
        self.modeselect.addItem('Arithmetic')
        self.modeselect.addItem('Algebra')
        self.modeselect.addItem('All')

        self.startButton = QPushButton("Begin Computation")
        self.startButton.setFixedSize(175, 40)
        self.startButton.clicked.connect(self.intialize)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.startButton)
        self.layout.addWidget(self.modeselect)
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
#FORMAT PLEASE
    def Algebra(self):
        algebra = [mg.basic_algebra(), mg.combine_like_terms(),mg.complex_quadratic(),mg.distance_two_points()]
        self.setWindowTitle("Algebra")
        self.submitButton = QPushButton("Submit")
        self.submitButton.setFixedSize(175, 40)
        self.submitButton.setCheckable(True)
        problem, solution = algebra[random.randint(0,3)]
        #self.submitButton.clicked.connect(self.collect)
        self.query = QLabel(problem)
        self.query.setFixedSize(300, 50)
        self.answer = QLineEdit()
        self.answer.setFixedSize(175,40)
        self.layout.addWidget(self.answer)
        self.layout.addWidget(self.query)
        self.layout.addWidget(self.submitButton)
    
    def All(self):
        self.setWindowTitle("All")
        self.submitButton = QPushButton("Submit")
        self.submitButton.setFixedSize(175, 40)
        self.submitButton.setCheckable(True)
        problem, solution = mg.genById(random.randint(0,1000))
        #self.submitButton.clicked.connect(self.collect)
        self.query = QLabel(problem)
        self.query.setMaximumSize(300, 40)
        self.answer = QLineEdit()
        self.answer.setFixedSize(175,40)
        self.layout.addWidget(self.answer)
        self.layout.addWidget(self.query)
        self.layout.addWidget(self.submitButton)

    def intialize(self):
        mode = str(self.modeselect.currentText())

        #BUG
        if mode == "Arithmetic":
            print("Showing Arithmetic")
            w = Arithmetic()
            w.show()
            try:
                sys.exit(w.exec_)
            except AttributeError:
                Arithmetic.show()

        elif mode == "Algebra":
            print("Showing Arithmetic")
            w = Algebra()
            w.show()
            try:
                sys.exit(w.exec_)
            except AttributeError:
                Algebra.show()

        elif mode == "All":
            print("Showing All")
            w = All()
            w.show()
            try:
                sys.exit(w.exec_)
            except AttributeError:
                All.show()
    
#segmentation fault error using alt classes

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec())