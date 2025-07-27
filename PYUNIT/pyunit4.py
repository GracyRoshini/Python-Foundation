import unittest

marks=[90,90,100]
dept="cse it ece eee mech civil"

#Apply pyunit
class Test(unittest.TestCase):
    def test_elementsIn_positive(self):
        self.assertIn(90,marks)

    def test_elementsIn_negative(self):
        self.assertIn(65,marks)

    def test_stringElements_positive(self):
        self.assertIn('eee',dept)
        self.assertIn('cse',dept)
        self.assertIn('it',dept)

    def test_string_Elements_negative(self):
        self.assertIn('accounts',dept)

    def test_string_Elements_mixed(self):
        self.assertIn('accounts',dept)
        self.assertIn('it',dept)

    def test_NotIn(self):
        self.assertNotIn('accounts',dept)




unittest.main()
