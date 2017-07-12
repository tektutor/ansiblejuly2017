#!/usr/bin/python

class Parent: 

   def __init__(self):
      print("Parent Constructor invoked")
      self.__privateMethod(0,0)

   def publicMethod(self):
      print("Parent Public member function")

   def _protectedMethod(self):
      print("Parent Protected member function")

   def __privateMethod(self, value1, value2):
       print("Parent private member function")
       self.x = value1
       self.y = value2

class Child(Parent):
   
   def __init__(self):
      Parent.__init__(self)
      print("Child constructor invoked")

def main():
   instance = Child()
   instance.publicMethod()

   instance._protectedMethod()

main()
