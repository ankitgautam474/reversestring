def reverse_string(input_str):
    reversed_str = input_str[::-1]
    return reversed_str

# Get input from the user
input_str = input("Enter a string: ")

# Call the reverse_string function with the user input
result = reverse_string(input_str)
print(result)
