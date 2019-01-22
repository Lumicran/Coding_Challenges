"""
Write a function nextPrimeArray(array) that takes in an array of numbers.
The function should return a new array where each prime number is replaced
with the prime number that come next sequentially. For example the prime number
that comes after 5 is 7.

Examples:

nextPrimeArray([-4, 2, 5, 4, 11]) => [ -4, 3, 7, 4, 13 ]
nextPrimeArray([9, 13, 5, 6]) => [ 9, 17, 7, 6 ]
nextPrimeArray([]) => []
"""

# Note that 2 and 3 are prime numbers. A trick to find prime numbers is to look at all multiples of
# six. The number below and above the multiple will be a prime number, unless it is 
# divisible by 5.

def foo(l):

  for i in range(len(l)):
    if l[i] == 3:
      l[i] = 5
      pass
    if l[i] % 5 == 0 and l[i] != 5:
      pass
    if (l[i] - 1) % 6 == 0:
      if (l[i] + 4) % 5 != 0:
        l[i] = l[i] + 4
        pass
      else:
        l[i] = l[i] + 6
      pass
    elif (l[i] + 1) % 6 == 0:
      if (l[i] + 2) % 5 != 0:
        l[i] = l[i] + 2
      else:
        l[i] = l[i] + 6

  return l


print(foo([9, 13, 5, 6]))
print(foo([-4, 2, 5, 4, 11]))


# function nextPrimeArray(arr) {
#   for (var i = 0; i < arr.length; i += 1) {
#     var num = arr[i];

#     if(isPrime(num)) {
#       arr[i] = nextPrime(num);
#     }
#   }
#   return arr;
# }

# function isPrime(n) {
#   if (n < 2) {
#     return false;
#   }

#   for (var i = 2; i < n; i += 1) {
#     if (n % i === 0) {
#       return false;
#     }
#   }
#   return true;
# }

# function nextPrime(n) {
#   n += 1;
#   while (!isPrime(n)) {
#     n += 1;
#   }
#   return n;
# }


# console.log(nextPrimeArray([-4, 2, 5, 4, 11])); //=> [ -4, 3, 7, 4, 13 ]
# console.log(nextPrimeArray([9, 13, 5, 6])) //=> [ 9, 17, 7, 6 ]
# console.log(nextPrimeArray([])) //=> []
