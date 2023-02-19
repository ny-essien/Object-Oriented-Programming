class Item:

    #class attribute

    pay_rate = 0.8 # after 20% discount

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


item1 = Item("Phone", 100)
#print(item1.calculate_total_price(item1._price, item1._quantity))
#print(item1.calculate_total_price())
item1.apply_discount()
print(item1._price)

item2 = Item("Laptop", 1000, 5)
#print(item2.calculate_total_price(item2._price, item2._quantity))
#print(item2.calculate_total_price())
item2.pay_rate  = 0.7
item2.apply_discount()
print(item2._price)

#accessing the class attribute using the class itself
#print(Item.pay_rate)
#accessing the class attribute from an instance 
#print(item2.pay_rate)

#magic attribute to view all other attributes
#print(Item.__dict__)
#print(item1.__dict__)