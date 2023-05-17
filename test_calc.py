import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply(self):
        assert self.calc.multiply(self, 4, 2) == 8

    def test_division(self):
        assert self.calc.division(self, 4, 2) == 2

    def test_subtraction(self):
        assert self.calc.subtraction(self, 4, 2) == 2

    def test_adding(self):
        assert self.calc.adding(self, 4, 2) == 6