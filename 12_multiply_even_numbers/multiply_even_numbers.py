def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    # result = 1
    # for num in nums:
    #     if num % 2 == 0:
    #         result = result * num
    # return result

    new_numbers = []
    for num in nums:
        if num % 2 == 0:
            new_numbers.append(num)

    result = 1

    for number in new_numbers:
        result = result * number
    return result


    # for num in nums:
    #     if num % 2 == 0:
    #         new_numbers.append(num)

    #     result = 1

    #     for number in new_numbers:
    #         result = result * number
    #     return result

    # new_numbers = []
    # for num in nums:
    #     if num % 2 == 0:
    #         new_numbers.append(num)
    # if len(new_numbers) == 0:
    #     return 1
    # else:
    #     result = 1
    #     for number in new_numbers:
    #         result = result * number
    #     return result

# nums=[1,2,3,4,5,6,7,8,9]
# evens = []
# for num in nums:
# 	if num % 2 == 0:
# 		evens.append(num)
# print(evens)


