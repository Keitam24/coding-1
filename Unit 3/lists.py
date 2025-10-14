# Lists - a system for collecting and organizing multiple pieces of data


# List syntax (how it is written)
# when we cant to create al ist, we first creae a variable name and assigh nit to the square brackets.
# we then put the data we want to collect inside of the square brackets.

shoppingcart = ['water', 'ice', 'cereal', 'apples']

# Accessing items in a list -
# When we want to access an item in a list we write the variable name and then we use the square brackets and pass in the item position in the brackets
# python is a zero-based index language, meaning; when counting items, zero is treated as an actual number.
# () = functions
# [] = list
print(shoppingcart[0])

shoppingcart.append('orange')

print(shoppingcart)

def additemtocart():
    bestbuycart = ['pc monitor', 'graphics card', 'speakers', 'pro controller']
    item = input("please add new item: ")

    bestbuycart.remove('graphics card')
    print(bestbuycart)

additemtocart()

def amazon():
    icantbuyallthis = ['nvidia 5080', '8khd monitor', 'expensive behind mouse']

    icantbuyallthis.remove('nvidia 5080')
    print(icantbuyallthis)

def howtosort(addnumber):

    numberlist = [256, 38, 360, 45, 67, 22, 3, 88]
    numberlist.append(addnumber)
    numberlist.sort()
    print(numberlist)

howtosort(60)