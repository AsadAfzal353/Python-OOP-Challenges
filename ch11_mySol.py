
class ValidatedScore:
    def __init__(self, score=130, class_name= None, min_score= 130, max_score=340):
        self.score = score
        self.class_name = class_name
        self.low = min_score
        self.high = max_score
        
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, onwer):
        if instance is None:
            return self
        return instance.__dict__.get(f"{self.class_name}_{self.name}", None)

    def __set__(self, instance, value):
        if not (self.low <= value <= self.high):
            raise ValueError(f"Score must fall between {self.low} and {self.high}")
        elif type(value) != int:
            raise TypeError("Score must be an integer")
        else:
            instance.__dict__[f"{self.class_name}_{self.name}"] = value
        
    def __delete__(self, instance):
            del instance.__dict__[f"{self.class_name}_{self.name}"]
            

class SATScore(ValidatedScore):
    def __init__(self, score=400):
        super().__init__(score=400, class_name=self.__class__.__name__, min_score=400, max_score=1600)

class GREScore(ValidatedScore):
    def __init__(self, score=130):
        super().__init__(score=130, class_name=self.__class__.__name__, min_score=130, max_score=340)



class StudentProfile():
    sat = SATScore()
    gre = GREScore()
    def __init__(self, name=None, sat= 400, gre=130):
        self.name = name
        self.sat = sat
        self.gre = gre

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, sat={self.sat}, gre={self.gre})"


if __name__ == "__main__":

    sp = StudentProfile(name="Andrew", sat=1220, gre=130)
    sp # StudentProfile(name='Andrew', sat=1220, gre=130)

    sp.__dict__
    # {'name': 'Andrew', 'SATScore_sat': 1220, 'GREScore_gre': 130}

    sp2 = StudentProfile("Liza", sat=400, gre=190)
    sp2 # StudentProfile(name='Liza', sat=400, gre=190)

    sp2.gre = 2000 # ValueError: Score must fall between 130 and 340

    sp2.gre = 1200.2 # TypeError: Score must be an integer