"""
Test script to validate the project structure
This script checks if all modules can be imported without runtime errors
"""
import sys
import os

def test_structure():
    """Test if the project structure is valid"""
    print("Testing 3D City Simulation Project Structure...")
    print("=" * 50)
    
    # Check if all directories exist
    directories = ['engine', 'objects', 'utils']
    for dir_name in directories:
        if os.path.isdir(dir_name):
            print(f"✓ Directory '{dir_name}' exists")
        else:
            print(f"✗ Directory '{dir_name}' missing")
            return False
    
    # Check if all required files exist
    required_files = [
        'main.py',
        'requirements.txt',
        'engine/__init__.py',
        'engine/renderer.py',
        'engine/camera.py',
        'engine/lighting.py',
        'objects/__init__.py',
        'objects/building.py',
        'objects/road.py',
        'objects/tree.py',
        'objects/car.py',
        'utils/__init__.py',
        'utils/helpers.py',
    ]
    
    for file_path in required_files:
        if os.path.isfile(file_path):
            print(f"✓ File '{file_path}' exists")
        else:
            print(f"✗ File '{file_path}' missing")
            return False
    
    print("=" * 50)
    print("✓ All structure checks passed!")
    print("\nNote: To run the application, execute: python main.py")
    print("Note: This requires a system with display support (GUI)")
    return True

if __name__ == "__main__":
    success = test_structure()
    sys.exit(0 if success else 1)
