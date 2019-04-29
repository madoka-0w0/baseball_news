from datetime import datetime
from baseball_news_picker.model.team import Team
from baseball_news_picker.model.game_status import GameStatus


class BaseballNews(object):
    def __init__(self):
        self.__my_team = ""
        self.__battle_team = ""
        self.__my_team_point = 0
        self.__battle_team_point = 0
        self.__status = ""
        self.__news_text = ""
        self.__date = None

    @property
    def my_team(self):
        return self.__my_team

    @my_team.setter
    def my_team(self, value):
        if Team.is_baseball_team(value):
            self.__my_team = value

    @property
    def battle_team(self):
        return self.__battle_team

    @battle_team.setter
    def battle_team(self, value):
        if Team.is_baseball_team(value):
            self.__battle_team = value

    @property
    def my_team_point(self):
        return self.__my_team_point

    @my_team_point.setter
    def my_team_point(self, value):
        if isinstance(value, int):
            self.__my_team_point = value

    @property
    def battle_team_point(self):
        return self.__battle_team_point

    @battle_team_point.setter
    def battle_team_point(self, value):
        if isinstance(value, int):
            self.__battle_team_point = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        if isinstance(value, str):
            self.__status = value

    @property
    def news_text(self):
        return self.__news_text

    @news_text.setter
    def news_text(self, value):
        if isinstance(value, str):
            self.__news_text = value

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        if isinstance(value, datetime):
            self.__date = value

    def issue(self):
        return self.my_team_point > self.battle_team_point

    def have_game(self):
        return not (self.status == GameStatus.NO_GAME
                    or self.status == GameStatus.CALLED_OFF)
