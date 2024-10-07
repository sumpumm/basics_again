# keyvalue pair pass garne ho
# dictionary ma save huncha

def person(**details):
    print(details)
    
person(name="ram",age=12)

# accessing keys
def person(**details):
    print(details['name'])
    
person(name="ram",age=12)