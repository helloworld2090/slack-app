class superman():
    def __init__(self, num):
        self.num = num
        self.lower = []
    
class low():
    def __init__(self, num1):
        self.num1 = num1


dict1 = {
    "test" : []
}

if __name__ == "__main__":
    first = low(10)
    up = superman(5)
    up.lower.append(first)
    dict1["test"].append(first)

    print("beofre")
    print(up.lower[0].num1)
    print(dict1["test"][0].num1)
    
    print("after")

    dict1["test"][0].num1 = 1000
    print(up.lower[0].num1)
    print(dict1["test"][0].num1)

    print("removing")
    del(up)

    #print(up.lower[0].num1)
    print(dict1["test"][0].num1)

