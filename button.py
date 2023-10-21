import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot

@Slot()
def say_hello():
    print("Button Clicked, Hello!")


#Create a qt application
app = QApplication(sys.argv)

#Create a button and connect it
button = QPushButton("Click me")
button.clicked.connect(say_hello)
button.show()

app.exec()
