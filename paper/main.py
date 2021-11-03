from requests_html import HTMLSession

session = HTMLSession()

url = 'https://news.google.com/topstories?hl=ru&gl=RU&ceid=RU:ru'

r = session.get(url)

r.html.render(sleep=1, scrolldown=5)

articles = r.html.find('article')

print(articles)