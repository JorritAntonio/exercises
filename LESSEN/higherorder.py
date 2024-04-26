
class Persoon:
    def __init__(self,naam,leeftijd,land):
        self.naam = naam
        self.leeftijd = leeftijd
        self.land = land

def check_age_lower_then_18(persoon):
    if persoon.leeftijd >= 18:
        return True
    else:
        return False

def is_allowed(fucntie,personen):
    return [p for p in personen if fucntie (p)]

p1 = Persoon("Serhat", 27, "Belgie")
p2 = Persoon("Tom", 12, "Rusland")
p3 = Persoon("Jef", 40, "Spanje")

personen = [p1,p2,p3]
filtered_personen = is_allowed(check_age_lower_then_18,personen)