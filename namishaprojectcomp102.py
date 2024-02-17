from functools import reduce
import random
class Account:
    def __init__(self,name,email,address,password,type):
        self.name = name
        self.email = email
        self.address = address
        self.password = password
        self.type = type
    def login(self,password):
        if self.password == password:
            return True
        else:
            return False
class Admin(Account):
    def __init__(self,name,email,address,password,adminid):
        super().__init__(name,email,address,password,'admin')
        self.adminid = adminid
    def addrestaurant(self):
        name = input('Enter name:')
        email = input('Enter email:')
        address = input('Enter address:')
        password = input('Enter password:')
        r_id = input('Enter your restaurant id:')
        global restaurants
        restaurants.append(Restaurant(self,name,email,address,password,r_id))
    def removerestaurant(self,name):
        global restaurants
        for i in restaurants:
            if i.name == name:
                restaurants.remove(i)
    def removecustomer(self,name):
        global customers
        for i in customers:
            if i.name == name:
                customers.remove(i)
class Customer(Account):
    def __init__(self,name,email,address,password,C_id):
        super().__init__(name,email,address,password,'customer')
        self.C_id = C_id
        self.orders = []
    def login(self,password):
        return super().login(password)
    def viewpopular(self):
        global restaurants
        print([i.name for i in restaurants if i.rating>3])
    def viewnearby(self):
        global restaurants
        print([i.name for i in restaurants if i.address == self.address])
    def giverating(self):
        restaurantname = input('Enter restaurant name:')
        rating = input('Enter rating (0-5)')
        global restaurants
        map(lambda x:x.ratings.append(rating),list(filter(lambda x:x.name == restaurantname,restaurants)))
    def placeorder(self):
        restaurantname = input('Enter restaurant name:')
        items = []
        global restaurants
        for i in restaurants:
            if i.name == restaurantname:
                restaurant = i
                i.displaymenu()
                item = input("Enter item order:")
                items.append(item)
                while item != '':
                    item = input("Enter item order:")
                    items.append(item)
                type = input('Enter D for delivery C for takeaway:')
                self.neworder = Order(self,i,items,type)
                self.orders.append(self.neworder)
        a = input('press A to add item to order, D to delete order').upper()
        if a == 'A':
            self.additem(input('Enter item name:'))
        elif a == 'D':
            self.removeitem(input('Enter item name:'))
        else:
            d = input('Press C to confirm order and make payment:').upper()
            if d == 'C':
                restaurantlog = open(restaurant.name, "a")
                n=1
                restaurantlog.write(str(n)+'Customer name:'+self.name+'Total bill:'+str(self.neworder.total)+'Rating:'+str(restaurant.calcrating()))
                n+=1
                self.neworder.payment()
                if self.neworder.type == 'D':
                    self.neworder.deliver.makedelivery()
                    customerlog = open(self.name, "a")
                    customerlog.write(self.neworder.payment.cardpayment())
                    customerlog.close()
                elif self.neworder.type == 'C':
                    customerlog = open(self.name, "a")
                    customerlog.write(self.neworder.payment.cashpayment())
                    customerlog.close()
        self.neworder.makereceipt()
    def additem(self,item):
        self.neworder.additem(self,item)
    def removeitem(self,item):
        self.neworder.delitem(self,item)
class Rider:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.available = 0 #0 if rider is availabe 1 if he is unavailable
    def deliver(self):
        self.available = 1
class Deliver:
    def __init__(self,deliveryaddress):
        self.address = deliveryaddress
    def makedelivery(self):
        global riders
        i = random.randint(0,1)
        if self.address in riders[i].address and riders[i].available == 0:
            riders[i].deliver()
        else:
            print('rider not available')
class Order:
    def __init__(self,customer,restaurant,items,type):
        self.customer = customer
        self.restaurant = restaurant
        self.type = type
        if self.type == 'D':
            self.deliver = Deliver(self.restaurant.address)
        self.items = [x for x in self.restaurant.menu if x.itemname in items]
        print(self.items)
        self.total = 0
        for i in self.items:
            self.total += i.price
    def makereceipt(self):
        customerlog = open(self.customer.name,'a')
        customerlog.write('--------------------Order-----------------------\n')
        customerlog.write('Restaurant name:'+self.restaurant.name+'\n')
        customerlog.write("{:<10} {:<10} {:<10}".format('Name','Type','Price')+'\n')
        for i in self.items:
            customerlog.write(i.display())
        customerlog.write('')
        customerlog.write('Total amount:'+str(self.total)+'\n')
        customerlog.close()
        restaurantlog = open(self.customer.name,'a')
        restaurantlog.write('--------------------Order-----------------------\n')
        restaurantlog.write('Customer name:'+self.customer.name+'\n')
        restaurantlog.write("{:<10} {:<10} {:<10}".format('Name','Type','Price')+'\n')
        for i in self.items:
            restaurantlog.write(i.display())
        restaurantlog.write('')
        restaurantlog.write('Total amount:'+str(self.total)+'\n')
        restaurantlog.close()
    def additem(self,item):
        for i in self.restaurant.menu:
            if i.itemname == item:
                self.items.append(i)
    def delitem(self,item):
        for i in self.restaurant.menu:
            if i.itemname == item:
                self.items.remove(i)
    def payment(self):
        self.payment = Payment(self.customer,self.total)
class Payment:
    def __init__(self,customer,totalamount):
        self.customer = customer
        self.totalamount = totalamount
    def cashpayment(self,total):
        p = input("Your total is:\n"+str(self.totalamount)+"Press P to make a payment \n").upper()
        if p == 'P':
            return('a cash payment of'+str(total)+'was made by customer'+self.customer.name+'for the order, orderID:'+str(self.orderid))
        else:
            return('Payment not made')
    def cardpayment(self,total):
        creditcardnum = input('Enter credit card num:')
        p = input("Your total is:\n"+str(self.totalamount)+"Press P to make a payment \n").upper()
        if p == "P":
            print('a card payment of'+str(total)+'was made by customer '+self.customer.name+'creditcardnum:'+creditcardnum+'for the order, orderID:'+str(self.orderid))
        else:
            print('Payment not made')
class Menu:
    def __init__(self,itemname,price,type):
        self.itemname = itemname
        self.price = price
        self.type = type
    def editprice(self,price):
        self.price = price
    def getprice(self):
        return self.price
    def display(self):
        return ("{:<10} {:<10} {:<10}".format(self.itemname,self.type,self.price))
class Restaurant(Account):
    def __init__(self,name,email,address,password,R_id,pricelvl,menulist):
        super().__init__(name,email,address,password,'restaurant')
        self.R_id = R_id
        self.ratings = []
        self.pricelvl = pricelvl
        self.orders = []
        self.menu = []
        for i in menulist:
            x,y,z= i
            self.menu.append(Menu(x,y,z))
    def login(self,password):
        if super().login(password):
            return True
        else:
            return False
    def displaymenu(self):
        print("{:<10} {:<10} {:<10}".format('Name','Type','Price'))
        for i in self.menu:
            print(i.display())
    def calcrevenue(self):
        return sum(self.orders.total)
    def calcrating(self):
        if len(self.ratings)<1:
            return 0
        return sum(self.ratings)/len(self.ratings)
rider1 = Rider('Kile',['Model Town','Johar Town'])
rider2 = Rider('Rob',['[DHA,Bahria'])
riders=[rider1,rider2]
customerobj1 = Customer('Jake','jake@gmail','Model town','abc',5863)
customerobj2 = Customer('Alan','alan@gmail','Bahria',2734,8465)
customers=[customerobj1,customerobj2]
restaurant1 = Restaurant('McDonalds','mcdonalds@gmail','MM ALAM','MC admin',3452,'$$$',[('Mc Chicken',350,'Burger'),('Big Mac', 850,'Burger'),('Pepsi',80,'Drink')])
restaurants=[restaurant1]
admin1 = Admin('Anna','anna@gmail','Johar town','admin123',3456)
admins= [admin1]
def main():
    print("Press A to login as admin")
    print("Press C to login as customer")
    print("Press R to login as restaurant")
    print('Press S to create customer account')
    exist = False
    x = input('Enter choice:').upper()
    if x == 'C':
        c_id = int(input("Enter customer ID:"))
        global customers
        for i in customers:
            if i.C_id == c_id:
                exist = True
                password = input("Enter password:")
                if i.login(password) == True:
                    customerobj = i
                    print('Press V to view popular')
                    print('Press N to view nearby')
                    print('Press P to place order')
                    print('Press R to give rating')
                    x = input('Enter choice:').upper()
                    if x == 'P':
                        customerobj.placeorder()
                    elif x == 'V':
                        customerobj.viewpopular()
                        b = input('Press P to order').upper()
                        if b == 'P':
                            customerobj.placeorder()
                    elif x == 'N':
                        customerobj.viewnearby()
                        c = input('Press P to order').upper()
                        if c == 'P':
                            customerobj.placeorder()
                    elif x == 'R':
                        customerobj.giverating()
                else:
                    print('Invalid password')
        if exist != True:
            print('Customer with the following id does not exist')
    elif x == 'R' :
        r_id = int(input("Enter Restaurant ID:"))
        global restaurants
        for i in restaurants:
            if i.R_id == r_id:
                exist = True
                password = input("Enter password:")
                if i.login(password) == True:
                    restaurantobj = i
                    print('Press O for order details')
                    print('Press M for revenue:')
                    print('Press R for rating')
                    x = input('Enter choice:').upper()
                    if x == 'M':
                        print(restaurantobj.calcrevenue())
                    elif x == 'R':
                        restaurantobj.orders
                    elif x == 'O':
                        print('Total no of orders:',len(restaurantobj.orders))
                        print('Total amount:',restaurantobj.calcrevenue())
                        print('Customers:')
                        for i in restaurantobj.orders:
                            print(i.customer.name)
        if exist != True:
            print('Restaurant with the following id does not exist')
    elif x == 'A':
         a_id = int(input("Enter admin ID:"))
         global admins
         for i in admins:
            if i.adminid == a_id:
                exist = True
                password = input("Enter password:").upper()
                if i.login(password) == True:
                    adminobj = i
                    print('Press A to remove Restaurant')
                    print('Press B to add Restaurant')
                    print('Press C to add Customer')
                    x = input('Enter choice:').upper()
                    if x == 'A':
                        adminobj.removerestaurant()
                    elif x == 'B':
                        adminobj.addrestaurant()
                    elif x == 'C':
                        adminobj.removecustomer()
         if exist != True:
            print('Admin with the following id does not exist')
    elif x == 'S':
        name = input('Enter name:')
        email = input('Enter email:')
        address = input('Enter address:')
        password = input('Enter password:')
        customerid = input('Enter your customer id:')
        i = Customer(name,email,address,password,customerid)
        customers.append(i)
        customerlog = open(i.name, "w")
        customerlog.write('Customer ID:'+str(i.C_id)+'\n'+"Customer name:"+i.name+'\n'+'Customer email:'+i.email,'\n')
        customerlog.close()
    else:
        print('Choice entered was not valid')
main()
