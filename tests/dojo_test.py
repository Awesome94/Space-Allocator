import unittest
from src.dojo import Dojo


class TestCreateRoom (unittest.TestCase):

    def setUp(self):
        self.dojo = Dojo()
        self.test_office = self.dojo.create_room("office", "test")
        self.test_living_space = self.dojo.create_room("living_space", "test living space")
        
    def test_create_room_successfully(self):
        my_class_instance = Dojo()
        initial_room_count = len(my_class_instance.all_rooms)
        blue_office = my_class_instance.create_room("office", "Blue")
        self.assertTrue(blue_office)
        new_room_count = len(my_class_instance.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_create_rooms_successfully(self):
        my_class_instance = Dojo()
        initial_room_count = len(my_class_instance.all_rooms)
        offices = my_class_instance.create_room("office", "Blue", "Black", "Brown")
        self.assertTrue(offices)
        new_room_count = len(my_class_instance.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 3)