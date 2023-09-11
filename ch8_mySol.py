from collections import UserDict

class BidirectionalDict(UserDict):

    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        if value in self:
            del self[value]
            
        super().__setitem__(key, value)
        super().__setitem__(value, key)
    
    def __len__(self):
        return super().__len__() // 2
    
    def __delitem__(self, key):
        super().__delitem__(self[key])
        super().__delitem__(key)
    
        
if __name__ == "__main__":

    bd = BidirectionalDict({"code": "more", "sleep": "less"})

    bd["code"] # 'more'
    bd["more"] # 'code'
    bd

    bd # {'code': 'more', 'more': 'code', 'sleep': 'less', 'less': 'sleep'}
    len(bd) # 2

    bd["code"] = "better"
    # bd["better"] # 'live'
    bd

    bd.update([("sleep", "deeper")])
    bd["deeper"] # 'sleep'

    bd

    bd.pop("sleep")
    bd # {'code': 'better', 'better': 'code'}

    del bd['code']
    bd # {}
