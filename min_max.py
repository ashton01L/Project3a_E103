# Author: Ashton Lee
# Github User: ashton01L
# Date: 7/10/2024

# Description: Write a program that asks the user how many integers they
# would like to enter. You can assume that this initial input will be
# an integer >= 1. The program will then prompt the user to enter that
# many integers. After all the numbers have been entered, the program
# should display the largest and smallest of those numbers (no, you cannot
# use lists, or any other material we haven't covered). Your code should
# work correctly no matter what integers the user enters.

def main():
    while True:
        try:
            # Prompt user for the number of integers
            num_integers = int(input("How many integers would you like to enter?\n"))

            if num_integers <1:
                raise ValueError("Invalid input. Please enter a valid integer.")

            # Initialize variables to store minimum and maximum integers
            minimum = None
            maximum = None

            # Prompt user to enter each integer and find smallest and largest
            for i in range(num_integers):
                num = int(input())

                # Update smallest and largest
                if minimum is None or num < minimum:
                    minimum = num
                if maximum is None or num > maximum:
                    maximum = num

            # Display the smallest and largest integers entered
            print(f"min: {minimum}")
            print(f"max: {maximum}")
            break

        except ValueError as ve:
            print(f"You have provoked a value error. Please enter a valid integer.")
        except Exception as e:
            print(f"You have provoked an unexpected error.")


if __name__ == "__main__":
    main()
