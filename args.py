def number(*numbers):
    total=0
    for x in numbers:
        total+=x
    print(total)

number(1,2,3)

def person(*names):
    for name in names:
        print(f"My name is {name}")
        
person("samarpan","sadil","anmol")

# args ma arguments haru tupples ma indexed bhayera save hunchan