class Stall(object):
   
    # fill your code
    def __init__(self,name,detail,contact,ownerName,basicPrice):
        self.name=name
        self.detail=detail
        self.contact=contact
        self.ownerName=ownerName
        self.basicPrice=basicPrice
    def display(self):
       # fill your code
       print'Name:',self.name
       print'Details:',self.detail
       print'Contact Number:',self.contact
       print'Owner Name:',self.ownerName
class GoldStall(Stall):
    # fill your code
    def __init__(self,extraAmount,name,detail,contact,ownerName,basicPrice):
        self.extraAmount=extraAmount
        super(GoldStall,self).__init__(name,detail,contact,ownerName,basicPrice)
        super(GoldStall,self).display()
    def display(self,basicPrice,extraAmount):
       # fill your code
       self=basicPrice+extraAmount
       print'Stall price per day:',self
class PlatinumStall(Stall):
   # fill your code
   def __init__(self,extraAmount,name,detail,contact,ownerName,basicPrice):
       self.extraAmount=extraAmount
       super(PlatinumStall,self).__init__(name,detail,contact,ownerName,basicPrice)
       super(PlatinumStall,self).display()
    
   def display(self,basicPrice,extraAmount):
       # fill your code
       self=basicPrice+extraAmount
       print'Stall price per day:',self
n=input("Menu\n1.Gold stall\n2.PlatinumStall    \nEnter customer choice\n")
# fill your code
if(n==1):
    a=raw_input("Enter Stall name\n")
    b=raw_input("Enter Stall Details\n")
    c=input("Enter contact number\n")
    d=raw_input("Enter Owner name\n")
    e=input("Enter Basic price\n")
    f=input("Enter the Extra amount for GoldStall\n")
    g=GoldStall(f,a,b,c,d,e)
    self=e+f
    g.display(e,f)
else:
    p=raw_input("Enter Stall name\n")
    q=raw_input("Enter Stall Details\n")
    r=input("Enter contact number\n")
    s=raw_input("Enter Owner name\n")
    t=input("Enter Basic price\n")
    u=input("Enter the Extra amount for PlatinumStall\n")
    v=PlatinumStall(u,p,q,r,s,t)
    self=t+u
    v.display(t,u)