import unittest
import rhyme

class TestRhyme(unittest.TestCase):


	def test_rhymes(self):

		self.assertTrue(rhyme.rhymes("how", "now"))
		self.assertFalse(rhyme.rhymes("brown", "cow"))
		
		self.assertTrue(rhyme.rhymes("violence", "silence"))
		self.assertTrue(rhyme.rhymes("me", "me"))
		self.assertFalse(rhyme.rhymes("arms", "harm"))
		self.assertTrue(rhyme.rhymes("broken", "spoken"))
		self.assertFalse(rhyme.rhymes("intense", "trivial"))
		self.assertTrue(rhyme.rhymes("remain", "pain"))
	
		self.assertFalse(rhyme.rhymes("relax", "contracts"))
		self.assertTrue(rhyme.rhymes("relax", "tacks"))

