from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic
from faker import Faker
from Settings import *
import sys
from pathlib import Path

class App(QMainWindow):

    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Anonymous in the Web')
        uic.loadUi(Path(__file__).parent / 'main.ui', self)
        
        # Храним состояние блокировки
        self.fields_locked = {
            'FirstName': False,
            'SecondName': False
        }
        
        # Настройки генерации
        self.faker = Faker()
        self.gender = None
        
        # Подключаем кнопки
        self.generate.clicked.connect(self.generate_names)
        self.settings_button.triggered.connect(self.open_settings)
        
        # Вешаем обработчики кликов
        self.FirstName.mousePressEvent = lambda e: self.toggle_lock('FirstName')
        self.SecondName.mousePressEvent = lambda e: self.toggle_lock('SecondName')

    def generate_names(self):
        """Генерация новых имен с учетом блокировок"""
        if not self.fields_locked['FirstName']:
            first_name = self._generate_first_name()
            self.FirstName.setText(first_name)
            
        if not self.fields_locked['SecondName']:
            last_name = self._generate_last_name()
            self.SecondName.setText(last_name)
        
        print(f"{self.FirstName.text()} {self.SecondName.text()}")

    def _generate_first_name(self):
        """Генерация имени с учетом пола"""
        if self.gender == 'female':
            return self.faker.first_name_female()
        elif self.gender == 'male':
            return self.faker.first_name_male()
        return self.faker.first_name()

    def _generate_last_name(self):
        """Генерация фамилии с учетом пола"""
        if self.gender == 'female':
            return self.faker.last_name_female()
        elif self.gender == 'male':
            return self.faker.last_name_male()
        return self.faker.last_name()

    def toggle_lock(self, field_name):
        """Переключение блокировки поля"""
        self.fields_locked[field_name] = not self.fields_locked[field_name]
        label = getattr(self, field_name)
        
        # Меняем цвет текста
        color = QApplication.palette().color(
            QPalette.ColorRole.Highlight if self.fields_locked[field_name] 
            else QPalette.ColorRole.WindowText
        )
        label.setStyleSheet(f"color: {color.name()};")

    def open_settings(self):
        """Открытие окна настроек"""
        dialog = Settings(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            region, self.gender = dialog.get_settings()
            if region:
                self.faker = Faker(region)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = App()
    window.show()
    sys.exit(app.exec())