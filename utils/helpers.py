"""
Helper functions for 3D city simulation
"""
import random
from objects.building import Building
from objects.tree import Tree
from objects.car import Car


def check_collision(x, z, width, depth, existing_buildings):
    """
    Check if a building at (x, z) would collide with existing buildings
    Args:
        x, z: Position of new building
        width, depth: Dimensions of new building
        existing_buildings: List of existing Building objects
    Returns:
        bool: True if collision detected, False otherwise
    """
    # Add some spacing buffer
    buffer = 1.0
    
    for building in existing_buildings:
        # Calculate distance between building centers
        dx = abs(x - building.x)
        dz = abs(z - building.z)
        
        # Check if bounding boxes overlap (with buffer)
        if (dx < (width + building.width) / 2 + buffer and 
            dz < (depth + building.depth) / 2 + buffer):
            return True
    
    return False


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
    
    # Define road dimensions (must match Road class)
    road_width = 8.0
    road_length = 60.0
    
    # Define safe zones for buildings (avoiding roads with margin)
    road_margin = 2.0
    
    # Quadrant positions (avoiding center cross roads)
    quadrants = [
        (-road_length/2, -road_length/2, -(road_width/2 + road_margin), -(road_width/2 + road_margin)),   # Bottom-left
        (road_width/2 + road_margin, -road_length/2, road_length/2, -(road_width/2 + road_margin)),     # Bottom-right
        (-road_length/2, road_width/2 + road_margin, -(road_width/2 + road_margin), road_length/2),     # Top-left
        (road_width/2 + road_margin, road_width/2 + road_margin, road_length/2, road_length/2),       # Top-right
    ]
    
    # Generate buildings with collision detection
    attempts = 0
    max_attempts = num_buildings * 20  # Prevent infinite loop
    
    while len(buildings) < num_buildings and attempts < max_attempts:
        attempts += 1
        
        # Pick random quadrant
        qx_min, qz_min, qx_max, qz_max = random.choice(quadrants)
        
        # Random position within quadrant
        x = random.uniform(qx_min, qx_max)
        z = random.uniform(qz_min, qz_max)
        
        # Create temporary building to get dimensions
        temp_building = Building(x, z)
        
        # Check for collisions
        if not check_collision(x, z, temp_building.width, temp_building.depth, buildings):
            buildings.append(temp_building)
    
    # Generate trees along both sides of roads
    tree_spacing = 4.0  # Space between trees
    tree_offset = road_width/2 + 2.0  # Distance from road center (increased to avoid overlap)
    
    # Exclusion zone at intersection to prevent trees from overlapping crossing roads
    intersection_exclusion = road_width/2 + 2.0  # Exclude trees within this distance from center
    
    # Trees along horizontal road (top side)
    for i in range(int(road_length / tree_spacing)):
        x = -road_length/2 + i * tree_spacing
        z = tree_offset
        # Skip trees in intersection zone
        if abs(x) > intersection_exclusion:
            trees.append(Tree(x, z))
    
    # Trees along horizontal road (bottom side)
    for i in range(int(road_length / tree_spacing)):
        x = -road_length/2 + i * tree_spacing
        z = -tree_offset
        # Skip trees in intersection zone
        if abs(x) > intersection_exclusion:
            trees.append(Tree(x, z))
    
    # Trees along vertical road (left side)
    for i in range(int(road_length / tree_spacing)):
        x = -tree_offset
        z = -road_length/2 + i * tree_spacing
        # Skip trees in intersection zone
        if abs(z) > intersection_exclusion:
            trees.append(Tree(x, z))
    
    # Trees along vertical road (right side)
    for i in range(int(road_length / tree_spacing)):
        x = tree_offset
        z = -road_length/2 + i * tree_spacing
        # Skip trees in intersection zone
        if abs(z) > intersection_exclusion:
            trees.append(Tree(x, z))
    
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
