class LengthConverter:
    feet_per_m = 3.28084
    inch_per_m = 39.3701

    def __init__(self):
        self.__length_in_meter = 0

    @property
    def meter(self):
        return self.__length_in_meter

    @meter.setter
    def meter(self, value):
        self.__length_in_meter = value

    @property
    def feet(self):
        return self.__length_in_meter * LengthConverter.feet_per_m

    @feet.setter
    def feet(self, value):
        self.__length_in_meter = value / LengthConverter.feet_per_m

    @property
    def inch(self):
        return self.__length_in_meter * LengthConverter.inch_per_m

    @inch.setter
    def inch(self, value):
        self.__length_in_meter = value / LengthConverter.inch_per_m
