#check given credit card no is valid or not
no=input("Enter Credit Card number:")
import re

def solve(s):
   if s.count("-")>0:
      a = s.split("-")
      p=1
      if len(a)!=4:
         p=None
         a=[]
      for b in a:
         if len(b)!=4:
            p=None
            break
         else:
            p = re.search("[456][0-9]{15}",s)
         s = s.replace("-","")
         q = re.search(".*([0-9])\1{3}.*",s)

         if p!=None and q==None:
            return True
         else:
            return False

s = "5423-2578-8632-6589"
print(solve(s))