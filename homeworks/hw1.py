import random

class Portfolio(object):
    def __init__(self):
        self.Cash=0
        self.Stock={}
        self.Stockprice={}
        self.MutualFund={}
        self.log=[]

    def addCash(self,amount):
        self.Cash+=amount
        self.log.append("$ %d added"%(amount))

    def withdrawCash(self,amount):
        if amount<self.Cash:
            return "Not enough cash"
        else:
            self.Cash-=amount
            self.log.append("$ %d withdrawn"%(amount))

    def buyStock(self,shares,stockname):
        if stockname.price*shares>self.Cash:
            return "Not enogh cash"
        elif stockname.symbol in dict.keys(self.Stock):
            self.Cash-=stockname.price*shares
            self.Stock[stockname.symbol]+=shares
            self.log.append("%s bought with $ %d"%(stockname.symbol,stockname.price*shares))
            self.Stockprice[stockname.symbol]=stockname.price

        else:
            self.Cash-=stockname.price*shares
            self.Stock[stockname.symbol]=shares
            self.log.append("%d %s bought at $ %d"%(shares,stockname.symbol,stockname.price*shares))
            self.Stockprice[stockname.symbol]=stockname.price

    def sellStock(self,shares,symbol):
        if not symbol in dict.keys(self.Stock):
            return "No stock by that name"
        elif shares<self.Stock[symbol]:
            return "Not enough stocks"
        else:
            self.Stock[symbol]-=shares
            temprice=random.uniform(.5,1.5)*self.Stockprice[symbol]
            self.Cash+=shares*temprice
            self.log.append("%d %s sold at $ %d"%(shares,symbol,temprice))


    def buyMutualFund(self,shares,fundname):
        if shares>self.Cash:
            return "Not enogh cash"
        elif fundname.symbol in dict.keys(self.MutualFund):
            self.Cash-=shares
            self.MutualFund[fundname.symbol]+=shares
            self.log.append("%d %s bought at %d"%(shares,fundname.symbol,1))
        else:
            self.Cash-=shares
            self.MutualFund[fundname.symbol]=shares
            self.log.append("%d %s bought at %d"%(shares,fundname.symbol,1))

    def sellMutualFund(self,shares,symbol):
        if not symbol in dict.keys(self.MutualFund):
            return "No mutual fund by that name"
        elif shares<self.MutualFund[symbol]:
            return "Not enough holdings"
        else:
            self.MutualFund[symbol]-=shares
            temprice=random.uniform(.9,1.2)
            self.Cash+=shares*temprice
            self.log.append("%d %s sold at $ %d"%(shares,symbol,temprice))



    def __str__(self):
        return ("Cash : $ %d\n"\
               "Stocks:%r\n"\
               "Mutual Funds:%r"%(self.Cash,self.Stock,self.MutualFund))
    def history(self):
        print(self.log)

#   def __str__(self):
#        return "Cash : $ %d" %(self.Cash)
#        return "\n Stocks\n"
#        for i in dict.keys(self.Stock):
#            return "%s :  %d \n" %(i,self.Stock[i])
#        return "Mutual Funds:\n"
#        for i in self.log:
#            return "%s :  %d \n" %(i,self.MutualFund[i])
#    def history(self):
#        for i in dict.keys(self.log):
#            print (self.log[i])

class MutualFund(object):
    def __init__(self, symbol):
        self.symbol=symbol


class Stock(object):
    def __init__(self,price,symbol):
       self.price=price
       self.symbol=symbol

expo=Portfolio()
expo.addCash(200)
expo.withdrawCash(100)
s=Stock(20,"HTH")
expo.buyStock(5,s)


expo.history()

print(expo)

