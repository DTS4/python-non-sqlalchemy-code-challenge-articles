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
    _all = []
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self.name = name
        self.category = category
        self._articles = []

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})


    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        from collections import Counter
        author_counts = Counter(article.author for article in self._articles)
        authors = [author for author, count in author_counts.items() if count > 2]
        return authors if authors else None
    
    @classmethod
    def top_publisher(cls):
        if not cls._all:
            return None
        return max(cls._all, key=lambda magazine: len(magazine.articles), default=None)