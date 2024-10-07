from abc import ABC,abstractmethod

# abstract method ko class bandaina
class Computer(ABC):
    
    def run(self,app):   
        self.process(app)
        
    @abstractmethod
    def process(self,app):
        pass
    
class Mobile(Computer):
    def process(self,app):
        print("mobile is runnning",app)
        
samsung=Mobile()
samsung.run("pubg")
    