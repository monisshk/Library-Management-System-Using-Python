#<<<<<<LIBRARY MANAGEMENT SYSTEM>>>>>>

class My_Dictionary:
    def __init__(self,l,n):

        self.l=l
        self.n=n

    def display_books(self):
        print(self.l)

    def lend_book(self,bn):
        self.l.remove(bn)

    def return_book(self,bn):
        self.l.append(bn)

    def add_book(self,bn):
        self.l.append(bn)

l1=["Html","Java","Python","C++","C","PHP"]
l2=[]

def maintain_list(l2,bn):
    l2.append(bn)
dict1={}
obj=My_Dictionary(l1,"My_Dict")


def maintain_dict(dict1,key,value):
    dict1[key]=value

while True:
    inp1=int(input("Press 1 to display books , 2 to lend a book , 3 to return a book 4 to donate a book:\n"))
    if inp1==1:
        obj.display_books()
    elif inp1==2:           # Lend Book
        n=input("Enter your name:")
        obj.display_books()
        print(n)
        bn=input("Enter the book name: ")
        if bn in l1:
            print("Book is available.")
            obj.lend_book(bn)
            maintain_list(l2,bn)
            print(l1)
            print(l2)
            maintain_dict(dict1,bn,n)
            print(dict1)
        else:
            print("Book is unavailable.")
            print("It is taken by ",dict1[bn])
    elif inp1==3:           # Return book
        n=input("Enter your name:")
        bn=input("Enter the book name: ")
        if bn in l2:
            obj.return_book(bn)
            print(11)
            print(l2)
        else:
            print("The book does not belong to our library .....")
    elif inp1==4:
        n=input("Enter your name:")
        bn=input("Enter the book name: ")
        obj.add_book(bn)
        print(l1)
