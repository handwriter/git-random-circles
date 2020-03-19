from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap
import sys
from PIL.ImageQt import ImageQt
from PIL import Image, ImageDraw
from random import randint
from design import Ui_Form as Design


class Widget(QWidget, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.circles)

    def circles(self):
        pixmap = QPixmap()
        image = Image.new('RGBA', (800, 800))
        draw = ImageDraw.Draw(image)
        for i in range(randint(2, 10)):
            a, x, y = randint(10, 180), randint(0, 800), randint(0, 800)
            draw.ellipse((x, y, x + a, y + a), fill=(randint(1, 255), randint(1, 255), randint(1, 255)))
            self.label.setPixmap(QPixmap.fromImage(ImageQt(image)))


app = QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec_())