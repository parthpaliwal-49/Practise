def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1], = numbers[j+1], numbers[j]
    return numbers

print(bubble_sort([1,2,3,2,1,4,5,7,3,4,5]))