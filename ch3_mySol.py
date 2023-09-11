
class Contact:

    def __init__(self, name, last_name, phone=None, email=None, display_mode="masked"):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.display_mode = display_mode
    
    # The trigger to the unmasked output can be through any formatting being done or the display
    def __repr__(self):
        if (self.display_mode == "masked"):
            self.hideName()
            return f"Contact(name={self.name}, last_name={self.last_name})"
        else:
            return f"Contact(name={self.name}, last_name={self.last_name}, phone={self.phone}, email={self.email})"
            
    def __format__(self, format_str):
        if (format_str != None or self.display_mode != "masked"):
            return f"Contact(name={self.name}, last_name={self.last_name}, phone={self.phone}, email={self.email})"
        return self.__repr__()

    def __str__(self):
        return f"{self.last_name[0]}{self.name[0]}"
    
    def __eq__(self, other):
        if not isinstance(other, Contact):
            return False
        
        cond1 = (self.phone and self.phone == other.phone) or (self.email and self.email == other.email)            
        cond2 = (self.name == other.name) and (self.last_name == other.last_name)
        return (cond1 or cond2) 
    
    def hideName(self):
        count1 = 0
        for i in self.name:
            if (count1 > 1):
                self.name = self.name.replace(i, "*")
            count1 += 1
        
        count2 = 0
        for j in self.last_name:
            if (count2 > 1):
                self.last_name = self.last_name.replace(j, "*")
            count2 += 1

        return self
    

if __name__ == "__main__":

    c1 = Contact("Andy", "Bek")
    c2 = Contact("Andy", "Bek", "647-537-9271")
    c3 = Contact("Andrew", "Bek", "647-537-9271", "hey@andybek.com")
    c4 = Contact("Andy", "Bek", "647-537-9271", display_mode="show")

    c2 == c3 # True # because the phone number is the same

    c1 # Contact(name=An***, last_name=B**)

    str(c1) # 'BA'

    "{c:unmasked}".format(c=c1)
    # 'Contact(name=Andy, last_name=Bek, phone=None, email=None)'

    f"{c2:unmasked}"
    # 'Contact(name=Andy, last_name=Bek, phone=647-537-9271, email=None)'

    format(c2, "unmasked")
    # 'Contact(name=Andy, last_name=Bek, phone=647-537-9271, email=None)'