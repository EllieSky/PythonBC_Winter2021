# reversed()
# list()
# tuple()
# range()
# enumerate()
# len()

alist = list("abcdefghijklmn")


for index, item in enumerate(alist):
    print(index)
    print("multiply letters:", item * index, sep="...")


for index in range(10):
    print(index)
    print("squared:", index * index, sep="...")


# exchange values
x = 12
y = 2


# solution
a = x
x = y
y = a


def count_odd_even(lst):
    even_count = 0
    odd_count = 0

    for num in lst:
        if type(num) is float or type(num) is int:
            if num % 2 == 0:
                even_count = even_count + 1
            else:
                odd_count = odd_count + 1

    print("Total count of odd number:", odd_count)
    print("Total count of even number:", even_count)

    return {'odd': odd_count, 'even': even_count}


# count odd/even numbers in the list
count_odd_even([3, 6, 9, 4, 7])
count_odd_even([])
count_odd_even([1, 1, 1, 1, 1, 1])
count_odd_even([2, 0, 4, -2])
count_odd_even([None, None])
count_odd_even(['a', 'b', 1, 4, 2])
count_odd_even([False, True, 3, 5, 2])


lst = [3, 6, 9, 4, 7]

# if length is odd middle will be rounded down
# if length is even middle will be exact
middle = int(len(lst) / 2)


print("\nLIST:", *lst)
for index, item in enumerate(lst):
    if index >= middle:
        break
    a = lst[index]
    lst[index] = lst[-1-index]
    lst[-1-index] = a
print("REVERSED:", *lst)

### VARIATION of reverse list
print("\nLIST:", *lst)
for index, item in enumerate(lst):
    if index >= middle:
        break

    lst[index] = lst[-1-index]
    lst[-1-index] = item
print("REVERSED:", *lst)

### ANOTHER VARIATION of reverse list
print("\nLIST:", *lst)
for index in range(middle):
    a = lst[index]
    lst[index] = lst[-1 - index]
    lst[-1 - index] = a
print("REVERSED:", *lst)



## Christmas Tree Example:
##    *
##   ***
##  *****
## *******
##    |


def print_christmas_tree(height):

    for less_space in range(height):
        print(' '*(height - less_space) + '*' * (less_space * 2 + 1))

    # the trunk
    print(' '*height + '|')

# print_christmas_tree(3)
print_christmas_tree(7)












