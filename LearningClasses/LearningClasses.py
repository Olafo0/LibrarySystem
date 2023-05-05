
from User_inforation_class import UserInfo 

# Objects are stored here
user_info = []

books = ["Harry Potter","Macbeth","One piece"]


def starter():
    print("1) Register\n2) Loan_book")
    
    return int(input("Please enter your selection (1-3) :"))

def register():
    #name = str(input("please enter your name"))
    #surname = str(input("pleaes enter your surname"))
    #id = int(input("please enter your id"))

    user_input = UserInfo("Oalf","Lo",1),UserInfo.BookInfo("Harry Potter",3)
    user_input1 = UserInfo("NooWMan","Yurr",2),UserInfo.BookInfo("Macbeth",4)
    
    # Data is formated in a way to prevent a tuple, which caused problems with program later on
    format_data = [user_input[0],[user_input[1]]]
    format_data1 = [user_input1[0],[user_input1[1]]]
    user_info.append(format_data)
    user_info.append(format_data1) 
    
    print("\n"*10)

def loan_book():

    def offer_book():
        print("\n"*20)
        print("------- User Details")
        print("NAME :",users[0].name)
        print("LASTNAME :",users[0].surname)
        print("--- Books taken out")
        for i in range(0,len(user_info[0][1])):
            print("*",users[1][i].book_name)
        print()
        print()
        print("Books availble to loan")
        for i in range(0, len(books)):
            print(f"{i+1}) {books[i]}")
        print()
        
        requested_book = int(input("Please enter what book you want (1-3) :"))
        requested_book -= 1
        print(f"Requested book : {books[requested_book]}")
        book_added = UserInfo.BookInfo(f"{books[requested_book]}",0)
        print(book_added)
        element_index = user_info.index(users)
        print(element_index)
        user_info[element_index][1].append(book_added)

    user_id = int(input("Please enter your user ID"))

    for users in user_info:
        if users[0].id == user_id:
            print(users)
            offer_book()
        else:
            pass

while True:
    user_starter_choice = starter()

    if user_starter_choice == 1:
        register()
    elif user_starter_choice == 2:
        loan_book()
    else:
        print("ERROR: 23")

