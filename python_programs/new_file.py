class myclass:
    def __init__(aman): #Constructor
        print("It is constructor ")
        aman.a =0
        aman.b = 10
    def data(swag):
        swag.a = int(input("Enter your number :"))
        swag.b = int(input("Enter your number b:"))


    def dis(awa):
        print("a =",awa.a)
        print("b= ",awa.b)


d1 = myclass
d1.data(3)
d1.dis()
print("********************")