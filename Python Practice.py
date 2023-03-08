# # def product(a, b):
# #     """Return product of a and b.

# #         >>> product(2, 2)
# #         4

# #         >>> product(2, -2)
# #         -4
# #     """

# #     return a * b


# # def weekday_name(day_of_week):
# #     """Return name of weekday.

# #         >>> weekday_name(1)
# #         'Sunday'

# #         >>> weekday_name(7)
# #         'Saturday'

# #     For days not between 1 and 7, return None

# #         >>> weekday_name(9)
# #         >>> weekday_name(0)
# #     """
# #     days = ['Sunday', 'Monday', 'Tuesday',
# #         'Wednesday', 'Thursday', 'Friday', 'Saturday']
# #     if day_of_week < 1 or day_of_week > 7:
# #         return None
# #     else: return day_of_week[-1]


# # def last_element(lst):
# #     """Return last item in list (None if list is empty.

# #
# #     if last_element == []:
# #         return None
# #     else:
# #         return last_element[-1]


# #        def number_compare(a, b):
# #     """Report on whether a>b, b>a, or b==a

# #     if a > b:
# #         return 'First is greater'
# #     elif b > a:
# #         return 'Second is greater'

# #     else: return 'Numbers are equal'


# from collections import Counter


# def reverse_string(phrase):

#     return phrase[::-1]


# def single_letter_count(word, letter):
#     """How many times does letter appear in word (case-insensitively)?"""

#     word = word.lower()
#     letter = letter.lower()

#     # Count the number of times the letter appears in the word using a list comprehension
#     count = len([char for char in word if char == letter])

#     return count


# def multiple_letter_count(phrase):
#     """Return dict of {ltr: frequency} from phrase.

#         >>> multiple_letter_count('yay')
#         {'y': 2, 'a': 1}

#         >>> multiple_letter_count('Yay')
#         {'Y': 1, 'a': 1, 'y': 1}
#     """

#     letter_count = {}

#     for char in phrase:
#         char = char.lower()
#         letter_count[char] = letter_count.get(char, 0) + 1

#         return letter_count


# def list_manipulation(lst, command, location, value=None):
#     """Mutate lst to add/remove from beginning or end.

#     - lst: list of values
#     - command: command, either "remove" or "add"
#     - location: location to remove/add, either "beginning" or "end"
#     - value: when adding, value to add

#     remove: remove item at beginning or end, and return item removed

#         >>> lst = [1, 2, 3]

#         >>> list_manipulation(lst, 'remove', 'end')
#         3

#         >>> list_manipulation(lst, 'remove', 'beginning')
#         1

#         >>> lst
#         [2]

#     add: add item at beginning/end, and return list

#         >>> lst = [1, 2, 3]

#         >>> list_manipulation(lst, 'add', 'beginning', 20)
#         [20, 1, 2, 3]

#         >>> list_manipulation(lst, 'add', 'end', 30)
#         [20, 1, 2, 3, 30]

#         >>> lst
#         [20, 1, 2, 3, 30]

#     Invalid commands or locations should return None:

#         >>> list_manipulation(lst, 'foo', 'end') is None
#         True

#         >>> list_manipulation(lst, 'add', 'dunno') is None
#         True
#     """

#     if location == 'end':
#         if command == 'remove':
#             return lst.pop()

#     elif location == 'beginning':
#         if command == 'remove':
#             return lst.pop(0)

#     elif command == 'add':
#         if location == 'end':
#             lst.append(value)

#     elif location == 'beginning':
#         lst.insert(0, value)
#         return lst

#     else:

#         return None

#     def is_palindrome(phrase):
#         # """Is phrase a palindrome?

#         phrase = ''.join(phrase.lower().split())
#         return phrase == phrase[::-1]


# def flip_case(phrase, to_swap):
#     """Flip [to_swap] case each time it appears in phrase.

#         >>> flip_case('Aaaahhh', 'a')
#         'aAAAhhh'

#         >>> flip_case('Aaaahhh', 'A')
#         'aAAAhhh'

#         >>> flip_case('Aaaahhh', 'h')
#         'AaaaHHH'

#     """

#     result = ''
#     for char in phrase:
#         if char.lower() == to_swap.lower():
#             if char.islower():
#                 char = char.upper()
#             else:
#                 char = char.lower()

#     result += char
#     return result


# def multiply_even_numbers(nums):
#     """Multiply the even numbers.

#         >>> multiply_even_numbers([2, 3, 4, 5, 6])
#         48

#         >>> multiply_even_numbers([3, 4, 5])
#         4

#     If there are no even numbers, return 1.

#         >>> multiply_even_numbers([1, 3, 5])
#         1
#     """
#     results = 1
#     for num in nums:

#         if num % 2 == 0:
#             results *= num

#             return results

#         def capitalize(phrase):
#     """Capitalize first letter of first word of phrase.

#         >>> capitalize('python')
#         'Python'

#         >>> capitalize('only first word')
#         'Only first word'
#     """

#     return phrase[0].upper()


# def compact(lst):
#     """Return a copy of lst with non-true elements removed.

#         >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
#         [1, 2, 'All done']
#     """

#     return [x for x in lst if x]


# def intersection(l1, l2):
#     """Return intersection of two lists as a new list::

#         >>> intersection([1, 2, 3], [2, 3, 4])
#         [2, 3]

#         >>> intersection([1, 2, 3], [1, 2, 3, 4])
#         [1, 2, 3]

#         >>> intersection([1, 2, 3], [3, 4])
#         [3]

#         >>> intersection([1, 2, 3], [4, 5, 6])
#         []
#     """

#     new_list = set(l1).intersection(l2)
#     new_list = list(new_list)
#     return new_list


# def partition(lst, fn):
#     """Partition lst by predicate.

#      - lst: list of items
#      - fn: function that returns True or False

#      Returns new list: [a, b], where `a` are items that passed fn test,
#      and `b` are items that failed fn test.

#         >>> def is_even(num):
#         ...     return num % 2 == 0

#         >>> def is_string(el):
#         ...     return isinstance(el, str)

#         >>> partition([1, 2, 3, 4], is_even)
#         [[2, 4], [1, 3]]

#         >>> partition(["hi", None, 6, "bye"], is_string)
#         [['hi', 'bye'], [None, 6]]
#     """
#     a = []
#     b = []
#     for item in list:
#         if fn(item):
#             a.append(item)
#         else:
#             b.append(item)
#     return [a, b]


# def mode(nums):
#     """Return most-common number in list.

#     For this function, there will always be a single-most-common value;
#     you do not need to worry about handling cases where more than one item
#     occurs the same number of times.

#         >>> mode([1, 2, 1])
#         1

#         >>> mode([2, 2, 3, 3, 2])
#         2
#     """

#     counter = Counter(nums)
#     most_common = counter.most_common(1)[0]
#     return most_common[0]


# def calculate(operation, a, b, make_int=False, message='The result is'):
#     """Perform operation on a + b, ()possibly truncating) & returning w/msg.

#     - operation: 'add', 'subtract', 'multiply', or 'divide'
#     - a and b: values to operate on
#     - make_int: (optional, defaults to False) if True, truncates to integer
#     - message: (optional) message to use (if not provided, use 'The result is')

#     Performs math operation (truncating if make_int), then returns as
#     "[message] [result]"

#         >>> calculate('add', 2.5, 4)
#         'The result is 6.5'

#         >>> calculate('subtract', 4, 1.5, make_int=True)
#         'The result is 2'

#         >>> calculate('multiply', 1.5, 2)
#         'The result is 3.0'

#         >>> calculate('divide', 10, 4, message='I got')
#         'I got 2.5'

#     If a valid operation isn't provided, return None.

#         >>> calculate('foo', 2, 3)

#     """
#     if operation == 'add':
#         result = a + b

#     elif operation == 'subtract':

#         result = a - b

#     elif operation == 'multiply':

#         result = a * b

#     elif operation == 'divide':

#         result = a / b

#         return f"{message} {result}"

#     def friend_date(a, b):
#     """Given two friends, do they have any hobbies in common?

#     - a: friend #1, a tuple of (name, age, list-of-hobbies)
#     - b: same, for friend #2

#     Returns True if they have any hobbies in common, False is not.

#         >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
#         >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
#         >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

#         >>> friend_date(elmo, sauron)
#         False

#         >>> friend_date(sauron, gandalf)
#         True
#     """

#     a_hobbies = [hobby for hobby in a[2]]
#     b_hobbies = [hobby for hobby in b[2]]

#     common_hobbies = set(a_hobbies).intersection(b_hobbies)

#     return bool(common_hobbies)


# def triple_and_filter(nums):
#     """Return new list of tripled nums for those nums divisible by 4.

#     Return every number in list that is divisible by 4 in a new list,
#     except multipled by 3.

#         >>> triple_and_filter([1, 2, 3, 4])
#         [12]

#         >>> triple_and_filter([6, 8, 10, 12])
#         [24, 36]

#         >>> triple_and_filter([1, 2])
#         []
#     """
#     new_nums = [num * 3 for num in nums if num % 4 == 0]

#     return new_nums


# def extract_full_names(people):
#     """Return list of names, extracting from first+last keys in people dicts.

#     - people: list of dictionaries, each with 'first' and 'last' keys for
#               first and last names

#     Returns list of space-separated first and last names.

#         >>> names = [
#         ...     {'first': 'Ada', 'last': 'Lovelace'},
#         ...     {'first': 'Grace', 'last': 'Hopper'},
#         ... ]

#         >>> extract_full_names(names)
#         ['Ada Lovelace', 'Grace Hopper']
#     """

#     return [f"{person['first']} {person['last']}" for person in people]


#  def sum_floats(nums):
#     """Return sum of floating point numbers in nums.

#         >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
#         3.9

#         >>> sum_floats([1, 2, 3])
#         0
#     """


#     # hint: to find out if something is a float, you should use the
#     # "isinstance" function --- research how to use this to find out
#     # if something is a float!

    
#     total = 0
#     for num in nums:
#      isinstance(num, float)

#      total += nums
#      return total
    


#     def list_check(lst):
#     """Are all items in lst a list?

#         >>> list_check([[1], [2, 3]])
#         True

#         >>> list_check([[1], "nope"])
#         False
#     """
#     for item in list:
#      if not isinstance(item, list):
#       return False
#     return True


# def remove_every_other(lst):
#     """Return a new list of other item.

#         >>> lst = [1, 2, 3, 4, 5]

#         >>> remove_every_other(lst)
#         [1, 3, 5]

#     This should return a list, not mutate the original:

#         >>> lst
#         [1, 2, 3, 4, 5]
#     """
#     return lst[::2]



# def sum_pairs(nums, goal):
#     """Return tuple of first pair of nums that sum to goal.

#     For example:

#         >>> sum_pairs([1, 2, 2, 10], 4)
#         (2, 2)

#     (4, 2) sum to 6, and come before (5, 1):

#         >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
#         (4, 2)

#     (4, 3) sum to 7, and finish before (5, 2):

#         >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
#         (4, 3)

#     No pairs sum to 100, so return empty tuple:

#         >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
#         ()
#     """


#     seen = set()
#     for num in nums:
#         diff = goal - num
#     if diff in seen:
#         return (diff, num)
#     seen.add(num)
#     return ()




# def vowel_count(phrase):
#     """Return frequency map of vowels, case-insensitive.

#         >>> vowel_count('rithm school')
#         {'i': 1, 'o': 2}
        
#         >>> vowel_count('HOW ARE YOU? i am great!') 
#         {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
#     """
#     vowels = set('aeiou')
#     freq_map = {}
#     for char in phrase.lower():
#         if char in vowels:
#             freq_map[char] = freq_map.get(char, 0) + 1
#     return freq_map

# def titleize(phrase):
#     """Return phrase in title case (each word capitalized).

#         >>> titleize('this is awesome')
#         'This Is Awesome'

#         >>> titleize('oNLy cAPITALIZe fIRSt')
#         'Only Capitalize First'
#     """
#     return phrase.title()
  

#   def find_factors(num):
#     """Find factors of num, in increasing order.

#     >>> find_factors(10)
#     [1, 2, 5, 10]

#     >>> find_factors(11)
#     [1, 11]

#     >>> find_factors(111)
#     [1, 3, 37, 111]

#     >>> find_factors(321421)
#     [1, 293, 1097, 321421]
#     """
#     return [x for x in range(1, num +1) if num % x == 0]




# def includes(collection, sought, start=None):
#     """Is sought in collection, starting at index start?

#     Return True/False if sought is in the given collection:
#     - lists/strings/sets/tuples: returns True/False if sought present
#     - dictionaries: return True/False if *value* of sought in dictionary

#     If string/list/tuple and `start` is provided, starts searching only at that
#     index. This `start` is ignored for sets/dictionaries, since they aren't
#     ordered.

#         >>> includes([1, 2, 3], 1)
#         True

#         >>> includes([1, 2, 3], 1, 2)
#         False

#         >>> includes("hello", "o")
#         True

#         >>> includes(('Elmo', 5, 'red'), 'red', 1)
#         True

#         >>> includes({1, 2, 3}, 1)
#         True

#         >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
#         True

#         >>> includes({"apple": "red", "berry": "blue"}, "blue")
#         True

#     """  
#     if isinstance(collection, dict):
#         return sought in collection.values()
#     elif isinstance(collection, (list, str, set, tuple)):
#         if start is None:
#             return sought in collection
#         else:
#             return sought in collection[start:]
#     else:
#         return False
    

#     def repeat(phrase, num):
#     """Return phrase, repeated num times.

#         >>> repeat('*', 3)
#         '***'

#         >>> repeat('abc', 2)
#         'abcabc'

#         >>> repeat('abc', 0)
#         ''

#     Ignore illegal values of num and return None:

#         >>> repeat('abc', -1) is None
#         True

#         >>> repeat('abc', 'nope') is None
#         True
#     """
#     return phrase * num


# def truncate(phrase, n):
#     """Return truncated-at-n-chars version of  phrase.
    
#     If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
#     longer than n.
    
#         >>> truncate("Hello World", 6)
#         'Hel...'
        
#         >>> truncate("Problem solving is the best!", 10)
#         'Problem...'
        
#         >>> truncate("Yo", 100)
#         'Yo'
        
#     The smallest legal value of n is 3; if less, return a message:
    
#         >>> truncate('Cool', 1)
#         'Truncation must be at least 3 characters.'

#         >>> truncate("Woah", 4)
#         'W...'

#         >>> truncate("Woah", 3)
#         '...'
#     """

#     if n < 3:
#         return 'Truncation must be at least 3 characters.'

#     if len(phrase) <= n:
#         return phrase

#     return phrase[:n-3] + '...'



# def two_list_dictionary(keys, values):
#     """Given keys and values, make dictionary of those.
    
#         >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
#         {'x': 9, 'y': 8, 'z': 7}
        
#     If there are fewer values than keys, remaining keys should have value
#     of None:
    
#         >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
#         {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
#     If there are fewer keys, ignore remaining values:

#         >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
#         {'a': 1, 'b': 2, 'c': 3}
#    """
    
#     dictionary = {}
#     for x in range(len(keys)):
#      if x < len(values):
#         dictionary[keys[x]] = values[x]
#     else:
#      dictionary[keys[x]] = None
#      return dictionary
    


#     def same_frequency(num1, num2):
#     """Do these nums have same frequencies of digits?
    
#         >>> same_frequency(551122, 221515)
#         True
        
#         >>> same_frequency(321142, 3212215)
#         False
        
#         >>> same_frequency(1212, 2211)
#         True
#     """


    
#     num1_str = str(num1)
#     num2_str = str(num2)

#     freq_1 = {}
#     freq_2 = {}

#     for digit in num1_str:
#         if digit in freq_1:

#            freq_1[digit] += 1
#     else:
#         freq_1[digit] = 1


#     for digit in num2_str:
#         if digit in freq_2:
#            freq_2[digit] += 1
#     else:
#         freq_2[digit] = 1

#         if freq_1 == freq_2:
#           return True
#         else:
#           return False
        

#         def two_oldest_ages(ages):
#     """Return two distinct oldest ages as tuple (second-oldest, oldest)..

#         >>> two_oldest_ages([1, 2, 10, 8])
#         (8, 10)

#         >>> two_oldest_ages([6, 1, 9, 10, 4])
#         (9, 10)

#     Even if more than one person has the same oldest age, this should return
#     two *distinct* oldest ages:

#         >>> two_oldest_ages([1, 5, 5, 2])
#         (2, 5)
#     """

#     # NOTE: don't worry about an optimized runtime here; it's fine if
#     # you have a runtime worse than O(n)

#     # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
#     # you may find it helpful to research the `sorted(iter)` function, which
#     # can take *any* type of list-like-thing, and returns a new, sorted list
#     # from it.

#     ages = list(set(ages))
#     ages.sort(reverse=True)
#     return ([ages[1], ages[0]])


# def find_the_duplicate(nums):
#     """Find duplicate number in nums.

#     Given a list of nums with, at most, one duplicate, return the duplicate.
#     If there is no duplicate, return None

#         >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
#         1

#         >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
#         9

#         >>> find_the_duplicate([2, 1, 3, 4]) is None
#         True
#     """

#     seen = set()
#     for num in nums:
#         if num in seen:
#             return num
#         seen.add(num)
#         return None
    

#     def sum_up_diagonals(matrix):
#     """Given a matrix [square list of lists], return sum of diagonals.

#     Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

#         >>> m1 = [
#         ...     [1,   2],
#         ...     [30, 40],
#         ... ]
#         >>> sum_up_diagonals(m1)
#         73

#         >>> m2 = [
#         ...    [1, 2, 3],
#         ...    [4, 5, 6],
#         ...    [7, 8, 9],
#         ... ]
#         >>> sum_up_diagonals(m2)
#         30
#     """

#     n = len(matrix)
#     diagonal1 = sum(matrix[i][i] for i in range(n))
#     diagonal2 = sum(matrix[i][n-1-i] for i in range(n))
#     return diagonal1 + diagonal2



# def min_max_keys(d):
#     """Return tuple (min-keys, max-keys) in d.

#         >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
#         (1, 10)

#     Works with any kind of key that can be compared, like strings:

#         >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
#         ('apple', 'cherry')
#     """


#     keys = list(dict.keys())
#     min_key = min(keys)
#     max_key = max(keys)
#     return (min_key, max_key)


# def find_greater_numbers(nums):
#     """Return # of times a number is followed by a greater number.

#     For example, for [1, 2, 3], the answer is 3:
#     - the 1 is followed by the 2 *and* the 3
#     - the 2 is followed by the 3

#     Examples:

#         >>> find_greater_numbers([1, 2, 3])
#         3

#         >>> find_greater_numbers([6, 1, 2, 7])
#         4

#         >>> find_greater_numbers([5, 4, 3, 2, 1])
#         0

#         >>> find_greater_numbers([])
#         0
#     """
    
#     count = 0
#     for i in range(len(nums)-1):
#         if nums[i] < nums[i+1]:
#             count += 1
#         return count
    
#     def is_odd_string(word):
#     """Is the sum of the character-positions odd?

#     Word is a simple word of uppercase/lowercase letters without punctuation.

#     For each character, find it's "character position" ("a"=1, "b"=2, etc).
#     Return True/False, depending on whether sum of those numbers is odd.

#     For example, these sum to 1, which is odd:
    
#         >>> is_odd_string('a')
#         True

#         >>> is_odd_string('A')
#         True

#     These sum to 4, which is not odd:
    
#         >>> is_odd_string('aaaa')
#         False

#         >>> is_odd_string('AAaa')
#         False

#     Longer example:
    
#         >>> is_odd_string('amazing')
#         True
#     """
#     if sum of word.ord() == odd:

#     # Hint: you may find the ord() function useful here

#      char_sum = 0
#      for char in word:
#         char_pos = ord(char.lower()) - ord('a') + 1
#         char_sum += char_pos
#     return char_sum % 2 == 1


#     def valid_parentheses(parens):
#     """Are the parentheses validly balanced?

#         >>> valid_parentheses("()")
#         True

#         >>> valid_parentheses("()()")
#         True

#         >>> valid_parentheses("(()())")
#         True

#         >>> valid_parentheses(")()")
#         False

#         >>> valid_parentheses("())")
#         False

#         >>> valid_parentheses("((())")
#         False

#         >>> valid_parentheses(")()(")
#         False
#     """

    
#     count = 0
#     for char in parens:
#         if char == '(':
#             count += 1
#         elif char == ')':
#             count -= 1
#         if count < 0:
#             return False
#     return count == 0

# def three_odd_numbers(nums):
#     """Is the sum of any 3 sequential numbers odd?"

#         >>> three_odd_numbers([1, 2, 3, 4, 5])
#         True

#         >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
#         True

#         >>> three_odd_numbers([5, 2, 1])
#         False

#         >>> three_odd_numbers([1, 2, 3, 3, 2])
#         False
#     """

#     for i in range(len(nums) - 2):
#         if (nums[i] + nums[i+1] + nums[i+2]) % 2 == 1:
#             return True
#     return False


# def reverse_vowels(s):
#     """Reverse vowels in a string.

#     Characters which re not vowels do not change position in string, but all
#     vowels (y is not a vowel), should reverse their order.

#     >>> reverse_vowels("Hello!")
#     'Holle!'

#     >>> reverse_vowels("Tomatoes")
#     'Temotaos'

#     >>> reverse_vowels("Reverse Vowels In A String")
#     'RivArsI Vewols en e Streng'

#     reverse_vowels("aeiou")
#     'uoiea'

#     reverse_vowels("why try, shy fly?")
#     'why try, shy fly?''
#     """

    
#     vowels = set("aeiouAEIOU")
#     substrings = s.split()
#     reversed_substrings = [substring[::-1] if any(char in vowels for char in substring) else substring for substring in substrings]
#     return "".join(reversed_substrings)