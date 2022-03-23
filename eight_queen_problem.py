from random import randint

MUTATION_PROBABILITY = 0.01
CROSSOVER_PROBABILITY = 0.7
CHROMOSOME_POPULATION = 10

# Define the chromosomes - This will keep changing with every iteration
population = []    

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
    for i in range(CHROMOSOME_POPULATION):
        print(population[i])

# Method to perform Mutation
def mutation(parent):
    pass

# Method to perform Crossover
def crossover(parent1, parent2):
    pass

# Method to perform Cloning
def cloning():
    pass

# Fitness function
def fitness_function(chromosome):
    
    # Initialize fitness_score for a passed chromosome
    fitness_score = 0

    # Check each queen in a column and count how many conflicts he doesnt have
    for i in range(8):
        column = chromosome[i]
        for j in range(8):      
            if i == j:
                continue
            # Do 2 queens belong to the same row - Not the same column assumption has been made
            if chromosome[j] == column:
                continue
            # Clash on Primary Diagonal
            if j + chromosome[j] == i + column:
                continue
            # Clash on Alternate Diagonal
            if j - chromosome[j] == i - column:
                continue
            fitness_score += 1        

    return fitness_score

# Selection method - Select parent individuals based on fitness function
def selection():
    pass

def main(): 
    # Generate a random poopulation and print
    generate_population()
    print_population()

     
    fitness_scores = []
    # Calculate fitness scores for a population
    for i in range(CHROMOSOME_POPULATION):
        chromosome = population[i]
        fitness_score = fitness_function(chromosome)
        fitness_scores.append(fitness_score)    

    print(fitness_scores)

if __name__ == '__main__':
    main()