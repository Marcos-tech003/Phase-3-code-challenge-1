def add_numbers(num1, num2):
    return num1 + num2

def is_even(number):
    return number % 2 == 0

def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def calculate_factorial(n):
    if n < 0:
        return "Invalid input. Enter a non-negative integer."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

@decorator_func
def apply_decorator(func):
    return func()

def sort_by_age(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])

def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")

if __name__ == "__main__":
    print(add_numbers(10, 5))
    print(is_even(4))
    print(is_even(7))
    print(reverse_string("hello"))
    print(count_vowels("OpenAI is amazing!"))
    print(calculate_factorial(5))
    print(calculate_factorial(0))

    @decorator_func
    def sample_function():
        return "Sample function executed"
    print(sample_function())

    people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    print(sort_by_age(people))

    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 3, 'c': 4, 'd': 5}
    print(merge_dicts(dict1, dict2))

    car = Car("Toyota", "Corolla", 2020)
    car.display_info()