#!/usr/bin/python

class MyClass:

  def __init__(self):
     self.x = 0
     self.y = 0

  def setInputs(self, value1, value2):
    self.x = value1
    self.y = value2

  def getInputs(self):
    self.x = raw_input ( 'Enter the value of x :' )
    self.y = raw_input ( 'Enter the value of y :' )

  def printValues(self):
     print ("Value of x is ", self.x )
     print ("Value of y is ", self.y )

  def printTypes(self):
     print ("Type of x is ", type(self.x) )
     print ("Type of y is ", type(self.y) )
     self.x = "abc"
     self.y = 1.3434 
     print ("Type of x is ", type(self.x) )
     print ("Type of y is ", type(self.y) )

def main():
   obj1 = MyClass()
   obj2 = MyClass()

   obj1.printValues()
   #obj1.getInputs()
   obj1.setInputs( 100, 200)
   obj1.printValues()
   obj1.printTypes()

   obj2.printValues()
   #obj2.getInputs()
   obj2.setInputs( 1000, 2000)
   obj2.printValues()
   obj2.printTypes()

main()
