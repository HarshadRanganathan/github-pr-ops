class PullRequest:
    def __init__(self, title='', url='', author='', days_since=''):
        self.title = title
        self.url = url
        self.author = author
        self.days_since = days_since

    def __str__(self):
        return f'{self.title} | {self.body} | {self.url}'
