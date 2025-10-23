from my_module import name
from my_module_2 import name
print(name)# can able to access only one module

#To access both modules
import my_module 
import my_module_2
print(my_module.name)
print(my_module_2.name)