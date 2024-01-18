from PIL import Image

def convert_image_to_binary_array(image_path):
    # Mở ảnh
    with Image.open(image_path) as img:
        # Chuyển ảnh về dạng đen trắng
        img = img.convert('1')  # '1' cho 1-bit pixels, đen trắng

        # Tạo mảng để lưu trữ dữ liệu pixel
        binary_array = []

        # Duyệt qua từng pixel
        for y in range(img.height):
            row = []
            for x in range(img.width):
                pixel = img.getpixel((x, y))
                # Thêm 0 hoặc 1 vào mảng tùy thuộc vào màu của pixel
                row.append(0 if pixel == 255 else 1)  # 255 là trắng, 0 là đen
            binary_array.append(row)

        return binary_array

# Đường dẫn đến file ảnh QR
image_path = 'qr.png'

# Chuyển đổi và in kết quả
binary_array = convert_image_to_binary_array(image_path)
for row in binary_array:
    print(' '.join(map(str, row)))
