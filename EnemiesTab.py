from PySide6.QtWidgets import QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QFont

class EnemiesTab(QWidget):
    def __init__(self):
        super().__init__()

        # タブのレイアウト
        enemy_layout = QVBoxLayout(self)
        enemy_table = QTableWidget()
        enemy_layout.addWidget(enemy_table)

        # リスト
        enemys = [
                ('シルバーメイン・狙撃手',"Silvermane Gunner"),
                ('シルバーメイン・近衛',"Silvermane Soldier"),
                ('流浪者',"Vagrant"),
                ('シルバーメイン・尉官',"Silvermane Lieutenant"),
                ('シルバーメイン・砲兵',"Silvermane Cannoneer"),
                ('カカリア',"Cocolia"),
                ('ジェパード',"Gepard"),
                ('ブローニャ',"Bronya"),
                ('スヴァローグ',"Svarog"),
                ('自動機兵・サバーカ',"Automaton Hound"),
                ('カカリア・虚妄の母',"Cocolia, Mother of Deception"),
                ('自動機兵・グリズリー',"Automaton Grizzly"),
                ('自動機兵・ジューク',"Automaton Beelte"),
                ('永冬の災影',"Everwinter Shadewalker"),
                ('自動機兵・パウーク',"Automaton Spider"),
                ('灼焔徘徊者',"Searing Prowler"),
                ('自動機兵・ヴォルク',"Automaton Direwolf"),
                ('雷の造物',"Thunderspawn"),
                ('焚火の災影',"Incineration Shadewalker"),
                ('雲騎軍・見廻兵士',"Cloud Knights Patroller"),
                ('冷寒徘徊者',"Frigid Prowler"),
                ('魔陰の身・兵卒',"Mara-Struc Soldier"),
                ('風の造物',"Windspawn"),
                ('入魔機巧・統率狻猊',"Entranced Ingenium: Obedient Dracolion"),
                ('薬王秘伝・鍛錬者',"Diciples of Sanctus Medicus: Shape Shifter"),
                ('金人・門番',"Aurumaton Gatekeeper"),
                ('入魔機巧・灯火龍魚',"Entranced Ingenium: Illumination Dragonfish"),
                ('炎の造物',"Flamespawn"),
                ('入魔機巧・黒雲金ガマ',"Entranced Ingenium: Golden Cloud Toad"),
                ('「星核ハンター」カフカ',"Stellaron Hunter: Kafka"),
                ('虚数の葉を織る者',"Imaginary Weaver"),
                ('霜の造物',"Frostspawn"),
                ('序列プーマン',"Sequence Trotter"),
                ('次元プーマン',"Warp Trotter"),
                ('無双仮面',"Mask of No Thought"),
                ('宇宙からの炎',"Blaze Out of Space"),
                ('宇宙からの氷',"Ice Out of Space"),
                ('バリオン',"Baryon"),
                ('蚕食者の影',"Decaying Shadow"),
                ('守護者の影',"Guardian Shadow"),
                ('ヴォイドレンジャー・略奪',"Voidranger: Reaver"),
                ('反バリオン',"Antibaryon"),
                ('ヴォイドレンジャー・蹂躙',"Voidranger: Trampler"),
                ('終末獣',"Doomsday Beast"),
                ('ストーム',"Stormbringer"),
                ('豊穣の玄鹿',"Abundant Ebon Deer"),
                ('嘉身の梢',"Twing of Lavish Fruits"),
                ('万花の梢',"Twing of Glorious Blooms"),
                ('黄葉の梢',"Twing of Marple Leaf"),
                ('厳風の梢',"Twing of Wintry Wind"),
                ('反物質エンジン',"Antimatter Engine"),
                ('黎明の左手',"Dawn's Left Hand"),
                ('厄災の右手',"Disaster's Right Hand"),
                ('氷刃',"Ice Edge"),
                ('無尽なる冬の槊',"Lance of the eternal Freeze"),
                ('壊滅プーマン',"Trotter of Destruction"),
                ('存護プーマン',"Trotter of Preservation"),
                ('薬王秘伝・内丹士',"Disciples of Sancuts Medicus - Internal Alchemist"),
                ('マニピュレーターユニット',"Auxiliary Robot Arm Unit"),
                ('豊穣プーマン',"Trotter of Abundance"),
                ('豊穣の玄蓮',"Abundance Lotus"),
                ('破滅の玄蓮',"Destruction Lotus"),
                ('狼影',"Shadow Jackhyena"),
                ('承露天人',"The Ascended"),
                ('薬王秘伝・器元士',"Disciples of Sancuts Medicus: Ballistarius"),
                ('豊穣の霊獣・奎木',"Abundance Sprite: Wooden Lupus"),
                ('豊穣の霊獣・婁金',"Abundance Sprite: Golden Hound"),
                ('豊穣の霊獣・長右',"Abundance Sprite: Malefic Ape"),
                ('不死の神実・幻朧',"Phantylia The Undying"),
                ('雲騎驍衛・彦卿',"Cloud Knight Lieutenant: Yanqing"),
                ('造物エンジン',"Engine of creation"),
                ('飛剣',"Flying Sword"),
                ('スウォーム・真蟄虫',"Swarm: True Sting"),
                ('「監督ロボット」プロトモデル2号',"Monitoring Automaton Prototype 2"),
                ('次蟄虫',"Lesser Sting"),
                ('幼蟄虫',"Juvenilie Sting"),
                ('ベテラン社員・チームリーダー',"Senior Staff: Team Leader"),
                ('平社員・警備',"Grunt: Security Personnel"),
                ('平社員・外勤',"Grund: Field Personnel"),
                ('幽府武弁',"Wraith Warden"),
                ('金人・勾魂',"Aurumaton Spectral Envoy"),
                ('魔陰武弁',"Mara-Struc Warden"),
                ('浮煙',"Cirrus"),
                ('アルジェンティ',"Argenti"),
                ('「槍先」','"Speartip"'),
                ('「盾」','"The Shield"'),
                ('「叙勲」','"The honored"'),
                ('蝕蟄虫',"Graw Sting"),
                ('砕星王虫・スキャラカバズ(模造)',"Starcrusher Swarm King: Skaracabaz (Synthetic)"),
                ('記憶域ミーム「砕け散った心」',"Memory Zone Meme 'Heartbreaker'"),
                ('ナイトメア劇団・スプリングディーラー',"Dreamjolt Troupe's Spring Loader"),
                ('ナイトメア劇団・ソーダドッグ',"Dreamjolt Troupe's Bubble Hound"),
                ('ナイトメア劇団・Mr.円幕',"Dreamjolt Troupe's Mr. Domescreen"),
                ('記憶域ミーム「偏在する視線」','Memory Zone Meme "Allseer"'),
                ('ナイトメア劇団・スウィート・ゴリラ',"Dreamjolt Troupe's Sweet Gorilla"),
                ('ナイトメア劇団・踊る仮面の鳥',"Dreamjolt Troupe's Birdskull"),
                ('記憶域ミーム「死へ向かうのは何物」',"Memory Zone Meme 'Something Unto Death'"),
                ('王のゴミ箱',"Lordly Trashcan"),
                ('永眠の墓碑',"Sombrous Sepulcher"),
                ('ナイトメア劇団・エクセスウェルダン',"Dreamjolg Troupe's Beyond Overcooked"),
                ('「星核ハンター」サム',"Stellaron Hunter: Sam"),
        ]

        # テーブルウィジェットの設定
        enemy_table.setColumnCount(2)
        enemy_table.setRowCount(len(enemys))

        for row, (enemy, japanese) in enumerate(enemys):
            enemy_table.setItem(row, 0, QTableWidgetItem(enemy))
            enemy_table.setItem(row, 1, QTableWidgetItem(japanese))

        # 一番上の行と一番左の列を非表示にする
        enemy_table.verticalHeader().setVisible(False)
        enemy_table.horizontalHeader().setVisible(False)

        # 行と列の大きさを設定
        for i in range(len(enemys)):
            enemy_table.setRowHeight(i, 75)  # 行の高さを75に設定
            enemy_table.setColumnWidth(0, 600)  # 日本語の列の幅を600に設定
            enemy_table.setColumnWidth(1, 1000)  # 英語の列の幅を1000に設定

        # フォントサイズを変更
        for row, (enemy, japanese) in enumerate(enemys):
            item1 = QTableWidgetItem(enemy)
            item1.setFont(QFont('Arial', 30))  # フォントサイズを30に設定
            item2 = QTableWidgetItem(japanese)
            item2.setFont(QFont('Arial', 30))  # フォントサイズを30に設定
            enemy_table.setItem(row, 0, item1)
            enemy_table.setItem(row, 1, item2)

        enemy_layout.addWidget(enemy_table)