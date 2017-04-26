import unittest
from src.dojo import Dojo


class TestCreateRoom (unittest.TestCase):
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

    def test_person_added_to_system(self):
        initial_person_count = len(self.dojo.all_people)
        person = self.dojo.add_person("Neil", "Armstrong", "Staff")
        self.assertTrue(person)
        new_person_count = len(self.dojo.all_people)
        self.assertEqual(new_person_count - initial_person_count, 1)