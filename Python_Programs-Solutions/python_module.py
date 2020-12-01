#import extra_code as ec # alias or short name

#if we want direct functions from other file to use here
#from extra_code import add,div

#if we want all functions to import
# from extra_code import *
# 
# print(add(5,7))
# print(div(5,8))
# print(sub(5,8))
# print(extra_code.add(10,5))
# print(extra_code.sub(10,5))
#print(ec.mul(10,5))

#---------------------------------------
# import extra_code as ec  #alias or short name
# 
# # print(extra_code.add(2,3))
# # print(extra_code.mul(2,3))
# 
# print(ec.div(3,2))

from extra_code import *

print(add(4,5))
print(sub(4,5))
print(mul(2,4))
print(div(2,4))
print(greet("Kaavya"))
