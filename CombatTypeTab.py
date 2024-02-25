from PySide6.QtWidgets import QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QFont

class CombatTypeTab(QWidget):
    def __init__(self):
        super().__init__()

        # タブのレイアウト
        combat_type_layout = QVBoxLayout(self)
        combat_type_table = QTableWidget()
        combat_type_layout.addWidget(combat_type_table)

        # リスト
        combat_types = [
            ('量子', 'Quantum'),
            ('物理', 'Physical'),
            ('風', 'Wind'),
            ('炎', 'Fire'),
            ('虚数', 'Imaginary'),
            ('雷', 'Lightning'),
            ('氷', 'Ice')
        ]

        # テーブルウィジェットの設定
        combat_type_table.setColumnCount(2)
        combat_type_table.setRowCount(len(combat_types))

        for row, (combat_type, japanese) in enumerate(combat_types):
            combat_type_table.setItem(row, 0, QTableWidgetItem(combat_type))
            combat_type_table.setItem(row, 1, QTableWidgetItem(japanese))

        # 一番上の行と一番左の列を非表示にする
        combat_type_table.verticalHeader().setVisible(False)
        combat_type_table.horizontalHeader().setVisible(False)

        # の行と列の大きさを設定
        for i in range(len(combat_types)):
            combat_type_table.setRowHeight(i, 100)  # 行の高さを100に設定
            combat_type_table.setColumnWidth(0, 200)  # 日本語の列の幅を200に設定
            combat_type_table.setColumnWidth(1, 600)  # 英語の列の幅を600に設定

        # フォントサイズを変更
        for row, (combat_type, japanese) in enumerate(combat_types):
            item1 = QTableWidgetItem(combat_type)
            item1.setFont(QFont('Arial', 60))  # フォントサイズを60に設定
            item2 = QTableWidgetItem(japanese)
            item2.setFont(QFont('Arial', 60))  # フォントサイズを60に設定
            combat_type_table.setItem(row, 0, item1)
            combat_type_table.setItem(row, 1, item2)

        combat_type_layout.addWidget(combat_type_table)