
from random import choice

class Password:
    # static variables
    db_dict = {
        "letters" : ["a", "A", "b", "B", "c", "C",
                     "d", "D", "e", "E", "f", "F",
                     "g", "G", "h", "H", "i", "I",
                     "j", "J", "k", "K", "l", "L",
                     "M", "m", "n", "N", "o", "O",
                     "p", "P", "q", "Q", "r", "R", 
                     "s", "S", "t", "T", "u", "U", 
                     "v", "V", "w", "W", "x", "X",
                     "y", "Y", "z", "Z"],
            
        "numbers" : [0, 1, 2, 3, 4,
                     5, 6, 7, 8 ,9],
            
        "punctuations" : ["`", "~", "!", "@", "#",
                          "$", "%", "^", "&", "*",
                          "(", ")", "-", "_", "=",
                          "+", "{", "}", "[", "]",
                          ";", ":", "|", "<", ">",
                          ",", ".", "?", "/", "'"]
            }
    
    default_lengths = {
                        "low": 8,
                        "mid": 12,
                        "high": 16
                    }
            

    # instance variables
    def __init__(self, strength="mid", length=None):
        self.strength = strength
        self.length = length
        self.set_lst()
        self.gen_password()


    # instance methods
    def set_lst(self):
        if (self.strength == "low"):
            self.lst = self.db_dict["letters"]
        elif (self.strength == "mid"):
            self.lst = self.db_dict["letters"] + \
                        self.db_dict["numbers"]
           
        elif (self.strength == "high"):
            self.lst = self.db_dict["letters"] + \
                        self.db_dict["numbers"] + \
                        self.db_dict["punctuations"]
        else:
            raise NameError("Invalid strength!")
        return self.lst

    def gen_password(self):
        self.password = []
        if not (self.length): # if no length given
            pass_len = self.default_lengths.get(self.strength, None)
        else:
            pass_len = self.length
            if not (pass_len):
                raise NameError("Invalid strength!")
        
        for i in range(pass_len):
            chr = choice(self.lst)
            self.password.append(chr)

        self.password = ''.join(map(str,self.password))
        return self.password

    def show_input_universe(self):
        return self.db_dict;


if __name__ == "__main__":

    p1 = Password(strength="low")
    p1.password # LAyuu4EI

    p2 = Password(strength="mid", length=37)
    p2.password # D6tjKt885vM2U5IwHYqhr9aL6SbIBhHJ16gZf

    p3 = Password(strength="high")
    p3.password # 71'Z>fG{9gIUQQ2a

    p4 = Password()
    p4.password # IGYY2veeqz1Q