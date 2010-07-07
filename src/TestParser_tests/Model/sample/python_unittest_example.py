#!/usr/bin/python3
'''
This is a python unittest suite to be used as sample input for Test Parser
(running and TestParser's unittests.)

It also serves as an example for end users so that they can see what will
work.

Note: this example is from Python's Unittest documentation, with minor
changes to make it work with both python 2.x and 3.x.

@date Jun 28, 2010
@author Matthew A. Todd

This file is part of Test Parser
by Matthew A. Todd

Test Parser is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Test Parser is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Test Parser.  If not, see <http://www.gnu.org/licenses/>.
'''

import random
import unittest
import sys

class TestSequenceFunctions(unittest.TestCase):

	def setUp(self):
		self.seq = [i for i in range(10)]

	def test_shuffle(self):
		# make sure the shuffled sequence does not lose any elements
		random.shuffle(self.seq)
		self.seq.sort()
		self.assertEqual(self.seq, [i for i in range(10)])

	def test_choice(self):
		element = random.choice(self.seq)
		self.assertTrue(element in self.seq)

	def test_sample(self):
		self.assertRaises(ValueError, random.sample, self.seq, 20)
		for element in random.sample(self.seq, 5):
			self.assertTrue(element in self.seq)

	def test_fail(self):
		self.fail()
		
	def test_error(self):
		raise NotImplementedError

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
	unittest.TextTestRunner(verbosity=2, stream=sys.stdout).run(suite)


