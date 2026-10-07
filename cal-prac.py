print("======= Welcome to My Simple Python Calculator =======")
#collect data from user
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
print()
#convert and store data as whole numbers while carrying out operations
addition = float(first_number) + float(second_number)
subtraction = float(first_number) - float(second_number)
multiplication = float(first_number) * float(second_number)
division = float(first_number) / float(second_number)
#display answers
print("======= Here's Your Results =======")
print(f"Addition: {addition} \nSubtraction: {subtraction} \nMultiplication: {multiplication} \nDivision: {division}")
