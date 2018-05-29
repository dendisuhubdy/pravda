from goose import Goose

class site(object):
    def __init__(self, url):
        self.url = url
        self.article = self.getArticle()

    def getArticle(self, url):
        g = Goose()
        article = g.extract(url=self.url)
        print(article)
