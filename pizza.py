
size = input("What pizza size do you want? S, M, L ")

add_pepperoni = input(" Do you want to add pepperoni ?")

extra_cheese = input(" Do you want to add extra cheese ?")

bill = 0

if size == "S":
        bill += 15
        print("Small size pizza order confirmed. ")

elif size == "M":
        bill += 20
        print("Medium size pizza order confirmed. ")
       
else:
        bill += 25
        print("Large size pizza order confirmed. ")
       
           
if add_pepperoni == "Y":
    print("Pepperoni added to your order. ")
   
    if size == "S":
        bill += 2
       
    else:
        bill += 3  
       
if extra_cheese == "Y":
    print("Extra cheese added to your order")
    bill +=1



print(f" The final bill will be £ {bill}. Thank you for your purchase. Enjoy! " )
