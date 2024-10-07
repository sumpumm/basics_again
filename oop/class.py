class car:
    # name='something'
    # year="2017"
    # color="red"
    # tyres=4
    
    def set_color(self,color):
        self.color=color
    
    def get_color(self):
        return self.color
    
    # constructor(magic method)
    def __init__(self,name,year):
        print("object created")
        self.name=name
        self.year=year
        
    
        

   
# object
BMW=car("BMW","2017")
print(BMW.name)

obj2=car("hyundai","2003")
obj2.set_color("black")
print(obj2.get_color())