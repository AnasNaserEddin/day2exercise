# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
items_dict={}
items_in_cart={}
# def reviews():
#     print("We want to take a one minute from you to give us a feedback ,if you agree press 1")
#     choice=input()
#     # if choice ==1


def showCustomerOptions():
    flag = True
    amount = 0
    buyed_item=open("buyed_items.txt","a")
    showlist()
    while flag:
        print("Write the item name to purchase - write finish to end ")
        try:
         item = input()
         if(item=="finish"):
             flag=False
         elif item in items_dict:
             price=items_dict.get(item)
             amount+=int(price)
             buyed_item.write(f"{item}\n")
         else:
             print("enter a valid item")
        except ValueError:
             print("")
    buyed_item.close()
    print(f"your totally amount is {amount}")
def showlist():
    f = open("items.txt", "r")
    try:
      for line in f:
         k , v = line.strip().split('-')
         items_dict[k.strip()] = v.strip()
         # print(v.strip()+" "+k.strip())

    except:
        print("")
    print(items_dict)
    f.close()
print("welcome to our supermarket,you can enter the item you want to buy,when you finish write finish")
# showlist()
showCustomerOptions()





