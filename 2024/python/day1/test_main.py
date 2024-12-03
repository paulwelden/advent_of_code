import unittest
import main

class TestMain(unittest.TestCase):
    def test_load_data(self):
        data = main.load_data('day1/example1.txt')
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0)

    def test_split_into_two_lists_per_lind(self):
        data = main.load_data('day1/example1.txt')
        list1, list2 = main.split_into_two_lists_per_line(data)
        self.assertEqual(len(list1), len(list2))
        self.assertEqual(len(list1), 6)
        self.assertEqual(len(list2), 6)

    def test_sort_lists(self):
        list1 = [2, 3, 1]
        list2 = [4, 6, 5]
        main.sort_lists(list1, list2)
        self.assertEqual(list1, [1, 2, 3])
        self.assertEqual(list2, [4, 5, 6])
    
    def test_calculate_differences_per_row(self):
        list1 = [1, 5, 2]
        list2 = [3, 2, 6]
        differences = main.calculate_differences_per_row(list1, list2)
        self.assertEqual(differences, [2, 3, 4])

    def test_calculate_total_differences(self):
        differences = [2, 3, 4]
        total = main.calculate_total_differences(differences)
        self.assertEqual(total, 9)

    def test_day1_part1_algorithm(self):
        total_differences = main.day1_part1_algorithm('day1/example1.txt')
        self.assertEqual(total_differences, 11)

    def test_calcualte_similarity_score(self):
        list1 = [1, 2, 3]
        list2 = [3, 1, 1]
        similarity_score = main.calculate_similarity_score(list1, list2)
        self.assertEqual(similarity_score, 5)
    
    def test_day1_part2_algorithm(self):
        similarity_score = main.day1_part2_algorithm('day1/example1.txt')
        self.assertEqual(similarity_score, 31)

if __name__ == '__main__':
    unittest.main()
