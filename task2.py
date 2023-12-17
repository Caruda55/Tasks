import math

def func(file_1, file_2):
    with open(file_1, 'r') as file_circle:
        contents = file_circle.readlines()
        for i in range(2):
            if i % 2 == 0:
                center = contents[i].split()
            else:
                rad = contents[i].split()
    
    with open(file_2, 'r') as file_points:
        contents = file_points.readlines()
        for i in contents:
            x1 = float(i.split()[0])
            x2 = float(i.split()[1])

            hyp = math.sqrt(x1 ** 2 + x2 ** 2)

            if hyp == float(rad[0]):
                print(0, '\n')
            elif hyp < float(rad[0]):
                print(1, '\n')
            elif hyp > float(rad[0]):
                print(2, '\n')

func(input('Окружность: '), input('Координаты точек: '))
