from item import Item
from keyboard import Keyboard
from phone import Phone

item1 = Phone("MyItem", 750)

#Setting an Attribute
item1.name = "OtherItem"

item1.apply_discount()

item2 = Keyboard("jscKeyboard", 1000, 3)

item2.apply_discount()

print(item1.price)
print(item2.price)