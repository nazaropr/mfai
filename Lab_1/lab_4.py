import random
import numpy as np
from matplotlib import pyplot as plt
import warnings

warnings.filterwarnings("ignore")


def generate_cities(n):
    cities = []
    with open('cities.txt', 'r') as file:
        for line in file:
            city = list(map(int, line.strip().split()))
            cities.append(city)
    return cities

def generate_pheromones(n):
    pheromones = []
    for i in range(n):
        pheromone = []
        for j in range(n):
            pheromone.append(1)
        pheromones.append(pheromone)
    return pheromones

def calculate_probabilities(cities, pheromones, alpha, beta, visited_cities, current_city):
    probabilities = []
    denominator = 0
    for i in range(len(cities)):
        if i not in visited_cities:
            denominator += (pheromones[current_city][i] ** alpha) * ((1 / cities[current_city][i]) ** beta)
    for i in range(len(cities)):
        if i not in visited_cities:
            numerator = (pheromones[current_city][i] ** alpha) * ((1 / cities[current_city][i]) ** beta)
            probability = numerator / denominator
            probabilities.append((i, probability))
    return probabilities

def choose_next_city(probabilities):
    probabilities.sort(key=lambda x: x[1], reverse=True)
    return probabilities[0][0]

def update_pheromones(pheromones, ants, cities, decay_factor, Q):
    for ant in ants:
        path_length = 0
        for i in range(len(ant) - 1):
            path_length += cities[ant[i]][ant[i + 1]]
        path_length += cities[ant[-1]][ant[0]]
        for i in range(len(ant) - 1):
            pheromones[ant[i]][ant[i + 1]] *= (1 - decay_factor)
            pheromones[ant[i]][ant[i + 1]] += (Q / path_length)
        pheromones[ant[-1]][ant[0]] *= (1 - decay_factor)
        pheromones[ant[-1]][ant[0]] += (Q / path_length)

def ant_colony_optimization(cities, num_ants, num_iterations, alpha, beta, decay_factor, Q):
    n = len(cities)
    best_path = None
    best_path_length = float('inf')
    pheromones = generate_pheromones(n)
    for iteration in range(num_iterations):
        ants = []
        for ant_index in range(num_ants):
            visited_cities = [random.randint(0, n - 1)]
            while len(visited_cities) < n:
                current_city = visited_cities[-1]
                probabilities = calculate_probabilities(cities, pheromones, alpha, beta, visited_cities, current_city)
                next_city = choose_next_city(probabilities)
                visited_cities.append(next_city)
            ants.append(visited_cities)
            path_length = 0
            for i in range(len(visited_cities) - 1):
                path_length += cities[visited_cities[i]][visited_cities[i + 1]]
            path_length += cities[visited_cities[-1]][visited_cities[0]]
            if path_length < best_path_length:
                best_path_length = path_length
                best_path = visited_cities
        update_pheromones(pheromones, ants, cities, decay_factor, Q)
        print(f'Iteration {iteration}: shortest path length is {best_path_length}')

    return best_path

def visualize_path(cities, path):
    x = []
    y = []
    for i in range(len(path)):
        x.append(cities[path[i]][0])
        y.append(cities[path[i]][1])
    x.append(cities[path[0]][0])
    y.append(cities[path[0]][1])

    plt.plot(x, y, 'ro-')
    plt.xticks(np.arange(0, max(x) + 10, 10))
    plt.yticks(np.arange(0, max(y) + 10, 10))

    for i in range(len(path)):
        plt.text(x[i], y[i], str(i), color='blue', fontsize=12, fontweight='bold')

    plt.show()



if __name__ == '__main__':
    num_cities = 25#random.randint(25, 35)
    num_ants = 16
    num_iterations = 50
    alpha = 3.0
    beta = 1.0
    decay_factor = 0.5
    Q = 100.0

    cities = generate_cities(num_cities)

    print("Cities:")
    print(np.array(cities))

    best_path = ant_colony_optimization(cities, num_ants, num_iterations, alpha, beta, decay_factor, Q)

    visualize_path(cities, best_path)

    print("Best Path:")
    print(best_path)