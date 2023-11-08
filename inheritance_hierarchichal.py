class Father:
    def __init__(self, name):
        self.fname = name


class Son1(Father):
    def __init__(self, father, name):
        super().__init__(father)
        self.s1name = name


class Son2(Father):
    def __init__(self, father, name):
        super().__init__(father)
        self.s2name = name
