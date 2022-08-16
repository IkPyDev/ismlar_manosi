# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

data = [5, 7, -20, 30, 5, 0, 12, 10, 8, 9, 0, 15]


# Press the green button in the gutter to run the script.
def sort(array):
    if len(array) <= 1:
        return array
    temp = array[0]
    left_nums = []
    middle_nums = []
    right_nums = []
    for a in array:
        c = compare(a, temp)
        if c > 0:
            right_nums.append(a)
        elif c < 0:
            left_nums.append(a)
        else:
            middle_nums.append(a)
    return sort(left_nums) + middle_nums + sort(right_nums)


def compare(a, b):
    return a - b


if __name__ == '__main__':
    print('Сортировка массива длиной:', len(data))
    print(sort(data))
