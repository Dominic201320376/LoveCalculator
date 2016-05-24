# coding: utf-8

import unittest
from InputVerification import InputVerification
from FlamesCalculator import FlamesCalculator
from TrueLoveCalculator import TrueLoveCalculator

class TestInputVerification(unittest.TestCase):

	def testEmptyString(self):
		verifier = InputVerification()
		self.assertFalse(verifier.validate(""))

	def testCommaOnly(self):
		verifier = InputVerification()
		self.assertTrue(verifier.validate(","))

	def testOneNameNoComma(self):
		verifier = InputVerification()
		self.assertFalse(verifier.validate("name"))

	def testOneNameWithComma(self):
		verifier = InputVerification()
		self.assertTrue(verifier.validate("name,"))

	def testTwoNames(self):
		verifier = InputVerification()
		self.assertTrue(verifier.validate("name,names"))

	def testNamesWithNumbers(self):
		verifier = InputVerification()
		self.assertTrue(verifier.validate("name456,names123"))

	def testNamesWithNonASCIICharacters(self):
		verifier = InputVerification()
		self.assertTrue(verifier.validate("name,µé±├"))

class FlamesUnitTest(unittest.TestCase):

	def testOutputF(self):
		calc = FlamesCalculator("carl", "marco")
		self.assertEqual(calc.output(), "F")

	def testOutputL(self):
		calc = FlamesCalculator("regina", "potato")
		self.assertEqual(calc.output(), "L")

	def testOutputA(self):
		calc = FlamesCalculator("michelle", "juan")
		self.assertEqual(calc.output(), "A")

	def testOutputM(self):
	 	calc = FlamesCalculator("isabella", "eduardo")
	 	self.assertEqual(calc.output(), "M")

	def testOutputE(self):
		calc = FlamesCalculator("dominic", "lenovo")
		self.assertEqual(calc.output(), "E")

	def testOutputS(self):
		calc = FlamesCalculator("adfgikmnrtu", "bcehjlopqsvwxyzaaa")
		self.assertEqual(calc.output(), "S")

class TrueLoveUnitTest(unittest.TestCase):

	def testOutputZero(self):
		calc = TrueLoveCalculator("amaya", "amaya")
		self.assertEqual(calc.output(), 0)

	def testOutputOneDigit(self):
		calc = TrueLoveCalculator("makoy", "lovi")
		self.assertEqual(calc.output(), 4)

	def testOutputTwoDigits(self):
		calc = TrueLoveCalculator("athena", "zeus")
		self.assertEqual(calc.output(), 42)
	
	def testOutputThreeDigits(self):
		calc = TrueLoveCalculator("truelen", "louvette")
		self.assertEqual(calc.output(), 108)

	def testOutputGreaterThanThreeDigits(self):
		calc = TrueLoveCalculator("christopher taker truest true true true ulysses tomlinson truelen tart queue evaluater", "ttttttttrrrrrrrruuuuuueeeeeeeuueueueueueeueueueueueue")
		self.assertEqual(calc.output(), 1010)

if __name__ == '__main__':
	unittest.main()