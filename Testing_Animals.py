import unittest
from my_code import *


class TestMyCode(unittest.TestCase):

    def test_dog_tail(self):
       self.assertEqual(dog.tail, 1)

    def test_incorrect_dog_tail(self):
       self.assertNotEqual(dog.tail, 2)

    def test_dog_wool(self):
       self.assertTrue(dog.wool)

    def test_false_dog_wool(self):
       self.assertFalse(dog.wool)

    def test_dog_paws(self):
       self.assertEqual(dog.paw, 4)

    def test_incorrect_dog_paws(self):
       self.assertNotEqual(dog.paw, 3)

    def test_lion_tail(self):
       self.assertEqual(lion.tail, 1)

    def test_lion_tail_incorrect(self):
        self.assertNotEqual(lion.tail, 2)

    def test_lion_wool(self):
        self.assertTrue(lion.wool)

    def test_lion_wool_false(self):
        self.assertFalse(lion.wool)

    def test_lion_paws(self):
        self.assertEqual(lion.paw, 4)

    def test_lion_paws_incorrect(self):
        self.assertNotEqual(lion.paw, 5)

    def test_cat1_tail(self):
        self.assertEqual(cat1.tail, 1)

    def test_cat1_tail_incorrect(self):
        self.assertNotEqual(cat1.tail, 2)

    def test_cat1_wool(self):
        self.assertTrue(cat1.wool)

    def test_cat1_wool_false(self):
        self.assertFalse(cat1.wool)

    def test_cat1_paws(self):
        self.assertEqual(cat1.paw, 4)

    def test_cat1_paws_incorrect(self):
        self.assertNotEqual(cat1.paw, 5)

    def test_cat2_tail(self):
        self.assertEqual(cat2.tail, 1)

    def test_cat2_tail_incorrect(self):
        self.assertNotEqual(cat2.tail, 2)

    def test_cat2_wool(self):
        self.assertFalse(cat2.wool)

    def test_cat2_wool_false(self):
        self.assertTrue(cat2.wool)

    def test_cat2_paws(self):
        self.assertEqual(cat2.paw, 4)

    def test_cat2_paws_incorrect(self):
        self.assertNotEqual(cat2.paw, 5)

    def test_rooster_tail(self):
        self.assertEqual(rooster1.tail, 1)

    def test_rooster_tail_incorrect(self):
        self.assertNotEqual(rooster1.tail, 2)

    def test_rooster_wool(self):
        self.assertFalse(rooster1.wool)

    def test_rooster_wool_false(self):
        self.assertTrue(rooster1.wool)

    def test_rooster_paws(self):
        self.assertEqual(rooster1.paw, 2)

    def test_rooster_paws_incorrect(self):
        self.assertNotEqual(rooster1.paw, 4)

