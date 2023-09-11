
from random import randint

class VisaMixin():
    def generate(self):
        return [4,2] + super().generate()

class MasterCardMixin():
    def generate(self):
        return [5,3] + super().generate()

class ValidMixin():
    def generate(self):
        cumsum = 0
        count = 0
        for n in reversed(super().generate()[:-1]):
            if count%2 == 0:
                cumsum += sum([int(i) for i in str(2*n)]) if 2*n > 9 else 2*n
            count += 1
        return super().generate()[:-1] + [10-cumsum%10]

class CreditCard():

    def __init__(self):
        self._number = self.generate()

    def generate(self):
            return [randint(0,9) for _ in range(14)]
    
    @property
    def number(self):
        return " ".join(["".join(map(str,(self._number[i:i+4]))) \
                         for i in range(0, len(self._number), 4)])
    

if __name__ == "__main__":

    class Visa(VisaMixin, CreditCard):
        pass

    Visa().number # 4266 8886 0014 6408

    class MasterCard(ValidMixin, MasterCardMixin, CreditCard):
        pass

    MasterCard().number # 5223 3755 8832 5379