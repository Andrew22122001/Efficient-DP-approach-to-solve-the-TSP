import math
import time

# function to calculate the distance between two cities
def distance(city1, city2):
    return int(math.sqrt((city1[0]-city2[0])**2 + (city1[1]-city2[1])**2) + 0.5)

# function to find the nearest neighbor of a city using Dynamic Programming
def nearest_neighbor(city, cities, visited):
    min_dist = float('inf')
    nearest = None
    for neighbor in cities:
        if neighbor[0] not in visited:
            dist = distance(city, neighbor)
            if dist < min_dist:
                min_dist = dist
                nearest = neighbor
    return nearest

# function to solve the TSP problem using dynamic programming
def tsp_nn(cities):
    visited = [cities[0][0]] # start from the first city
    total_dist = 0
    current_city = cities[0]
    while len(visited) < len(cities):
        next_city = nearest_neighbor(current_city, cities, visited)
        visited.append(next_city[0]) # type: ignore
        total_dist += distance(current_city, next_city)
        current_city = next_city
    # add the distance from the last city to the first city
    total_dist += distance(current_city, cities[0])
    return visited, total_dist

# read the dataset
with open('att532.tsp') as file:
    data = file.readlines()

# extract the city coordinates from the dataset
cities = []
for line in data[6:-1]:
    city = [int(x) for x in line.strip().split()[:]]
    cities.append(city)
#print(cities) 

# solve the TSP problem using the Nearest Neighbor Algorithm
start_time = time.time()
tour, cost = tsp_nn(cities)
end_time = time.time()
execution_time = end_time - start_time

# print the optimal tour and cost
print('Optimal Tour:', tour)
print('Cost:', cost)
print("Execution time:", execution_time)
