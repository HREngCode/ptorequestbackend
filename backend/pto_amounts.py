class Accrual:
    def __init__(self, service, value):
        self.service = service
        self.value = value


class Level_One(Accrual):
    def __init__(self):
        super(Level_One, self).__init__("Level_One", 4.0000)


class Level_Two(Accrual):
    def __init__(self):
        super(Level_Two, self).__init__("Level_Two", 5.0000)


class Level_Three(Accrual):
    def __init__(self):
        super(Level_Three, self).__init__("Level_Three", 6.0000)


class Level_Four(Accrual):
    def __init__(self):
        super(Level_Four, self).__init__("Level_Four", 7.0000)


class Level_Five(Accrual):
    def __init__(self):
        super(Level_Five, self).__init__("Level_Five", 8.0000)