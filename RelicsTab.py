from PySide6.QtWidgets import QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QFont

class RelicsTab(QWidget):
    def __init__(self):
        super().__init__()

        # タブのレイアウト
        relics_layout = QVBoxLayout(self)
        relics_table = QTableWidget()
        relics_layout.addWidget(relics_table)

        # リスト
        relicss = [
                ('吹雪と対峙する兵士','Guard of Wuthering Snow'),
                ('成り上がりチャンピオン','Champion of Streetwise Boxing'),
                ('昼夜の狭間を翔ける鷹','Eagle of Twilight Line'),
                ('雷鳴轟くバンド','Band of Sizzling Thunder'),
                ('生命のウェンワーク','Sprightly Vonwacq'),
                ('流星の跡を追う怪盗','Thief of Shooting Meteor'),
                ('草の穂ガンマン','Musketeer of Wild Wheat'),
                ('流雲無痕の過客','Passerby of Wandering Cloud'),
                ('雪の密林の狩人','Hunter of Glacial Forest'),
                ('純庭教会の聖騎士','Knight of Purity Palace'),
                ('盗賊公国タリア','Talia: Kingdom of Banditry'),
                ('老いぬ者の仙舟','Fleet of the Ageless'),
                ('星のごとく輝く天才','Genius of Brilliant Stars'),
                ('汎銀河商事会社','Pan-Cosmic commerical Enterprise'),
                ('宇宙封印ステーション','Space Sealing Station'),
                ('荒地で盗みを働く腐土客','Wastelander of Banditry Desert'),
                ('天体階差機関','Celestial Differntiator'),
                ('溶岩で鍛造する火匠','Firesmith of Lava-Forging'),
                ('建創者のベロブルグ','Belobog of the Architects'),
                ('自転が止まったサルソット','Inert Salsotto'),
                ('折れた竜骨','Broken Keel'),
                ('宝命長存の蒔者','Longevous Disciple'),
                ('仮想空間を漫遊するメッセンジャー','Messenger Traversing Hackerspace'),
                ('星々の競技場','Rutilant Arena'),
                ('夢の地ピノコニー','Penacony Land of the Dreams'),
                ('蒼穹戦線グラモス','Firmament Frontline Glamoth'),
                ('深い牢獄の囚人','Prisoner in Deep Confinement'),
                ('灰燼を燃やし尽くす大公','The Ashblazing Grand Duke')
        ]

        # テーブルウィジェットの設定
        relics_table.setColumnCount(2)
        relics_table.setRowCount(len(relicss))

        for row, (relics, japanese) in enumerate(relicss):
            relics_table.setItem(row, 0, QTableWidgetItem(relics))
            relics_table.setItem(row, 1, QTableWidgetItem(japanese))

        # 一番上の行と一番左の列を非表示にする
        relics_table.verticalHeader().setVisible(False)
        relics_table.horizontalHeader().setVisible(False)

        # 行と列の大きさを設定
        for i in range(len(relicss)):
            relics_table.setRowHeight(i, 75)  # 行の高さを75に設定
            relics_table.setColumnWidth(0, 600)  # 日本語の列の幅を600に設定
            relics_table.setColumnWidth(1, 800)  # 英語の列の幅を800に設定

        # フォントサイズを変更
        for row, (relics, japanese) in enumerate(relicss):
            item1 = QTableWidgetItem(relics)
            item1.setFont(QFont('Arial', 30))  # フォントサイズを30に設定
            item2 = QTableWidgetItem(japanese)
            item2.setFont(QFont('Arial', 30))  # フォントサイズを30に設定
            relics_table.setItem(row, 0, item1)
            relics_table.setItem(row, 1, item2)

        relics_layout.addWidget(relics_table)