# Упражнение 2.1
#
# def NOD(a, b):
#     if b == 0:
#         return a
#     else:
#         return NOD(b, a % b)
#
# Упражнение 2.2
#
# def express(stroka):
#     if '*' in stroka and '+' in stroka: # Если в строке и + и -
#         if stroka.index('*') < stroka.index('+'): # Если * стоит раньше +, метод index отправляет индекс первого появления аргумента в строке
#             a = int(stroka[:stroka.index('*')]) * int(stroka[stroka.index('*')+1])  # Использую срезы для перемножения чисел до * и после
#             return express(str(a) + stroka[stroka.index('*')+2:]) # Рекурсия ниже код анологичен
#         else:
#             a = stroka[:stroka.index('+')]
#             return int(a) + int(express(stroka[2:]))
#     elif '+' in stroka:
#         a = stroka[:stroka.index('+')]
#         return int(a) + int(express(stroka[2:]))
#     elif '*' in stroka:
#         a = stroka[:stroka.index('*')]
#         return int(a) * int(express(stroka[2:]))
#     else:
# Если подается 1 число
#         return int(stroka)
#
# Упражнение 2.3
#
# def bsearch(list, left, right, val):
#     if (right < left): # Если алгоритм ничего не нашел
#         return 'Нет нужного числа'
#     else:
#         midval = left + ((right - left) // 2) # Определяем границы поиска
#         if list[midval] > val:
#             return bsearch(list, left, midval - 1, val)
#         elif list[midval] < val:
#             return bsearch(list, midval + 1, right, val)
#         else:
#             return midval
#
# Подматрица из единиц
# def printMaxSubSquare(matrix):
#     rows = len(matrix)
#     column = len(matrix[0])
#
#     S = [[0 for k in range(column)] for l in range(rows)]
#
#     # здесь мы установили первую строку и столбец S [] []
#
#     # Построить другие записи
#
#     for i in range(1, rows):
#
#         for j in range(1, column):
#
#             if (matrix[i][j] == 1):
#
#                 S[i][j] = min(S[i][j - 1], S[i - 1][j],
#
#                               S[i - 1][j - 1]) + 1
#
#             else:
#
#                 S[i][j] = 0
#
#     # Найти максимальную запись и
#
#     # индексы максимальной записи в S [] []
#
#     max_of_s = S[0][0]
#     max_i = 0
#     max_j = 0
#     for i in range(rows):
#         for j in range(column):
#             if (max_of_s < S[i][j]):
#                 max_of_s = S[i][j]
#                 max_i = i
#                 max_j = j
#
#     print("Подматрица: ")
#     for i in range(max_i, max_i - max_of_s, -1):
#         for j in range(max_j, max_j - max_of_s, -1):
#             print(matrix[i][j], end=" ")
#         print("")
#
# Упражнение 3.3
# class Queue:  # класс очереди
#     def __init__(self, enter, max):
#         self.items = []
#         self.enter = enter
#         self.max = max
#
#     def isEmpty(self):
#         return self.items == []
#
#     def enqueue(self, item):  # Добавить в очередь
#         self.items.insert(0, item)
#
#     def dequeue(self):  # Исключить из очереди
#         return self.items.pop()
#
#     def size(self):  # Отправляет размер очереди для самопроверки
#         size = 0
#         for _ in self.items:
#             size += 1
#         return size
#
#     def __iter__(self):
#         self.count = 0
#         return self
#
#     def __next__(self):
#         if self.count >= self.max:
#             raise StopIteration
#         self.count += 1
#         return self.count
#
#
# q = Queue(0, 2)  # создание очереди
#
# q.enqueue(1) # добавление эллементов
# q.enqueue(2)
#
# print_count_inter = iter(q) # Подсчет эллементов
# print(next(print_count_inter))
#
# print(next(print_count_inter))
# print(q.size()) # Размер очереди
#
# Упражнение 3.8
#
# Tree = {
#     1: [2, 8],
#     2: [1, 3, 8],
#     3: [2, 4, 8],
#     4: [3, 7, 9],
#     5: [6, 7],
#     6: [5],
#     7: [4, 5, 8],
#     8: [1, 2, 3, 7],
#     9: [4],
# }
#
# visited = set()  # Посещена ли вершина?
#
#
# def search(X):  # X нужная вершина
#
#     visited = set()  # Посещена ли вершина?
#
#     def dfs(v):
#         if v in visited:  # Если вершина уже посещена, выходим
#             return
#         visited.add(v)  # Посетили вершину v
#         for i in Tree[v]:  # Все смежные с v вершины
#             if not i in visited:
#                 dfs(i)
#
#     start = 1
#     dfs(start)  # start - начальная вершина обхода
#     if X not in visited: # Если X нет то добавляю
#         Tree[X] = []
#         print(Tree)
#     else:
#         print(f"{X} находится в дереве")
