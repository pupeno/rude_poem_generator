import unittest
import rhyme

class TestRhyme(unittest.TestCase):


	def test_rhymes(self):

		self.assertTrue(rhyme.ipa_rhymes("tip", "rip"))
		self.assertFalse(rhyme.ipa_rhymes("tip", "rig"))
		
		self.assertTrue(rhyme.rhymes("how", "now"))
		self.assertFalse(rhyme.rhymes("brown", "cow"))
	
		self.assertFalse(rhyme.rhymes("relax", "contracts"))
		self.assertTrue(rhyme.rhymes("relax", "tacks"))

