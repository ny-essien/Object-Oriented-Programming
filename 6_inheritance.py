import csv

class Item:

    #class attribute

    pay_rate = 0.8 # after 20% discount

    #creating a n empty list that wil be used to save each insatnce
    all = []

    def __init__(self, name , price, quantity = 0):

        #run validations to the received arguments
        #price and quntity arguments should not be less than zero

        assert type(price) == int
        assert type(name) == str
        assert price >= 0 , f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        

        #Assign to self object

        self._name = name
        self._price = price
        self._quantity = quantity
        print(f"{name} {price} {quantity}")

        #Actions to execute
        Item.all.append(self)


    def calculate_total_price(self):
        #return f"Total Price : {x * y}"
        return self._price * self._quantity

    
    def apply_discount(self):

        #getting the pay rate from the class level
        #self._price =  self._price * Item.pay_rate
        
        #to make the pay rate so that you can overwrite
        #it on the instance level
        #use self.pay_rate instead of Item.pay_rate

        self._price = self._price * self.pay_rate

    
    #to convert a method to a class method
    #you add a decorators
    #class method

    @classmethod
    def instantiate_from_csv(cls):

        #open csv file
        #pass in permission 'r'

        with open('items.csv', 'r') as f:

            #method to read csv which will convert it to a python dictionary
            reader = csv.DictReader(f)
            #convert dictionary to a list
            items = list(reader)

        for item in items:
            #print(item)
            #instantiating instances
            Item(

                name = item.get('name'),
                #you can convert type to float is values from csv files
                #are not integers

                price =int( item.get('price')),
                quantity = int(item.get('quantity')),
            )
    #static methods
    #a static method should do some work for you that has a logical
    #connection to a class
    #if you want to check if a number is an interger or a float this is a good 
    #candidate for creating a static method

    @staticmethod
    def is_integer(num):
        #we will count out the floats that are point zero
        #For i.e 5.0, 10.0

        if isinstance(num, float):
            #count out the floats that are point zero
            return num.is_integer()

        elif isinstance(num, int):
            return True

        else:
            return False



    #A method to view the list of intances
    def __repr__(self):
        #to get the instance generically
        return f"{self.__class__.__name__}({self._name}, {self._price}, {self._quantity})"

item1 = Item("Phones", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print("==================================================================")

#print(Item.all)

#print all the names for all intances
#for instance in Item.all:
    #print(instance._name)


#calling the class method
#Item.instantiate_from_csv()
#print(Item.all)

#calling the static method
print(Item.is_integer(7))


class Phone(Item):

    #by calling the super function we have access to all the class attributes of Item()
    #so we no longer the all attribute in the child class
    #all = []

    def __init__(self, name , price, quantity = 0, broken_phones = 0):

        super().__init__(

            name, price, quantity
        )

        #run validations to received arguments
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than or equal to zero "

        #Assign to self object
        self._broken_phones = broken_phones

        #Actions to execute
        #Phone.all.append(self)

phone1 = Phone("jscPhonev10", 500, 5, 1)
#print(phone1.calculate_total_price())

#phone2 = Phone("jscPhonev20", 700, 5, 1)
print(Phone.all)
print(Item.all)