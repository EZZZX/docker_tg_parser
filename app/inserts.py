# # 1 - imports
# from datetime import date

# from user import User
# from base import Session, engine, Base
# from article import Article

# from parser  import get_current_news

# Base.metadata.create_all(engine)
# session = Session()

# user_1 = User(1413049174, 1631541675.6310208, "active")


# # 5 - creates actors
# article_1 = Article("binance-limits-sgd-product-offerings-in-singapore-amid-regulatory-warnings", "Binance limits SGD product offerings in Singapore amid regulatory warnings", date(2021,9,5), 1630856371.7474759, "https://cointelegraph.com/news/binance-limits-sgd-product-offerings-in-singapore-amid-regulatory-warnings", "The Monetary Authority of Singapore placed Binance on its investor alert list on Sept.1 over concerns that the crypto exchange may have violated local payments regulations.")

# fresh_news = get_current_news()
# if len(fresh_news) > 0:
#     for k, v in fresh_news.items():
#         # print(v['article_title'])
#         if (session.query(Article.id).filter(id == k).first() is None):
#             session.add(Article(k,v['article_title'], v['article_date'], v['article_time'], v['article_link'], v['article_description']))


# # 9 - persists data
# # session.add(article_1)
# session.add(user_1)


# # 10 - commit and close session
# session.commit()
# session.close()