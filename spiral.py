def create_spiral(num):
    """
    Функция, которая создает спиральное расположение чисел
    """
    direction = 'right'
    x, y = 0, 0
    limit = num - 1
    current_num = num ** 2
    spiral = [[None] * num for _ in range(num)]
    
    while current_num > 0:
        spiral[y][x] = current_num
        current_num -= 1
        
        if direction == 'right':
            if x == limit:
                direction = 'down'
                y += 1
            else:
                x += 1
                
        elif direction == 'down':
            if y == limit:
                direction = 'left'
                x -= 1
            else:
                y += 1
                
        elif direction == 'left':
            if x == num - limit - 1:
                direction = 'up'
                y -= 1
            else:
                x -= 1
                
        elif direction == 'up':
            if y == num - limit - 1:
                direction = 'right'
                x += 1
                limit -= 1
            else:
                y -= 1
    
    return spiral
    
def print_spiral(num):
    """
    Функция, которая выводит спиральное расположение чисел на экран
    """
    spiral = create_spiral(num)
    center = num // 2
    
    for i in range(num):
        for j in range(num):
            if i == center and j == center:
                print('{:^5}'.format(num ** 2), end=' ')
            elif spiral[i][j]:
                print('{:^5}'.format(spiral[i][j]), end=' ')
            else:
                print('{:^5}'.format(''), end=' ')
        print()
