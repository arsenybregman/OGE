import sys
import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QInputDialog
from random import randint


MAX_COUNTER = 10


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.label.hide()
        self.answer_button.hide()
        self.example.hide()
        self.right_number.hide()
        self.list_buttons.hide()
        self.show_button.hide()
        self.next_button.hide()
        self.back_button.hide()
        self.finder = 0
        self.right_counter = 0
        self.counter = 1
        self.test_counter = 1
        self.max_counter = 10
        self.show_status = False
        self.answer_counter = 1
        self.pixmap = ''
        self.test_button.clicked.connect(self.run)
        self.answer_button.clicked.connect(self.check)
        self.list_button.clicked.connect(self.run_two)
        self.number1.clicked.connect(self.list_1)
        self.number2.clicked.connect(self.list_2)
        self.number3.clicked.connect(self.list_3)
        self.number4.clicked.connect(self.list_4)
        self.number5.clicked.connect(self.list_5)
        self.number6.clicked.connect(self.list_6)
        self.number7.clicked.connect(self.list_7)
        self.number8.clicked.connect(self.list_8)
        self.number9.clicked.connect(self.list_9)
        self.number10.clicked.connect(self.list_10)
        self.next_button.clicked.connect(self.next_example)
        self.back_button.clicked.connect(self.back_example)
        self.show_button.clicked.connect(self.list_show)

    
    def connect(self, type, table_name):
        self.finder = choice()
        con = sqlite3.connect('inf_oge.db')
        kur = con.cursor()
        line_1 = kur.execute(f"SELECT {type} FROM {table_name} WHERE id = ?", self.finder).fetchall()
        con.commit()
        con.close()
        if type == 'text':
            self.example.setText(str(line_1[0][0]))
        elif type == 'image':
            line_2 = str(line_1[0][0])
            self.pixmap = QPixmap(line_2)
            self.example.setPixmap(self.pixmap)

    def run(self):
        self.test_button.setEnabled(False)
        self.list_button.setEnabled(False)
        self.show_button.hide()
        self.next_button.hide()
        self.back_button.hide()
        self.list_buttons.hide()
        self.right_number.hide()
        self.label.hide()
        self.answer_button.show()
        self.example.show()
        if self.test_counter == 1:
            self.finder = choice()
            con = sqlite3.connect('inf_oge.db')
            kur = con.cursor()
            line_1 = kur.execute("""SELECT text FROM number_1 WHERE id = ?""", self.finder).fetchall()
            con.commit()
            con.close()
            self.example.setText(str(line_1[0][0]))
        elif self.test_counter == 2:
            self.finder = choice()
            con = sqlite3.connect('inf_oge.db')
            kur = con.cursor()
            line_2 = kur.execute("""SELECT text FROM number_2 WHERE id = ?""", self.finder).fetchall()
            con.commit()
            con.close()
            self.example.setText(str(line_2[0][0]))
        elif self.test_counter == 3:
            self.finder = choice()
            con = sqlite3.connect('inf_oge.db')
            kur = con.cursor()
            line_2 = kur.execute("""SELECT image FROM number_3 WHERE id = ?""", self.finder).fetchall()
            con.commit()
            con.close()
            line_2 = str(line_2[0][0])
            self.pixmap = QPixmap(line_2)
            self.example.setPixmap(self.pixmap)
        elif self.test_counter == 4:
            self.finder = choice()
            con = sqlite3.connect('inf_oge.db')
            kur = con.cursor()
            line_2 = kur.execute("""SELECT image FROM number_4 WHERE id = ?""", self.finder).fetchall()
            con.commit()
            con.close()
            line_2 = str(line_2[0][0])
            self.pixmap = QPixmap(line_2)
            self.example.setPixmap(self.pixmap)
        elif self.test_counter == 5:
            self.finder = choice()
            con = sqlite3.connect('inf_oge.db')
            kur = con.cursor()
            line_1 = kur.execute("""SELECT text FROM number_5 WHERE id = ?""", self.finder).fetchall()
            con.commit()
            con.close()
            self.example.setText(str(line_1[0][0]))
        elif self.test_counter == 6:
            self.finder = choice()
            con = sqlite3.connect('inf_oge.db')
            kur = con.cursor()
            line_1 = kur.execute("""SELECT text FROM number_6 WHERE id = ?""", self.finder).fetchall()
            con.commit()
            con.close()
            self.example.setText(str(line_1[0][0]))
        elif self.test_counter == 7:
            self.finder = choice()
            con = sqlite3.connect('inf_oge.db')
            kur = con.cursor()
            line_1 = kur.execute("""SELECT text FROM number_7 WHERE id = ?""", self.finder).fetchall()
            con.commit()
            con.close()
            self.example.setText(str(line_1[0][0]))
        elif self.test_counter == 8:
            self.finder = choice()
            con = sqlite3.connect('inf_oge.db')
            kur = con.cursor()
            line_2 = kur.execute("""SELECT image FROM number_8 WHERE id = ?""", self.finder).fetchall()
            con.commit()
            con.close()
            line_2 = str(line_2[0][0])
            self.pixmap = QPixmap(line_2)
            self.example.setPixmap(self.pixmap)
        elif self.test_counter == 9:
            self.finder = choice()
            con = sqlite3.connect('inf_oge.db')
            kur = con.cursor()
            line_2 = kur.execute("""SELECT image FROM number_9 WHERE id = ?""", self.finder).fetchall()
            con.commit()
            con.close()
            line_2 = str(line_2[0][0])
            self.pixmap = QPixmap(line_2)
            self.example.setPixmap(self.pixmap)
        elif self.test_counter == 10:
            self.finder = choice()
            con = sqlite3.connect('inf_oge.db')
            kur = con.cursor()
            line_2 = kur.execute("""SELECT image FROM number_10 WHERE id = ?""", self.finder).fetchall()
            con.commit()
            con.close()
            line_2 = str(line_2[0][0])
            self.pixmap = QPixmap(line_2)
            self.example.setPixmap(self.pixmap)

    def check(self):
        self.test_button.setEnabled(True)
        self.list_button.setEnabled(True)
        user_answer, ok_pressed = QInputDialog.getText(self, '', 'Введите ответ')
        if ok_pressed:
            if self.test_counter == 1:
                con = sqlite3.connect('inf_oge.db')
                kur = con.cursor()
                line = kur.execute("""SELECT right_answer FROM number_1 WHERE id = ?""", self.finder).fetchall()
                con.commit()
                con.close()
                right_line = str(line[0][0])
            elif self.test_counter == 2:
                con = sqlite3.connect('inf_oge.db')
                kur = con.cursor()
                line = kur.execute("""SELECT right_answer FROM number_2 WHERE id = ?""", self.finder).fetchall()
                con.commit()
                con.close()
                right_line = str(line[0][0])
            elif self.test_counter == 3:
                con = sqlite3.connect('inf_oge.db')
                kur = con.cursor()
                line = kur.execute("""SELECT right_answer FROM number_3 WHERE id = ?""", self.finder).fetchall()
                con.commit()
                con.close()
                right_line = str(line[0][0])
            elif self.test_counter == 4:
                con = sqlite3.connect('inf_oge.db')
                kur = con.cursor()
                line = kur.execute("""SELECT right_answer FROM number_4 WHERE id = ?""", self.finder).fetchall()
                con.commit()
                con.close()
                right_line = str(line[0][0])
            elif self.test_counter == 5:
                con = sqlite3.connect('inf_oge.db')
                kur = con.cursor()
                line = kur.execute("""SELECT right_answer FROM number_5 WHERE id = ?""", self.finder).fetchall()
                con.commit()
                con.close()
                right_line = str(line[0][0])
            elif self.test_counter == 6:
                con = sqlite3.connect('inf_oge.db')
                kur = con.cursor()
                line = kur.execute("""SELECT right_answer FROM number_6 WHERE id = ?""", self.finder).fetchall()
                con.commit()
                con.close()
                right_line = str(line[0][0])
            elif self.test_counter == 7:
                con = sqlite3.connect('inf_oge.db')
                kur = con.cursor()
                line = kur.execute("""SELECT right_answer FROM number_7 WHERE id = ?""", self.finder).fetchall()
                con.commit()
                con.close()
                right_line = str(line[0][0])
            elif self.test_counter == 8:
                con = sqlite3.connect('inf_oge.db')
                kur = con.cursor()
                line = kur.execute("""SELECT right_answer FROM number_8 WHERE id = ?""", self.finder).fetchall()
                con.commit()
                con.close()
                right_line = str(line[0][0])
            elif self.test_counter == 9:
                con = sqlite3.connect('inf_oge.db')
                kur = con.cursor()
                line = kur.execute("""SELECT right_answer FROM number_9 WHERE id = ?""", self.finder).fetchall()
                con.commit()
                con.close()
                right_line = str(line[0][0])
            elif self.test_counter == 10:
                con = sqlite3.connect('inf_oge.db')
                kur = con.cursor()
                line = kur.execute("""SELECT right_answer FROM number_10 WHERE id = ?""", self.finder).fetchall()
                con.commit()
                con.close()
                right_line = str(line[0][0])
            if right_line == str(user_answer).lower():
                self.right_counter += 1
            self.test_counter += 1
            if self.test_counter > MAX_COUNTER:
                self.test_counter = 1
                self.label.hide()
                self.answer_button.hide()
                self.example.hide()
                self.label.show()
                self.right_number.show()
                self.right_number.display(self.right_counter)
                self.right_counter = 0
            else:
                self.run()

    def run_two(self):
        self.test_counter = 1
        self.counter = 1
        self.label.hide()
        self.answer_button.hide()
        self.example.setText('')
        self.example.show()
        self.right_number.hide()
        self.list_buttons.show()
        self.show_button.show()
        self.next_button.show()
        self.back_button.show()

    def list_1(self, status=-1):
        if not status:
            self.answer_counter = 1
        self.back_button.setEnabled(False)
        self.next_button.setEnabled(True)
        self.counter_check()
        self.counter = 1
        self.show_button.setText('Показать решение и ответ')
        self.show_status = False
        self.finder = tuple(str(self.answer_counter))
        con = sqlite3.connect('inf_oge.db')
        kur = con.cursor()
        line_1 = kur.execute("""SELECT text FROM number_1 WHERE id = ?""", self.finder).fetchall()
        con.commit()
        con.close()
        self.example.setText(str(line_1[0][0]))

    def list_2(self, status=-1):
        if not status:
            self.answer_counter = 1
        self.back_button.setEnabled(False)
        self.next_button.setEnabled(True)
        self.counter_check()
        self.counter = 2
        self.show_button.setText('Показать решение и ответ')
        self.show_status = False
        self.finder = tuple(str(self.answer_counter))
        con = sqlite3.connect('inf_oge.db')
        kur = con.cursor()
        line_1 = kur.execute("""SELECT text FROM number_2 WHERE id = ?""", self.finder).fetchall()
        con.commit()
        con.close()
        self.example.setText(str(line_1[0][0]))

    def list_3(self, status=-1):
        if not status:
            self.answer_counter = 1
        self.back_button.setEnabled(False)
        self.next_button.setEnabled(True)
        self.counter_check()
        self.counter = 3
        self.show_button.setText('Показать решение и ответ')
        self.show_status = False
        self.finder = tuple(str(self.answer_counter))
        con = sqlite3.connect('inf_oge.db')
        kur = con.cursor()
        line_1 = kur.execute("""SELECT image FROM number_3 WHERE id = ?""", self.finder).fetchall()
        con.commit()
        con.close()
        line_1 = str(line_1[0][0])
        self.pixmap = QPixmap(line_1)
        self.example.setPixmap(self.pixmap)

    def list_4(self, status=-1):
        if not status:
            self.answer_counter = 1
        self.back_button.setEnabled(False)
        self.next_button.setEnabled(True)
        self.counter_check()
        self.counter = 4
        self.show_button.setText('Показать решение и ответ')
        self.show_status = False
        self.finder = tuple(str(self.answer_counter))
        con = sqlite3.connect('inf_oge.db')
        kur = con.cursor()
        line_1 = kur.execute("""SELECT image FROM number_4 WHERE id = ?""", self.finder).fetchall()
        con.commit()
        con.close()
        line_1 = str(line_1[0][0])
        self.pixmap = QPixmap(line_1)
        self.example.setPixmap(self.pixmap)

    def list_5(self, status=-1):
        if not status:
            self.answer_counter = 1
        self.back_button.setEnabled(False)
        self.next_button.setEnabled(True)
        self.counter_check()
        self.counter = 5
        self.show_button.setText('Показать решение и ответ')
        self.show_status = False
        self.finder = tuple(str(self.answer_counter))
        con = sqlite3.connect('inf_oge.db')
        kur = con.cursor()
        line_1 = kur.execute("""SELECT text FROM number_5 WHERE id = ?""", self.finder).fetchall()
        con.commit()
        con.close()
        self.example.setText(str(line_1[0][0]))

    def list_6(self, status=-1):
        if not status:
            self.answer_counter = 1
        self.back_button.setEnabled(False)
        self.next_button.setEnabled(True)
        self.counter_check()
        self.counter = 6
        self.show_button.setText('Показать решение и ответ')
        self.show_status = False
        self.finder = tuple(str(self.answer_counter))
        con = sqlite3.connect('inf_oge.db')
        kur = con.cursor()
        line_1 = kur.execute("""SELECT text FROM number_6 WHERE id = ?""", self.finder).fetchall()
        con.commit()
        con.close()
        self.example.setText(str(line_1[0][0]))

    def list_7(self, status=-1):
        if not status:
            self.answer_counter = 1
        self.back_button.setEnabled(False)
        self.next_button.setEnabled(True)
        self.counter_check()
        self.counter = 7
        self.show_button.setText('Показать решение и ответ')
        self.show_status = False
        self.finder = tuple(str(self.answer_counter))
        con = sqlite3.connect('inf_oge.db')
        kur = con.cursor()
        line_1 = kur.execute("""SELECT text FROM number_7 WHERE id = ?""", self.finder).fetchall()
        con.commit()
        con.close()
        self.example.setText(str(line_1[0][0]))

    def list_8(self, status=-1):
        if not status:
            self.answer_counter = 1
        self.back_button.setEnabled(False)
        self.next_button.setEnabled(True)
        self.counter_check()
        self.counter = 8
        self.show_button.setText('Показать решение и ответ')
        self.show_status = False
        self.finder = tuple(str(self.answer_counter))
        con = sqlite3.connect('inf_oge.db')
        kur = con.cursor()
        line_1 = kur.execute("""SELECT image FROM number_8 WHERE id = ?""", self.finder).fetchall()
        con.commit()
        con.close()
        line_1 = str(line_1[0][0])
        self.pixmap = QPixmap(line_1)
        self.example.setPixmap(self.pixmap)

    def list_9(self, status=-1):
        if not status:
            self.answer_counter = 1
        self.back_button.setEnabled(False)
        self.next_button.setEnabled(True)
        self.counter_check()
        self.counter = 9
        self.show_button.setText('Показать решение и ответ')
        self.show_status = False
        self.finder = tuple(str(self.answer_counter))
        con = sqlite3.connect('inf_oge.db')
        kur = con.cursor()
        line_1 = kur.execute("""SELECT image FROM number_9 WHERE id = ?""", self.finder).fetchall()
        con.commit()
        con.close()
        line_1 = str(line_1[0][0])
        self.pixmap = QPixmap(line_1)
        self.example.setPixmap(self.pixmap)

    def list_10(self, status=-1):
        if not status:
            self.answer_counter = 1
        self.back_button.setEnabled(False)
        self.next_button.setEnabled(True)
        self.counter_check()
        self.counter = 10
        self.show_button.setText('Показать решение и ответ')
        self.show_status = False
        self.finder = tuple(str(self.answer_counter))
        con = sqlite3.connect('inf_oge.db')
        kur = con.cursor()
        line_1 = kur.execute("""SELECT image FROM number_10 WHERE id = ?""", self.finder).fetchall()
        con.commit()
        con.close()
        line_1 = str(line_1[0][0])
        self.pixmap = QPixmap(line_1)
        self.example.setPixmap(self.pixmap)

    def next_example(self):
        if self.counter == 1:
            self.answer_counter += 1
            self.list_1(1)
        elif self.counter == 2:
            self.answer_counter += 1
            self.list_2(1)
        elif self.counter == 3:
            self.answer_counter += 1
            self.list_3(1)
        elif self.counter == 4:
            self.answer_counter += 1
            self.list_4(1)
        elif self.counter == 5:
            self.answer_counter += 1
            self.list_5(1)
        elif self.counter == 6:
            self.answer_counter += 1
            self.list_6(1)
        elif self.counter == 7:
            self.answer_counter += 1
            self.list_7(1)
        elif self.counter == 8:
            self.answer_counter += 1
            self.list_8(1)
        elif self.counter == 9:
            self.answer_counter += 1
            self.list_9(1)
        elif self.counter == 10:
            self.answer_counter += 1
            self.list_10(1)

    def back_example(self):
        if self.counter == 1:
            self.answer_counter -= 1
            self.list_1(1)
        elif self.counter == 2:
            self.answer_counter -= 1
            self.list_2(1)
        elif self.counter == 3:
            self.answer_counter -= 1
            self.list_3(1)
        elif self.counter == 4:
            self.answer_counter -= 1
            self.list_4(1)
        elif self.counter == 5:
            self.answer_counter -= 1
            self.list_5(1)
        elif self.counter == 6:
            self.answer_counter -= 1
            self.list_6(1)
        elif self.counter == 7:
            self.answer_counter -= 1
            self.list_7(1)
        elif self.counter == 8:
            self.answer_counter -= 1
            self.list_8(1)
        elif self.counter == 9:
            self.answer_counter -= 1
            self.list_9(1)
        elif self.counter == 10:
            self.answer_counter -= 1
            self.list_10(1)

    def counter_check(self):
        if self.answer_counter == 1:
            self.back_button.setEnabled(False)
            self.next_button.setEnabled(True)
        elif self.answer_counter == 5:
            self.next_button.setEnabled(False)
            self.back_button.setEnabled(True)
        else:
            self.back_button.setEnabled(True)
            self.next_button.setEnabled(True)

    def list_show(self):
        if not self.show_status:
            self.show_button.setText('Скрыть решение')
            self.show_status = True
            if self.counter == 1:
                self.finder = tuple(str(self.answer_counter))
                con = sqlite3.connect('inf_oge.db')
                kur = con.cursor()
                line_1 = kur.execute("""SELECT text_answer FROM number_1 WHERE id = ?""", self.finder).fetchall()
                con.commit()
                con.close()
                self.example.setText(str(line_1[0][0]))
            elif self.counter == 2:
                self.finder = tuple(str(self.answer_counter))
                con = sqlite3.connect('inf_oge.db')
                kur = con.cursor()
                line_1 = kur.execute("""SELECT text_answer FROM number_2 WHERE id = ?""", self.finder).fetchall()
                con.commit()
                con.close()
                self.example.setText(str(line_1[0][0]))
            elif self.counter == 3:
                self.finder = tuple(str(self.answer_counter))
                con = sqlite3.connect('inf_oge.db')
                kur = con.cursor()
                line_1 = kur.execute("""SELECT text_answer FROM number_3 WHERE id = ?""", self.finder).fetchall()
                con.commit()
                con.close()
                self.example.setText(str(line_1[0][0]))
            elif self.counter == 4:
                self.finder = tuple(str(self.answer_counter))
                con = sqlite3.connect('inf_oge.db')
                kur = con.cursor()
                line_1 = kur.execute("""SELECT text_answer FROM number_4 WHERE id = ?""", self.finder).fetchall()
                con.commit()
                con.close()
                self.example.setText(str(line_1[0][0]))
            elif self.counter == 5:
                self.finder = tuple(str(self.answer_counter))
                con = sqlite3.connect('inf_oge.db')
                kur = con.cursor()
                line_1 = kur.execute("""SELECT text_answer FROM number_5 WHERE id = ?""", self.finder).fetchall()
                con.commit()
                con.close()
                self.example.setText(str(line_1[0][0]))
            elif self.counter == 6:
                self.finder = tuple(str(self.answer_counter))
                con = sqlite3.connect('inf_oge.db')
                kur = con.cursor()
                line_1 = kur.execute("""SELECT text_answer FROM number_6 WHERE id = ?""", self.finder).fetchall()
                con.commit()
                con.close()
                self.example.setText(str(line_1[0][0]))
            elif self.counter == 7:
                self.finder = tuple(str(self.answer_counter))
                con = sqlite3.connect('inf_oge.db')
                kur = con.cursor()
                line_1 = kur.execute("""SELECT text_answer FROM number_7 WHERE id = ?""", self.finder).fetchall()
                con.commit()
                con.close()
                self.example.setText(str(line_1[0][0]))
            elif self.counter == 8:
                self.finder = tuple(str(self.answer_counter))
                con = sqlite3.connect('inf_oge.db')
                kur = con.cursor()
                line_1 = kur.execute("""SELECT text_answer FROM number_8 WHERE id = ?""", self.finder).fetchall()
                con.commit()
                con.close()
                line_1 = str(line_1[0][0])
                self.pixmap = QPixmap(line_1)
                self.example.setPixmap(self.pixmap)
            elif self.counter == 9:
                self.finder = tuple(str(self.answer_counter))
                con = sqlite3.connect('inf_oge.db')
                kur = con.cursor()
                line_1 = kur.execute("""SELECT text_answer FROM number_9 WHERE id = ?""", self.finder).fetchall()
                con.commit()
                con.close()
                self.example.setText(str(line_1[0][0]))
            elif self.counter == 10:
                self.finder = tuple(str(self.answer_counter))
                con = sqlite3.connect('inf_oge.db')
                kur = con.cursor()
                line_1 = kur.execute("""SELECT text_answer FROM number_10 WHERE id = ?""", self.finder).fetchall()
                con.commit()
                con.close()
                self.example.setText(str(line_1[0][0]))
        else:
            self.show_button.setText('Показать решение и ответ')
            self.show_status = False
            if self.counter == 1:
                self.list_1(1)
            elif self.counter == 2:
                self.list_2(1)
            elif self.counter == 2:
                self.list_2(1)
            elif self.counter == 3:
                self.list_3(1)
            elif self.counter == 4:
                self.list_4(1)
            elif self.counter == 5:
                self.list_5(1)
            elif self.counter == 6:
                self.list_6(1)
            elif self.counter == 7:
                self.list_7(1)
            elif self.counter == 8:
                self.list_8(1)
            elif self.counter == 9:
                self.list_9(1)
            elif self.counter == 10:
                self.list_10(1)


def choice():
    return tuple(str(randint(1, 5)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
