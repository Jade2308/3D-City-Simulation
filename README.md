# 3D City Simulation
Bài tập nhóm môn Đồ Họa Máy Tính - Mô phỏng thành phố 3D đơn giản

## Giới thiệu
Dự án mô phỏng thành phố 3D được xây dựng bằng Python, sử dụng PyOpenGL và Pygame. Chương trình hiển thị một thành phố với các tòa nhà, đường xá, cây cối và xe hơi di chuyển.

## Tính năng

### Đối tượng 3D
- **Tòa nhà**: Các hình hộp chữ nhật với chiều cao và màu sắc ngẫu nhiên
- **Đường xá**: Mạng lưới đường giao nhau với vạch kẻ đường
- **Cây cối**: Cây đơn giản với thân cây (cylinder) và tán lá (sphere)
- **Xe hơi**: Xe di chuyển tự động trên đường

### Điều khiển Camera
- **Xoay camera**: Kéo chuột để xoay góc nhìn
- **Zoom**: Sử dụng con lăn chuột hoặc phím +/-
- **Góc nhìn có sẵn**:
  - Phím 1: Top view (nhìn từ trên xuống)
  - Phím 2: Street view (nhìn từ mặt đường)
  - Phím 3: 45° view (góc nhìn 45 độ)

### Giao diện điều khiển (GUI)
- **Start/Stop Animation**: Tạm dừng/tiếp tục hoạt ảnh
- **Speed Slider**: Điều chỉnh tốc độ di chuyển của xe
- **View Presets**: Chọn góc nhìn nhanh
- **Random City**: Tạo lại bố cục thành phố ngẫu nhiên

### Môi trường
- Ánh sáng cơ bản (OpenGL lighting)
- Bóng đổ và hiệu ứng ánh sáng trên các vật thể
- Nền trời xanh và mặt đất xanh lá

## Cài đặt

### Yêu cầu hệ thống
- Python 3.7 trở lên
- Windows/Linux/MacOS

### Cài đặt thư viện
```bash
pip install -r requirements.txt
```

### Chạy chương trình
```bash
python main.py
```

## Cấu trúc dự án

```
3D-City-Simulation/
│
├── main.py                 # File chính, chứa logic ứng dụng và GUI
│
├── engine/                 # Module xử lý render và camera
│   ├── __init__.py
│   ├── renderer.py        # Xử lý render OpenGL
│   ├── camera.py          # Điều khiển camera 3D
│   └── lighting.py        # Cài đặt ánh sáng
│
├── objects/               # Module chứa các đối tượng 3D
│   ├── __init__.py
│   ├── building.py        # Class Building (tòa nhà)
│   ├── road.py            # Class Road (đường)
│   ├── tree.py            # Class Tree (cây)
│   └── car.py             # Class Car (xe hơi)
│
├── utils/                 # Module tiện ích
│   ├── __init__.py
│   └── helpers.py         # Hàm hỗ trợ (tạo thành phố ngẫu nhiên, v.v.)
│
├── requirements.txt       # Danh sách thư viện cần thiết
└── README.md             # File này
```

## Hướng dẫn sử dụng

### Điều khiển bàn phím
- **Space**: Tạm dừng/tiếp tục hoạt ảnh
- **R**: Tạo lại thành phố ngẫu nhiên
- **1**: Chuyển sang góc nhìn từ trên
- **2**: Chuyển sang góc nhìn mặt đường
- **3**: Chuyển sang góc nhìn 45 độ
- **+/-**: Zoom in/out
- **ESC**: Thoát chương trình

### Điều khiển chuột
- **Kéo chuột trái**: Xoay camera
- **Con lăn chuột**: Zoom in/out

### Giao diện điều khiển
Cửa sổ GUI cho phép:
- Bật/tắt hoạt ảnh
- Điều chỉnh tốc độ xe (0.0 - 3.0x)
- Chọn góc nhìn nhanh
- Tạo thành phố mới

## Công nghệ sử dụng

- **Python**: Ngôn ngữ lập trình chính
- **PyOpenGL**: Thư viện đồ họa 3D
- **Pygame**: Xử lý cửa sổ và sự kiện
- **Tkinter**: Tạo giao diện điều khiển
- **NumPy**: Tính toán vector và ma trận

## Tác giả
Nhóm sinh viên môn Đồ Họa Máy Tính

## Giấy phép
Dự án mã nguồn mở cho mục đích học tập
