import sys
import datetime as dt
import PySide6.QtWidgets as Qw
import PySide6.QtCore as Qc
from PySide6.QtGui import QFont
from PySide6_VerticalQTabWidget import VerticalQTabWidget

# MainWindowクラス定義 ####
class MainWindow(Qw.QMainWindow):
  
    def __init__(self):
        super().__init__() 
        self.setWindowTitle('hsrdictionaryje') 

        # ウィンドウの位置をスクリーン中央に設定
        rect = Qc.QRect()
        rect.setSize(Qc.QSize(600,700))
        rect.moveCenter(Qw.QApplication.primaryScreen().availableGeometry().center())
        self.setGeometry(rect) 

        # レイアウトを作成
        layout = Qw.QVBoxLayout()

        # メインウィンドウのセントラルウィジェットにレイアウトを設定
        central_widget = Qw.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # ボタンを追加
        buttons = ['キャラクター', '光円錐', '遺物', '属性', '運命', '模擬宇宙']
        for button_text in buttons:
            button = Qw.QPushButton(button_text, self)
            # ボタンの高さを設定
            button.setFixedHeight(100)  # 100ピクセルの高さに設定
            # ボタンのフォントサイズを大きくする
            font = QFont()
            font.setPointSize(70)  # フォントサイズを70に設定
            button.setFont(font)
            layout.addWidget(button)
            # ボタンのclickedシグナルに対応するスロットを接続
            if button_text == 'キャラクター':
                button.clicked.connect(self.btn_Character_clicked)
            elif button_text == '光円錐':
                button.clicked.connect(self.btn_LightCone_clicked)
            elif button_text == '遺物':
                button.clicked.connect(self.btn_Relics_clicked)
            elif button_text == '属性':
                button.clicked.connect(self.btn_CombatType_clicked)
            elif button_text == '運命':
                button.clicked.connect(self.btn_Path_clicked)
            elif button_text == '模擬宇宙':
                button.clicked.connect(self.btn_SimulatedUniverse_clicked)

    # ボタンがクリックされたときのコールバック関数
    def btn_Character_clicked(self):
        self.character_window = CharacterWindow()
        self.character_window.show()

    def btn_LightCone_clicked(self):
        self.light_cone_window = LightConeWindow()
        self.light_cone_window.show()

    def btn_Relics_clicked(self):
        self.Relics_window = RelicsWindow()
        self.Relics_window.show()

    def btn_CombatType_clicked(self):
        self.combat_type_window = CombatTypeWindow()
        self.combat_type_window.show()

    def btn_Path_clicked(self):
        self.path_window = PathWindow()
        self.path_window.show()

    def btn_SimulatedUniverse_clicked(self):
        self.simulated_universe_window = SimulatedUniverseWindow()
        self.simulated_universe_window.show()

# キャラクターウィンドウクラス定義
class CharacterWindow(Qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("キャラクター(Character)")

        # ウィンドウの位置をスクリーン中央に設定
        rect = Qc.QRect()
        rect.setSize(Qc.QSize(640,480))
        rect.moveCenter(Qw.QApplication.primaryScreen().availableGeometry().center())
        self.setGeometry(rect) 

# 光円錐ウィンドウクラス定義
class LightConeWindow(Qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("光円錐(Light Cone)")

        # ウィンドウの位置をスクリーン中央に設定
        rect = Qc.QRect()
        rect.setSize(Qc.QSize(640,480))
        rect.moveCenter(Qw.QApplication.primaryScreen().availableGeometry().center())
        self.setGeometry(rect) 

# 遺物ウィンドウクラス定義
class RelicsWindow(Qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("遺物(Relics)")

        # ウィンドウの位置をスクリーン中央に設定
        rect = Qc.QRect()
        rect.setSize(Qc.QSize(640,480))
        rect.moveCenter(Qw.QApplication.primaryScreen().availableGeometry().center())
        self.setGeometry(rect) 

# 属性ウィンドウクラス定義
class CombatTypeWindow(Qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("属性(Combat Type)")
        self.setFixedSize(430, 450)  # ウィンドウの固定サイズを設定

        # 表示する属性と対応する日本語のリスト
        attributes = [
            ('量子', 'Quantum'),
            ('物理', 'Physical'),
            ('風', 'Wind'),
            ('炎', 'Fire'),
            ('虚数', 'Imaginary'),
            ('雷', 'Lightning'),
            ('氷', 'Ice')
        ]

        # テーブルウィジェットを作成
        table_widget = Qw.QTableWidget()
        table_widget.setColumnCount(2)
        table_widget.setRowCount(len(attributes))

        # セルの幅と高さを設定
        for row in range(len(attributes)):
            table_widget.setRowHeight(row, 60)  # 行の高さを60に設定
            for col in range(2):
                table_widget.setColumnWidth(col, 200)  # 列の幅を200に設定

        for row, (attribute, japanese) in enumerate(attributes):
            table_widget.setItem(row, 0, Qw.QTableWidgetItem(attribute))
            table_widget.setItem(row, 1, Qw.QTableWidgetItem(japanese))

        # 一番左側の行、一番上列のを非表示にする
        table_widget.verticalHeader().setVisible(False)
        table_widget.horizontalHeader().setVisible(False)
        
        # テーブルウィジェットのフォントサイズを設定
        font = QFont()
        font.setPointSize(30)  # フォントサイズを16に設定
        table_widget.setFont(font)

        # レイアウトを作成し、テーブルウィジェットを配置
        layout = Qw.QVBoxLayout()
        layout.addWidget(table_widget)
        self.setLayout(layout)

# 運命ウィンドウクラス定義
class PathWindow(Qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("運命(Path)")

        # ウィンドウの位置をスクリーン中央に設定
        rect = Qc.QRect()
        rect.setSize(Qc.QSize(640,480))
        rect.moveCenter(Qw.QApplication.primaryScreen().availableGeometry().center())
        self.setGeometry(rect) 

        # 表示する運命と対応する日本語のリスト
        attributes = [
            ('壊滅','Destruction'),
            ('巡狩','Hunt'),
            ('知恵','Erudition'),
            ('調和','Harmony'),
            ('虚無','Nihility'),
            ('存護','Preservation'),
            ('豊穣','Abundance'),
            ('記憶','Remembrance'),
            ('愉悦','Elation'),
            ('繁殖','Propagation'),
            ('開拓','Trailblaze'),
            ('貪欲','Voracity'),
            ('純美','Beauty'),
            ('不朽','Permanence'),
            ('神秘','Enigmata'),
            ('均衡','Equilibrium'),
            ('終焉','Finality'),
            ('秩序','Order'),
        ]

        # テーブルウィジェットを作成
        table_widget = Qw.QTableWidget()
        table_widget.setColumnCount(2)
        table_widget.setRowCount(len(attributes))

        # セルの幅と高さを設定
        for row in range(len(attributes)):
            table_widget.setRowHeight(row, 60)  # 行の高さを60に設定
            for col in range(2):
                table_widget.setColumnWidth(col, 290)  # 列の幅を300に設定

        for row, (attribute, japanese) in enumerate(attributes):
            table_widget.setItem(row, 0, Qw.QTableWidgetItem(attribute))
            table_widget.setItem(row, 1, Qw.QTableWidgetItem(japanese))

        # 一番左側の行、一番上列のを非表示にする
        table_widget.verticalHeader().setVisible(False)
        table_widget.horizontalHeader().setVisible(False)
        
        # テーブルウィジェットのフォントサイズを設定
        font = QFont()
        font.setPointSize(30)  # フォントサイズを16に設定
        table_widget.setFont(font)

        # レイアウトを作成し、テーブルウィジェットを配置
        layout = Qw.QVBoxLayout()
        layout.addWidget(table_widget)
        self.setLayout(layout)

# 模擬宇宙ウィンドウクラス定義
class SimulatedUniverseWindow(Qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("模擬宇宙(Simulated Universe)")

        # ウィンドウの位置をスクリーン中央に設定
        rect = Qc.QRect()
        rect.setSize(Qc.QSize(640,480))
        rect.moveCenter(Qw.QApplication.primaryScreen().availableGeometry().center())
        self.setGeometry(rect) 


# 本体
if __name__ == '__main__':
    app = Qw.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
