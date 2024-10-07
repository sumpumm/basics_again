class Grandfather:
    house="thuylo ghar"
        
class Father(Grandfather):
    def __init__(self,car) -> None:
        self.car=car
    
grandfather=Grandfather()
father=Father("BMW")
print(father.house)