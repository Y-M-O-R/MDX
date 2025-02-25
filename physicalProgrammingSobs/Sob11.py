import random
class book:
    def __init__(self, name, stock):
        self.name=name
        self.stock=stock
        #self.borrow=borrow
        
        self.isbn = f'ISBN {random.randint(900,999)}-{random.randint(10,99)}-{random.randint(10000,99999)}-{random.randint(10,99)}-{random.randint(1,9)}'
    def __repr__(self):
        return f'Title- {self.name}, InStock- {self.stock}, {self.isbn}'
    
    def nameCall(self):
        print(self.name)
    
    def borrow(self):
        if self.stock<0:
            print("This book is out of stock")
        else:
            self.stock-=1
            
    
    def ret(self):
        self.stock+=1 
    

libraryList = {}
libraryList['myBook']= book("The Hobbit", 4)


# this code is demonstrating how to use the class 
option = int(input("Are you a Libarian -0  or Customer -1 "))
if option == 0: # libarian system
    option2 = int(input("Will you like to Modify -0 or add a Book -1"))
    if option2 == 0:
        pass
    elif option2 == 1:
        run = True
        while run:
            
            bookDetails = input("Book ID, Book Name, Stock")
            bookDetails = bookDetails.split(",")
            libraryList[bookDetails[0]]=  book(bookDetails[1],int(bookDetails[2]))# uses the class using name and stock and stores it in dictionary using the Id
            
            option3 = int(input("Exit -0, Addmore -1"))
            if option3 ==0:
                run = False
                
    
print(libraryList)