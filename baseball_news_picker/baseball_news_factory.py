import re
from datetime import datetime

from baseball_news_picker.baseball_news_picker import BaseballNewsPicker
from baseball_news_picker.model.baseball_news import BaseballNews
from baseball_news_picker.model.game_status import GameStatus
from baseball_news_picker.model.team import Team


class BaseballNewsFactory:
    def __init__(self, team_name, news_picker: BaseballNewsPicker):
        self.team_name = team_name
        self.__news_picker = news_picker

    def create_news(self, _date=None):
        _date = datetime.now() if _date is None else _date

        news = BaseballNews()
        news.my_team = self.team_name
        news.date = _date
        news.status = self.__get_status(_date)

        if news.have_game():
            news.news_text = self.__get_news_text(_date)
            news.my_team_point, news.battle_team_point = self.__get_scores(_date)
            news.battle_team = self.__get_battle_team(_date)
        return news

    def __get_date_elements(self, _date):
        elements = self.__news_picker.get_schedule_page(_date)
        tds = elements.find_all("td")
        for td in tds:
            em = td.find(class_="bb-calendarTable__date")
            if em is not None:
                if em.text == str(_date.day):
                    return td

    def __get_status(self, _date):
        element = self.__get_date_elements(_date)
        status = element.find(class_="bb-calendarTable__status")
        if status:
            return status.text.strip()
        else:
            return GameStatus.NO_GAME

    def __get_scores(self, _date):
        """
        my team, battle teamの順でスコアを返却する
        """
        pattern = "[0-9]+"

        element = self.__get_date_elements(_date)
        if element:
            span = element.find("p", class_="bb-calendarTable__score")
            win = span.find(class_="bb-calendarTable__win") is not None
            if span.text:
                score = re.findall(pattern, span.text)
                if len(score) == 2:
                    scores = [int(score[0]), int(score[1])]
                    if win:
                        scores = sorted(scores, reverse=True)
                    else:
                        scores = sorted(scores)
                    return scores[0], scores[1]
        return 0, 0

    def __get_news_page(self, _date):
        element = self.__get_date_elements(_date)
        if element:
            a = element.find("a", class_="bb-calendarTable__status")
            if a:
                url = a.get("href")
                if url:
                    return self.__news_picker.get_page(url)

    def __get_news_text(self, _date):
        news_elem = self.__get_news_page(_date)
        if news_elem:
            div = news_elem.find("p", class_="bb-paragraph")
            if div:
                return div.text

    def __get_battle_team(self, _date):
        element = self.__get_date_elements(_date)
        if element:
            span = element.find("a", class_="bb-calendarTable__versusLogo")
            href = span.get("href")
            team_id = int(href.split("/")[3])
            return Team.get_team(team_id)
