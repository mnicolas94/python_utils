import unittest

from mnd_utils.datastructures.stream import Stream


class TestStream(unittest.TestCase):
	"""
	Tests para la clase mnd_utils.datastructures.Stream.
	"""

	def test_stream(self):
		def gen(count):
			for i in range(count):
				yield i
		s = Stream(gen(10))
		self.assertIn(0, s)
		self.assertEqual([0, 1, 2], s[:3])
		self.assertEqual([], s[-5:4])
		self.assertEqual([5, 6, 7], s[5:8])
		self.assertEqual(3, s[3])
		self.assertEqual(7, s[-3])
		self.assertEqual(list(range(10)), s[:])
		self.assertEqual([5, 6, 7, 8], s[-5:9])
		self.assertEqual([5, 6, 7, 8], s[-5:-1])

		# las mismas pruebas pero reiniciando el stream antes de cada una
		s = Stream(gen(10))
		self.assertEqual([0, 1, 2], s[:3])
		s = Stream(gen(10))
		self.assertEqual([], s[-5:4])
		s = Stream(gen(10))
		self.assertEqual([5, 6, 7], s[5:8])
		s = Stream(gen(10))
		self.assertEqual(3, s[3])
		s = Stream(gen(10))
		self.assertEqual(7, s[-3])
		s = Stream(gen(10))
		self.assertEqual(list(range(10)), s[:])
		s = Stream(gen(10))
		self.assertEqual([5, 6, 7, 8], s[-5:9])
		s = Stream(gen(10))
		self.assertEqual([5, 6, 7, 8], s[-5:-1])


if __name__ == '__main__':
	unittest.main()
