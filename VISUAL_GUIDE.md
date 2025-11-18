# Screenshots & Visual Guide

## Expected Output

When you run `python main.py`, you should see:

### Main 3D Window (800x600)
- **Sky**: Light blue background
- **Ground**: Green grass plane
- **Roads**: Dark gray cross-shaped roads with yellow dashed center lines
- **Buildings**: Gray cuboid buildings of varying heights distributed in quadrants
- **Trees**: Green sphere foliage on brown cylinder trunks
- **Cars**: Colorful boxes (red, blue, yellow, green, orange) moving along roads

### Control Panel Window (300x350)
```
┌────────────────────────────────────────┐
│      3D City Simulation                │
├────────────────────────────────────────┤
│ Mouse: Drag to rotate                  │
│ Wheel: Zoom                             │
│ Space: Pause/Resume                     │
│ R: Regenerate city                      │
├────────────────────────────────────────┤
│ ┌─ Animation Control ────────────────┐ │
│ │                                    │ │
│ │  [Stop Animation]                  │ │
│ │                                    │ │
│ │  Car Speed:                        │ │
│ │  ├────────●──────────┤ 1.0        │ │
│ │                                    │ │
│ └────────────────────────────────────┘ │
├────────────────────────────────────────┤
│ ┌─ Camera Views ─────────────────────┐ │
│ │                                    │ │
│ │  [Top View]                        │ │
│ │  [Street View]                     │ │
│ │  [45° View]                        │ │
│ │                                    │ │
│ └────────────────────────────────────┘ │
├────────────────────────────────────────┤
│  [🔄 Generate Random City]             │
└────────────────────────────────────────┘
```

## Visual Features to Look For

### 1. Buildings
- Various heights (5-20 units)
- Different widths (2-5 units)
- Gray colors (0.5-0.8 brightness)
- Positioned in 4 quadrants around the road cross
- Proper 3D cuboid shape with all faces visible

### 2. Roads
- Main horizontal road from left to right
- Main vertical road from top to bottom
- Dark gray surface (0.2, 0.2, 0.2 RGB)
- Yellow dashed center lines (0.9, 0.9, 0.0 RGB)
- Width: 4 units each

### 3. Trees
- Brown cylinder trunks (height: 2 units, radius: 0.2)
- Green sphere foliage (radius: 1 unit)
- Positioned near buildings and roads
- Smooth shading from OpenGL lighting

### 4. Cars
- Box-shaped body (2 x 0.8 x 1 units)
- Smaller cab/roof on top
- Bright colors: red, blue, yellow, green, or orange
- Smooth movement along roads
- Automatic looping behavior

### 5. Lighting Effects
- Directional light from upper angle
- Ambient light for overall brightness
- Diffuse shading on all objects
- Specular highlights on surfaces
- Realistic shadows and depth

### 6. Camera Views

**Top View (Press 1)**
- Looking straight down at the city
- See the cross-shaped road layout clearly
- Buildings appear as rectangles
- Good for understanding city layout

**Street View (Press 2)**
- Eye-level view from the road
- Buildings tower above
- Feel like walking in the city
- Cars pass by at eye level

**45° View (Press 3)**
- Angled perspective
- Best view for screenshots
- Shows depth and 3D nature
- Balanced view of all elements

### 7. Animation
- Cars move smoothly along horizontal and vertical roads
- Multiple cars at different positions
- Continuous looping motion
- Speed adjustable via GUI slider
- Can be paused with Space key or Stop button

## Testing Checklist

When you run the application, verify:

- [ ] Main window opens (800x600)
- [ ] Control panel opens separately
- [ ] Sky is light blue
- [ ] Ground is green
- [ ] Roads are visible (dark gray with yellow lines)
- [ ] Buildings are rendered (gray cuboids)
- [ ] Trees are visible (brown + green)
- [ ] Cars are moving
- [ ] Mouse drag rotates camera
- [ ] Mouse wheel zooms in/out
- [ ] Keyboard shortcuts work (Space, R, 1, 2, 3, +, -)
- [ ] GUI buttons respond
- [ ] Speed slider changes car speed
- [ ] View buttons change camera position
- [ ] Generate button creates new city
- [ ] No errors in console
- [ ] Smooth frame rate (60 FPS)

## Performance Indicators

**Good Performance**:
- Smooth camera rotation
- Fluid car movement
- No stuttering or lag
- Responsive controls
- ~60 FPS

**If Performance Issues**:
- Try reducing number of buildings in `helpers.py`
- Ensure graphics drivers are up to date
- Check system has OpenGL support
- Close other applications

## Common Visual Issues

**Issue: Black screen**
- Problem: OpenGL not initialized
- Solution: Update graphics drivers

**Issue: Objects not visible**
- Problem: Camera too far or wrong angle
- Solution: Press '3' for 45° view or use mouse to rotate

**Issue: Flat/No lighting**
- Problem: Lighting not enabled
- Solution: Check lighting.py is being called

**Issue: Flickering**
- Problem: Z-fighting or depth buffer issue
- Solution: Normal with overlapping surfaces

**Issue: Jerky animation**
- Problem: Low FPS
- Solution: Reduce object count or check CPU usage

## Screenshots to Take

For documentation/presentation, capture:

1. **Overview shot**: 45° view showing whole city
2. **Top view**: Bird's eye view of layout
3. **Street view**: Eye-level perspective
4. **Close-up**: Zoomed view of buildings and trees
5. **GUI panel**: Control window
6. **Different city layouts**: Press R several times

## Video Demo Ideas

If making a video demonstration:

1. Start with top view
2. Slowly rotate camera 360°
3. Zoom in to street level
4. Show cars moving
5. Open control panel
6. Adjust speed slider
7. Try different view presets
8. Generate new random city
9. Pause/resume animation
10. Show keyboard shortcuts

---

**Note**: Since this is a headless environment, actual screenshots cannot be generated here. Run the application on a system with display support to capture these visuals.
