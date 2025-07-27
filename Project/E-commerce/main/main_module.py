import sys

sys.path.append(r"C:\Gracy_Info\Hexaware\Python Foundation Training - Batch 2\Project\E-commerce")

from dao.OrderProcessRepository import OrderProcessRepository
from dao.OrderProcessorImpl import OrderProcessorImpl
from entity.products import Products
from entity.customers import Customers
from exception.cart_empty import CartEmptyException
from exception.custom_exception import CustomException
from exception.customer_not_found import CustomerNotFoundException
from exception.product_not_found import ProductNotFoundException
from utill.DBConnUtil import DBConnUtil
from utill.PropertyUtil import PropertyUtil

def main():
    processor=OrderProcessorImpl()

    print("\n---------- E-Commerce System ----------")
    print("1. Create Product")
    print("2. Create Customer")
    print("3. Add to Cart")
    print("4. View Cart")
    print("5. Place Order")
    print("6. View All Order Details")
    print("7. Exit")

    while True:
        choice=input("\n Enter Your choice: ")

        if choice=="1":    #--Create Product
            name=input("Enter Product Name: ")
            price = float(input("Enter Price: "))
            desc=input("Enter Description: ")
            qty=int(input("Enter Stock Quantity: "))
            product = Products(name=name, price=price, description=desc, stock_quantity=qty)
            if processor.create_product(product):
                print("Product created successfully!")


        elif choice=='2':    #--Create Customer
            name=input("Enter Customer Name: ")
            email=input("Enter Email: ")
            password =input("Enter password: ")
            customer = Customers(name=name, email=email, password=password)
            if processor.create_customer(customer):
                print("Customer created successfully.")


        elif choice=='3':    #--Add to Cart
            try:
                cust_id=int(input("Enter Customer ID: "))
                prod_id = int(input("Enter Product ID: "))
                quantity=int(input("Enter Quantity: "))
                
                customer=Customers(customer_id=cust_id)
                product=Products(product_id=prod_id)
                
                if processor.add_to_cart(customer, product, quantity):
                    print("Added to cart!")

            except ProductNotFoundException as pe:
                print(f"\n Exception from ProductNotFoundException! {pe}")
            except CustomerNotFoundException as ce:
                print(f"\n Exception from CustomerNotFoundException! {ce}")
            except CustomException as ce:
                print(f"\n CustomException: {ce}")
            except Exception as e:
                print(f"\n Unknown error: {e}")


        elif choice=='4':    #--Get All From Cart, View Cart
            try:
                cust_id=int(input("Enter Customer ID: "))
                
                customer=Customers(customer_id=cust_id)
                cart_items=processor.get_all_from_cart(customer)
                
                print("\n Cart Items: ")
                for item in cart_items:
                    print(f"Product ID: {item[0]}, Name: {item[1]}, Price: {item[2]}, Quantity: {item[3]}")
            except CartEmptyException as ce:
                print(f"\n Exception from CartEmptyException! {ce}")
            except CustomException as ce:
                print(f"\n Exception from CustomException {ce}")
            except Exception as e:
                print(f"\n Unexpected Error: {e}")

        elif choice=='5':    #--Place Order
            cust_id=int(input("Enter Customer ID: "))
            customer=Customers(customer_id=cust_id)
            product_qty_list=[]

            while True:
                pid=int(input("Enter product ID: "))
                qty=int(input("Enter Quantity: "))
                """product=Products(product_id=pid)
                product_qty_list.append((product, qty))"""

                # Fetch full product details from DB
                cursor = DBConnUtil.get_connection().cursor()
                cursor.execute("SELECT name, price, description, stockQuantity FROM products WHERE product_id=?", (pid,))
                row = cursor.fetchone()
                if not row:
                    print(f"Product ID {pid} not found!")
                    continue

                name, price, description, stock = row
                product = Products(product_id=pid, name=name, price=price, description=description, stock_quantity=stock)
                product_qty_list.append((product, qty))

                
                cont=input("Add another product? (y/n): ")
                if cont.lower()!='y':
                    break

            address=input("Enter Shipping Address: ")
            order_id=processor.place_order(customer, product_qty_list, address)
            print(f"Order placed successfully! Order ID:{order_id}")


        elif choice=='6':
            orders=processor.get_all_orders_details()
            print("\n----------All Order Details----------")
            for row in orders:
                print(f""" Order ID: {row[0]} | Order Date:{row[1]} | Total Price: {row[2]}|Shipping Address:{row[3]}
 Customer ID:{row[4]} | Name: {row[5]} |Email :{row[6]}
 Product ID: {row[7]} | Product Name: {row[8]} | Price: {row[9]} | Quantity: {row[10]}
 -------------------------------------------------------------------------------""")

        elif choice=='7':
            print("Thank you!")
            break


        else:
            print("Invalid choice! Try again!")


if __name__=="__main__":
    main()
