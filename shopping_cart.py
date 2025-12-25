# Creating a shopping cart demo

#Products available
products={1:("Pencil",15),
          2:("Pen",20),
          3:("Eraser",10),
          4:("Sharpner",10),
          5:("A-4 size sheets",50),
          6:("Ruled sheets",50),
          7:("Registers",60)
          }

#show products
def show_products():
    print("\nAvailable Products:")
    for pid,(name, price) in products.items():
        print(f"{pid}.{name}-{price}")
        print()

#add to cart
cart={}
def add_to_cart():
   try:
     pid=int(input("Enter the product Id:"))
     if pid not in products:
        print("Invalid product Id")
        return
     qnt=int(input("Enter the quantity:"))
     if qnt<=0:
        print("Enter a positive quantity")
        return
     if pid in cart:
        cart[pid]+=qnt
     else:
        cart[pid]=qnt
   except ValueError:
      print("Give valid numbers")

#remove itmes from cart
def remove_item():
   try:
      pid=int(input("Enter the product Id:"))
      if pid not in cart:
        print("Item is not in cart")
        return
      qnt=int(input("Enter the quantity:"))
      if qnt<=0:
        print("Enter a positive quantity")
        return
      if qnt >= cart[pid]:
         del cart[pid]
         print(f"Removed {products[pid][0]} from cart.")
      else:
         cart[pid] -= qnt
         print(f"Removed {qnt} x {products[pid][0]}. Remaining: {cart[pid]}")
   except ValueError:
     print("Please enter valid numbers.")

#view cart
def view_cart():
   if not cart:
      print("Your cart is empty")
      return
   print("\nYour cart")
   total=0
   for pid,qnt in cart.items():
     name,price=products[pid]
     subtotal=price*qnt
     print(f"{name}X{qnt}={subtotal}")
     total+=subtotal
   print("Total amount:",total)

#main menu
def main():
   while True:
       print("=== Shopping Cart Menu ===")
       print("1. Show products")
       print("2. Add to cart")
       print("3. Remove from cart")
       print("4. View cart")
       print("5. Checkout / Exit")
       choice = input("Choose an option: ").strip()

       if choice == "1":
            show_products()
       elif choice == "2":
            add_to_cart()
       elif choice == "3":
            remove_item()
       elif choice == "4":
            view_cart()
       elif choice == "5":
            view_cart()
            print("Thank you for shopping! Goodbye.")
            break
       else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()

   
      


