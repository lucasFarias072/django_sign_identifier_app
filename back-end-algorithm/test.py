

from unittest import TestCase
from algorithm import Sign


class SignTest(TestCase):
    def setUp(self) -> None:
        self.obj = Sign(arbitrary=True, mock_name='Betânia', mock_birth='02/01/2000')
        self.obj2 = Sign(arbitrary=True)
        self.obj3 = Sign(arbitrary=True)
        self.obj4 = Sign(arbitrary=True, mock_birth='02/11/2002')

    def test_get_input(self):
        self.assertEqual(self.obj.error, True)
        self.assertEqual(self.obj2.error, False)

    def test_get_born_date(self):
        self.assertEqual(self.obj2.person_birthday_string != self.obj3.person_birthday_string, False)
        self.assertEqual(self.obj.person_birthday_string != self.obj2.person_birthday_string, True)

    def test_generate_birthday_datatime(self):
        self.assertEqual(str(self.obj2.person_birthday_string) != str(self.obj3.person_birthday_string), False)
        self.assertEqual(str(self.obj.person_birthday_string) != str(self.obj2.person_birthday_string), True)

    def test_calculate_lifetime(self):
        self.assertEqual(self.obj2.person_days_alive != self.obj3.person_days_alive, False)
        self.assertEqual(self.obj.person_days_alive != self.obj2.person_days_alive, True)

    def test_find_sign(self):
        self.assertEqual(self.obj2.person_sign == self.obj3.person_sign, True)
        self.assertEqual(self.obj.person_sign == self.obj4.person_sign, False)
