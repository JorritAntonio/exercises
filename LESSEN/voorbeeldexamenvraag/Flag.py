class Flag:
    def __init__(self, country, colors, horizontal):
        self.country = country
        self.colors = colors
        self.horizontal = horizontal


    @property
    def colors(self):
        return self.__colors    

    @colors.setter
    def colors(self, value):
        if value is None or len(value) == 0:
            raise ValueError()
        self.__colors = value

    