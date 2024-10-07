class Pizza:
    def dough(self):
        print("Pizza ko dough banyo")
        return self
    
    def sauce(self):
        print("red tomato sauce halye")
        return self
        
    def cheese(self):
        print("Cheese halye")
        return self
    
object=Pizza()
object.dough().sauce().cheese()
        