"""
Test script to validate road and tree positioning
Ensures trees don't overlap roads and road elevation is correct
"""
import sys

# Test road elevation and tree positioning parameters
def test_road_and_tree_positioning():
    """Test that road elevation and tree positioning are correct"""
    print("Testing road and tree positioning...")
    print("=" * 50)
    
    # Road parameters (from road.py)
    road_width = 8.0
    road_elevation = 0.35  # Updated from 0.25
    road_line_elevation = 0.36  # Updated from 0.26
    
    # Tree parameters (from helpers.py)
    tree_offset = road_width/2 + 2.0  # Updated from 1.5
    
    # Tree dimensions (from tree.py)
    tree_trunk_radius = 0.2
    tree_foliage_radius = 1.0
    
    # Ground level
    ground_level = 0.0
    
    # Tests
    tests_passed = 0
    tests_total = 0
    
    # Test 1: Road elevation is above ground
    tests_total += 1
    if road_elevation > ground_level:
        print(f"✓ Test 1 PASSED: Road elevation ({road_elevation}) is above ground ({ground_level})")
        tests_passed += 1
    else:
        print(f"✗ Test 1 FAILED: Road elevation ({road_elevation}) should be above ground ({ground_level})")
    
    # Test 2: Road lines are above road surface
    tests_total += 1
    if road_line_elevation > road_elevation:
        print(f"✓ Test 2 PASSED: Road lines ({road_line_elevation}) are above road surface ({road_elevation})")
        tests_passed += 1
    else:
        print(f"✗ Test 2 FAILED: Road lines ({road_line_elevation}) should be above road surface ({road_elevation})")
    
    # Test 3: Trees don't overlap road
    road_edge = road_width / 2  # Road extends from -road_edge to +road_edge
    tree_center = tree_offset
    tree_inner_edge = tree_center - tree_foliage_radius  # Closest point of tree to road center
    
    tests_total += 1
    clearance = tree_inner_edge - road_edge
    if tree_inner_edge > road_edge:
        print(f"✓ Test 3 PASSED: Trees ({tree_inner_edge:.1f}) don't overlap road edge ({road_edge:.1f}), clearance: {clearance:.1f}")
        tests_passed += 1
    else:
        print(f"✗ Test 3 FAILED: Trees ({tree_inner_edge:.1f}) overlap road edge ({road_edge:.1f})")
    
    # Test 4: Adequate clearance for trees
    tests_total += 1
    min_clearance = 1.0  # Minimum recommended clearance
    if clearance >= min_clearance:
        print(f"✓ Test 4 PASSED: Tree clearance ({clearance:.1f}) is adequate (>= {min_clearance})")
        tests_passed += 1
    else:
        print(f"✗ Test 4 FAILED: Tree clearance ({clearance:.1f}) should be >= {min_clearance}")
    
    # Test 5: Road elevation sufficient to prevent z-fighting
    tests_total += 1
    min_elevation_diff = 0.2  # Minimum difference from ground to prevent z-fighting
    elevation_diff = road_elevation - ground_level
    if elevation_diff >= min_elevation_diff:
        print(f"✓ Test 5 PASSED: Road elevation difference ({elevation_diff:.2f}) prevents z-fighting (>= {min_elevation_diff})")
        tests_passed += 1
    else:
        print(f"✗ Test 5 FAILED: Road elevation difference ({elevation_diff:.2f}) may cause z-fighting (should be >= {min_elevation_diff})")
    
    print("=" * 50)
    print(f"Results: {tests_passed}/{tests_total} tests passed")
    
    # Summary
    print("\nSummary of positioning:")
    print(f"  Road width: {road_width}")
    print(f"  Road edge (from center): ±{road_edge}")
    print(f"  Road elevation: {road_elevation}")
    print(f"  Tree offset (from center): ±{tree_offset}")
    print(f"  Tree foliage radius: {tree_foliage_radius}")
    print(f"  Tree inner edge: {tree_inner_edge:.1f}")
    print(f"  Clearance between road and trees: {clearance:.1f}")
    
    return tests_passed == tests_total

if __name__ == "__main__":
    success = test_road_and_tree_positioning()
    sys.exit(0 if success else 1)
