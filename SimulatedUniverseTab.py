from PySide6.QtWidgets import QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem
from PySide6_VerticalQTabWidget import VerticalQTabWidget
from PySide6.QtGui import QFont

class SimulatedUniverseTab(QWidget):
    def __init__(self):
        super().__init__()

        # 模擬宇宙タブのメインウィジェット
        simulated_universe_tab = VerticalQTabWidget()

        # 祝福タブのメインウィジェット
        blessing_tab = VerticalQTabWidget()

        # 祝福タブ
        simulated_universe_tab.addTab(blessing_tab, "祝福")

        # 愉悦タブ
        elation_tab = QWidget()
        blessing_tab.addTab(elation_tab, "愉悦")
        
        # 愉悦データを追加
        elations = [
                ('四番屠畜場・皆眠りて','Slaughterhouse No. 4: Rest in Peace'),
                ('『自動ハーモニカ・茫々たる白夜』','Auto Harmonica: Whitest Night'),
                ('『チャンピオンのディナー・猫のゆりかご』',"Champion's Dinner: Cat's Cradle"),
                ('『燃ゆる男の肖像』','Portrait of a Man On Fire'),
                ('『十二のサルと怒れる男』','12 Monkeys and Angry Men'),
                ('『汚されたアホウドリ』','The Painted Albatross'),
                ('『キャッチ=21』','Twenty-First Military Rule'),
                ('『流れよ汝が涙』','Just Keep on Crying!'),
                ('『砂時計の幼稚園』','The Hourglass Kindergarten'),
                ('『リルタ重力の虹』','Aiden Gravitational Rainbow'),
                ('『サスペンス』','Suspiria'),
                ('『素行満点』','Exemplary Conduct'),
                ('『仄暗い炎』','Pale Fire'),
                ('『医者の異常な愛情』','Doctor of Love'),
                ('『白金時代』','Platinum Age'),
                ('『ほとんど有害』','Mostly Harmful'),
                ('『灯台へ戻ろう』','Back to the Lighthouse'),
                ('『時計仕掛けのリンゴ』','Clockwork Apple'),
        ]

        # 愉悦タブに新しいテーブルウィジェットを追加
        elation_table_widget = QTableWidget()
        elation_table_widget.setColumnCount(2)
        elation_table_widget.setRowCount(len(elations))

        # 愉悦データを追加2
        for row, (name, description) in enumerate(elations):
            elation_table_widget.setItem(row, 0, QTableWidgetItem(name))
            elation_table_widget.setItem(row, 1, QTableWidgetItem(description))

        layout = QVBoxLayout(elation_tab)
        layout.addWidget(elation_table_widget)

        # 愉悦フォントサイズを変更
        for row, (path, japanese) in enumerate(elations):
            item1 = QTableWidgetItem(path)
            item1.setFont(QFont('Arial', 30))  # フォントサイズを30に設定
            item2 = QTableWidgetItem(japanese)
            item2.setFont(QFont('Arial', 30))  # フォントサイズを30に設定
            elation_table_widget.setItem(row, 0, item1)
            elation_table_widget.setItem(row, 1, item2)
        # 行と列の大きさを設定
        for i in range(len(elations)):
            elation_table_widget.setRowHeight(i, 75)  # 行の高さを75に設定
            elation_table_widget.setColumnWidth(0, 600)  # 日本語の列の幅を600に設定
            elation_table_widget.setColumnWidth(1, 800)  # 英語の列の幅を800に設定
        # 一番上の行と一番左の列を非表示にする
        elation_table_widget.verticalHeader().setVisible(False)
        elation_table_widget.horizontalHeader().setVisible(False)


        # 豊穣タブ
        abundance_tab = QWidget()
        blessing_tab.addTab(abundance_tab, "豊穣")

        # 豊穣データを追加
        abundances = [
                ('彼の遐齢を延さん','Prosperity, Longevity'),
                ('若の罪福、皆に施願を','Mudra of Blessing'),
                ('衆生に豊穣を','Being of Abundance, Becoming One Mind'),
                ('天人不動衆','Mortals of the Buddha-Field'),
                ('日月を燭らす宝光','Precious Moon-Like Candlelight'),
                ('邪穢の苦を厭離す','Aversion to Suffering'),
                ('大愿、般若の船','Prajna Boat'),
                ('滅罪生善','Good Deeds Come After Old Sins'),
                ('慧海を渡る慈航','Salvation From Damnation'),
                ('明澄琉璃の身','Clear Lucite Body'),
                ('加持','Blessing'),
                ('勝軍','Victorious Force'),
                ('延寿','Extended Life'),
                ('厄払い','Dispel Disaster'),
                ('甘露','Sweet Dew'),
                ('願印','Seal'),
                ('回生','Rebirth'),
                ('法雨','Rain of Truth')
        ]

        # 豊穣タブに新しいテーブルウィジェットを追加
        abundance_table_widget = QTableWidget()
        abundance_table_widget.setColumnCount(2)
        abundance_table_widget.setRowCount(len(abundances))

        # 豊穣データを追加2
        for row, (name, description) in enumerate(abundances):
            abundance_table_widget.setItem(row, 0, QTableWidgetItem(name))
            abundance_table_widget.setItem(row, 1, QTableWidgetItem(description))

        layout = QVBoxLayout(abundance_tab)
        layout.addWidget(abundance_table_widget)

        # 豊穣フォントサイズを変更
        for row, (path, japanese) in enumerate(abundances):
            item1 = QTableWidgetItem(path)
            item1.setFont(QFont('Arial', 40))  # フォントサイズを40に設定
            item2 = QTableWidgetItem(japanese)
            item2.setFont(QFont('Arial', 40))  # フォントサイズを40に設定
            abundance_table_widget.setItem(row, 0, item1)
            abundance_table_widget.setItem(row, 1, item2)
        # 行と列の大きさを設定
        for i in range(len(abundances)):
            abundance_table_widget.setRowHeight(i, 75)  # 行の高さを75に設定
            abundance_table_widget.setColumnWidth(0, 500)  # 日本語の列の幅を500に設定
            abundance_table_widget.setColumnWidth(1, 1000)  # 英語の列の幅を1000に設定
        # 一番上の行と一番左の列を非表示にする
        abundance_table_widget.verticalHeader().setVisible(False)
        abundance_table_widget.horizontalHeader().setVisible(False)

        # 壊滅タブ
        destruction_tab = QWidget()
        blessing_tab.addTab(destruction_tab, "壊滅")
                # 壊滅データを追加
        destructions = [
                ('熱的死の固有値','Universal Heat Death Characteristic'),
                ('反物質非可逆方程式','Non-Inverse Antimatter Equation'),
                ('対消滅回帰不等式','Regression Inequality of Annihilation'),
                ('災難的共振','Catastrophic Resonance'),
                ('破壊的フレア','Destructive Flare'),
                ('壊滅的降着','Devastating Accretion'),
                ('逓増的終末','Incremental Doomsday'),
                ('戒律的フラッシュ','Disciplinary Flicker'),
                ('予兆的被写界深度','Indicative Depth of Field'),
                ('危害的余光','Hazardous Lucent Residue'),
                ('原始ブラックホール','Primordial Black Hole'),
                ('永久崩壊天体','Eternally Collapsing Object'),
                ('不安定帯','Instability Strip'),
                ('偏光受容体','Polarization Receptor'),
                ('光壊変','Reflection'),
                ('軌道赤方偏移','Orbital Redshift'),
                ('備蓄計量','Metric Reservation'),
                ('哨戒衛星','Sentinel Satellite')
        ]

        # 壊滅タブに新しいテーブルウィジェットを追加
        destruction_table_widget = QTableWidget()
        destruction_table_widget.setColumnCount(2)
        destruction_table_widget.setRowCount(len(destructions))

        # 壊滅データを追加2
        for row, (name, description) in enumerate(destructions):
            destruction_table_widget.setItem(row, 0, QTableWidgetItem(name))
            destruction_table_widget.setItem(row, 1, QTableWidgetItem(description))

        layout = QVBoxLayout(destruction_tab)
        layout.addWidget(destruction_table_widget)

        # 壊滅フォントサイズを変更
        for row, (path, japanese) in enumerate(destructions):
            item1 = QTableWidgetItem(path)
            item1.setFont(QFont('Arial', 30))  # フォントサイズを40に設定
            item2 = QTableWidgetItem(japanese)
            item2.setFont(QFont('Arial', 40))  # フォントサイズを40に設定
            destruction_table_widget.setItem(row, 0, item1)
            destruction_table_widget.setItem(row, 1, item2)
        # 行と列の大きさを設定
        for i in range(len(destructions)):
            destruction_table_widget.setRowHeight(i, 75)  # 行の高さを75に設定
            destruction_table_widget.setColumnWidth(0, 500)  # 日本語の列の幅を500に設定
            destruction_table_widget.setColumnWidth(1, 800)  # 英語の列の幅を1000に設定
        # 一番上の行と一番左の列を非表示にする
        destruction_table_widget.verticalHeader().setVisible(False)
        destruction_table_widget.horizontalHeader().setVisible(False)

        # 記憶タブ
        remembrance_tab = QWidget()
        blessing_tab.addTab(remembrance_tab, "記憶")

        # 記憶データを追加
        remembrances = [
                ('完璧体験：純真','Perfect Experience: Innocence'),
                ('完璧体験：沈黙','Perfect Experience: Reticence'),
                ('完璧体験：浮黎','Perfect Experience: Fuli'),
                ('極端体験：戦慄','Ultimate Experience: Shudder'),
                ('極端体験：多感','Ultimate Experience: Sentimentality'),
                ('極端体験：眩暈','Ultimate Experience: Dizziness'),
                ('極端体験：異端児','Ultimate Experience: Maverick'),
                ('極端体験：感銘','Ultimate Experience: Indelibility'),
                ('極端体験：無感覚','Ultimate Experience: Insensitivity'),
                ('極端体験：茫然自失','Ultimate Experience: Melancholia'),
                ('体験：凄烈な憎悪','Experience: Stone Cold Hatred'),
                ('体験：病の苛み','Experience: Pain & Suffering'),
                ('体験：反響の興奮','Experience: Responsive Excitement'),
                ('体験：上昇の刺激','Experience: Thrill of Escalation'),
                ('体験：疎遠の苦しみ','Experience: The Torment of Alienation'),
                ('体験：言えない恥','Experience: Unspeakable Shame'),
                ('体験：原初の苦衷','Experience: Primordial Hardship'),
                ('体験：失われた記憶','Experience: Lost Memory')
        ]

        # 記憶タブに新しいテーブルウィジェットを追加
        remembrance_table_widget = QTableWidget()
        remembrance_table_widget.setColumnCount(2)
        remembrance_table_widget.setRowCount(len(remembrances))

        # 記憶データを追加2
        for row, (name, description) in enumerate(remembrances):
            remembrance_table_widget.setItem(row, 0, QTableWidgetItem(name))
            remembrance_table_widget.setItem(row, 1, QTableWidgetItem(description))

        layout = QVBoxLayout(remembrance_tab)
        layout.addWidget(remembrance_table_widget)

        # 記憶フォントサイズを変更
        for row, (path, japanese) in enumerate(remembrances):
            item1 = QTableWidgetItem(path)
            item1.setFont(QFont('Arial', 40))  # フォントサイズを40に設定
            item2 = QTableWidgetItem(japanese)
            item2.setFont(QFont('Arial', 30))  # フォントサイズを40に設定
            remembrance_table_widget.setItem(row, 0, item1)
            remembrance_table_widget.setItem(row, 1, item2)
        # 行と列の大きさを設定
        for i in range(len(remembrances)):
            remembrance_table_widget.setRowHeight(i, 75)  # 行の高さを75に設定
            remembrance_table_widget.setColumnWidth(0, 500)  # 日本語の列の幅を500に設定
            remembrance_table_widget.setColumnWidth(1, 800)  # 英語の列の幅を800に設定
        # 一番上の行と一番左の列を非表示にする
        remembrance_table_widget.verticalHeader().setVisible(False)
        remembrance_table_widget.horizontalHeader().setVisible(False)

        # 巡狩タブ
        hunt_tab = QWidget()
        blessing_tab.addTab(hunt_tab, "巡狩")

        # 巡狩データを追加
        hunts = [
                ('太清を徹す断空の帝弓','Celestial Annihilation'),
                ('光越す制勝の帝車','Imperishable Victory'),
                ('帝星臨めば穹桑を制す','Imperial Reign'),
                ('遅彝弓を執る序師',"Adept's Bow"),
                ('忌み物追う流嵐','Flowing Mist'),
                ('射御を決する白矢','Archery Duel'),
                ('鑿齒を誅つ飛虹','Monster-Expelling Rainbow'),
                ('歩離を駆逐せし雲鏑','Ejecting the Borisin'),
                ('狩月を助ける景星','Auspicious Star'),
                ('夙敵繳める天舟','Battle Against the Old Foe'),
                ('背孤撃虚','Shrewd Arrangement'),
                ('烏号綦箭','Blessed Bow and Arrow'),
                ('背生撃死','Skirting Life and Death'),
                ('緋弓素矢','Vermeil Bow and White Arrow'),
                ('危宮へ歩む天棓','Catastrophic Constellation'),
                ('桑弧蓬矢','Vaulting Ambition'),
                ('牛斗射る紫電','Constellation Surge'),
                ('雷車動地','Thundering Chariot')
        ]

        # 巡狩タブに新しいテーブルウィジェットを追加
        hunt_table_widget = QTableWidget()
        hunt_table_widget.setColumnCount(2)
        hunt_table_widget.setRowCount(len(hunts))

        # 巡狩データを追加2
        for row, (name, description) in enumerate(hunts):
            hunt_table_widget.setItem(row, 0, QTableWidgetItem(name))
            hunt_table_widget.setItem(row, 1, QTableWidgetItem(description))

        layout = QVBoxLayout(hunt_tab)
        layout.addWidget(hunt_table_widget)

        # 巡狩フォントサイズを変更
        for row, (path, japanese) in enumerate(hunts):
            item1 = QTableWidgetItem(path)
            item1.setFont(QFont('Arial', 40))  # フォントサイズを40に設定
            item2 = QTableWidgetItem(japanese)
            item2.setFont(QFont('Arial', 40))  # フォントサイズを40に設定
            hunt_table_widget.setItem(row, 0, item1)
            hunt_table_widget.setItem(row, 1, item2)
        # 行と列の大きさを設定
        for i in range(len(hunts)):
            hunt_table_widget.setRowHeight(i, 75)  # 行の高さを75に設定
            hunt_table_widget.setColumnWidth(0, 600)  # 日本語の列の幅を500に設定
            hunt_table_widget.setColumnWidth(1, 800)  # 英語の列の幅を800に設定
        # 一番上の行と一番左の列を非表示にする
        hunt_table_widget.verticalHeader().setVisible(False)
        hunt_table_widget.horizontalHeader().setVisible(False)

        # 存護タブ
        preservation_tab = QWidget()
        blessing_tab.addTab(preservation_tab, "存護")

        # 存護データを追加
        preservations = [
                ('神性構築・共鳴伝達','Divine Construct: Resonance Transfer'),
                ('神性構築・不静定構造','Divine Construct: Metastatic Field'),
                ('神性構築・マクロ偏析','Divine Construct: Macrosegregation'),
                ('星間構築・格子欠陥','Interstellar Construct: Burst Lattice'),
                ('星間構築・安全荷重','Interstellar Construct: Safe Load'),
                ('星間構築・剪断構造','Interstellar Construct: Shear Structure'),
                ('星間構築・固溶強化','Interstellar Construct: Solid Solution'),
                ('星間構築・反作用庇護','Interstellar Construct: Sanctuary'),
                ('星間構築・四角錐','Interstellar Construct: Quadrangular Pyramid'),
                ('星間構築・亜共晶','Interstellar Construct: Hypoeutectoid'),
                ('構築・専念','Construct: Concentration'),
                ('構築・勃発','Construct: Burst'),
                ('構築・哨戒','Construct: Sentinel'),
                ('構築・確固','Construct: Firmness'),
                ('構築・回転','Construct: Rotation'),
                ('構築・溶着','Construct: Patch'),
                ('構築・集塑','Construct: Assemble'),
                ('構築・補填','Construct: Compensation')
        ]

        # 存護タブに新しいテーブルウィジェットを追加
        preservation_table_widget = QTableWidget()
        preservation_table_widget.setColumnCount(2)
        preservation_table_widget.setRowCount(len(preservations))

        # 存護データを追加2
        for row, (name, description) in enumerate(preservations):
            preservation_table_widget.setItem(row, 0, QTableWidgetItem(name))
            preservation_table_widget.setItem(row, 1, QTableWidgetItem(description))

        layout = QVBoxLayout(preservation_tab)
        layout.addWidget(preservation_table_widget)

        # 存護フォントサイズを変更
        for row, (path, japanese) in enumerate(preservations):
            item1 = QTableWidgetItem(path)
            item1.setFont(QFont('Arial', 40))  # フォントサイズを40に設定
            item2 = QTableWidgetItem(japanese)
            item2.setFont(QFont('Arial', 30))  # フォントサイズを30に設定
            preservation_table_widget.setItem(row, 0, item1)
            preservation_table_widget.setItem(row, 1, item2)
        # 行と列の大きさを設定
        for i in range(len(preservations)):
            preservation_table_widget.setRowHeight(i, 75)  # 行の高さを75に設定
            preservation_table_widget.setColumnWidth(0, 600)  # 日本語の列の幅を600に設定
            preservation_table_widget.setColumnWidth(1, 800)  # 英語の列の幅を800に設定
        # 一番上の行と一番左の列を非表示にする
        preservation_table_widget.verticalHeader().setVisible(False)
        preservation_table_widget.horizontalHeader().setVisible(False)

        # 虚無タブ
        nihility_tab = QWidget()
        blessing_tab.addTab(nihility_tab, "虚無")

        # 虚無データを追加
        nihilitys = [
                ('なぜすべては消えぬか',"Why Hasn't Everything Already Disappeared?"),
                ('箱に入った人','The Man in the Cover'),
                ('感覚追奉者の葬式','Funeral of Sensory Pursuivant'),
                ('発端と結末','Beginning and End'),
                ('他人は地獄','Hell is Other People'),
                ('自己欺瞞カフェ','Café Self-Deceit'),
                ('焚火の外の夜','Night Beyond Pyre'),
                ('広野の呼び声','Call of the Wilderness'),
                ('根拠なき賛歌','All Things are Possible'),
                ('存在の黄昏','Twilight of Existence'),
                ('漠視主義','Ignosticism'),
                ('虚妄の供物','Offerings of Deception'),
                ('意義への詰問','Questioning of Purpose'),
                ('日の出前','Before Sunrise'),
                ('悲劇講座','Tragic Lecture'),
                ('知覚の壁','Sensory Labyrinth'),
                ('盲目の視界','Blind Vision'),
                ('情緒捨離','Emotional Decluttering')
        ]

        # 虚無タブに新しいテーブルウィジェットを追加
        nihility_table_widget = QTableWidget()
        nihility_table_widget.setColumnCount(2)
        nihility_table_widget.setRowCount(len(nihilitys))

        # 虚無データを追加2
        for row, (name, description) in enumerate(nihilitys):
            nihility_table_widget.setItem(row, 0, QTableWidgetItem(name))
            nihility_table_widget.setItem(row, 1, QTableWidgetItem(description))

        layout = QVBoxLayout(nihility_tab)
        layout.addWidget(nihility_table_widget)

        # 虚無フォントサイズを変更
        for row, (path, japanese) in enumerate(nihilitys):
            item1 = QTableWidgetItem(path)
            item1.setFont(QFont('Arial', 40))  # フォントサイズを40に設定
            item2 = QTableWidgetItem(japanese)
            item2.setFont(QFont('Arial', 40))  # フォントサイズを40に設定
            nihility_table_widget.setItem(row, 0, item1)
            nihility_table_widget.setItem(row, 1, item2)
        # 行と列の大きさを設定
        for i in range(len(nihilitys)):
            nihility_table_widget.setRowHeight(i, 75)  # 行の高さを75に設定
            nihility_table_widget.setColumnWidth(0, 500)  # 日本語の列の幅を500に設定
            nihility_table_widget.setColumnWidth(1, 1000)  # 英語の列の幅を1000に設定
         # 一番上の行と一番左の列を非表示にする
        nihility_table_widget.verticalHeader().setVisible(False)
        nihility_table_widget.horizontalHeader().setVisible(False)   

        # 繁殖タブ
        propagation_tab = QWidget()
        blessing_tab.addTab(propagation_tab, "繁殖")

        # 繁殖データを追加
        propagations = [
                ('子嚢放出','Spore Discharge'),
                ('膿菌','Fungal Pustule'),
                ('鎌状付属肢','Scythe Limbs'),
                ('腐植腫','Putrefaction Ulcer'),
                ('分解酵素','Lytic Enzyme'),
                ('代謝腔','Metabolic Cavity'),
                ('興奮腺','Excitatory Gland'),
                ('裸脳質','Exposed Brain Matter'),
                ('節関膜','Intersegmental Membrane'),
                ('触媒','Catalyst'),
                ('骨刃','Osseus Blade'),
                ('脊刺','Spinal Spur'),
                ('口針','Channeled Needle'),
                ('結膜','Conjunctiva'),
                ('鱗翅','Scaled Wing'),
                ('複眼','Compound Eye'),
                ('胞子嚢','Sporangium'),
                ('液嚢','Vesicle')
        ]

        # 繁殖タブに新しいテーブルウィジェットを追加
        propagation_table_widget = QTableWidget()
        propagation_table_widget.setColumnCount(2)
        propagation_table_widget.setRowCount(len(propagations))

        # 繁殖データを追加2
        for row, (name, description) in enumerate(propagations):
            propagation_table_widget.setItem(row, 0, QTableWidgetItem(name))
            propagation_table_widget.setItem(row, 1, QTableWidgetItem(description))

        layout = QVBoxLayout(propagation_tab)
        layout.addWidget(propagation_table_widget)

        # 繁殖フォントサイズを変更
        for row, (path, japanese) in enumerate(propagations):
            item1 = QTableWidgetItem(path)
            item1.setFont(QFont('Arial', 40))  # フォントサイズを40に設定
            item2 = QTableWidgetItem(japanese)
            item2.setFont(QFont('Arial', 40))  # フォントサイズを40に設定
            propagation_table_widget.setItem(row, 0, item1)
            propagation_table_widget.setItem(row, 1, item2)
        # 行と列の大きさを設定
        for i in range(len(propagations)):
            propagation_table_widget.setRowHeight(i, 75)  # 行の高さを75に設定
            propagation_table_widget.setColumnWidth(0, 300)  # 日本語の列の幅を300に設定
            propagation_table_widget.setColumnWidth(1, 800)  # 英語の列の幅を800に設定
        # 一番上の行と一番左の列を非表示にする
        propagation_table_widget.verticalHeader().setVisible(False)
        propagation_table_widget.horizontalHeader().setVisible(False)

        # 知恵タブ
        erudition_tab = QWidget()
        blessing_tab.addTab(erudition_tab, "知恵")

        # 知恵データを追加
        eruditions = [
                ('BCI-34型灰白質','BCI-34 Gray Matter'),
                ('SMR-2型扁桃体','SMR-2 Amygdala'),
                ('VEP-18型後頭葉','VEP-18 Occipital Lobe'),
                ('付加：前庭器官','Attachment: Vestibular System'),
                ('模倣：神経伝達物質合成','Imitation: Transmitter Synthesis'),
                ('インプラント：顕在的記憶','Implant: Explicit Memory'),
                ('擬態：神経路','Mimesis: Tactile Pathway'),
                ('分析：サブリミナル効果','Analysis: Subliminal Sensation'),
                ('積載：有線皮質','Load: Striated Cortex'),
                ('刺激：跳躍伝導','Stimulation: Saltatory Conduction'),
                ('歯車が組合う王座','Throne of Engaged Gears'),
                ('導線が取り巻く指輪','Ring of Bent Wires'),
                ('エネルギー渦巻く王笏','Scepter of Energy Torque'),
                ('アンチラグの炬火','Torch of Anti-Lag Ignition'),
                ('遅延回折の燭光','Candle of Delayed Diffraction'),
                ('古びた金属の華蓋','Canopy of Mottled Metal'),
                ('コイルが織りなす装束','Garment of Coiled Wires'),
                ('交錯するパイプの冠','Wreath of Interlaced Pipes')
        ]

        # 知恵タブに新しいテーブルウィジェットを追加
        erudition_table_widget = QTableWidget()
        erudition_table_widget.setColumnCount(2)
        erudition_table_widget.setRowCount(len(eruditions))

        # 知恵データを追加2
        for row, (name, description) in enumerate(eruditions):
            erudition_table_widget.setItem(row, 0, QTableWidgetItem(name))
            erudition_table_widget.setItem(row, 1, QTableWidgetItem(description))

        layout = QVBoxLayout(erudition_tab)
        layout.addWidget(erudition_table_widget)

        # 知恵フォントサイズを変更
        for row, (path, japanese) in enumerate(eruditions):
            item1 = QTableWidgetItem(path)
            item1.setFont(QFont('Arial', 40))  # フォントサイズを40に設定
            item2 = QTableWidgetItem(japanese)
            item2.setFont(QFont('Arial', 40))  # フォントサイズを40に設定
            erudition_table_widget.setItem(row, 0, item1)
            erudition_table_widget.setItem(row, 1, item2)
        # 行と列の大きさを設定
        for i in range(len(eruditions)):
            erudition_table_widget.setRowHeight(i, 75)  # 行の高さを75に設定
            erudition_table_widget.setColumnWidth(0, 600)  # 日本語の列の幅を600に設定
            erudition_table_widget.setColumnWidth(1, 800)  # 英語の列の幅を800に設定
         # 一番上の行と一番左の列を非表示にする
        erudition_table_widget.verticalHeader().setVisible(False)
        erudition_table_widget.horizontalHeader().setVisible(False) 

        # 奇物タブ
        curio_tab = QWidget()
        simulated_universe_tab.addTab(curio_tab, "奇物")

        # 奇物データを追加
        curios = [
                ('跳躍複眼','Warping Compund Eye'),
                ('次元削減ダイス','Dimension Reduction Dice'),
                ('混沌の雲芝','Chaos Trametes'),
                ('異木の果実','Fruit of the Alien Tree'),
                ('不確定の匣','Casket of Inaccuracy'),
                ('香涎チーズ','Ambergris Cheese'),
                ('おしゃべり羊皮紙','The parchment That Always Eats'),
                ('幸福クリーム','Fortune Glue'),
                ('博士のローブ',"The Doctor's Robe"),
                ('記憶の封蝋','Sealing Wax of Remembrance'),
                ('壊滅の封蝋','Sealing Wax of Destruction'),
                ('巡狩の封蝋','Sealing Wax of The Hunt'),
                ('愉悦の封蝋','Sealing Wax of Elation'),
                ('存護の封蝋','Sealing Wax of Preservation'),
                ('輝くトラペゾヘドロンサイコロ','Shining Trapezohedron Die'),
                ('万象無常のサイコロ','Entropic Die'),
                ('天外聖歌隊のレコード','Record from Beyond the Sky'),
                ('全知袋','Omniscient Capsule'),
                ('空無の芯切り','Void Wick Trimmer'),
                ('分裂金貨','Gold Coin of Discord'),
                ('純美のローブ','Robe of The Beauty'),
                ('クラブチケット','Society Ticket'),
                ('機械式鳩時計','Mechanical Cuckoo Clock'),
                ('信仰債権','Faith Bond'),
                ('カンパニー鳩時計','IPC Cuckoo Clock'),
                ('ビーコン着色剤','Beacon Coloring Paste'),
                ('パンクロード精神','Punklorde mentality'),
                ('永久鳩時計','Perpetual Motion Cuckoo Clock'),
                ('黒森鳩時計','Black Forest Cuckoo Clock'),
                ('占い鳩時計','Divination Cuckoo Clock'),
                ('銀河ビッグロッタリー','Cosmic Big Lotto'),
                ('時空のプリズム','Space-Time Prisim'),
                ('換境桂冠','Laurel Crown of Planar Shifts'),
                ('虫網','Insect Web'),
                ('湮滅の芯切り','Obliteration Wick Trimmer'),
                ('砕けた星の釣り餌','Shattered Star Bait'),
                ('無限再帰するコード','Infinitely Recursive Code'),
                ('注釈がないコード','Mysterious Code'),
                ('正確で完璧なコード','Elegant Code'),
                ('杓子定規なコード','Normal Code'),
                ('少し怪しげなコード','Odd Code'),
                ('ぐちゃぐちゃなコード','Corrupted Code'),
                ('豊穣の封蝋','Sealing Wax of Abundance'),
                ('虚無の封蝋','Sealing Wax of Nihility'),
                ('天使型謝債発行機','Angel-type I.O.U. Dispenser'),
                ('繁殖の封蝋','Sealing Wax of Propagation'),
                ('ピンクショック','The Pinkest Collision'),
                ('ターラの毒火炎','Thalan Toxi-Flame'),
                ('人造隕石','Man-Made Meteorite'),
                ('虚構機兵','Illusory Automaton'),
                ('純美の騎士道','Spirit of the Knights of Beauty'),
                ('邪悪な機械衛星#900','Vile Mechanical Satellite #900'),
                ('愚者の仮面',"Fool's Mask"),
                ('天才クラブの他愛もない噂話','Typical Genius Society Gossip'),
                ('ブラックホールの罠','Black Hole Trap'),
                ('血錦の徽章','Medal of the Glorblood Era'),
                ('『ボサ頭探偵』','Tousled Detective'),
                ('ファミリーの絆結び','Family Ties'),
                ('トライアングル','Triangular Drum-roll Device'),
                ('虫歯星系模型','Cavity System Model'),
                ('ルパート帝国の機械歯車','Rubert Empire Mechanical Cogwheel'),
                ('混沌の特攻霊薬','Tonic of Efficacious Chaos'),
                ('ひげの爆薬','A Pinch of Bearded Gunpowder'),
                ('分裂鳩時計','Fissured Cuckoo Clock'),
                ('分裂銀貨','Silver Coin of Discord'),
                ('星間ビッグロッタリー','Interastral Big Lotto'),
                ('万象無常のサイコロ∞','Entropic Die (Infinitie)'),
                ('銀河ビッグロッタリー∞','CosmicBigLotto (Infinitie)'),
                ('全知袋∞','Omniscient Capsule (Infinitie)'),
                ('信仰債権∞','Faith Bond (Infinitie)'),
                ('パンクロード精神∞','PunkLorde Mentality (Infinitie)'),
                ('湮滅の芯切り∞','obliteration Wich Trimmer (Infinitie)'),
                ('クラブチケット∞','Society Ticket (Infinitie)'),
                ('分裂金貨∞','Gold Coin of Discord (Infinitie)'),
                ('純美のローブ∞','Robe of The Beauty (Infinitie)'),
                ('天使型謝債発行機∞','Angel-type I.O.U. Dispenser (Infinitie)'),
                ('砕けた星の釣り餌∞','Shattered Star Bait (Infinitie)'),
                ('「神秘」の磁力','Mysterious Magnetism'),
                ('理性の崩壊',"Rationality's Fall"),
                ('知恵の封蝋','Sealing Wax of Erudition'),
                ('ルアン袋','A-Ruan Pouch'),
                ('平和の代価','Price of Peace'),
                ('「奇想天外」培養脳','"Wildminder" Machine Cell'),
                ('「有機の心臓」','"Organic Heart"'),
                ('「意気消沈」暗号機','"Ashheart" Ciphertech'),
                ('「階段の上のクラゲ」','"Jellyfish on the Staircase"'),
                ('腐敗した異木の果実','Rotting Fruit of the Alien Tree'),
                ('「最高アイデア」レインボー機','"Revelrous" Rainbowmaker'),
                ('「平凡アイデア」集団機','"Cognito Averagifier" Communal Nexus'),
                ('「無効アイデア」コード機','"Cognito Invalidater" Codebuilder'),
                ('願い星','Wish Upon a Star'),
                ('計り知れない匣','Indecipherable Box'),
                ('スポンジ王','King of Sponges')
        ]

        # 奇物タブに新しいテーブルウィジェットを追加
        curio_table_widget = QTableWidget()
        curio_table_widget.setColumnCount(2)
        curio_table_widget.setRowCount(len(curios))

        # データを追加2
        for row, (name, description) in enumerate(curios):
            curio_table_widget.setItem(row, 0, QTableWidgetItem(name))
            curio_table_widget.setItem(row, 1, QTableWidgetItem(description))

        layout = QVBoxLayout(curio_tab)
        layout.addWidget(curio_table_widget)

        # 奇物フォントサイズを変更
        for row, (path, japanese) in enumerate(curios):
            item1 = QTableWidgetItem(path)
            item1.setFont(QFont('Arial', 30))  # フォントサイズを30に設定
            item2 = QTableWidgetItem(japanese)
            item2.setFont(QFont('Arial', 30))  # フォントサイズを30に設定
            curio_table_widget.setItem(row, 0, item1)
            curio_table_widget.setItem(row, 1, item2)
        # 行と列の大きさを設定
        for i in range(len(curios)):
            curio_table_widget.setRowHeight(i, 75)  # 行の高さを75に設定
            curio_table_widget.setColumnWidth(0, 500)  # 日本語の列の幅を600に設定
            curio_table_widget.setColumnWidth(1, 800)  # 英語の列の幅を800に設定
        # 一番上の行と一番左の列を非表示にする
        curio_table_widget.verticalHeader().setVisible(False)
        curio_table_widget.horizontalHeader().setVisible(False)      
        
        # カスタムサイコロタブ
        dice_tab = QWidget()
        simulated_universe_tab.addTab(dice_tab, "カスタムサイコロ")

        # カスタムサイコロデータを追加
        dices = [
                ('プーマン推演','Trotter Extrapolation'),
                ('行人の共生','Walker Symbiosis'),
                ('長距離ビーコン','Ultra-Remote Beacon'),
                ('イベント推演','Occurrence Extrapolation'),
                ('戦闘推演','Combat Extrapolation'),
                ('追猟','PUrsuit'),
                ('カウントダウン','Countdown'),
                ('琥珀の防壁','Amber Barrier'),
                ('投資と売却','Investment Sale'),
                ('カンパニー時刻','Company Time'),
                ('奇物推演','Cuiro Extrapolation'),
                ('データ膨張','Data Inflation')
        ]

        # カスタムサイコロタブに新しいテーブルウィジェットを追加
        dice_table_widget = QTableWidget()
        dice_table_widget.setColumnCount(2)
        dice_table_widget.setRowCount(len(dices))

        # データを追加2
        for row, (name, description) in enumerate(dices):
            dice_table_widget.setItem(row, 0, QTableWidgetItem(name))
            dice_table_widget.setItem(row, 1, QTableWidgetItem(description))

        layout = QVBoxLayout(dice_tab)
        layout.addWidget(dice_table_widget)

        # カスタムサイコロフォントサイズを変更
        for row, (path, japanese) in enumerate(dices):
            item1 = QTableWidgetItem(path)
            item1.setFont(QFont('Arial', 30))  # フォントサイズを30に設定
            item2 = QTableWidgetItem(japanese)
            item2.setFont(QFont('Arial', 30))  # フォントサイズを30に設定
            dice_table_widget.setItem(row, 0, item1)
            dice_table_widget.setItem(row, 1, item2)
        # 行と列の大きさを設定
        for i in range(len(dices)):
            dice_table_widget.setRowHeight(i, 75)  # 行の高さを75に設定
            dice_table_widget.setColumnWidth(0, 400)  # 日本語の列の幅を600に設定
            dice_table_widget.setColumnWidth(1, 600)  # 英語の列の幅を800に設定
        # 一番上の行と一番左の列を非表示にする
        dice_table_widget.verticalHeader().setVisible(False)
        dice_table_widget.horizontalHeader().setVisible(False)
            
        # サイコロ面タブ
        dice_face_tab = QWidget()
        simulated_universe_tab.addTab(dice_face_tab, "サイコロ面")

        # データを追加
        dice_faces = [
            ('ビーコン・幾何','Beacon: Geometry'),
            ('ビーコン・想像','Beacon: Imagination'),
            ('ビーコン・置き換え','Beacon:Replacement'),
            ('ビーコン・獲物','Beacon: Prey'),
            ('ビーコン・シャッフル','Beacon:Shuffle'),
            ('ビーコン・無限','Beacon: Infinitiy'),
            ('ビーコン・親しみ','Beacon: Intimacy'),
            ('ビーコン・抽象','Beacon: Abstraction'),
            ('エリア・売り','Domain: Sell'),
            ('エリア・代価','Domain: Cost'),
            ('エリア・情緒','Domain: Emotion'),
            ('エリア・忘却','Domain: Oblivion'),
            ('エリア・社交','Domain: Social'),
            ('エリア・挑戦','Domain: Challenge'),
            ('エリア・経験','Domain: Experience'),
            ('エリア・直感','Domain: Intuition'),
            ('エリア・イド','Domain: Self'),
            ('エリア・連想','Domain: Association'),
            ('エリア・フラクタル','Domain: Classfication'),
            ('エリア・想像','Domain: Creation'),
            ('知識・引き算','Knowledge: Subtraction'),
            ('知識・チップ','Knowledge: Wager'),
            ('知識・原則','Knowledge: Principle'),
            ('知識・等差数列','Knowledge: Arithmetic Progression'),
            ('知識・事前販売','Knowledge: Pre-sale'),
            ('知識・超越','Knowledge: Transcendence'),
            ('知識・推牌','Knowledge: Winning Hand'),
            ('知識・極限','Knowledge: Extreme'),
            ('知識・実証','Knowledge: Evidence'),
            ('知識・狂想','Knowledge: Grandiose Fantasy'),
            ('知識・曲線','Knowledge: Curve'),
            ('知識・保護欲','Knowledge: Protectiveness'),
            ('知識・思考','Knowledge: Reflection'),
            ('異質・インフレ','Heterogeneity: Inflation'),
            ('異質・珍品','Heterogeneity: Treasure'),
            ('異質・再構築','Heterogeneity: Reforge'),
            ('異質・二相性','Heterogeneity: Biphasic'),
            ('異質・異化','Heterogeneity: Alienation'),
            ('異質・利息','Heterogeneity: Interest'),
            ('異質・消費主義','Heterogeneity: Consumerism'),
            ('汎用・壊滅欲','Heterogeneity: Vandalism'),
            ('汎用・トポロジー','Heterogeneity: Topology'),
            ('汎用・無色','General: Colorless'),
            ('汎用・無想','General: Phaseless'),
            ('汎用・揺蕩い','General: Hesitation'),
            ('汎用・弥漫','General: Diffusion'),
            ('汎用・着想','General: Inspiration'),
            ('汎用・推論','General: Deduction'),
            ('汎用・拝聴','General: Attention'),
            ('汎用・観測','General: Observation'),
            ('汎用・感性','General: Snsibility'),
            ('汎用・考証','General: Confirmation'),
            ('汎用・有利','General: Counteract'),
            ('汎用・正義','General: Justice'),
            ('汎用・対奕','General: Duel'),
            ('汎用・指数敵爆発','General: Exponential Explosion'),
            ('汎用・嗅覚','General: Olfactory'),
            ('汎用・冒険傾向','General: Adventure Preference'),
            ('汎用・時間販売','General: Time Trade'),
            ('汎用・質入れ','General: Pawn Shop'),
            ('汎用・抹消','General: Erasure'),
            ('汎用バフ・規律','General Buff: Pattern'),
            ('汎用バフ・法則','General Buff: Law'),
            ('汎用バク・殉道','General Buff: Martyrdom'),
            ('汎用バフ・投資','General Buff: Investment'),
            ('汎用バフ・先手','General Buff: Initiative'),
            ('汎用バフ・仇討ち','General Buff: Vengeance') ,
            ('汎用バフ・限界','General Buff: Baseline'),
            ('汎用・模倣','General: Imitation'),
            ('汎用バフ・迅速','General Buff: Dexterity'),
            ('汎用・回甘','General: Rejuvenation'),
            ('汎用バフ・贔屓','General Buff: Preference'),
            ('汎用バフ・起爆','General Buff: Detonation'),
            ('汎用バフ・脆弱','General Buff: Fragility'),
            ('汎用バフ・バリア','General Buff: Shield'),
            ('汎用・エントロピー増大','General: Entropy'),
            ('汎用・運算','General: Arithmetic'),
            ('汎用・弁証','General: Dialectics'),
            ('汎用・知覚','General: Perception'),
            ('汎用バフ・秘密の匣','General Buff: Select Box')
        ]

        # サイコロ面タブに新しいテーブルウィジェットを追加
        dice_face_table_widget = QTableWidget()
        dice_face_table_widget.setColumnCount(2)
        dice_face_table_widget.setRowCount(len(dice_faces))

        # データを追加2
        for row, (name, description) in enumerate(dice_faces):
            dice_face_table_widget.setItem(row, 0, QTableWidgetItem(name))
            dice_face_table_widget.setItem(row, 1, QTableWidgetItem(description))

        layout = QVBoxLayout(dice_face_tab)
        layout.addWidget(dice_face_table_widget)

        # サイコロ面フォントサイズを変更
        for row, (path, japanese) in enumerate(dice_faces):
            item1 = QTableWidgetItem(path)
            item1.setFont(QFont('Arial', 30))  # フォントサイズを30に設定
            item2 = QTableWidgetItem(japanese)
            item2.setFont(QFont('Arial', 30))  # フォントサイズを30に設定
            dice_face_table_widget.setItem(row, 0, item1)
            dice_face_table_widget.setItem(row, 1, item2)
        # 行と列の大きさを設定
        for i in range(len(dice_faces)):
            dice_face_table_widget.setRowHeight(i, 75)  # 行の高さを75に設定
            dice_face_table_widget.setColumnWidth(0, 300)  # 日本語の列の幅を300に設定
            dice_face_table_widget.setColumnWidth(1, 1000)  # 英語の列の幅を1000に設定
        # 一番上の行と一番左の列を非表示にする
        dice_face_table_widget.verticalHeader().setVisible(False)
        dice_face_table_widget.horizontalHeader().setVisible(False)

        layout = QVBoxLayout(self)
        layout.addWidget(simulated_universe_tab)
        self.setLayout(layout)# 模擬宇宙タブのレイアウト