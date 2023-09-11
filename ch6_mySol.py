
class Tablet:

    max_memory = 1024
    model_types = {"lite": (2, 32),
                   "pro": (3, 64),
                   "max": (4, 128)}
    
    def __init__(self, model):
        self.model = model
        self._added_storage = 0
        self._storage = 0
        
    
    def __repr__(self):
        return f'Tablet(model="{self._model}", base_storage={self._base_storage}, added_storage={self._added_storage}, memory={self._memory})'
    
    @property
    def memory(self):
        return self._memory
    
    @property
    def base_storage(self):
        return self._base_storage
    
    @property
    def storage(self):
        self._storage = self._base_storage + self._added_storage
        return self._storage
    
    @storage.setter
    def storage(self, amount):
        self._added_storage = 0
        if  (amount-self._base_storage < 0) or (amount-self._base_storage > self.max_memory):
            raise ValueError("Memory cannot exceed 1024 or less than base storage")
        self._added_storage = amount - self._base_storage 


    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, value):
        value = value.lower()
        if value not in self.model_types.keys():
            raise ValueError("Unrecognized model")
        else:
            self._model = value
            self._memory, self._base_storage = self.model_types[value]
    
    def add_storage(self, amount):
        if (self.base_storage + amount > self.max_memory):
            raise ValueError("Memory cannot exceed 1024")
        self._added_storage += amount


if __name__ == "__main__":

    t1 = Tablet("lite")
    t2 = Tablet("pro")
    t1 # Tablet(model="lite", base_storage=32, added_storage=0, memory=2)

    Tablet("Batman") # ValueError: Unrecognized model

    t1.add_storage(16)
    t1 # Tablet(model="lite", base_storage=32, added_storage=16, memory=2)

    t1.storage # 48

    t1.storage = 256
    t1 # Tablet(model="lite", base_storage=32, added_storage=224, memory=2)

    t2.storage = 256
    t2 # Tablet(model="pro", base_storage=64, added_storage=192, memory=3)

    t1.add_storage(1024-256) # ValueError: Memory cannot exceed 1024
    t1

    t1.memory
    t1.memory = 2 # AttributeError: can't set attribute

    t1.base_storage # 32

    t1.base_storage = 64 # AttributeError: can't set attribute