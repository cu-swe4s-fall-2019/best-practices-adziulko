import unittest
import get_column_stats as gcs



class TestCalc(unittest.TestCase):

    def test_mean_empty_list(self):
        r = gcs.mean([])
        self.assertEqual(r, None)

    def test_mean_null_list(self):
        r = gcs.mean(None)
        self.assertEqual(r, None)

    def test_mean_const_small(self):
        r = gcs.mean([1])
        self.assertEqual(r, 1)

    def test_mean_list_not_passed(self):
        with self.assertRaises(TypeError) as ex:
            r = gcs.mean('not a list')
            self.assertEqual(str(ex.exception), 'Mean undefined.')


if __name__ == '__main__':
    unittest.main()
