from PySide6.QtWidgets import QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QFont

class PathTab(QWidget):
    def __init__(self):
        super().__init__()

        # タブのレイアウト
        path_layout = QVBoxLayout(self)
        path_table = QTableWidget()
        path_layout.addWidget(path_table)

        # リスト
        paths = [
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
            ('秩序','Order')
        ]

        # テーブルウィジェットの設定
        path_table.setColumnCount(2)
        path_table.setRowCount(len(paths))

        for row, (path, japanese) in enumerate(paths):
            path_table.setItem(row, 0, QTableWidgetItem(path))
            path_table.setItem(row, 1, QTableWidgetItem(japanese))

        # 一番上の行と一番左の列を非表示にする
        path_table.verticalHeader().setVisible(False)
        path_table.horizontalHeader().setVisible(False)

        # 行と列の大きさを設定
        for i in range(len(paths)):
            path_table.setRowHeight(i, 100)  # 行の高さを100に設定
            path_table.setColumnWidth(0, 200)  # 日本語の列の幅を200に設定
            path_table.setColumnWidth(1, 600)  # 英語の列の幅を600に設定

        # フォントサイズを変更
        for row, (path, japanese) in enumerate(paths):
            item1 = QTableWidgetItem(path)
            item1.setFont(QFont('Arial', 60))  # フォントサイズを60に設定
            item2 = QTableWidgetItem(japanese)
            item2.setFont(QFont('Arial', 60))  # フォントサイズを60に設定
            path_table.setItem(row, 0, item1)
            path_table.setItem(row, 1, item2)

        path_layout.addWidget(path_table)