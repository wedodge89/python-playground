# my solution
def highest_even(list):
    even_numbers = []
    answer = 0
    for item in list:
        if (item %2 == 0):
            even_numbers.append(item)
    even_numbers.sort()
    answer = even_numbers[-1]
    return answer

print(highest_even([1, 2, 3, 4, 5, 8, 10, 80, 20]))

# andrei's solution
# def highest_even(li):
#     evens = []
#     for item in li:
#         if item %2 ==0:
#             evens.append(item)
#     return max(evens)