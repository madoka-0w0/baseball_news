class Team:
    YOMIURI = "巨人"
    TOKYO = "ヤクルト"
    YOKOHAMA = "DeNA"
    CHUNICHI = "中日"
    HANSHIN = "阪神"
    HIROSHIMA = "広島"

    SEIBU = "西武"
    NICHIHAMU = "日本ハム"
    LOTTE = "ロッテ"
    ORIX = "オリックス"
    SOFTBANK = "ソフトバンク"
    RAKUTEN = "楽天"

    __team_number_dict = {
        YOMIURI: 1,
        TOKYO: 2,
        YOKOHAMA: 3,
        CHUNICHI: 4,
        HANSHIN: 5,
        HIROSHIMA: 6,
        SEIBU: 7,
        NICHIHAMU: 8,
        LOTTE: 9,
        ORIX: 11,
        SOFTBANK: 12,
        RAKUTEN: 376
    }
    __team_name_dict = {
        "巨": YOMIURI,
        "ヤ": TOKYO,
        "デ": YOKOHAMA,
        "中": CHUNICHI,
        "神": HANSHIN,
        "広": HIROSHIMA,
        "西": SEIBU,
        "日": NICHIHAMU,
        "ロ": LOTTE,
        "オ": ORIX,
        "ソ": SOFTBANK,
        "楽": RAKUTEN,
    }

    @staticmethod
    def get_name(omit_team_name):
        return Team.__team_number_dict.get(omit_team_name)

    @staticmethod
    def get_number(team_name):
        return Team.__team_number_dict.get(team_name)

    @staticmethod
    def is_baseball_team(team):
        return team in Team.__team_number_dict
