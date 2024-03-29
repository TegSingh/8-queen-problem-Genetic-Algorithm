from audioop import cross
from cgitb import small
from random import randint, random
from select import select

MUTATION_PROBABILITY = 0.2
CROSSOVER_PROBABILITY = 0.7
CHROMOSOME_POPULATION = 20
FITNESS_SOLUTION_VALUE = 56

# Define the chromosomes - This will keep changing with every iteration
population = []    
# List the best fit scores per generation
best_fits = []

def generate_population():

    for i in range(CHROMOSOME_POPULATION):
        # Initialize the chromosome
        chromosome = []
        for j in range(8):
            # Generate Random number for a chromosome
            value = randint(1, 8)
            chromosome.append(value)

        # Add the chromosome to the population
        population.append(chromosome)

# Method to print population
def print_population():
    print("New Population: ")
    for i in range(CHROMOSOME_POPULATION):
        print(population[i], fitness_function(population[i]))

# Method to perform Mutation
def mutation(parent):

    for i in range(len(parent)):
        if random() < MUTATION_PROBABILITY:
            parent[i] = randint(1, 8)
    return parent
    

# Method to perform Crossover
def crossover(parent1, parent2):
    
    # Initialize the children
    child1 = []
    child2 = []
    # Generate a crossover point
    crossover_point = randint(1, 7)
    for i in range(len(parent1)):
        if i >= crossover_point:
            child1.append(parent2[i])
            child2.append(parent1[i])
            continue
        child1.append(parent1[i])
        child2.append(parent2[i])

    return child1, child2


# Fitness function
def fitness_function(chromosome):
    
    # Initialize fitness_score for a passed chromosome
    fitness_score = 0
    
    # Check each queen in a column and count how many conflicts he doesnt have
    for i in range(8):
        for j in range(8):      
            if i == j:
                continue
            # Do 2 queens belong to the same row - Not the same column assumption has been made
            if chromosome[j] == chromosome[i]:
                continue
            if chromosome[i] - chromosome[j] == j - i:
                continue
            if chromosome[i] - chromosome[j] == i - j:
                continue
            fitness_score += 1        

    return fitness_score

# Method to calculate fitness probability
def get_fitness_probability(fitness_scores):
    sum = 0
    fitness_probabilities = []
    for i in fitness_scores:
        sum += i
    
    check_sum = 0
    for i in fitness_scores:
        fitness_probabilities.append(i/sum)
        check_sum += i/sum

    return fitness_probabilities

# Method to calculate cumulative probabilities from the provided fitness probability for the roulette wheel
def get_cumulative_probability(fitness_probabilities):
    cumulative_probabilities = []
    sum = 0
    for i in fitness_probabilities:
        sum += i
        if len(cumulative_probabilities) == 9:
            cumulative_probabilities.append(1.000)
            continue
        cumulative_probabilities.append(sum)

    return cumulative_probabilities

# Selection method - Select parent individuals based on fitness function
def selection(fitness_probabilities):
    
    # Get values and indexes
    parent_index1, max = get_largest(fitness_probabilities)
    parent_index2, smax = get_second_largest(fitness_probabilities)
    parent1 = population[parent_index1]
    parent2 = population[parent_index2]
    return parent_index1, parent_index2

def get_largest(input_list):
    max_index = 0
    max = 0
    for i in range(len(input_list)):
        if max < input_list[i]:
            max = input_list[i]
            max_index = i

    return max_index, max

def get_second_largest(input_list):
    smax_index = 0
    smax = 0
    max_index, max = get_largest(input_list)

    for i in range(len(input_list)):
        if i == max_index:
            continue
        if smax < input_list[i]:
            smax_index = i
            smax = input_list[i]

    return smax_index, smax

def main(): 

    # Generate a random poopulation and print
    generate_population()
    print_population()

    current_fit = 0
    counter = 0
    solutions = []
    while len(solutions) != 92:

        population.clear()
        generate_population()
        # print_population()

        # Start the generations
        while current_fit != 56 and counter < 20000:

            fitness_scores = []
            current_fit = 0

            max_index = 0
            # Calculate fitness scores for a population
            for i in range(CHROMOSOME_POPULATION):
                
                chromosome = population[i]
                fitness_score = fitness_function(chromosome)
                
                if current_fit < fitness_score:
                    current_fit = fitness_score
                    max_index = i
                fitness_scores.append(fitness_score)    

            # Check if a solution was found
            if current_fit == 56:
                solution = population[max_index]

                solution_exists = False
                # Check if the solution exists
                for i in solutions:
                    if i == solution:
                        solution_exists = True
                        break
                
                
                if solution_exists:
                    print("Solution already exists in keys")
                    counter = 0
                    current_fit = 0
                    break
                else:
                    print("Solution: ", solution, "Score: ", fitness_function(solution), "Counter: ", counter)
                    solutions.append(solution)
                    
                    # Mirror the solution to get 2 distinct values
                    mirror_solution = solution[::-1]
                    solutions.append(mirror_solution)
                    print("Mirror Solution: ", mirror_solution, "Score: ", fitness_function(mirror_solution), "Counter: ", counter)

                    counter = 0
                    current_fit = 0
                    break

            # Get the fitness probability from the fitness scores
            fitness_probabilities = get_fitness_probability(fitness_scores)

            # Start selection
            parent_index1, parent_index2 = selection(fitness_probabilities)
            parent1 = population[parent_index1]
            parent2 = population[parent_index2]

            crossover_count = 0
            index = 0
            # Crossover the fittest chromosomes and random crossover points to the new population
            while crossover_count < CHROMOSOME_POPULATION/2:
                child1, child2 = crossover(parent1, parent2)
            
                # Update the population with crossover children
                population[index] = child1
                population[index + 1] = child2

                crossover_count += 1
                index += 2
            
            # Mutate and Update population
            new_child1 = mutation(child1)
            population[parent_index1] = new_child1
            new_child2 = mutation(child2)
            population[parent_index2] = new_child2

            # Replace in population
            counter += 1

    # Write solutions to a file
    f = open("solutions.txt", "w")
    for i in solutions:
        f.write(str(i))
        f.write('\n')

    # Write new solutions
    f = open("board_solutions.txt", "w")
    
    for index in solutions:
        counter = 8
        while counter >= 1:
            board_row = []
            for i in index:
                if i == counter:
                    board_row.append(1)
                else:
                    board_row.append(0)
            f.write(str(board_row))
            f.write(str('\n'))
            counter -= 1
        f.write('\n\n')

if __name__ == '__main__':
    main()