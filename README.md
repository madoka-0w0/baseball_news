# baseball_news
baseball news picker. pick from yahoo sports news. this is created for Alexa.

## How To Use
```python
from baseball_news_picker.baseball_news_picker import BaseballNewsPicker
from baseball_news_picker.baseball_news_factory import BaseballNewsFactory

if __name__ == '__main__':
    pick = BaseballNewsFactory("中日", BaseballNewsPicker("中日"))
    news = pick.create_news()
    
    print(news.date)
    print("{} vs {}".format(news.my_team, news.battle_team))
    print(news.status)
    print("{} - {}".format(news.my_team_point, news.battle_team_point))
    print(news.news_text)
```
### Output
#### before game
```text
2019-07-04 00:22:38.875034
中日 vs 巨人
試合前
0 - 0

巨人の注目は丸。今季の中日戦では、セ・リーグの対戦カード別でトップとなる打率．３９６をマークしている。相手先発・ロメロからも８打数５安打と好相性の背番号８は、得意な相手から今日も快音を連発できるか。対する中日は、昨日の試合で猛打賞を記録した平田に注目。今季は左投手に対し打率．３１７と好成績を残している。相手先発サウスポー・今村から今夜も快打を放ち、チームを勝利に導けるか。

```
#### after game
```text
2019-06-30 00:00:00
中日 vs 阪神
結果
1 - 0

6月30日（日）中日 vs. 阪神 11回戦
中日が劇的なサヨナラ勝ち。中日は両軍無得点で迎えた延長11回裏、2死一三塁から相手の暴投の間に三塁走者が生還し、試合を決めた。投げては、先発・柳が8回4安打無失点の快投。その後は3人の継投で完封リレーを飾った。敗れた阪神は打線がつながりを欠き、投手陣を援護できなかった。
```