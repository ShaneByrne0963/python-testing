def even_number_of_evens(numbers):
    """
    Should Raise a TypeError if a list in not passed into the function
    error message: "A list was not passed into the function"
    if the list is empty it will return False
    if the number of even numbers is odd - return False
    if the numner of even numbers is even - return True
    """

    if isinstance(numbers, list):
        even_numbers = sum([1 for n in numbers if n % 2 == 0])

        return even_numbers and even_numbers % 2 == 0
    else:
        raise TypeError


if __name__ == "__main__":
    print(even_number_of_evens(5))
