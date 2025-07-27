import sys
import os
import uuid
sys.path.append("C:/Gracy_Info/Hexaware/Python Foundation Training - Batch 2/Project/E-commerce")

import unittest
from dao.OrderProcessorImpl import OrderProcessorImpl
from entity.products import Products
from entity.customers import Customers
from exception.customer_not_found import CustomerNotFoundException
from exception.product_not_found import ProductNotFoundException
from exception.custom_exception import CustomException

class TestEcommerceService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.processor=OrderProcessorImpl()

    def test_create_product(self):
        product=Products(name="TestProduct", price=1000, description="Testing", stock_quantity=10)
        result=self.processor.create_product(product)
        self.assertTrue(result)
        
    def test_create_customer(self):
        unique_email = f"testuser_{uuid.uuid4().hex[:6]}@example.com"    #--Universally Unique Identifier, testuser_ab12cd@example.com
        customer=Customers(name="TestUser", email=unique_email, password="test123")
        result=self.processor.create_customer(customer)
        self.assertTrue(result)

    def test_add_to_cart_succes(self):
        customer=Customers(customer_id=1)
        product=Products(product_id=1)
        result=self.processor.add_to_cart(customer, product,1)
        self.assertTrue(result)

    def test_place_order_success(self):
        customer=Customers(customer_id=1)
        product=Products(product_id=1, name="Printer", price=4202, description="All-in-one", stock_quantity=36)
        result=self.processor.place_order(customer,[(product,1)], "TestAddress")
        self.assertIsInstance(result,int)

    def test_get_cart_items(self):
        customer=Customers(customer_id=99)
        cart_items=self.processor.get_all_from_cart(customer)
        self.assertIsInstance(cart_items,list)

    def test_get_orders_by_customer(self):
        orders=self.processor.get_orders_by_customer(1)
        self.assertIsInstance(orders,list)

    def test_customer_not_found_exception(self):
        with self.assertRaises(CustomException):
            self.processor.delete_customer(99999)

    def test_product_not_found_exception(self):
        with self.assertRaises(CustomException):
            self.processor.delete_product(99999)

if __name__=='__main__':
        unittest.main()
