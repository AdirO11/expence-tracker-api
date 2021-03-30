from django.test import TestCase
from unittest import TestCase
import time


def two_int_sum(a, b):
    return a + b


class TestSum(TestCase):
    def test_sum(self):
        self.assertEqual(two_int_sum(1, 2), 3)
