# 14 menu driven python program with a dictionary of words and their meanings
# menu_dict.py
# creating the dictionary class
class my_dict(dict):
  def my_dict (self):
      self=dict()
# function to add key:value
  def add(self,key,value): 
          self[key]=value
# main function
dict_obj=my_dict()
ans='y'
while ans=="y":
      print("M E N U")
      print("********************")
      print("1.create a dictionary")
      print("2.print the dictionary")
      print("3.exit")
      print("********************")
      ch=int(input("enter your choice:"))
      if ch==1:
              n=int(input("enter the no of key/value pair in a dictionary:"))
              i=1
              while i<=n:
                    dict_obj.key=input("enter the word:")
                    dict_obj.value=input("enter the meaning:")
                    i=i+2
      elif ch==2:
              print("the dictionary object is")
              print(dict_obj)
      elif ch==3:
              exit()
      else:
              print("wrong choice")
              ans=input("do you want to continue(y/w)?")
                                 
