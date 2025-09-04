fruits=["APPLE","BANANA","GRAPES","GUVA","MANGO","ORANGE","WATERMELON"]
stock=[20,20,30,60,40,10,20]
selling_price=[200,100,150,100,120,150,50]
cost_price=[150,60,100,60,80,100,30]
sold_qty=[0]*len(fruits) 
cart=[]
total_amount=0
while True:
    print("*"*5,"WELCOME TO A* FRUIT SHOP","*"*5)
    print("1.Fruit Seller ")
    print("2.Customer ")
    print("3.Exit  ")
    choice=int(input("enter your choice: "))
    if choice==1:
        while True:
            print("1.View quantity")
            print("2.Add new fruit")
            print("3.Update Stock")
            print("4.Update price")
            print("5.Seller Report")
            print("6.Back to Menu")w
            choose=int(input("enter your option from menu(1/2/3/4): "))
            if choose==1:
                print("------ Current Stock ------")
                print("Fruit" + " " * 7 + "Qty" + " " * 5 + "Amount")
                for i in range(len(fruits)):
                    print(fruits[i]+"  " + " - ₹" + str(selling_price[i]) + "/kg - " +"  "+ str(stock[i]) + " kg available")
                print("---------------------------")
            elif choose==2: 
                fruit_name=input("Enter fruit name: ").upper()
                sp=int(input("Enter Selling Price per kg: "))
                cp=int(input("Enter Cost Price per kg: "))
                ustock=int(input("enter stock quantity: "))
                fruits.append(fruit_name)
                selling_price.append(sp)
                cost_price.append(cp)
                stock.append(ustock)
                sold_qty.append(0)
                print("Fruit added sucessfully!")
                
            elif choose==3:
                update_fruit=input("enter fruit name to update: ").upper()
                if update_fruit in fruits:
                    index=fruits.index(update_fruit)
                    print("1. Add stock")
                    print("2. Remove stock")
                    action=int(input("Choose Your Option(1/2): "))
                    if action==1:
                        update_stock=int(input("Enter quantity to add: "))
                        stock[index]+=update_stock
                        print("Stock updated sucessfully!\n")
                    elif action==2:
                        update_stock=int(input("Enter quantity to remove: "))
                        if update_stock<=stock[index]:
                            stock[index]-=update_stock
                            print("Stock removed sucessfully!\n")
                        else:
                            print("Not Enough stock to remove that quantity.")
                    else:
                        print("Invalid choice for update.")
                    #dispaly updated stock
                    print("Updated stock is :")
                    for i in range(len(fruits)):
                        print(fruits[i] + " - ₹" + str(selling_price[i]) + "/kg - " + str(stock[i]) + " kg available")
                else:
                    print("Fruit is not found")
            elif choose==4:
                fruit_name=input("Enter fruit name to update Price: ").upper()
                if fruit_name in fruits:
                    index=fruits.index(fruit_name)
                    new_price=int(input("Enter new price: "))
                    selling_price[index]=new_price
                    print("Price Updated sucessfully!\n")
                    print("Updated stock with new prices are :")
                    for i in range(len(fruits)):
                        print(fruits[i] + " - ₹" + str(selling_price[i]) + "/kg - " + str(stock[i]) + " kg available")
                else:
                    print("Fruit not found!\n ")
            elif choose==5:#seller report
                 print("=========== Seller Report ===========")
                 total_profit=0
                 for i in range(len(fruits)):
                     if sold_qty[i]>0:
                         profit=(selling_price[i]-cost_price[i])*sold_qty[i]
                         total_profit+=profit
                         print(fruits[i]+" | Sold: "+str(sold_qty[i])+" kg | Profit: ₹"+str(profit))
                 print("------------------------------------")
                 print("Total Profit: ₹"+str(total_profit))
                 print("====================================")
                         
                
                
            elif choose==6:
                print("Returning to Main Menu.....")
                break
            else:
                print("Invalid choice! Please try again.")
                    
                                         
        
    elif choice==2:
        while True:
            print("------------------------------------------------------------")
            for i in range(len(fruits)):
                print(fruits[i] + " - ₹" + str(selling_price[i]) + "/kg - " + str(stock[i]) + " kg available")
            print("------------------------------------------------------------")
                
            print("1.Add")
            print("2.Remove")
            print("3.View")
            print("4.Bill")
            print("5.Exit")
            ch=int(input("Enter option from menu(1/2/3/4) : "))
            if ch==1:
                fruit=input("choose the fruit: ").upper()
                if fruit in fruits:
                    idx=fruits.index(fruit)
                    fruit_price=selling_price[idx]
                    if fruit in cart:
                        print(fruit,"is already available")
                    else:
                        qty=int(input("enter quantity(kg's only): "))
                        if qty>stock[idx]:
                            print("Only ",str(stock[idx])," kg available.")
                        else:
                            cart.append([fruit,qty,selling_price[idx]])
                            stock[idx]-=qty
                            sold_qty[idx]+=qty
                            print(fruit," fruit is added")
                            print("Remaining Stock is ",stock[idx])
                else:
                    print(fruit," is not available in our shop.")
            elif ch==2:
                fruit=input("Which fruit want to remove: ").upper()
                remove_qty=int(input("How many kg's want to remove: "))
                found=False
                for item in cart:
                    if item[0]==fruit:
                        qty=item[1]
                        fruit_price=item[2]
                        
                        if remove_qty<=qty:
                            index=fruits.index(fruit)
                            stock[index]+=remove_qty
                            sold_qty[index]-=remove_qty 
                            item[1]-=remove_qty

                            if item[1]==0:
                                cart.remove(item)
                            print(fruit,"removed",remove_qty,"kg from cart")
                        else:
                            print("You only have",qty,"kg of",fruit,"in cart.")
                        found=True
                        break
                    
                if not found:
                    print(fruit,"is not available in cart.")
            elif ch==3:
                if len(cart)==0:
                    print("Cart is Empty.")
                else:
                    print("*"*5,"CART","*"*5)
                    print("Fruit" + " " * 7 + "Qty" + " " * 5 + "Amount")
                    total=0
                    for item in cart:
                        fruit=item[0]
                        qty=item[1]
                        idx=fruits.index(fruit)
                        amt=qty*selling_price[idx]
                        total+=amt
                        print(fruit + " " * (12 - len(fruit)) + str(qty) + " " * (8 - len(str(qty))) + str(amt))
            elif ch==4:
                name=input("Enter Your Name: ").upper()
                number=input("Enter Your Number: ")
                if len(number)==10 and number.isdigit():
                    print("------------------------------BILL----------------------------------")
                    print("Customer Name is: ",name)
                    print("Customer Number: ",number)
                    print("-------------------------------------------------------------------")
                    print("Fruit" + " " * 7 + "Qty" + " " * 5 + "Amount")
                    total=0
                    for item in cart:
                        fruit=item[0]
                        qty=item[1]
                        idx=fruits.index(fruit)
                        amt=qty*selling_price[idx]
                        total+=amt
                        print(fruit + " " * (12 - len(fruit)) + str(qty) + " " * (8 - len(str(qty))) + str(amt))
                    print("The Bill: Rs. " + str(total))
                    print("Thank You for Visting A* Fruit Shop! ")
                    print("------------------------------------------------------------")
                    cart.clear()
                else:
                    print("Invalid Phone Number")
                
            elif ch==5:
                print("Thank you for visiting A* Fruit Shop! ")
                print("------------------------------------------------------------")
                break
                

            else:
                print("enter valid choice")
    else:
        print("Exiting")
        break
            
                
            
