import random
import math
#Визначення ціни дошки
def get_board_cost(board):
    cost = 0
    for i in range(len(board)):
        for j in range(i+1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                cost += 1
    return cost
#Зміна випадковим чином положення одного ферзя в існуючій дошці
def get_neighbor(board):
    neighbor = board.copy()
    i = random.randint(0, len(board)-1)
    j = random.randint(0, len(board)-1)
    neighbor[i] = j
    return neighbor

# Алгоритм імітації відпалу
def simulated_annealing(n_queens, max_iterations, max_temperature):
    initial_board = [random.randint(0, n_queens-1) for _ in range(n_queens)]
    current_board = initial_board
    current_cost = get_board_cost(current_board)
    iterations = 0
    for i in range(max_iterations):
        iterations += 1

        temperature = max_temperature * (1 - i/max_iterations)
        if current_cost == 0:
            return current_board, iterations
        neighbor = get_neighbor(current_board)
        neighbor_cost = get_board_cost(neighbor)
        cost_delta = neighbor_cost - current_cost
        if cost_delta < 0:

            current_board = neighbor
            current_cost = neighbor_cost
        else:

            acceptance_prob = math.exp(-cost_delta / temperature)
            if random.random() < acceptance_prob:

                current_board = neighbor
                current_cost = neighbor_cost
    return None
#Вивід дошки в консоль
def print_board(board):

    for row in range(len(board)):
        line = ""
        for col in range(len(board)):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()


n_queens = 15
max_iterations = 1000000
max_temperature = 10

initial_board = [random.randint(0, n_queens-1) for _ in range(n_queens)]
print("Початкова дошка:")
print_board(initial_board)

solution = simulated_annealing(n_queens, max_iterations, max_temperature)

if solution is not None:
    print("Кількість ітерацій - ", solution[1])
    print("Розв'язок:")
    print_board(solution[0])
else:
    print("Розв'язок не знайдено.")
