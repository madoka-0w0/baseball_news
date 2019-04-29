#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import random

from alexa.alexa_context import AlexaHandler
from baseball_news_picker.baseball_news_factory import BaseballNewsFactory
from baseball_news_picker.baseball_news_picker import BaseballNewsPicker
from alexa.settings import settings


class AlexaListener(AlexaHandler):
    speak_text = ["今日も一日お疲れ様です。ゆっくり休みましょう。", "ぴっぴかちゅう"]

    def __init__(self):
        super().__init__("試合の結果を教えて、または昨日の結果を教えてと言ってください。")

    def lambda_handler(self, event, context):
        request = event['request']
        request_type = request['type']
        intent = request.get('intent', {})
        if request_type == 'LaunchRequest' or (
                request_type == "IntentRequest" and intent.get("name") == 'GetNewsIntent'):
            return self.get_news(intent, context)
        return super().lambda_handler(event, context)

    def get_news(self, intent, session):
        row_date = None
        if intent:
            slot = intent.get('slots')
            if slot:
                _date = slot.get('Date')
                if _date:
                    row_date = _date.get('value')
        if row_date is None:
            date = datetime.date.today()
        else:
            date = datetime.datetime.strptime(row_date, "%Y-%m-%d")
        picker = BaseballNewsFactory(settings.team_name, BaseballNewsPicker(settings.team_name))
        news = picker.create_news(date)

        if news.have_game(date):
            if news.issue():
                return self.emit(news.news_text)
            else:
                index = random.randrange(len(self.speak_text))
                return self.speak_text[index]
        else:
            return self.emit("試合はありませんでした。")
