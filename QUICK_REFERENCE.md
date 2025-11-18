# Quick Reference - 3D City Simulation

## Chạy chương trình
```bash
python main.py
```

## Điều khiển nhanh

### Bàn phím
| Phím | Chức năng |
|------|-----------|
| **Space** | Tạm dừng/Tiếp tục animation |
| **R** | Tạo lại thành phố ngẫu nhiên |
| **1** | Góc nhìn từ trên (Top View) |
| **2** | Góc nhìn mặt đường (Street View) |
| **3** | Góc nhìn 45 độ |
| **+** hoặc **=** | Zoom in |
| **-** | Zoom out |
| **ESC** | Thoát chương trình |

### Chuột
| Thao tác | Chức năng |
|----------|-----------|
| **Kéo chuột trái** | Xoay camera quanh thành phố |
| **Con lăn lên** | Zoom in |
| **Con lăn xuống** | Zoom out |

## GUI Controls (Cửa sổ điều khiển)

### Animation Control
- **Start/Stop Animation**: Bật/tắt chuyển động của xe
- **Speed Slider**: Điều chỉnh tốc độ xe (0.0 - 3.0x)

### Camera Views
- **Top View**: Nhìn từ trên xuống
- **Street View**: Nhìn từ mặt đường
- **45° View**: Góc nhìn chéo 45 độ

### City Generation
- **Generate Random City**: Tạo thành phố mới với layout ngẫu nhiên

## Đối tượng trong scene

1. **Tòa nhà** (Buildings)
   - Hình hộp chữ nhật màu xám
   - Chiều cao và kích thước ngẫu nhiên
   - Phân bố trong 4 khu vực xung quanh đường

2. **Đường** (Roads)
   - Đường giao nhau hình chữ thập
   - Màu xám đậm với vạch kẻ vàng
   - Xe chạy trên đường này

3. **Cây** (Trees)
   - Thân cây màu nâu (cylinder)
   - Tán lá màu xanh (sphere)
   - Phân bố gần đường và tòa nhà

4. **Xe hơi** (Cars)
   - Màu sắc ngẫu nhiên (đỏ, xanh, vàng, v.v.)
   - Tự động di chuyển trên đường
   - Lặp lại hành trình

## Tips & Tricks

1. **Xem toàn cảnh**: Nhấn phím **1** để chuyển sang Top View
2. **Xem chi tiết**: Nhấn phím **2** để xem ở góc đường
3. **Góc đẹp nhất**: Nhấn phím **3** cho góc nhìn 45°
4. **Thử nghiệm**: Nhấn **R** nhiều lần để thấy các layout thành phố khác nhau
5. **Tốc độ cao**: Kéo slider speed lên 3.0x để xem xe chạy nhanh
6. **Dừng và quan sát**: Nhấn **Space** để tạm dừng và xoay camera thoải mái

## Cấu trúc code

```
main.py              → Entry point, chứa logic chính
├── engine/
│   ├── renderer.py  → Xử lý render OpenGL
│   ├── camera.py    → Điều khiển camera 3D
│   └── lighting.py  → Cài đặt ánh sáng
├── objects/
│   ├── building.py  → Class tòa nhà
│   ├── road.py      → Class đường
│   ├── tree.py      → Class cây
│   └── car.py       → Class xe (có animation)
└── utils/
    └── helpers.py   → Hàm tiện ích
```

## Thông số kỹ thuật

- **Ngôn ngữ**: Python 3.7+
- **Render**: PyOpenGL
- **Window**: Pygame
- **GUI**: Tkinter
- **FPS**: 60 (có thể thay đổi trong code)
- **Resolution**: 800x600 (có thể thay đổi trong code)

## Tùy chỉnh

### Thay đổi số lượng đối tượng
Mở `main.py` và tìm dòng:
```python
self.buildings, self.trees = generate_random_city(num_buildings=15, num_trees=10)
self.cars = create_cars(num_cars=4)
```

### Thay đổi kích thước cửa sổ
Mở `main.py` và tìm dòng:
```python
self.renderer = Renderer(800, 600)  # width, height
```

### Thay đổi tốc độ xe mặc định
Mở `objects/car.py` và tìm dòng:
```python
self.speed = 0.05  # Tăng giá trị này để xe chạy nhanh hơn
```

## Troubleshooting

**Q: Chương trình không chạy?**
A: Kiểm tra đã cài đặt dependencies: `pip install -r requirements.txt`

**Q: Màn hình đen?**
A: Kiểm tra driver card màn hình và OpenGL support

**Q: GUI không hiện?**
A: Tkinter có thể cần cài thêm trên Linux: `sudo apt-get install python3-tk`

**Q: Xe không chạy?**
A: Nhấn nút "Start Animation" trong GUI hoặc phím Space
