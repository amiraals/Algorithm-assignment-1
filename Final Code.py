import time
from enum import Enum
import random

# Defining an Enum for different Chocolate types
class ChocolateType(Enum):
    ALMOND = "Almond chocolate"
    PEANUT_BUTTER = "Peanut butter chocolate"
    MILK = "Milk chocolate"
    DARK = "Dark chocolate"
    WHITE = "White chocolate"
    CARAMEL = "Caramel Chocolate"

# Defining a class for Chocolates
class Chocolate:
    """Class that represent a chocolate"""
    def __init__(self, weight, price, chocolate_type, id_number):
        # The chocolates attributes
        self.weight = weight
        self.price = price
        self.type = chocolate_type
        self.id = id_number

# Defining a function to generate random chocolates
def generate_random_chocolates(num_chocolates):
    chocolates = []  #Creating an empty list to store the generated chocolates
    for i in range(1, num_chocolates + 1):
        weight = random.randint(2, 12)  # Assuming weight range is between 2gm to 12gm
        price = random.randint(5, 45)    # Assuming price range is between 5 to 45 AED
        chocolate_type = random.choice(list(ChocolateType))  # Choses a random chocolate from the ENUM of ChocolateType
        chocolates.append(Chocolate(weight, price, chocolate_type, i))  #Appending the chocolate object to the chocolate list
    return chocolates

# Defining a function to generate student names
def generate_student_names(num_students):
    return [f"Student {i+1}" for i in range(num_students)]

# Defining a iterative function to distribute chocolates to students
def distribute_chocolates_iteratively(chocolates, students):
    distribution = {}   # Creating an empty dictionary to store the distribution of chocolates to students
    # Iterate over the range of the number of students
    for i in range(len(chocolates)):
        if i < len(chocolates):   # Check if there are enough chocolates for the current student
            distribution[students[i]] = chocolates[i]    # Assign the chocolate at index i to the student at index i
    return distribution

# Defining a recursive function to distribute chocolates to  students
def distribute_chocolates_recursively(chocolates, students, index=0, distribution=None):
    if distribution is None:
        distribution = {}    # Creating an empty dictionary to store the distribution of chocolates to students
    if index >= len(students) or index >= len(chocolates):  #Base Case
        return distribution
    distribution[students[index]] = chocolates[index]  # Assigning the chocolate at the current index to the student at the current index in the distribution dictionary
    return distribute_chocolates_recursively(chocolates, students, index + 1, distribution)   # Recursive call: Increase the index and call the function again with the updated index and distribution

# Generating random chocolates
chocolates = generate_random_chocolates(20)

# Generating list of student names based on the number of chocolates
students = generate_student_names(len(chocolates))


# Iterative distribution time
start_time_iterative = time.time()
distribution_iterative = distribute_chocolates_iteratively(chocolates, students)
end_time_iterative = time.time()
iterative_time = end_time_iterative - start_time_iterative

# Recursive distribution time
start_time_recursive = time.time()
distribution_recursive = distribute_chocolates_recursively(chocolates, students)
end_time_recursive = time.time()
recursive_time = end_time_recursive - start_time_recursive

if len(chocolates) == 0 or len(students) == 0:
    print(f"Iterative Distribution Time: {iterative_time:.6f} seconds")
    print(f"Recursive Distribution Time: {recursive_time:.6f} seconds")
else:
    print(f"Iterative Distribution Time: {iterative_time:.6f} seconds")
    print(f"Recursive Distribution Time: {recursive_time:.6f} seconds")

    def merge_sort(chocolates, key):
        if len(chocolates) <= 1:  # Base Case
            return chocolates
        mid = len(chocolates) // 2    # Finding the middle index of the chocolates list

        # Spliting the chocolates list into two halves: left_half and right_half
        left_half = chocolates[:mid]
        right_half = chocolates[mid:]

        # Recursive calls: Sort the left_half and right_half using the merge_sort function
        left = merge_sort(left_half, key)
        right = merge_sort(right_half, key)

        # Merging the sorted left and right halves using the merge function and then returning the merged result
        return merge(left, right, key)


    def merge(left, right, key):
        merged = []    # Creating an empty list to store the merged result
        i = j = 0    # Initializing two pointers, i and j, for the left and right lists
        while i < len(left) and j < len(right):
            # Comparing the elements from the left and right lists, and merge them in sorted order
            if getattr(left[i], key) <= getattr(right[j], key):
                # If the value in the left element is smaller or equal, we append it to the merged list
                merged.append(left[i])
                i += 1
            else:
                # If the value in the right element is smaller, we append it to the merged list
                merged.append(right[j])
                j += 1

        # Extend the merged list with any remaining elements from the left and right lists
        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged


    # Timing merge sort (sorting by weight)
    start_time_sort_weight = time.time()
    chocolates_sorted_by_weight = merge_sort(chocolates, 'weight') # Calling the function to sort by weight
    end_time_sort_weight = time.time()
    weight_sort_time = end_time_sort_weight - start_time_sort_weight

    # Timing merge sort (sorting by price)
    start_time_sort_price = time.time()
    chocolates_sorted_by_price = merge_sort(chocolates, 'price')  # Calling the function to sort by price
    end_time_sort_price = time.time()
    price_sort_time = end_time_sort_price - start_time_sort_price

    print(f"Sorting by weight time: {weight_sort_time:.6f} seconds")

    print()
    print(f"Sorting by price time: {price_sort_time:.6f} seconds")

    # Adjusting the binary search to find chocolate, then find which student has it
    def binary_search_chocolates(chocolates, target, key):
        low = 0
        high = len(chocolates) - 1

        while low <= high:
            mid = (low + high) // 2  # Calculating the middle index
            if key == "weight":
                mid_val = chocolates[mid].weight  # Getting the weight value of the chocolate at the middle index
            elif key == "price":
                mid_val = chocolates[mid].price  # Getting the price value of the chocolate at the middle index
            else:
                return "Invalid key"

            if mid_val < target:
                low = mid + 1  # If the middle value is less than the target, we narrow the search range to the upper half
            elif mid_val > target:
                high = mid - 1  # If the middle value is greater than the target, we narrow the search range to the lower half
            else:
                    chocolate = chocolates[mid]
                    student_name = students[chocolate.id - 1]  # Assuming student names are 0-based index
                    return f"The chocolate with {key} {target} was found with {student_name} (ID {chocolate.id})."
        return f"No chocolate with {key} {target} found."


    # Timing search by weight
    start_time_weight = time.time()
    weight_search_result = binary_search_chocolates(chocolates_sorted_by_weight,10 , 'weight')
    end_time_weight = time.time()
    search_weight_time = end_time_weight - start_time_weight

    # Timing search by price
    start_time_price = time.time()
    price_search_result = binary_search_chocolates(chocolates_sorted_by_price, 19, "price")
    end_time_price = time.time()
    search_price_time = end_time_price - start_time_price


    # Assuming merge_sort function is defined somewhere above as shown in the previous context
    print()
    print("Searching by weight:")
    print(weight_search_result)
    print(f"Binary search  weight time: {search_weight_time:.6f} seconds")

    print()
    print("Searching by price:")
    print(price_search_result)
    print(f"Binary search price time: {search_price_time:.6f} seconds")

