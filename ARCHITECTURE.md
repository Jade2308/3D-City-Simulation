# Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                         main.py                              │
│  ┌────────────────────┐        ┌─────────────────────────┐  │
│  │  CitySimulation    │        │    ControlGUI           │  │
│  │  - Core logic      │◄───────┤    - Tkinter GUI        │  │
│  │  - Event handling  │        │    - User controls      │  │
│  │  - Main loop       │        └─────────────────────────┘  │
│  └─────┬──────────────┘                                      │
└────────┼─────────────────────────────────────────────────────┘
         │
         ├──────────────────────────────────────┐
         │                                       │
         ▼                                       ▼
┌─────────────────────┐              ┌─────────────────────┐
│   engine/           │              │   objects/          │
│                     │              │                     │
│  ┌──────────────┐   │              │  ┌──────────────┐   │
│  │  Renderer    │   │              │  │  Building    │   │
│  │  - OpenGL    │   │              │  │  - Random    │   │
│  │  - Window    │   │              │  │  - Cuboid    │   │
│  └──────────────┘   │              │  └──────────────┘   │
│                     │              │                     │
│  ┌──────────────┐   │              │  ┌──────────────┐   │
│  │  Camera      │   │              │  │  Road        │   │
│  │  - View      │   │              │  │  - Cross     │   │
│  │  - Rotation  │   │              │  │  - Lines     │   │
│  └──────────────┘   │              │  └──────────────┘   │
│                     │              │                     │
│  ┌──────────────┐   │              │  ┌──────────────┐   │
│  │  Lighting    │   │              │  │  Tree        │   │
│  │  - OpenGL    │   │              │  │  - Cylinder  │   │
│  │  - Setup     │   │              │  │  - Sphere    │   │
│  └──────────────┘   │              │  └──────────────┘   │
│                     │              │                     │
└─────────────────────┘              │  ┌──────────────┐   │
                                     │  │  Car         │   │
                                     │  │  - Animated  │   │
         ┌────────────────────────►  │  │  - Loop      │   │
         │                           │  └──────────────┘   │
         │                           └─────────────────────┘
         │
┌─────────────────────┐
│   utils/            │
│                     │
│  ┌──────────────┐   │
│  │  helpers.py  │   │
│  │  - City gen  │   │
│  │  - Car gen   │   │
│  └──────────────┘   │
└─────────────────────┘
```

## Data Flow

1. **Initialization**
   ```
   main.py
     └─> CitySimulation.__init__()
           ├─> Renderer.init_pygame()
           ├─> Camera()
           ├─> Lighting.setup()
           └─> generate_random_city() → Buildings, Trees
   ```

2. **Main Loop**
   ```
   CitySimulation.run()
     └─> while running:
           ├─> handle_events() → Mouse/Keyboard input
           ├─> update() → Car positions
           └─> render() → Draw all objects
   ```

3. **Rendering Pipeline**
   ```
   render()
     ├─> renderer.clear_screen()
     ├─> camera.apply_view()
     ├─> lighting.update_position()
     ├─> draw_ground()
     ├─> road.draw()
     ├─> for building in buildings:
     │     └─> building.draw()
     ├─> for tree in trees:
     │     └─> tree.draw()
     └─> for car in cars:
           └─> car.draw()
   ```

## Component Responsibilities

### main.py
- Application entry point
- Event loop management
- GUI integration
- User input handling

### engine/renderer.py
- OpenGL context setup
- Window management (Pygame)
- Viewport configuration
- Buffer swapping

### engine/camera.py
- View matrix calculation
- Camera transformations (rotation, zoom)
- Preset views (top, street, 45°)

### engine/lighting.py
- OpenGL lighting setup
- Light properties (ambient, diffuse, specular)
- Material properties

### objects/building.py
- Building geometry (cuboid)
- Random size and color generation
- OpenGL quad rendering

### objects/road.py
- Road network layout
- Asphalt surface rendering
- Lane marker lines

### objects/tree.py
- Tree geometry (cylinder + sphere)
- Trunk and foliage rendering
- GLU quadric objects

### objects/car.py
- Car geometry (box + cab)
- Animation logic
- Path following
- Speed control

### utils/helpers.py
- City layout generation
- Random placement algorithms
- Car initialization

## Key Design Patterns

1. **Object-Oriented Design**
   - Each 3D object is a self-contained class
   - Encapsulation of geometry and rendering logic

2. **Separation of Concerns**
   - Rendering engine separate from objects
   - GUI separate from simulation logic

3. **Modular Architecture**
   - Each module has a single responsibility
   - Easy to extend and modify

4. **Event-Driven**
   - Pygame event loop
   - User input triggers camera/animation changes
