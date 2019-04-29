class Team:
    YOMIURI = "巨人"
    TOKYO = "ヤクルト"
    YOKOHAMA = "DeNA"
    CHUNICHI = "中日"
    HANSHIN = "阪神"
    HIROSHIMA = "広島"

    __team_number_dict = {
        YOMIURI: 1,
        TOKYO: 2,
        YOKOHAMA: 3,
        CHUNICHI: 4,
        HANSHIN: 5,
        HIROSHIMA: 6,
    }
    __team_name_dict = {
        "巨": YOMIURI,
        "ヤ": TOKYO,
        "デ": YOKOHAMA,
        "中": CHUNICHI,
        "神": HANSHIN,
        "広": HIROSHIMA,
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
