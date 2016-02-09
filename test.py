import unittest
import sys
from StringIO import StringIO

from app import FizzBuzz

class TestSuite(unittest.TestCase):

    def test_one(self):
        app = FizzBuzz()
        self.failIf(app.calc(1) != 1)

    def test_run(self):
        output = StringIO()

        app = FizzBuzz()
        app.run(100, output)

        self.failIf(len(output.getvalue().splitlines()) != 100)
		
    def test_Fizz(self):
        app = FizzBuzz()
        self.failIf(app.calc(6) != "Fizz")
        self.failIf(app.calc(24) != "Fizz")
        self.failIf(app.calc(36) != "Fizz")
        
        
    def test_Buzz(self):
        app = FizzBuzz()
        self.failIf(app.calc(10) != "Buzz")
        self.failIf(app.calc(40) != "Buzz")
        self.failIf(app.calc(50) != "Buzz")
		
    def test_FizzBuzz(self):
        app = FizzBuzz()
        self.failIf(app.calc(15) != "FizzBuzz")
        self.failIf(app.calc(45) != "FizzBuzz")
        self.failIf(app.calc(60) != "FizzBuzz")
		
	def test_prime(self):
		app = FizzBuzz()
		self.failIf(app.calc(2) != "2 is a prime")
		self.failIf(app.calc(47) != "47 is a prime")
		self.failIf(app.calc(97) != "97 is a prime")
		
	def test_notprime(self):
		app = FizzBuzz()
		self.failIf(app.calc(6) == "6 is a prime")
		self.failIf(app.calc(32) == "32 is a prime")
		self.failIf(app.calc(54) == "54 is a prime")

def main():
    unittest.main()

if __name__ == "__main__":
    main()
