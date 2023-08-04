from db_con import dbConn as conn

global item,qty

shopping_list = []
x = []
shoes = []
shirts = []
pents = []
perfume = []
belts = []
jackets = []
bill = []

def insertProducts():
    db = conn()                              ### connect database with python 
    res = db.cursor()
    a = int(input("How many products do yo want to insert ? "))
    print("------------------------------------------")
    for a in range (0,a):
        p_name = input("Enter product name : ")
        p_price = input("Enter product price : ")
        p_qty = input("Enter product quantity : ")
        print("------------------------------------------")
        query = "insert into big_bazaar (Product_Name,Product_Price,Product_Qty) values (%s,%s,%s)"   ###   Query to insert products
        values = (p_name, p_price, p_qty)
        res.execute (query,values)
        db.commit()
        print(res.rowcount,"new products are inserted")   
    
def showProducts():    
    db = conn()
    res = db.cursor()
    query = "select * from big_bazaar"   ###  Query to dispaly price and product_name of all products
    res.execute(query)
    data = res.fetchall()
    for x in data:
        print ("Product_Name  : ",x[1],"\t\t Product_Price : ",x[2])         

def getProductPriceShoes():
    db = conn()
    res = db.cursor()
    query = "select Product_Price from big_bazaar where Product_Name='Shoes Men';"
    res.execute(query)
    data = res.fetchall()
    for x in data:        
        cost = x[0] * shoes[0]
        bill.append(cost)
        
def getProductPriceShirts():
    db = conn()
    res = db.cursor()
    query = "select Product_Price from big_bazaar where Product_Name='T-Shirts';"
    res.execute(query)
    data = res.fetchall()
    for x in data:        
        cost = x[0] * shirts[0]
        bill.append(cost)        
        
def getProductPriceTrousers():
    db = conn()
    res = db.cursor()
    query = "select Product_Price from big_bazaar where Product_Name='Trousers';"
    res.execute(query)
    data = res.fetchall()
    for x in data:
        cost = x[0] * pents[0]
        bill.append(cost)

def getProductPriceBelts():
    db = conn()
    res = db.cursor()
    query = "select Product_Price from big_bazaar where Product_Name='Leather Belts';"
    res.execute(query)
    data = res.fetchall()
    for x in data:        
        cost = x[0] * belts[0]
        bill.append(cost)
        
def getProductPricePerfumes():
    db = conn()
    res = db.cursor()
    query = "select Product_Price from big_bazaar where Product_Name='Perfumes';"
    res.execute(query)
    data = res.fetchall()
    for x in data:        
        cost = x[0] * perfume[0]
        bill.append(cost)

def getProductPriceJackets():
    db = conn()
    res = db.cursor()
    query = "select Product_Price from big_bazaar where Product_Name='Jackets Men';"
    res.execute(query)
    data = res.fetchall()
    for x in data:        
        cost = x[0] * jackets[0]
        bill.append(cost)


def userBill():
    print("HEY ! Customer your total bill :",sum(bill))
    if (sum(bill) > 0):
        print("Visit here again ! ......")
    else:
        print("You haven't bought anything yet ! Go ahead and buy now .....")


def addItem():
    n = int(input("How many products you want to buy : "))
    print("------------------------------------")
    for n in range(0,n):
        item = input("Enter product you want to add : ")
        qty = int(input("Enter qyauntity of product : "))
        print("------------------------------------")
        x = {"Product Name" : item,"Product Qunatity" : qty}
        
        if (item == "Shoes Men"):
            shoes.append(qty)
            shopping_list.append(x)
            print(item,"has been added to the list")
            print("------------------------------------")
            getProductPriceShoes()
        
        elif (item == "T-Shirts"):
            shirts.append(qty)
            shopping_list.append(x)
            print(item,"has been added to the list")
            print("------------------------------------")
            getProductPriceShirts()
        
        elif (item == "Trousers"):
            pents.append(qty)
            shopping_list.append(x)
            print(item,"has been added to the list")
            print("------------------------------------")
            getProductPriceTrousers()
        
        elif (item == "Leather Belts"):
            belts.append(qty)
            shopping_list.append(x)
            print(item,"has been added to the list")
            print("------------------------------------")
            getProductPriceBelts()
        
        elif (item == "Perfumes"):
            perfume.append(qty)
            shopping_list.append(x)
            print(item,"has been added to the list")
            print("------------------------------------")
            getProductPricePerfumes()
        
        elif (item == "Jackets Men"):
            jackets.append(qty)
            shopping_list.append(x)
            print(item,"has been added to the list")
            print("------------------------------------")
            getProductPriceJackets()
        
        else:
            print("Item not available !")
            print("------------------------------------")
        

def viewList():
    print("--------------- SHOPPING LIST ---------------\n")
    for i in shopping_list:
        print(i)



def listLength():
    print("There are",len(shopping_list),"items in the shopping list")


def clearList():
    shopping_list.clear()
    bill.clear()
    print("The shopping list is empty now")
    

while(True):
    print("------------------------------------------------- WELCOME  TO  BIG  BAZAAR -------------------------------------------------")
    print("\nAre you Owner or Buyer ? (If you are the Owner and want to enter into admin section....Please input your secret code below..)")
    print("------------------------------------")
    choice = input("Enter secret code OR Enter customer name (Press 0 to exit) : ")
    print("------------------------------------")
    if (choice == "0"):
        print("Thanks and visit again ! ......")
        exit()
    elif (choice == "555"):
        print("Select from the given options to perform any function\n 0. Exit\n 1. Add products to the database\n 2. Show all the products")
        print("------------------------------------")
        input1 = int(input("Select your choice : "))
        print()
        if (input1 == 0):
            print("Thanks and visit again ! .....")
            exit()
        elif (input1 == 1):
            insertProducts()
            print("------------------------------------")
        elif (input1 == 2):
            showProducts()
            print("------------------------------------")
        else:
            print("Enter correct number")
     
    
    elif (choice != "555"):
        while (True):
        
            print("Select from the given options to perform any function\n 0. Exit\n 1. Add products to the shopping list\n 2. View Shopping List\n 3. Check no. of products in Shopping List\n 4. Delete all products from Shopping List\n 5. View Total Bill")
            print("------------------------------------")
            input2 = int(input("Select your choice : "))
            print()
            if (input2 == 0):
                print("Thanks and visit again ! .....")
                exit()
            elif (input2 == 1):
                showProducts()
                print("\nYou can buy anything from the above given products")
                print("\n(P.S. Write product name as mentioned above)\n")
                addItem()
                print("------------------------------------")
            elif (input2 == 2):
                viewList()
                print("------------------------------------")
            elif (input2 == 3):
                listLength()
                print("------------------------------------")
            elif (input2 == 4):
                clearList()
                print("------------------------------------")
            elif (input2 == 5):
                userBill()
                print("------------------------------------")
            else:
                print("Enter correct number")
                print("------------------------------------")
                