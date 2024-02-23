class BMICalculator:
    def __init__(self, weight_in_kg, height_in_m):
        self.kg = weight_in_kg
        self.m = height_in_m

    @property
    def bmi(self):
        return self.kg / self.m**2
    
    @property
    def category(self):
        bmi = self.bmi
        if bmi < 18.5:
            return "underweight"
        if bmi < 25:
            return "normal"
        else:
            return "overweight"
