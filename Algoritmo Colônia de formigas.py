import numpy as np
import time
import matplotlib.pyplot as plt


class AntColonyTSP:
    def __init__(self, num_ants, num_iterations, pheromone_evaporation, alpha, beta):
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.pheromone_evaporation = pheromone_evaporation
        self.alpha = alpha
        self.beta = beta

    def solve_tsp(self, distance_matrix):
        num_cities = distance_matrix.shape[0]
        pheromone_matrix = np.ones((num_cities, num_cities))
        best_path = None
        best_distance = np.inf

        for iteration in range(self.num_iterations):
            ant_paths = self.generate_ant_paths(distance_matrix, pheromone_matrix)
            self.update_pheromones(pheromone_matrix, ant_paths, distance_matrix)

            best_path_current = min(ant_paths, key=lambda path: self.calculate_path_distance(path, distance_matrix))
            best_distance_current = self.calculate_path_distance(best_path_current, distance_matrix)

            if best_distance_current < best_distance:
                best_path = best_path_current
                best_distance = best_distance_current

            pheromone_matrix *= self.pheromone_evaporation

        return best_path, best_distance

    def generate_ant_paths(self, distance_matrix, pheromone_matrix):
        num_cities = distance_matrix.shape[0]
        ant_paths = []

        for _ in range(self.num_ants):
            path = [0]
            visited_cities = set(path)

            for _ in range(num_cities - 1):
                next_city = self.choose_next_city(path[-1], visited_cities, pheromone_matrix, distance_matrix)
                path.append(next_city)
                visited_cities.add(next_city)

            ant_paths.append(path)

        return ant_paths

    def choose_next_city(self, current_city, visited_cities, pheromone_matrix, distance_matrix):
        unvisited_cities = [city for city in range(distance_matrix.shape[0]) if city not in visited_cities]
        probabilities = []

        for city in unvisited_cities:
            pheromone = pheromone_matrix[current_city, city]
            distance = distance_matrix[current_city, city]
            probabilities.append((city, pheromone ** self.alpha * (1.0 / distance) ** self.beta))

        total_probability = sum(prob for _, prob in probabilities)
        probabilities = [(city, prob / total_probability) for city, prob in probabilities]

        chosen_city = np.random.choice([city for city, _ in probabilities], p=[prob for _, prob in probabilities])
        return chosen_city

    def update_pheromones(self, pheromone_matrix, ant_paths, distance_matrix):
        for ant_path in ant_paths:
            path_distance = self.calculate_path_distance(ant_path, distance_matrix)
            for i in range(len(ant_path) - 1):
                pheromone_matrix[ant_path[i], ant_path[i + 1]] += 1.0 / path_distance

    def calculate_path_distance(self, path, distance_matrix):
        distance = 0
        for i in range(len(path) - 1):
            distance += distance_matrix[path[i], path[i + 1]]
        distance += distance_matrix[path[-1], path[0]]
        return distance


def read_city_coordinates(file_path):
    cities = []
    with open(file_path, 'r') as file:
        for line in file:
            _, x, y = map(float, line.strip().split())
            cities.append((x, y))
    return cities


if __name__ == "__main__":
    np.random.seed(90)
    city_coordinates = read_city_coordinates("cidades.txt")
    num_cities = len(city_coordinates)
    distance_matrix = np.zeros((num_cities, num_cities))

    for i in range(num_cities):
        for j in range(num_cities):
            x1, y1 = city_coordinates[i]
            x2, y2 = city_coordinates[j]
            distance_matrix[i, j] = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    num_ants = 200
    num_iterations = 200
    pheromone_evaporation = 0.5
    alpha = 1.0
    beta = 2.0

    ant_colony = AntColonyTSP(num_ants, num_iterations, pheromone_evaporation, alpha, beta)

    start_time = time.time()
    best_path, best_distance = ant_colony.solve_tsp(distance_matrix)
    best_path.append(0)
    end_time = time.time()

    elapsed_time = end_time - start_time

    print("Melhor caminho:", best_path)
    print("Melhor distância:", best_distance)
    print("Tempo de execução:", elapsed_time, "segundos")

    # Adicione esta parte para criar um gráfico do melhor percurso
    best_path_coordinates = [city_coordinates[i] for i in best_path]
    x, y = zip(*best_path_coordinates)  # Separe as coordenadas x e y

    plt.figure(figsize=(8, 6))  # Defina o tamanho da figura
    plt.plot(x, y, marker='o', markerfacecolor='red', linestyle='-', color='b')  # Crie o gráfico do percurso
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.title('Melhor Percurso Encontrado no ACO')
    plt.grid(True)
    plt.show()  # Exiba o gráfico
