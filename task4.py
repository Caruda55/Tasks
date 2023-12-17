
def func(file_read):
    with open(file_read, 'r') as file:
        contents = file.readlines()

        nums = [int(contents[i]) for i in range(len(contents))]
        m = sorted(nums)[len(nums) // 2]
        print(sum(abs(v - m) for v in nums))

func(input('Файл с числами: '))

