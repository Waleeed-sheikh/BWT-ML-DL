# Question 6
# Write a code for function `update_inventory(inventory_dict, item, quantity)` that will:
# 1. Take a dictionary where keys are item names and values are quantities, an item name, and a quantity to add or remove.
# 2. Updates the inventory by adding or removing the specified quantity (use negative values for removal).
# 3. Ensures that the quantity of any item does not go below zero.
# 4. Returns the updated dictionary.

# Use this function to
# 1. Initialize an inventory dictionary with at least 5 items.
# 2. Prompt the user to update the inventory by adding or removing quantities of 3 items.
# 3. Display the updated inventory.

def inventoryUpdate(inventoryDictionary,item,quantity,operation):
    originalQuantity=inventoryDictionary[item]
    afterRemoving=originalQuantity-int(quantity)
    afterAdding=originalQuantity+int(quantity)
    if(operation=="ADD"):
        inventoryDictionary[item]=afterAdding
    elif(operation=="REMOVE"):
      if(afterRemoving>0):
        inventoryDictionary[item]=afterRemoving
      else: 
        inventoryDictionary["Warning"]="The removal of given quantity will cause quantity to go below 0 so the operation can't be performed"
# i added the parameter remove because i thougth a prompt on what to do will make things easy to understand
#the issue i faced in this one was for the problem if the quantity goes below 0
#so i thought i will add warning to the dictionary because there were no instruction given in the question on what to do with the below 0 problem
#i thought about using the warning message to ask for the reduction of quantity to remove fom the user , but that didnt make any sense so i left it as it is

    

itemsList={
    "chocolates":3,
    "mangoes":56,
    "gums":3,
    "chips":44,
    "biscuits":34
}
 

for i in range(3):
    print(itemsList )#i wanted to display the items in array in a more representable form not directly as a dictionary but could not find a perfect  method and time was running short
  #but wil try to make this code more neat
    items=input("Select a single item from the above list:")
    quantity=input("Select the quantity you want to add or delete:")
    operation=input("DO YOU WANT TO ADD OR REMOVE ?")
    inventoryUpdate(itemsList,items,quantity,operation.upper())

print(itemsList)
