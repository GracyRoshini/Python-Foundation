import sys

sys.path.append("C:/Gracy_Info/Hexaware/Python Foundation Training - Batch 2/Project/E-commerce")

from dao.OrderProcessRepository import OrderProcessRepository
from utill.DBConnUtil import DBConnUtil

from exception.custom_exception import CustomException
from exception.product_not_found import ProductNotFoundException
from exception.customer_not_found import CustomerNotFoundException
from exception.cart_empty import CartEmptyException

class OrderProcessorImpl(OrderProcessRepository):
    def __init__(self):
        self.conn=DBConnUtil.get_connection()

    def create_product(self, product):
        try:
            cursor=self.conn.cursor()
            cursor.execute("Insert into products(name,price,description,stockQuantity) Values(?,?,?,?)",
                           (product.get_name(), product.get_price(), product.get_description(), product.get_stock_quantity()))
            self.conn.commit()
            return True
        except Exception as e:
            raise CustomException(f"Create Product Failed: {e}")

    def create_customer(self, customer):
        try:
            cursor=self.conn.cursor()
            cursor.execute("Insert into customers(name,email,password) Values(?,?,?)",
                           (customer.get_name(), customer.get_email(), customer.get_password()))
            self.conn.commit()
            return True
        except Exception as e:
            raise CustomException(f"Create Customer Failed: {e}")

    def delete_product(self, product_id):
        try:
            cursor=self.conn.cursor()
            cursor.execute("Delete From products where product_id=?", (product_id,))
            if cursor.rowcount==0:
                raise ProductNotFoundException("Product ID not found")
            self.conn.commit()
            return True
        except Exception as e:
           raise CustomException(f"Delete Product Failed: {e}")

    def delete_customer(self, customer_id):
        try:
            cursor=self.conn.cursor()
            cursor.execute("Delete from customers where customer_id=?", (customer_id,))
            if cursor.rowcount==0:
                raise CustomerNotFoundException("Customer ID not found")
            self.conn.commit()
            return True
        except Exception as e:
            raise CustomException(f"Delete Customer Failed: {e}")

    def add_to_cart(self, customer, product, quantity):
        try:
            cursor=self.conn.cursor()
            
            cursor.execute("SELECT * FROM customers WHERE customer_id=?", (customer.get_customer_id(),))
            if not cursor.fetchone():
                raise CustomerNotFoundException("Customer ID not found")

            cursor.execute("SELECT * FROM products WHERE product_id=?", (product.get_product_id(),))
            if not cursor.fetchone():
                raise ProductNotFoundException("Product ID not found")

            cursor.execute("Insert into cart(Customer_id, product_id, quantity) values(?,?,?)",
                           (customer.get_customer_id(), product.get_product_id(), quantity))
            self.conn.commit()
            return True
        except (CustomerNotFoundException, ProductNotFoundException):
            raise
        except Exception as e:
            raise CustomException(f"Add to Cart Failed: {e}")

    def remove_from_cart(self, customer, product):
        try:
            cursor=self.conn.cursor()
            cursor.execute("Delete from cart Where customer_id=? AND product_id=?",
                           (customer.get_customer_id(), product.get_product_id()))
            if cursor.rowcount==0:
                raise ProductNotFoundException("Product not in cart")
            self.conn.commit()
            return True
        except Exception as e:
            raise CustomException(f"Remove From Cart Failed: {e}")

    def get_all_from_cart(self, customer):
        try:
            cursor=self.conn.cursor()
            cursor.execute("Select p.product_id, p.name, p.price, ct.quantity From cart ct INNER JOIN products p ON p.product_id=ct.product_id where ct.customer_id=?",
                           (customer.get_customer_id(),))
            rows=cursor.fetchall()
            if not rows:
                raise CartEmptyException("Cart is empty. Please add items first.")
            return rows
        except CartEmptyException as ce:
            raise ce 
        except Exception as e:
            raise CustomException(f"Get All From Cart Failed: {e}")

    def place_order(self, customer, product_qty_list, shipping_address):
        try:
            cursor=self.conn.cursor()

            total_price=sum([product.get_price() *qty for product, qty in product_qty_list])
            cursor.execute("""INSERT INTO orders(customer_id, total_price, shipping_address)
                              OUTPUT INSERTED.order_id
                              VALUES (?, ?, ?)""",
                           (customer.get_customer_id(), total_price, shipping_address))

            order_id=cursor.fetchone()[0]


            for product, qty in product_qty_list:
                cursor.execute("""Insert into order_items(order_id, product_id,quantity, price) values (?,?,?,?)""",
                               (order_id, product.get_product_id(), qty, product.get_price()))
            self.conn.commit()
            return order_id

        except Exception as e:
            raise CustomException(f"Place Order Failed: {e}")

    def get_orders_by_customer(self, customer_id):
        try:
            cursor=self.conn.cursor()
            cursor.execute("""Select o.order_id, p.product_id, p.name, oi.quantity
                              From orders o
                              INNER JOIN order_items oi
                              ON o.order_id=oi.order_id
                              INNER JOIN products p
                              ON oi.product_id=p.product_id
                              Where o.customer_id=?""", (customer_id,))
            rows=cursor.fetchall()
            """if not rows:
                raise OrderNotFoundException("No orders found for this customer")"""
            return rows
        except Exception as e:
            raise CustomException(f"Get orders Failed: {e}")


    def get_all_orders_details(self):
        try:
            cursor= self.conn.cursor()
            cursor.execute("""SELECT o.order_id, o.order_date, o.total_price, o.shipping_address,
                                     c.customer_id, c.name, c.email,
                                     p.product_id, p.name, p.price,
                                     oi.quantity
                              From orders o
                              INNER JOIN customers c
                              ON o.customer_id=c.customer_id
                              INNER JOIN order_items oi ON o.order_id=oi.order_id
                              INNER JOIN products p ON oi.product_id = p.product_id
                              Order by o.order_id""")
            return cursor.fetchall()
        except EXception as e:
            raise CustomException(f"Fetch All Order Details Failed: {e}")
                                     
