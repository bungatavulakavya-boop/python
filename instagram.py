class Instagram:
    def __init__(self):
        self.username = "kavya"
        self.__password = 123  
    def setpassword(self, p):
        self.__password = p
    def getpassword(self):
        return self.__password
user = Instagram()
print(user.username)        
print(user.getpassword())   
user.setpassword(456)
print(user.getpassword())
