# coding: utf-8

import unittest
from InputValidator import InputValidator
from FlamesCalculator import FlamesCalculator
from TrueLoveCalculator import TrueLoveCalculator

class TestInputValidator(unittest.TestCase):

	def testEmptyString(self):
		verifier = InputValidator()
		self.assertFalse(verifier.validate(""))

	def testCommaOnly(self):
		verifier = InputValidator()
		self.assertFalse(verifier.validate(","))

	def testMoreThanOneComma(self):
		verifier = InputValidator()
		self.assertFalse(verifier.validate(",,"))

	def testOneNameNoComma(self):
		verifier = InputValidator()
		self.assertFalse(verifier.validate("name"))

	def testOneNameWithComma(self):
		verifier = InputValidator()
		self.assertFalse(verifier.validate("name,"))

	def testTwoNames(self):
		verifier = InputValidator()
		self.assertTrue(verifier.validate("name,names"))

	def testNamesWithNumbers(self):
		verifier = InputValidator()
		self.assertFalse(verifier.validate("name456,names123"))

	def testNamesWithNonASCIICharacters(self):
		verifier = InputValidator()
		self.assertFalse(verifier.validate("name,µé±├"))

class FlamesUnitTest(unittest.TestCase):

	def testOutputF(self):
		calc = FlamesCalculator("carl", "marco")
		self.assertEqual(calc.output(), "Friendship")

	def testOutputL(self):
		calc = FlamesCalculator("regina", "potato")
		self.assertEqual(calc.output(), "Love")

	def testOutputA(self):
		calc = FlamesCalculator("michelle", "juan")
		self.assertEqual(calc.output(), "Affection")

	def testOutputM(self):
	 	calc = FlamesCalculator("isabella", "eduardo")
	 	self.assertEqual(calc.output(), "Marriage")

	def testOutputE(self):
		calc = FlamesCalculator("dominic", "lenovo")
		self.assertEqual(calc.output(), "Enemy")

	def testOutputS(self):
		calc = FlamesCalculator("adfgikmnrtu", "bcehjlopqsvwxyzaaa")
		self.assertEqual(calc.output(), "Sister")

class TrueLoveUnitTest(unittest.TestCase):

	def testOutputZero(self):
		calc = TrueLoveCalculator("amaya", "amaya")
		self.assertEqual(calc.output(), "0")

	def testOutputOneDigit(self):
		calc = TrueLoveCalculator("makoy", "lovi")
		self.assertEqual(calc.output(), "4")

	def testOutputTwoDigits(self):
		calc = TrueLoveCalculator("athena", "zeus")
		self.assertEqual(calc.output(), "42")
	
	def testOutputThreeDigits(self):
		calc = TrueLoveCalculator("truelen", "louvette")
		self.assertEqual(calc.output(), "108")

	def testOutputGreaterThanThreeDigits(self):
		calc = TrueLoveCalculator("christopher taker truest true true true ulysses tomlinson truelen tart queue evaluater", "ttttttttrrrrrrrruuuuuueeeeeeeuueueueueueeueueueueueue")
		self.assertEqual(calc.output(), "9740")

if __name__ == '__main__':
	unittest.main()