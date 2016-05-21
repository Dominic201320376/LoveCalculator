# coding: utf-8

import unittest
from InputVerification import InputVerification

class TestInputVerification(unittest.TestCase):

	def testEmptyString(self):
		verifier = InputVerification()
		self.assertFalse(verifier.validate(""))

	def testCommaOnly(self):
		verifier = InputVerification()
		self.assertTrue(verifier.validate(","))

	def testOneNameNoComma(self):
		verifier = InputVerification()
		self.assertFalse(verifier.validate("Name"))

	def testOneNameWithComma(self):
		verifier = InputVerification()
		self.assertTrue(verifier.validate("Name,"))

	def testTwoNames(self):
		verifier = InputVerification()
		self.assertTrue(verifier.validate("Name,Names"))

	def testNamesWithNumbers(self):
		verifier = InputVerification()
		self.assertTrue(verifier.validate("Name456,Names123"))

	def testNamesWithNonASCIICharacters(self):
		verifier = InputVerification()
		self.assertTrue(verifier.validate("Name,µé±├"))

if __name__ == '__main__':
	unittest.main()