"""
Helper functions for 3D city simulation
"""
import random
from objects.building import Building
from objects.tree import Tree
from objects.car import Car


def generate_random_city(num_buildings=15, num_trees=10):
    """
    Generate random city layout
    Args:
        num_buildings: Number of buildings to generate
        num_trees: Number of trees to generate
    Returns:
        tuple: (buildings_list, trees_list)
    """
    buildings = []
    trees = []
    
    # Define grid positions avoiding roads (center cross)
    # We'll place buildings in 4 quadrants
    
    # Quadrant positions
    quadrants = [
        (-20, -20, -5, -5),   # Bottom-left
        (5, -20, 20, -5),     # Bottom-right
        (-20, 5, -5, 20),     # Top-left
        (5, 5, 20, 20),       # Top-right
    ]
    
    # Generate buildings
    for _ in range(num_buildings):
        # Pick random quadrant
        qx_min, qz_min, qx_max, qz_max = random.choice(quadrants)
        
        # Random position within quadrant
        x = random.uniform(qx_min, qx_max)
        z = random.uniform(qz_min, qz_max)
        
        building = Building(x, z)
        buildings.append(building)
    
    # Generate trees (near roads and buildings)
    for _ in range(num_trees):
        # Pick random quadrant
        qx_min, qz_min, qx_max, qz_max = random.choice(quadrants)
        
        # Random position within quadrant (but closer to edges)
        if random.random() > 0.5:
            x = random.uniform(qx_min, qx_min + 3)
        else:
            x = random.uniform(qx_max - 3, qx_max)
            
        if random.random() > 0.5:
            z = random.uniform(qz_min, qz_min + 3)
        else:
            z = random.uniform(qz_max - 3, qz_max)
        
        tree = Tree(x, z)
        trees.append(tree)
    
    return buildings, trees


def create_cars(num_cars=4):
    """
    Create cars for animation
    Args:
        num_cars: Number of cars to create
    Returns:
        list: List of Car objects
    """
    cars = []
    
    # Create cars on horizontal and vertical roads
    for i in range(num_cars):
        if i % 2 == 0:
            car = Car(path_type='horizontal')
            # Stagger starting positions
            car.position = -30.0 + (i * 15)
        else:
            car = Car(path_type='vertical')
            car.position = -30.0 + (i * 15)
        
        cars.append(car)
    
    return cars
