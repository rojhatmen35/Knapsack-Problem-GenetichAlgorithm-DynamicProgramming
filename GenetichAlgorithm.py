import random
import matplotlib.pyplot as plt
import time

class KnapsackItem:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def generate_random_population(item_list, population_size):
    population = []
    for _ in range(population_size):
        chromosome = [random.randint(0, 1) for _ in range(len(item_list))]
        population.append(chromosome)
    return population


def calculate_fitness(chromosome, item_list, max_weight):
    total_value = 0
    total_weight = 0
    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            total_value += item_list[i].value
            total_weight += item_list[i].weight
    if total_weight > max_weight:
        return 0  # Sadece burada sıfır döndürerek total değeri sıfırlayabilirsiniz.
    return total_value



def selection(population, item_list, max_weight, elite_size):
    population_fitness = []
    for chromosome in population:
        fitness = calculate_fitness(chromosome, item_list, max_weight)
        population_fitness.append((chromosome, fitness))
    population_fitness.sort(key=lambda x: x[1], reverse=True)
    elite = [individual for individual, _ in population_fitness[:elite_size]]
    return elite


def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


def mutation(chromosome, mutation_rate):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]
    return chromosome


def evolve_population(population, item_list, max_weight, elite_size, mutation_rate):
    elite = selection(population, item_list, max_weight, elite_size)
    new_population = elite[:]
    while len(new_population) < len(population):
        parent1, parent2 = random.choices(elite, k=2)
        child1, child2 = crossover(parent1, parent2)
        child1 = mutation(child1, mutation_rate)
        child2 = mutation(child2, mutation_rate)
        new_population.extend([child1, child2])
    return new_population


def knapsack_genetic_algorithm(item_list, max_weight, population_size, elite_size, mutation_rate, generations):
    population = generate_random_population(item_list, population_size)
    for _ in range(generations):
        population = evolve_population(population, item_list, max_weight, elite_size, mutation_rate)
    best_chromosome = max(population, key=lambda x: calculate_fitness(x, item_list, max_weight))
    best_fitness = calculate_fitness(best_chromosome, item_list, max_weight)
    return best_chromosome, best_fitness


def read_data_from_file(file_path):
    item_list = []
    max_weight = 0
    with open(file_path, "r") as file:
        lines = file.readlines()
        max_weight = int(lines[0].split()[1])
        for line in lines[1:]:
            value, weight = map(int, line.split())
            item = KnapsackItem(value, weight)
            item_list.append(item)
    return item_list, max_weight


def main():
    
    
    
    file_path = "ks_19_0.txt"
    population_size = 100
    elite_size = 20
    mutation_rate = 0.1
    generations = 1000
    
    sizes = 4
    times = []
    
    start_time = time.time()
    
    

    item_list, max_weight = read_data_from_file(file_path)

    best_chromosome, best_fitness = knapsack_genetic_algorithm(item_list, max_weight, population_size,
                                                               elite_size, mutation_rate, generations)

    print("Best Chromosome:", best_chromosome)
    print("Best Fitness:", best_fitness)
    
    end_time = time.time()
    execution_time = end_time - start_time
    times.append(execution_time)
    plt.plot(sizes, times)
    plt.xlabel('Girdi Boyutu')
    plt.ylabel('Çalışma Zamanı (s)')
    plt.title('Boyut-Çalışma Zamanı Grafiği')
    plt.show()


if __name__ == "__main__":
    main()

