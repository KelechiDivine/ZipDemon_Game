import pandas as pd

class UserSignUp():
    
    # create a constructor that returns the object of the class
    
    def __int__(self, firstname, email,  lastname, username, mobileNumber, password, dateOfBirth):
        self.__user_firstname = firstname
        self.__user_email = email
        self.__user_lastname = lastname
        self.__user_user_name = username
        self.__user_mobile_number = mobileNumber
        self.__user_password = password
        self.__user_date_of_birth = dateOfBirth

    def set_email(self, user_email):
        
        if "@gmail.com" in user_email:
            print("email is valid")
            
        else:
            print("Invalid email")
            
        
            
        self.__user_email= user_email

    def getEmail(self):
        return self.__user_email
        
    def setLastname(self, lastname) :
        print(f"Dear {lastname} " + " I hope you are keeping warm today? ")
        self.__user_lastname = lastname
        
    def getLastname(self) -> str:
        return self.__user_lastname
    
    def setUsername(self, username) :
        print(f"Dear{username}, this could be a permanent username... I hope you'd love it so much!"
              f" It's actually sound nice to call you {username} ")
        self.user_user_name = username
    
    def getUsername(self):
        return self.__user_user_name


    def setFirstName(self, firstname):
        if firstname is None:
            print("username can't be empty")
        
        else:
            print(f"Hi {firstname}")
        self.__user_firstname = firstname

    def getFirstName(self) -> str:
        return self.__user_firstname
    
    
    def setUserMobile(self, mobileNumber):
        while len(mobileNumber) == 13:
    
            if len(mobileNumber > 13):
                Exception("Mobile length of out of bound.")
                
            if "+234" in mobileNumber:
                print(mobileNumber)
                
            else:
                break
            
        if len(mobileNumber) < 11:
            Exception("Invalid phone number format.")
            
        self.__user_mobile_number = mobileNumber

    def getUserMobile(self) -> str:
        return self.__user_mobile_number

    # def setUserPassword(self, password):
    #     self.userp = password
    #
    # def  getUserPassword(self) -> str:
    #     return self.userp
    #
    # def setUerDateOfBirth(self, dob) :
    #     self.userdateob = dob
    #
    # def getUserDateOfBirth(self)-> int:
    #     return self.userdateob
