class Url:

    def __init__(self, scheme='', authority='', path=None, query=None, fragment=''):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    def __eq__(self, other):
        return self.__str__() == str(other)

    def __str__(self):
        self.url = ''

        if self.scheme != '':
            self.url += self.scheme + '://'

        if self.authority != '':
            self.url += self.authority

        if self.path is not None and isinstance(self.path, list) and len(self.path) > 0:
            self.url += '/' + '/'.join(self.path)

        if self.query is not None and isinstance(self.query, dict) and len(self.query) > 0:
            self.url += '?'
            for key, value in self.query.items():
                self.url += f'{key}={value}&'
            self.url = self.url[:-1]

        if self.fragment != '':
            self.url += '#' + self.fragment

        return self.url


class HttpsUrl(Url):

    def __init__(self, authority='', path=None, query=None, fragment=''):
        super().__init__('https', authority, path, query, fragment)


class HttpUrl(Url):

    def __init__(self, authority='', path=None, query=None, fragment=''):
        super().__init__('http', authority, path, query, fragment)


class GoogleUrl(HttpsUrl):

    def __init__(self, path=None, query=None, fragment=''):
        super().__init__('google.com', path, query, fragment)


class WikiUrl(HttpsUrl):

    def __init__(self, path=None, query=None, fragment=''):
        super().__init__('wikipedia.org', path, query, fragment)


assert GoogleUrl() == HttpsUrl(authority='google.com')
assert GoogleUrl() == Url(scheme='https', authority='google.com')
assert GoogleUrl() == 'https://google.com'
assert WikiUrl() == str(Url(scheme='https', authority='wikipedia.org'))
assert WikiUrl(path=['wiki', 'python']) == 'https://wikipedia.org/wiki/python'
assert GoogleUrl(query={'q': 'python', 'result': 'json'}) == 'https://google.com?q=python&result=json'