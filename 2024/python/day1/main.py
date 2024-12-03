import os

def load_data(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

def split_into_two_lists_per_line(data):
    list1 = []
    list2 = []
    for line in data.splitlines():
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)
    return list1, list2

def sort_lists(list1, list2):
    list1.sort()
    list2.sort()

def calculate_differences_per_row(list1, list2):
    differences = []
    for i in range(len(list1)):
        differences.append(abs(list1[i] - list2[i]))
    return differences

def calculate_total_differences(differences):
    return sum(differences)

def day1_part1_algorithm(filename):
    data = load_data(filename)
    list1, list2 = split_into_two_lists_per_line(data)
    sort_lists(list1, list2)
    differences = calculate_differences_per_row(list1, list2)
    return calculate_total_differences(differences)

def calculate_similarity_score(list1, list2):
    runningSimilarityScore = 0
    for i in range(len(list1)):
        # for value list1[i], count number of times it appears in list2
        count = list2.count(list1[i])
        runningSimilarityScore += count * list1[i]
    return runningSimilarityScore

def day1_part2_algorithm(filename):
    data = load_data(filename)
    list1, list2 = split_into_two_lists_per_line(data)
    return calculate_similarity_score(list1, list2)

if __name__ == '__main__':
    total_differences = day1_part1_algorithm('day1/puzzleinput1.txt')
    print(f'Day1 Part 1 - {total_differences}')
    similarity_score = day1_part2_algorithm('day1/puzzleinput1.txt')
    print(f'Day1 Part 2 - {similarity_score}')