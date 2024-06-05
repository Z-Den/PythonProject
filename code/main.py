import sys
import sqlite3
import os

import datetime as dt
from PIL import Image

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QColorDialog, QInputDialog, QFileDialog
from PyQt5.QtWidgets import QMessageBox, QListWidgetItem
from PyQt5.QtGui import QIcon, QPixmap

from ui_main import Ui_MainWindow
from ui_new_item import Ui_New_Item_Form
from ui_settings import Ui_Settings_Form
from ui_instruction import Ui_Instruction_Form
from ui_change_fridge import Ui_Change_Fridge_Form
from ui_change_db import Ui_Change_Db_Form


class MainForm(QMainWindow, Ui_MainWindow):
    """Класс основного окна программы."""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(380, 580)
        self.setWindowIcon(QIcon('icon.ico'))

        self.update_fridge()

        self.btnInstruction.clicked.connect(self.open_instruction_form)
        self.btnSettings.clicked.connect(self.open_settings_form)
        self.btnFridgeTxt.clicked.connect(self.convert_fridge_to_txt)
        self.btnDbTxt.clicked.connect(self.convert_db_to_txt)
        self.btnClear.clicked.connect(self.clear)
        self.btnFridgeChange.clicked.connect(self.open_change_fridge_form)
        self.btnDbChange.clicked.connect(self.open_change_db_form)
        self.btnChoose.clicked.connect(self.choose)
        self.btnNew.clicked.connect(self.open_new_item_form)

    def open_instruction_form(self):  # инструкция
        self.instruction_form = InstructionForm(self)  # форма инструкции
        self.instruction_form.show()

    def open_settings_form(self):  # настройки
        self.settings_form = SettingsForm(self)  # форма настроек
        self.settings_form.show()

    def update_fridge(self):  # обновить
        con = sqlite3.connect("items_db.sqlite")
        cur = con.cursor()

        # загрузка цветов блоков
        result_one = cur.execute("""select first from colors""").fetchall()
        result_two = cur.execute("""select second from colors""").fetchall()
        result_three = cur.execute("""select third from colors""").fetchall()
        self.lstFresh.setStyleSheet(f'background-color: {result_one[0][0]}')
        self.lstTired.setStyleSheet(f'background-color: {result_two[0][0]}')
        self.lstOld.setStyleSheet(f'background-color: {result_three[0][0]}')

        # убрать отметку (см. convert_fridge_to_txt, convert_db_to_txt)
        self.btnFridgeTxt.setText('Холодильник в txt')
        self.btnDbTxt.setText('БД в txt')

        # обновление холодильника
        self.lstFresh.clear()
        self.lstTired.clear()
        self.lstOld.clear()

        result_fridge = cur.execute("""select * from fridge""").fetchall()
        # сортировка продуктов по дате
        result_fridge.sort(key=lambda x: x[2], reverse=True)

        for item in result_fridge:
            date_item = f'истекает {item[2].split("-")[2]}.' \
                        f'{item[2].split("-")[1]}.{item[2].split("-")[0]}'
            result_items = cur.execute(f"""select item, image from items
                                            where id = {item[1]}""").fetchall()
            name = result_items[0][0]
            image = result_items[0][1]

            timedelta1 = dt.timedelta(days=2)
            timedelta2 = dt.timedelta(days=0)
            today = dt.date.today()
            item_day = dt.date(int(item[2].split("-")[0]),
                               int(item[2].split("-")[1]),
                               int(item[2].split("-")[2]))

            # добавление изображения продукта в списке
            item_widget = QListWidgetItem(f'{name}, {date_item}')
            item_widget.setIcon(QIcon(image))

            if item_day - today > timedelta1:
                self.lstFresh.addItem(item_widget)
            elif timedelta2 <= item_day - today <= timedelta1:
                self.lstTired.addItem(item_widget)
            elif timedelta2 > item_day - today:
                self.lstOld.addItem(item_widget)

        con.close()

    def convert_fridge_to_txt(self):  # конвертировать холодильник в txt
        self.btnFridgeTxt.setText('Холодильник в txt')

        con = sqlite3.connect("items_db.sqlite")
        cur = con.cursor()

        result_fridge = cur.execute("""select * from fridge""").fetchall()
        result_fridge.sort(key=lambda x: x[2], reverse=True)

        lst_fresh = []
        lst_tired = []
        lst_old = []

        for item in result_fridge:
            date_item = f'истекает {item[2].split("-")[2]}.' \
                        f'{item[2].split("-")[1]}.{item[2].split("-")[0]}'
            result_items = cur.execute(f"""select item from items
                                           where id = {item[1]}""").fetchall()
            name = result_items[0][0]

            timedelta1 = dt.timedelta(days=2)
            timedelta2 = dt.timedelta(days=0)
            today = dt.date.today()
            item_day = dt.date(int(item[2].split("-")[0]),
                               int(item[2].split("-")[1]),
                               int(item[2].split("-")[2]))

            if item_day - today > timedelta1:
                lst_fresh.append(f'{name}, {date_item}\n')
            elif timedelta2 <= item_day - today <= timedelta1:
                lst_tired.append(f'{name}, {date_item}\n')
            elif timedelta2 > item_day - today:
                lst_old.append(f'{name}, {date_item}\n')

        # вывод диалога выбора папки сохранения txt
        dir_name = QFileDialog.getExistingDirectory(self,
                                                    "Выберите папку для "
                                                    "сохранения файла",
                                                    ".")

        if dir_name != '':
            f = open(f"{dir_name}/Холодильник.txt", 'w', encoding="utf8")

            f.write(
                f'В холодильнике {len(result_fridge)} продуктов питания\n\n\n')

            f.write('Срок годности пока не истекает:\n\n')
            if lst_fresh:
                for i, line in enumerate(lst_fresh):
                    f.write(f'{i + 1}) {line}')
            else:
                f.write('Нет\n')

            f.write('\n\nСрок годности истечёт через 1-2 дня:\n\n')
            if lst_tired:
                for i, line in enumerate(lst_tired):
                    f.write(f'{i + 1}) {line}')
            else:
                f.write('Нет\n')

            f.write('\n\nСрок годности истёк:\n\n')
            if lst_old:
                for i, line in enumerate(lst_old):
                    f.write(f'{i + 1}) {line}')
            else:
                f.write('Нет\n')

            f.close()

            # отображение успешного выполнения конвертации
            self.btnFridgeTxt.setText('Холодильник в txt ✔')

        con.close()

    def convert_db_to_txt(self):  # конвертировать БД в txt
        self.btnDbTxt.setText('БД в txt')

        con = sqlite3.connect("items_db.sqlite")
        cur = con.cursor()

        result_bd = cur.execute("""select * from items""").fetchall()

        # вывод диалога выбора папки сохранения txt
        dir_name = QFileDialog.getExistingDirectory(self,
                                                    "Выберите папку для "
                                                    "сохранения файла",
                                                    ".")

        if dir_name != '':
            f = open(f"{dir_name}/База данных.txt", 'w', encoding="utf8")

            f.write(f'В базе данных {len(result_bd)} продуктов питания\n\n')

            if result_bd:
                for i, line in enumerate(result_bd):
                    f.write(
                        f'{i + 1}) {line[1]}, id: {line[0]}, '
                        f'изображение: {line[2]}\n')
            else:
                f.write('Продуктов нет\n')

            f.close()

            # отображение успешного выполнения конвертации
            self.btnDbTxt.setText('БД в txt ✔')

        con.close()

    def clear(self):  # удалить просроченные
        self.lstOld.clear()

        con = sqlite3.connect("items_db.sqlite")
        cur = con.cursor()

        result_fridge = cur.execute("""select * from fridge""").fetchall()

        for item in result_fridge:
            timedelta = dt.timedelta(days=0)
            today = dt.date.today()
            item_day = dt.date(int(item[2].split("-")[0]),
                               int(item[2].split("-")[1]),
                               int(item[2].split("-")[2]))

            if timedelta > item_day - today:
                cur.execute(f"""delete from fridge
                                where id = {item[0]}""").fetchall()

        con.commit()
        con.close()

        self.update_fridge()

    def open_change_fridge_form(self):  # изменить холодильник
        con = sqlite3.connect("items_db.sqlite")
        cur = con.cursor()
        result_fridge = cur.execute("""select * from fridge""").fetchall()
        con.close()

        if result_fridge:
            self.change_fridge_form = ChangeFridgeForm(
                self)  # форма изменения продукта в холодильнике
            self.change_fridge_form.show()
        else:
            # вызов окна ошибки открытия
            self.message = QMessageBox.warning(self, "Ошибка",
                                               "Холодильник пуст!")
            self.show()

    def open_change_db_form(self):  # изменить БД
        con = sqlite3.connect("items_db.sqlite")
        cur = con.cursor()
        result_items = cur.execute("""select * from items""").fetchall()
        con.close()

        if result_items:
            self.change_db_form = ChangeDbForm(
                self)  # форма изменения продукта в БД
            self.change_db_form.show()
        else:
            # вызов окна ошибки открытия
            self.message = QMessageBox.warning(self, "Ошибка",
                                               "В базе данных ничего нет!")
            self.show()

    def choose(self):  # добавить известный
        con = sqlite3.connect("items_db.sqlite")
        cur = con.cursor()
        result = cur.execute("""select id, item from items""").fetchall()
        items = tuple(
            map(lambda x: ') '.join(list(map(lambda y: str(y), x))), result))

        if items:
            # вызов диалога выбора продукта из базы данных
            item, ok_pressed_item = QInputDialog.getItem(
                self, "Выберите продукт", "Какой продукт хотите добавить?",
                items, 0, False)

            if ok_pressed_item:
                # вызов диалога ввода даты
                date, ok_pressed_date = QInputDialog.getText(self,
                                                             "Введите дату",
                                                             "Когда "
                                                             "кончается срок "
                                                             "годности (в "
                                                             "формате "
                                                             "ДД.ММ.ГГГГ)?")
                try:
                    # проверка даты
                    date = date.split('.')
                    if 31 < int(date[0]) or int(date[0]) < 1 or len(
                            date[0]) != 2:
                        raise ValueError
                    if 12 < int(date[1]) or int(date[1]) < 1 or len(
                            date[1]) != 2:
                        raise ValueError
                    if 1752 > int(date[2]) or int(date[2]) > 9999 or len(
                            date[2]) != 4:
                        raise ValueError
                    check = dt.date(int(date[2]), int(date[1]), int(date[0]))
                    id_item = int(item.split(') ')[0])
                    date_item = '-'.join(date[::-1])
                    cur.execute(f"""insert into fridge(item, date)
                                    values('{id_item}',
                                           '{date_item}')""").fetchall()
                except ValueError:
                    # вызов окна ошибки даты
                    self.message = QMessageBox.warning(self, "Ошибка",
                                                       "Неверный формат даты!")
                    self.show()
        else:
            # вызов окна ошибки выбора
            self.message = QMessageBox.warning(self, "Ошибка",
                                               "В базе данных нет продуктов!")
            self.show()

        con.commit()
        con.close()

        form.update_fridge()

    def open_new_item_form(self):  # добавить новый
        self.new_item_form = NewItemForm(
            self)  # форма добавления нового продукта
        self.new_item_form.show()


class InstructionForm(QWidget, Ui_Instruction_Form):
    """Класс окна инструкции по работе с программой."""

    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(400, 400)
        self.setWindowIcon(QIcon('icon2.ico'))
        self.textBrowser.setStyleSheet(
            'border: 0px solid black; background-color: rgb(255, 255, 255, 0)')


class SettingsForm(QWidget, Ui_Settings_Form):
    """Класс окна настройки цветов у блоков основного окна, отображающих
    продукты. """

    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(300, 160)
        self.setWindowIcon(QIcon('icon3.ico'))

        # загрузка цветов блоков
        con = sqlite3.connect("items_db.sqlite")
        cur = con.cursor()
        result_one = cur.execute("""select first from colors""").fetchall()
        result_two = cur.execute("""select second from colors""").fetchall()
        result_three = cur.execute("""select third from colors""").fetchall()
        con.close()
        self.btn1.setStyleSheet(f'background-color: {result_one[0][0]}')
        self.btn2.setStyleSheet(f'background-color: {result_two[0][0]}')
        self.btn3.setStyleSheet(f'background-color: {result_three[0][0]}')

        self.btnDefault.clicked.connect(self.set_default_colors)
        self.buttonGroup.buttonClicked.connect(self.set_color)

        form.update_fridge()

    def set_color(self, btn):  # изменить цвет
        # вызов диалога выбора цвета
        color = QColorDialog.getColor()

        if color.isValid():
            btn.setStyleSheet(f'background-color: {color.name()}')

            con = sqlite3.connect("items_db.sqlite")
            cur = con.cursor()
            if btn.objectName() == 'btn1':
                cur.execute(
                    f"""update colors
                        set first = '{color.name()}'""").fetchall()
            elif btn.objectName() == 'btn2':
                cur.execute(
                    f"""update colors
                        set second = '{color.name()}'""").fetchall()
            elif btn.objectName() == 'btn3':
                cur.execute(
                    f"""update colors
                        set third = '{color.name()}'""").fetchall()
            con.commit()
            con.close()

        form.update_fridge()

    def set_default_colors(self):  # сбросить цвета
        self.btn1.setStyleSheet('background-color: #98fb98')
        self.btn2.setStyleSheet('background-color: #fffacd')
        self.btn3.setStyleSheet('background-color: #f08080')

        con = sqlite3.connect("items_db.sqlite")
        cur = con.cursor()
        cur.execute("""update colors
                       set first = '#98fb98',
                           second = '#fffacd',
                           third = '#f08080'""").fetchall()
        con.commit()
        con.close()

        form.update_fridge()


class NewItemForm(QWidget, Ui_New_Item_Form):
    """Класс окна добавления нового продукта питания."""

    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(340, 180)
        self.setWindowIcon(QIcon('icon4.ico'))

        # стандартное изображение продукта
        self.image_name = 'image/default.png'
        # установление сегодняшеней даты
        self.date.setDate(
            QtCore.QDate.fromString(str(dt.date.today()), 'yyyy-MM-dd'))

        self.btnImage.clicked.connect(self.select_image)
        self.btnAdd.clicked.connect(self.add_item)

    def select_image(self):  # выбрать изображение продукта
        # вызов диалога выбора изображения продукта
        self.image_name = QFileDialog.getOpenFileName(
            self, 'Выбрать изображение', '',
            'PNG-image (*.png);;JPG-image (*.jpg);;Все файлы (*)')[0]

        if self.image_name != 'image/default.png' and self.image_name != '':
            # отображение успешного выполнения выбора
            self.btnImage.setStyleSheet(f'background-color: #98fb98')

    def add_item(self):  # добавить новый продукт в БД и холодильник
        name = self.title.text()

        con = sqlite3.connect("items_db.sqlite")
        cur = con.cursor()

        cur.execute(f"""insert into items(item, image)
                        values('{name}', 'image/default.png')""").fetchall()
        id_item = cur.execute(f"""select id from items where item = '{name}'
                        and image = 'image/default.png'""").fetchall()[0][0]

        # если нет названия продукта, присваивается стандартное «Продукт №%»
        if name == '':
            cur.execute(f"""update items set item = 'Продукт №{id_item}'
            where id = {id_item}""").fetchall()

        # если нет изображения пользователья, присваивается стандартное
        if self.image_name != 'image/default.png' and self.image_name != '':
            im = Image.open(self.image_name)
            im_new = im.resize((512, 512))
            im_new.save(f'image/{id_item}.png', 'PNG', optimize=True)
            cur.execute(f"""update items
                                set image = 'image/{id_item}.png'
                                where id = {id_item}""").fetchall()

        cur.execute(f"""insert into fridge(item, date)
                        values('{id_item}',
                '{self.date.dateTime().toString('yyyy-MM-dd')}')""").fetchall()

        con.commit()
        con.close()

        form.update_fridge()

        self.close()


class ChangeDbForm(QWidget, Ui_Change_Db_Form):
    """Класс окна изменения БД."""

    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(340, 230)
        self.setWindowIcon(QIcon('icon5.ico'))

        self.btnSave.clicked.connect(self.save)
        self.btnDelete.clicked.connect(self.delete)
        self.btnChange.clicked.connect(self.change_image)
        self.btnDefault.clicked.connect(self.default_image)
        self.title.activated[str].connect(self.choice_item)

        con = sqlite3.connect("items_db.sqlite")
        cur = con.cursor()

        # добавление продуктов в QComboBox
        result_fridge = cur.execute("""select * from items""").fetchall()

        for item in result_fridge:
            id_item = item[0]
            name_item = item[1]
            image_item = item[2]

            self.title.addItem(QIcon(image_item), f'[{id_item}] {name_item}')

        # загрузка данных продукта
        self.choice_item(self.title.itemText(0))
        self.item = self.title.itemText(0)

        # загрузка данных изображения
        self.im = cur.execute(f"""select image from items where id =
                            {int(self.item.split()[0].lstrip('[').rstrip(']'))}
                                                        """).fetchall()[0][0]
        self.pixmap = QPixmap(self.im).scaled(
            self.image.size())  # изменение размера изображения

        con.close()

    def save(self):  # сохранение в БД
        id_item = int(self.item.split()[0].lstrip('[').rstrip(']'))

        con = sqlite3.connect("items_db.sqlite")
        cur = con.cursor()

        cur.execute(f"""update items set item = '{self.name.text()}'
                        where id = {id_item}""").fetchall()

        if self.im != 'image/default.png' and self.im != '':
            im = Image.open(self.im)
            im_new = im.resize((512, 512))
            im_new.save(f'image/{id_item}.png', 'PNG', optimize=True)
            cur.execute(f"""update items
                                set image = 'image/{id_item}.png'
                                where id = {id_item}""").fetchall()

        elif self.im == 'image/default.png':
            cur.execute(f"""update items
                                set image = 'image/default.png'
                                where id = {id_item}""").fetchall()

            # удаление старого изображения
            try:
                file_path = f'image/{id_item}.png'
                os.remove(file_path)
            except FileNotFoundError:
                pass

        con.commit()
        con.close()

        form.update_fridge()

        self.close()

    def delete(self):  # удаление из БД
        con = sqlite3.connect("items_db.sqlite")
        cur = con.cursor()

        cur.execute(f"""delete from fridge where item =
            {int(self.item.split()[0].lstrip('[').rstrip(']'))}""").fetchall()
        cur.execute(f"""delete from items
                        where id =
                        {int(self.item.split()[0].lstrip('[').rstrip(']'))}
                                                            """).fetchall()

        if self.im != 'image/default.png' and self.im != '':
            # удаление старого изображения
            f_path = f'image/' \
                     f'{int(self.item.split()[0].lstrip("[").rstrip("]"))}.png'
            os.remove(f_path)

        con.commit()
        con.close()

        form.update_fridge()

        self.close()

    def change_image(self):  # выбрать новое изображение
        # вызов диалога выбора изображения продукта
        self.im = QFileDialog.getOpenFileName(
            self, 'Выбрать изображение', '',
            'PNG-image (*.png);;JPG-image (*.jpg);;Все файлы (*)')[0]

        if self.im != '':
            self.pixmap = QPixmap(self.im).scaled(
                self.image.size())  # изменение размера изображения
            self.image.setPixmap(self.pixmap)

    def default_image(self):  # выбрать стандартное изображение
        self.im = 'image/default.png'
        self.pixmap = QPixmap(self.im).scaled(
            self.image.size())  # изменение размера изображения
        self.image.setPixmap(self.pixmap)

    def choice_item(self, item):  # выбрать продукт из списка
        self.item = item

        self.name.setText(' '.join(self.item.split()[1:]).rstrip(','))

        con = sqlite3.connect("items_db.sqlite")
        cur = con.cursor()
        self.im = cur.execute(f"""select image from items
                                  where id =
                            {int(self.item.split()[0].lstrip('[').rstrip(']'))}
                                                        """).fetchall()[0][0]
        self.pixmap = QPixmap(self.im).scaled(
            self.image.size())  # изменение размера изображения
        self.image.setPixmap(self.pixmap)
        con.close()


class ChangeFridgeForm(QWidget, Ui_Change_Fridge_Form):
    """Класс окна изменения холодильника."""

    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(340, 140)
        self.setWindowIcon(QIcon('icon5.ico'))

        self.btnSave.clicked.connect(self.save)
        self.btnDelete.clicked.connect(self.delete)
        self.title.activated[str].connect(self.choice_item)

        con = sqlite3.connect("items_db.sqlite")
        cur = con.cursor()

        # добавление продуктов в QComboBox
        result_fridge = cur.execute("""select * from fridge""").fetchall()
        result_fridge.sort(key=lambda x: x[2], reverse=True)

        for item in result_fridge:
            id_item = item[0]
            date_item = f'истекает {item[2].split("-")[2]}.' \
                f'{item[2].split("-")[1]}.{item[2].split("-")[0]}'
            result_items = cur.execute(f"""select item, image from items
                                            where id = {item[1]}""").fetchall()
            name = result_items[0][0]
            image = result_items[0][1]

            self.title.addItem(QIcon(image),
                               f'[{id_item}] {name}, {date_item}')

        # загрузка данных продукта
        self.choice_item(self.title.itemText(0))
        self.item = self.title.itemText(0)

        con.close()

    def save(self):  # сохранение в холодильник
        con = sqlite3.connect("items_db.sqlite")
        cur = con.cursor()

        cur.execute(f"""update fridge
                        set date =
                                '{self.date.dateTime().toString('yyyy-MM-dd')}'
                        where id =
            {int(self.item.split()[0].lstrip('[').rstrip(']'))}""").fetchall()

        con.commit()
        con.close()

        form.update_fridge()

        self.close()

    def delete(self):  # удаление из холодильника
        con = sqlite3.connect("items_db.sqlite")
        cur = con.cursor()

        cur.execute(f"""delete from fridge
                        where id =
            {int(self.item.split()[0].lstrip('[').rstrip(']'))}""").fetchall()

        con.commit()
        con.close()

        form.update_fridge()

        self.close()

    def choice_item(self, item):  # выбрать продукт из списка
        self.item = item
        self.date.setDate(
            QtCore.QDate.fromString(self.item.split()[-1], 'dd.MM.yyyy'))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
