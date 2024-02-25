import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6_VerticalQTabWidget import VerticalQTabWidget
from PySide6.QtGui import QFont
import PySide6.QtCore
from CharactersTab import CharactersTab
from EnemiesTab import EnemiesTab 
from LightConeTab import LightConeTab
from RelicsTab import RelicsTab
from CombatTypeTab import CombatTypeTab
from PathTab import PathTab
from SimulatedUniverseTab import SimulatedUniverseTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('hsrtemporarydictionaryje2.0')

        # ウィンドウの位置をスクリーン中央に設定
        rect = PySide6.QtCore.QRect()
        rect.moveCenter(QApplication.primaryScreen().availableGeometry().center())
        self.setGeometry(rect) 

        tab_widget = VerticalQTabWidget()
        tab_widget.addTab(CharactersTab(), "キャラクター")
        tab_widget.addTab(EnemiesTab(), "敵")
        tab_widget.addTab(LightConeTab(), "光円錐")
        tab_widget.addTab(RelicsTab(), "遺物")
        tab_widget.addTab(CombatTypeTab(),"属性")
        tab_widget.addTab(PathTab(),"運命")
        tab_widget.addTab(SimulatedUniverseTab(), "模擬宇宙")

        font = QFont()
        font.setPointSize(40)  # フォントサイズを40に設定
        tab_widget.setFont(font)


        self.setCentralWidget(tab_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.showMaximized()
    sys.exit(app.exec())
