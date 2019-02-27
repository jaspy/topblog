from django.test import TestCase

class TemporaryTest(TestCase):
    def test_if_two_equals_two(self):
        self.assertEqual(2, 2)
