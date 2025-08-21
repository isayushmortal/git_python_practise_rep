# Question 1
'''Even or Odd Number Check: Write a Python program that takes an integer as input from
 the user and determines whether it is an even or an odd number.'''
'''def check_even_odd(number):
    if number % 2 == 0:
        print("number is even")
    else:
        print("number is odd")


print(check_even_odd(5))'''
    




# Question 2
'''Calculate the Factorial: Write a Python function that calculates the factorial of a 
non-negative integer. The factorial of a number n is the product of all positive integers
 less than or equal to n. (e.g., 5! = 5 * 4 * 3 * 2 * 1 = 120).'''
'''def factorial(number):
    product = 1
    for i in range (1,number+1):
        product *= i

    return product
print(factorial(4))'''

    

# Question 3
'''Reverse a String: Write a Python program that takes a string as input and prints its reversed version.

'''
'''string = input("Enter a string: ")

reversed_string = string[::-1]

print("Reversed string:", reversed_string)'''


# Question 4
'''Find the Largest Number in a List: Write a Python program that finds and prints the largest number
 in a given list of integers.'''
'''numbers = [12, 45, 78, 23, 56, 89, 5, 34]

largest_number = max(numbers)

print("The largest number in the list is:", largest_number)'''

# Question 5
'''Count Vowels in a String: Write a Python function that takes a string as input and returns the count 
of vowels (a, e, i, o, u, case-insensitive) present in the string.'''
def cou_vowel():
    ay = "gayudlhg"
    ay = ay.upper()
    vowel = ['A','I','E','O','U']
    count = 0

    for i in range(1,len(ay)):
        if ay[i] in vowel:
            count += 1
    return  count


print(cou_vowel())



