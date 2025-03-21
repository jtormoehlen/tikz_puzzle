import unittest


def search(numbers, elem):
    mid = len(numbers) // 2

    if mid <= 1:
        return False
    else:
        if numbers[mid] == elem:
            return True
        
        left = list(numbers[:mid])
        right = list(numbers[mid:])

        search(left, elem)
        search(right, elem)


# Unit-Tests für die Funktion search()

class TestSearchFunction(unittest.TestCase):

    def test_number_exists_in_list(self):
        self.assertTrue(search([1, 2, 3, 4, 5], 3))  # 3 ist in der Liste

    def test_number_does_not_exist_in_list(self):
        self.assertFalse(search([1, 2, 3, 4, 5], 6))  # 6 ist nicht in der Liste

    def test_empty_list(self):
        self.assertFalse(search([], 1))  # Leere Liste, keine Zahl vorhanden

    def test_number_is_first_element(self):
        self.assertTrue(search([1, 2, 3], 1))  # 1 ist das erste Element

    def test_number_is_last_element(self):
        self.assertTrue(search([1, 2, 3], 3))  # 3 ist das letzte Element

    def test_number_in_large_list(self):
        self.assertTrue(search(list(range(1000)), 500))  # 500 ist in der Liste von 0 bis 999

    def test_negative_number(self):
        self.assertTrue(search([-1, -2, -3, -4], -3))  # -3 ist in der Liste

    def test_positive_and_negative_numbers(self):
        self.assertTrue(search([-1, 0, 1, 2], 0))  # 0 ist in der Liste

if __name__ == '__main__':
    unittest.main()
        