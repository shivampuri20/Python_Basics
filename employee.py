class Employee:

    def __init__(self, first, last,pay):
        self.first = first
        self.last = last
        self.pay =pay

    @property   # it is added because we do not want to access email as method but as attribute.
    def email(self):
        return '{}{}@gmail.com'.format(self.first, self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

