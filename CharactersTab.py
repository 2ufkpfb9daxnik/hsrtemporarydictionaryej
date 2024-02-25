from PySide6.QtWidgets import QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QFont

class CharactersTab(QWidget):
    def __init__(self):
        super().__init__()

        # タブのレイアウト
        character_layout = QVBoxLayout(self)
        character_table = QTableWidget()
        character_layout.addWidget(character_table)

        # リスト
        characters = [
                ('開拓者','Trailblazer'),
                ('三月なのか','March 7th'),
                ('丹恒','Dan Heng'),
                ('姫子','Himeko'),
                ('ヴェルト','Welt'),
                ('アーラン','Arlan'),
                ('アスター','Asta'),
                ('ヘルタ','Herta'),
                ('ブローニャ','Bronya'),
                ('ゼーレ','Seele'),
                ('セーバル','Serval'),
                ('ジェパード','Gepard'),
                ('ナターシャ','Natasha'),
                ('ペラ','Pela'),
                ('クラーラ','Clara'),
                ('サンポ','Sampo'),
                ('フック','Hook'),
                ('青雀','Qingque'),
                ('停雲','Tingyun'),
                ('景元','Jing Yuan'),
                ('素裳','Sushang'),
                ('彦卿','Yanqing'),
                ('白露','Bailu'),
                ('銀狼','Silver Wolf'),
                ('羅刹','Luocha'),
                ('御空','Yukong'),
                ('刃','Blade'),
                ('カフカ','Kafka'),
                ('ルカ','Luka'),
                ('符玄','Fu Xuan'),
                ('丹恒・飲月','Dan Heng・Imbibitor Lunae'),
                ('リンクス','Lynx'),
                ('鏡流','Jingliu'),
                ('トパーズ&カブ','Topaz & Numby'),
                ('桂乃芬','Guinaifen'),
                ('フォフォ','Huohuo'),
                ('アルジェンティ','Argenti'),
                ('寒鴉','Hanya'),
                ('ルアン・メェイ','Ruan Mei'),
                ('Dr.レイシオ','Dr. Ratio'),
                ('雪衣','Xueyi'),
                ('ブラックスワン','Black Swan'),
                ('花火','Sparkle'),
                ('ミーシャ','Misha'),
                ('黄泉','Acheron'),
                ('アベンチュリン','Aventurine'),
                ('ギャラガー','Gallagher')
        ]

        # テーブルウィジェットの設定
        character_table.setColumnCount(2)
        character_table.setRowCount(len(characters))

        for row, (character, japanese) in enumerate(characters):
            character_table.setItem(row, 0, QTableWidgetItem(character))
            character_table.setItem(row, 1, QTableWidgetItem(japanese))

        # 一番上の行と一番左の列を非表示にする
        character_table.verticalHeader().setVisible(False)
        character_table.horizontalHeader().setVisible(False)

        # 行と列の大きさを設定
        for i in range(len(characters)):
            character_table.setRowHeight(i, 100)  # 行の高さを100に設定
            character_table.setColumnWidth(0, 500)  # 日本語の列の幅を500に設定
            character_table.setColumnWidth(1, 1000)  # 英語の列の幅を1000に設定

        # フォントサイズを変更
        for row, (character, japanese) in enumerate(characters):
            item1 = QTableWidgetItem(character)
            item1.setFont(QFont('Arial', 60))  # フォントサイズを60に設定
            item2 = QTableWidgetItem(japanese)
            item2.setFont(QFont('Arial', 60))  # フォントサイズを60に設定
            character_table.setItem(row, 0, item1)
            character_table.setItem(row, 1, item2)

        character_layout.addWidget(character_table)