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


def generate_random_city(num_buildings=60, num_trees=40):
    """
    Generate random city layout - expanded version with more area
    Args:
        num_buildings: Number of buildings to generate
        num_trees: Number of trees to generate (not including road-side trees)
    Returns:
        tuple: (buildings_list, trees_list)
    """
    buildings = []
    trees = []
    
    # Define road dimensions (must match Road class)
    road_width = 8.0
    road_length = 150.0
    grid_spacing = 50.0  # Spacing between parallel roads
    
    # Define safe zones for buildings (avoiding roads with margin)
    road_margin = 7.0
    
    # Define city blocks (areas between roads)
    # With 3 horizontal and 3 vertical roads at -50, 0, 50, we have blocks:
    # Block boundaries are from road edge + margin to next road edge - margin
    blocks = []
    road_positions = [-grid_spacing, 0, grid_spacing]
    
    # Generate blocks between roads
    for i in range(len(road_positions) + 1):
        for j in range(len(road_positions) + 1):
            # Calculate block boundaries
            if i == 0:
                x_min = -road_length/2
                x_max = road_positions[0] - road_width/2 - road_margin
            elif i == len(road_positions):
                x_min = road_positions[-1] + road_width/2 + road_margin
                x_max = road_length/2
            else:
                x_min = road_positions[i-1] + road_width/2 + road_margin
                x_max = road_positions[i] - road_width/2 - road_margin
            
            if j == 0:
                z_min = -road_length/2
                z_max = road_positions[0] - road_width/2 - road_margin
            elif j == len(road_positions):
                z_min = road_positions[-1] + road_width/2 + road_margin
                z_max = road_length/2
            else:
                z_min = road_positions[j-1] + road_width/2 + road_margin
                z_max = road_positions[j] - road_width/2 - road_margin
            
            # Only add valid blocks (where min < max)
            if x_min < x_max and z_min < z_max:
                blocks.append((x_min, z_min, x_max, z_max))
    
    # Generate buildings with collision detection
    attempts = 0
    max_attempts = num_buildings * 30  # Prevent infinite loop
    
    while len(buildings) < num_buildings and attempts < max_attempts:
        attempts += 1
        
        # Pick random block
        if not blocks:
            break
        qx_min, qz_min, qx_max, qz_max = random.choice(blocks)
        
        # Random position within block
        x = random.uniform(qx_min, qx_max)
        z = random.uniform(qz_min, qz_max)
        
        # Create temporary building to get dimensions
        temp_building = Building(x, z)
        
        # Check for collisions
        if not check_collision(x, z, temp_building.width, temp_building.depth, buildings):
            buildings.append(temp_building)
    
    # Generate trees along both sides of all roads
    tree_spacing = 4.0  # Space between trees
    tree_offset = road_width/2 + 2.0  # Distance from road center
    
    # Exclusion zone at intersections
    intersection_exclusion = road_width/2 + 2.0
    
    # Trees along all horizontal roads
    for road_z in road_positions:
        for i in range(int(road_length / tree_spacing)):
            x = -road_length/2 + i * tree_spacing
            # Skip trees near intersections with vertical roads
            skip = False
            for road_x in road_positions:
                if abs(x - road_x) < intersection_exclusion:
                    skip = True
                    break
            if not skip:
                trees.append(Tree(x, road_z + tree_offset))
                trees.append(Tree(x, road_z - tree_offset))
    
    # Trees along all vertical roads
    for road_x in road_positions:
        for i in range(int(road_length / tree_spacing)):
            z = -road_length/2 + i * tree_spacing
            # Skip trees near intersections with horizontal roads
            skip = False
            for road_z in road_positions:
                if abs(z - road_z) < intersection_exclusion:
                    skip = True
                    break
            if not skip:
                trees.append(Tree(road_x + tree_offset, z))
                trees.append(Tree(road_x - tree_offset, z))
    
    return buildings, trees


def create_cars(num_cars=8):
    """
    Create cars for animation on the expanded road network
    Args:
        num_cars: Number of cars to create
    Returns:
        list: List of Car objects
    """
    cars = []
    
    # Road positions for the grid (-50, 0, 50)
    road_positions = [-50.0, 0.0, 50.0]
    
    # Create cars on different roads in the grid
    for i in range(num_cars):
        if i % 2 == 0:
            car = Car(path_type='horizontal')
            # Assign to different horizontal roads
            road_index = (i // 2) % len(road_positions)
            car.lane_offset = road_positions[road_index]
            # Stagger starting positions across the longer road
            car.position = -75.0 + (i * 20)
        else:
            car = Car(path_type='vertical')
            # Assign to different vertical roads
            road_index = (i // 2) % len(road_positions)
            car.lane_offset = road_positions[road_index]
            car.position = -75.0 + (i * 20)
        
        cars.append(car)
    
    return cars
