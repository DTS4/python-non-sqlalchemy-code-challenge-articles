class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    def __init__(self, name):
        if not isinstance(name,str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name
        self._articles = []

    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        if not isinstance(magazine,Magazine):
            raise ValueError("Magazine must be an instance of the Magazine class.")
        new_article=Article(self, magazine, title)
        self._articles.append(new_article)
        magazine._article.append(new_article)

    def topic_areas(self):
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass