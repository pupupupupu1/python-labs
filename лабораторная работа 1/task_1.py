numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
#
# TODO заменить значение пропущенного элемента средним арифметическим

# print("Измененный список:", ...)

mis = numbers.index(None)
sum_of_nums = sum(numbers[:mis] + numbers[mis+1:])
count_of_nums = len(numbers)
average = sum_of_nums/count_of_nums
numbers[mis] = average
print("Измененный список:", numbers)