
import unittest
import isbn


class MyTestCase(unittest.TestCase):

    def test_isValidISBN10(self):
        
        digits = "0316066524"
        output = isbn.isValidISBN10(digits)
        self.assertEqual(output,"Valid")

    def test_isInvalidISNB10(self):
        
        digits = "0330301824"
        output = isbn.isInvalidISBN10(digits)
        self.assertEqual(output,"Invalid")

    def test_isValidISBN13(self):

        digits = "9783866155237"
        output = isValidISNB13(digits)
        self.assertEqual(output,"Valid")
        
    
    def test_isInvalidISBN13(self):

        digits = "9783876155237"
        output = isbn.verify_isbn13(digits)
        self.assertEqual(output,"Invalid")
    
    def test_convertISBN10(self):
        
        digits = "0316066524"
        result = "9780316066525"
        output = isbn.convertISBN10(digits)
        self.assertEqual(output,result)