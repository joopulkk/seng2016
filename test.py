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
        app =FizzBuzz()
        self.failIf(app.calc(3) != "Fizz")
        self.failIf(app.calc(21) != "Fizz")
        self.failIf(app.calc(63) != "Fizz")
        
        
    def test_Buzz(self):
        app =FizzBuzz()
        self.failIf(app.calc(5) != "Buzz")
        self.failIf(app.calc(10) != "Buzz")
        self.failIf(app.calc(25) != "Buzz")
		
    def test_FizzBuzz(self):
        app =FizzBuzz()
        self.failIf(app.calc(15) != "FizzBuzz")
        self.failIf(app.calc(45) != "FizzBuzz")
        self.failIf(app.calc(60) != "FizzBuzz")

def main():
    unittest.main()

if __name__ == "__main__":
    main()
