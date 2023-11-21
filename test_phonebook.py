from phonebook import Phonebook
import unittest, names

class TestPhonebook(unittest.TestCase):
    def setUp(self):
        self.phonebook = Phonebook()

    def test_add_contact(self):
        name = names.get_full_name()
        self.phonebook.add_contact(name, "123456789")
        self.assertIn(name, self.phonebook.contacts)
        self.assertEqual(self.phonebook.contacts[name], "123456789")

    def test_add_existing_contact(self):
        name = names.get_full_name()
        self.phonebook.add_contact(name, "012345678")
        self.assertIn(name, self.phonebook.contacts)
        self.assertEqual(self.phonebook.add_contact(name, "012345678"), f"Contact {name} already exists.")

    def test_remove_existing_contact(self):
        name = names.get_full_name()
        self.phonebook.add_contact(name, "987654321")
        self.phonebook.remove_contact(name)
        self.assertNotIn(name, self.phonebook.contacts)

    def test_remove_nonexistent_contact(self):
        name = names.get_full_name()
        result = self.phonebook.remove_contact(name)
        self.assertEqual(result, f"Contact {name} was not found.")

    def test_find_existing_contact(self):
        name = names.get_full_name()
        self.phonebook.add_contact(name, "555555555")
        result = self.phonebook.find_contact(name)
        self.assertEqual(result, f"Name: {name}, Phone: 555555555")

    def test_find_nonexistent_contact(self):
        name = names.get_full_name()
        result = self.phonebook.find_contact(name)
        self.assertEqual(result, f"Contact {name} was not found.")

    def test_empty_contacts_list(self):
        result = self.phonebook.list_contacts()
        self.assertEqual(result, "The phonebook is empty.")

    def test_contacts_list(self):
        name = names.get_full_name(gender='male')
        other_name = names.get_full_name(gender='female')
        self.phonebook.add_contact(name, "111111111")
        self.phonebook.add_contact(other_name, "222222222")
        result = self.phonebook.list_contacts()
        expected_result = {f'{name}' : '111111111', f'{other_name}' : '222222222'}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
