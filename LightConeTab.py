from PySide6.QtWidgets import QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QFont

class LightConeTab(QWidget):
    def __init__(self):
        super().__init__()

        # タブのレイアウト
        light_cone_layout = QVBoxLayout(self)
        light_cone_table = QTableWidget()
        light_cone_layout.addWidget(light_cone_table)

        # リスト
        light_cones = [
                ('矢じり','Arrows'),
                ('物穣','Cornucopia'),
                ('天傾','Collapsing Sky'),
                ('琥珀','Amber'),
                ('幽邃','Void'),
                ('斉頌','Chorus'),
                ('アーカイブ','Data Bank'),
                ('離弦','Darting Arrow'),
                ('嘉果','Fine Fruit'),
                ('楽壊','Shattered Home'),
                ('防衛','Defense'),
                ('淵環','Loop'),
                ('輪契','Meshing Cogs'),
                ('霊鍵','Passkey'),
                ('手術後の会話','Post-Op Conversation'),
                ('お休みなさいと寝顔','Good Night and Sleep Well'),
                ('余生の初日','Day One of My New Life'),
                ('沈黙のみ','Only Silence Remains'),
                ('記憶の中の姿','Memories of the Past'),
                ('モグラ党へようこそ','The Moles Welcome You'),
                ('「私」の誕生','The Birth of the Self'),
                ('同じ気持ち','Shared Feeling'),
                ('獲物の視線','Eyes of the prey'),
                ('ランドゥーの選択',"Landau's Choice"),
                ('論剣','Swordplay'),
                ('惑星との出会い','Planetary Redezvous'),
                ('秘密の誓い','A Secret Vow'),
                ('この世界に喧騒を','Make the World Clamor'),
                ('ワン！散歩の時間！','Woof! Walk Time!'),
                ('朝食の儀式感','The Seriousness of Breakfast'),
                ('暖かい夜は長くない','Warmth Shortens Cold Nights'),
                ('またお会いしましょう','We Will Meet Again'),
                ('これがウチだよ！','This Is Me!'),
                ('幽冥に帰す','Return to Darkness'),
                ('彫月裁雲の意','Crave the Moon, Weave the Clouds'),
                ('逃げ場なし','Nowhere to Run'),
                ('今日も平和な一日','Today Is Another Peaceful Day'),
                ('銀河鉄道の夜','Night on the Milky Way'),
                ('夜の帳の中で','In the Night'),
                ('かけがえのないもの','Something Irreplaceable'),
                ('だが戦争は終わらない',"But The Battle Isn't Over"),
                ('世界の名を以て','In the Name of the World'),
                ('勝利の刹那','Moment of Vivtory'),
                ('夜明け前','Before Dawn'),
                ('泥の如き眠り','Sleep Like The Dead'),
                ('時節は居らず','Time Waits for No One'),
                ('とある星神の殞落を記す','On the Fall of an Aeon'),
                ('星海巡航','Crusing in the Stellar Sea'),
                ('記憶の素材','Texture of Memories'),
                ('今がちょうど','Perfect Timing'),
                ('決意は汗のように輝く','Resolution Shines As Pearls of Sweat'),
                ('星間市場のトレンド','Trend of the Universal Market'),
                ('フォローして！','Subscribe for More!'),
                ('ダンス！ダンス！ダンス！','Dance! Dance! Dance!'),
                ('青空の下で','Under the Blue Sky'),
                ('天才たちの休息',"Geniuses' Repose"),
                ('等価交換','Quid Pro Quo'),
                ('フェルマータ','Fermata'),
                ('我ら地炎','We Are Wildfire'),
                ('春水に初生する','River Flows in Spring'),
                ('過去と未来','Past and Future'),
                ('相抗','Adversarial'),
                ('見識','Sagacity'),
                ('新天地','Pioneering'),
                ('蕃殖','Multiplication'),
                ('同調','Mediation'),
                ('倶歿','Mutual Demise'),
                ('匿影','Hidden Shadow'),
                ('降り止まぬ雨','Incessant Rain'),
                ('棺のこだま','Echoes of the Coffin'),
                ('初めてのクエストの前に','Before the Tutorial Mission Starts'),
                ('着かない彼岸','The Unreachable Side'),
                ('待つのみ','Patience Is All You Need'),
                ('陽光より輝くもの','Brighter Then the Sun'),
                ('閉ざした瞳','She Already Shut Her Eyes'),
                ('孤独の癒やし','Solitary Healing'),
                ('悩んで笑って','Worrisome, Blissful'),
                ('この身は剣なり','I Shall Be My Own Sword'),
                ('その一刻、目に焼き付けて','As Instant Before A Gaze'),
                ('よぉ、ここにいるぜ','Hey Over Here'),
                ('驚魂の夜','Night of Fright'),
                ('鏡の中の私','Past Self in Mirror'),
                ('純粋なる思惟の洗礼','Baptism of Pure Thought'),
                ('何が真か','What Is Real?'),
                ('ドリームタウンの大冒険','Dreamville Adventure'),
                ('最後の勝者','Final Victor'),
                ('烈火の彼方','Flames Afar'),
                ('運命を紡ぐ糸',"Destiny's Threads Forewoven"),
                ('銀河が陥落した日','The Day The Cosmos Fell'),
                ('ショーの始まり',"It's Showtime"),
                ('心に刻まれた約束','Indelible Promise'),
                ('人生は遊び','Earthly Escapade'),
                ('時間の記憶を再構築して','Reforged Remenbarance')
        ]

        # テーブルウィジェットの設定
        light_cone_table.setColumnCount(2)
        light_cone_table.setRowCount(len(light_cones))

        for row, (light_cone, japanese) in enumerate(light_cones):
            light_cone_table.setItem(row, 0, QTableWidgetItem(light_cone))
            light_cone_table.setItem(row, 1, QTableWidgetItem(japanese))

        # 一番上の行と一番左の列を非表示にする
        light_cone_table.verticalHeader().setVisible(False)
        light_cone_table.horizontalHeader().setVisible(False)

        # 行と列の大きさを設定
        for i in range(len(light_cones)):
            light_cone_table.setRowHeight(i, 75)  # 行の高さを75に設定
            light_cone_table.setColumnWidth(0, 500)  # 日本語の列の幅を500に設定
            light_cone_table.setColumnWidth(1, 900)  # 英語の列の幅を900に設定

        # フォントサイズを変更
        for row, (light_cone, japanese) in enumerate(light_cones):
            item1 = QTableWidgetItem(light_cone)
            item1.setFont(QFont('Arial', 30))  # フォントサイズを30に設定
            item2 = QTableWidgetItem(japanese)
            item2.setFont(QFont('Arial', 30))  # フォントサイズを30に設定
            light_cone_table.setItem(row, 0, item1)
            light_cone_table.setItem(row, 1, item2)

        light_cone_layout.addWidget(light_cone_table)