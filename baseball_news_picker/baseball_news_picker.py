from urllib.parse import urlencode

from baseball_news_picker.model.team import Team
from baseball_news_picker.news_picker import NewsPicker


class BaseballNewsPicker(NewsPicker):
    NEWS_URL_FORMAT = "https://baseball.yahoo.co.jp/npb/teams/{}"
    SCHEDULE_URL_FORMAT = NEWS_URL_FORMAT + "/schedule"

    def __init__(self, team_name):
        team_num = Team.get_number(team_name)
        self.__news = self.NEWS_URL_FORMAT.format(team_num)
        self.__schedule = self.SCHEDULE_URL_FORMAT.format(team_num)

    def get_schedule_page(self, _date):
        year_month = _date.strftime('%Y-%m')
        page = self.get_page("{}?{}".format(self.__schedule, urlencode({"month": year_month})))
        return page
