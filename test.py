import unittest
import cu

class Test(unittest.TestCase):
	def test(self):
		tests = 100
		val = cu.cu(1,5)

		for test in range(tests):
			self.assertNotEqual(val(), val())

if __name__ == '__main__':
    unittest.main()
