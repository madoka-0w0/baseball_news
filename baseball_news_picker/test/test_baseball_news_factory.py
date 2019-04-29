import unittest
from unittest.mock import Mock
from baseball_news_picker.baseball_news_factory import BaseballNewsFactory
from datetime import datetime
from bs4 import BeautifulSoup


class BaseballNewsFactoryTest(unittest.TestCase):
    def test_create_news(self):
        with open("sample.html", "r")as f:
            soup = BeautifulSoup(f, "html.parser")
            news_picker = Mock()
            news_picker.get_page.return_value = soup
            news_picker.get_schedule_page.return_value = soup

            # 試合があるケース
            _date = datetime(2019, 4, 27)
            factory = BaseballNewsFactory("中日", news_picker)
            news = factory.create_news(_date)

            self.assertEqual(news.my_team, "中日")
            self.assertEqual(news.battle_team, "阪神")
            self.assertEqual(news.my_team_point, 5)
            self.assertEqual(news.battle_team_point, 4)
            self.assertEqual(news.status, "結果")
            self.assertEqual(news.date, _date)

            # 試合なし
            _date = datetime(2019, 4, 26)
            factory = BaseballNewsFactory("中日", news_picker)
            news = factory.create_news(_date)

            self.assertEqual(news.my_team, "中日")
            self.assertEqual(news.battle_team, "")
            self.assertEqual(news.my_team_point, 0)
            self.assertEqual(news.battle_team_point, 0)
            self.assertEqual(news.status, "試合なし")
            self.assertEqual(news.date, _date)


if __name__ == '__main__':
    unittest.main()
