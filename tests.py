

#Write a program that prints the numbers from 1 to 100. For multiples of 3, 
# print "Fizz"; for multiples of 5, print "Buzz"; 
# and for numbers that are multiples of both 3 and 5, print "FizzBuzz".

for num in range(0, 100):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
        
    elif num % 5 == 0:
        print("Buzz")
        
    elif num % 3 == 0:
        print("Fizz")
        
    else:
        print(num)


# Question 2: Fibonacci Sequence
# Write a program to generate the Fibonacci sequence up to 100.
def fib_seq(n):
    fib_serie = [0, 1]  
    while fib_serie[-1] + fib_serie[-2] <= n:
        fib_serie.append(fib_serie[-1] + fib_serie[-2]) 
    return fib_serie 

fibonacci_numbers = fib_seq(100)  
print(fibonacci_numbers)  





# Question 3: Power of Two
# Write a program that takes an integer as
# input and returns true if the input is a power of two.

def power_of_two(n):
    if n > 0 and (n & (n-1)) == 0:
        return True
    else:
        return False
print(power_of_two(10))  





# Question 4: Capitalize Words
# Write a program that accepts a string as input, 
# capitalizes the first letter of each word in the string,
# and then returns the result string.
def caps(my_str):
    return my_str.title()

my_str = "i am a sofware engineer"
output = caps(my_str)
print(output)  

# Write a program that takes an integer as input 
# and returns an integer with reversed digit ordering.
# Examples:
def integer_reverse(num):
    if num < 0:
        return int(str(num)[0] + str(num)[:0:-1])
    else:
        return int(str(num)[::-1])

print(integer_reverse(500))  # Output: 5
print(integer_reverse(-56))  # Output: -65
print(integer_reverse(-90))  # Output: -9
print(integer_reverse(91))   # Output: 19



# Question 6: Count Vowels
# Write a program that counts the number of vowels in a sentence.
def vowel_count(sentence):
    vowels = "aeiouAEIOU"
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count
sentence = "Hello World"
print(vowel_count(sentence))  
        
   

