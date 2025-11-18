# Hướng dẫn cài đặt trên Windows

## Yêu cầu
- Windows 10 hoặc Windows 11
- Python 3.7 trở lên (khuyến nghị Python 3.10 hoặc 3.11)

## Các bước cài đặt

### Bước 1: Cài đặt Python
1. Tải Python từ https://www.python.org/downloads/
2. Chạy installer và **nhớ tích chọn "Add Python to PATH"**
3. Kiểm tra cài đặt bằng cách mở Command Prompt và gõ:
   ```cmd
   python --version
   ```

### Bước 2: Clone hoặc tải project
```cmd
git clone https://github.com/Jade2308/3D-City-Simulation.git
cd 3D-City-Simulation
```

Hoặc tải file ZIP từ GitHub và giải nén.

### Bước 3: Cài đặt các thư viện cần thiết
Mở Command Prompt tại thư mục project và chạy:
```cmd
pip install -r requirements.txt
```

**Lưu ý**: Nếu gặp lỗi với PyOpenGL, hãy thử:
```cmd
pip install --upgrade pip
pip install PyOpenGL PyOpenGL_accelerate
pip install pygame numpy
```

### Bước 4: Chạy chương trình
```cmd
python main.py
```

## Xử lý lỗi thường gặp

### Lỗi: "python is not recognized"
- Cài lại Python và nhớ tích "Add Python to PATH"
- Hoặc thử dùng `py` thay vì `python`:
  ```cmd
  py main.py
  ```

### Lỗi: "No module named ..."
- Chạy lại lệnh cài đặt:
  ```cmd
  pip install -r requirements.txt
  ```

### Lỗi: "Failed to initialize OpenGL"
- Cập nhật driver card màn hình
- Đảm bảo hệ thống hỗ trợ OpenGL (hầu hết Windows đều hỗ trợ)

### Lỗi: pygame window không hiển thị
- Kiểm tra không có ứng dụng nào khác đang chiếm cổng hiển thị
- Thử chạy với quyền Administrator

## Kiểm tra cài đặt
Chạy script kiểm tra:
```cmd
python test_structure.py
```

Nếu tất cả đều hiển thị ✓, nghĩa là cài đặt thành công!

## Hỗ trợ
Nếu gặp vấn đề, hãy:
1. Kiểm tra phiên bản Python: `python --version`
2. Kiểm tra các package đã cài: `pip list`
3. Đảm bảo đang ở đúng thư mục project
