from collections import Counter

numbers = ["Randy", "Mikhael", "Ribka", "Randy"]
count = Counter(numbers)

unique_elements = [num for num, freq in count.items() if freq == 1]
print(unique_elements)