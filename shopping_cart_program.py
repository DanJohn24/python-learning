class Purchase:
    def __init__(self,name,netPrice,VBand):
        self.__name = name
        self.__netPrice = netPrice
        self.__VBand = VBand
    def getName(self):
        return self.__name
    def getPriceExcVAT(self):
        return self.__netPrice
    def getVBand(self):
        return self.__VBand
    def getVAT(self):
        band = self.getVBand()
        if band == 0:
            return 0 
        elif band == 1:
            return 0.05 * self.getPriceExcVAT()
        elif band == 2:
            return 0.2 * self.getPriceExcVAT()
        else:
            return 0 
    def getPriceIncVAT(self):
        vat = self.getVAT()
        price = self.getPriceExcVAT()
        calculation = price + vat
        return calculation

class ShoppingCart:
    def __init__(self):
        self.__contents = []     
    def add(self,product):
        self.__contents.append(product)
    def getTotalVAT(self):
        total = 0       
        for product in self.__contents:
            total += product.getVAT()
        return total
    def getTotalIncVAT(self):
        total = 0
        for product in self.__contents:
            total += product.getPriceIncVAT()
        return total
    def getTotalExcVAT(self):
        total = 0        
        for product in self.__contents:
            total += product.getPriceExcVAT()
        return total

#output for first excersise
p1 = Purchase('Complete Works of Shakespeare',30,0)
p2 = Purchase('Car Seat',100,1)
p3 = Purchase('Chocolate Shortbread',5,2)
print('VAT on',p1.getName(),'=',p1.getVAT())
print('VAT on',p2.getName(),'=',p2.getVAT())
print('VAT on',p3.getName(),'=',p3.getVAT())
print('Price of', p3.getName(),'exc. VAT =',p3.getPriceExcVAT())
print('Price of', p3.getName(),'inc. VAT =',p3.getPriceIncVAT())

print("\n")

#output for second excersise
s = ShoppingCart()
s.add(p1)
s.add(p2)
s.add(p3)

print('Cart total exc. VAT = ',s.getTotalExcVAT())
print('Cart total inc. VAT = ',s.getTotalIncVAT())
print('Cart total VAT = ',s.getTotalVAT())
