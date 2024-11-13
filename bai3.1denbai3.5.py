### Bài 3.1
import numpy as np

# Lấy phiên bản NumPy hiện tại
print("Phiên bản NumPy hiện tại:", np.__version__)

# Tạo một mảng NumPy mẫu để hiển thị cấu trúc của nó
arr = np.array([1, 2, 3, 4, 5])
print("\nMảng mẫu:", arr)

# Kiểm tra kiểu dữ liệu của mảng
print("Kiểu dữ liệu của mảng:", arr.dtype)

# Kiểm tra kích thước của mảng
print("Kích thước của mảng:", arr.shape)

# Kiểm tra số chiều của mảng
print("Số chiều của mảng:", arr.ndim)

# Kiểm tra kích thước bộ nhớ của mảng
print("Kích thước bộ nhớ của mỗi phần tử (bytes):", arr.itemsize)
print("Kích thước toàn bộ mảng (bytes):", arr.nbytes)


### Bài 3.2
import numpy as np

# Câu 1:
arr = np.arange(10)
print("Mảng arr:", arr)
print("Kiểu dữ liệu của arr:", arr.dtype)
print("Kích thước của arr:", arr.shape)

# Câu 2: 
arr_odd = arr[arr % 2 != 0] 
arr_even = arr[arr % 2 == 0]  
print("Mảng arr_odd (phần tử lẻ):", arr_odd)
print("Mảng arr_even (phần tử chẵn):", arr_even)

# Câu 3: 
arr_update_1 = arr.copy()
arr_update_1[arr_update_1 % 2 != 0] = 100
print("Mảng arr_update_1:", arr_update_1)



### Bài 3.3
import numpy as np

# Khởi tạo các mảng arr_a và arr_b
arr_a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
arr_b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

# Câu 1: 
arr_c = np.intersect1d(arr_a, arr_b)
print("Mảng arr_c (các phần tử xuất hiện ở cả arr_a và arr_b):", arr_c)

# Câu 2:
arr_d = np.setdiff1d(arr_a, arr_b)
print("Mảng arr_d (các phần tử chỉ xuất hiện ở arr_a):", arr_d)

# Câu 3:
arr_e = np.array([2, 6, 1, 9, 3, 27, 8, 6, 25, 16])
arr_f = arr_e[arr_e % 5 == 0]
print("Mảng arr_f (các phần tử chia hết cho 5 từ arr_e):", arr_f)


### Bài 3.4
import numpy as np

# Câu 1: 
arr_zeros = np.zeros(10, dtype=int)
arr_zeros[5] = 1
print("Mảng arr_zeros sau khi cập nhật:", arr_zeros)

# Câu 2: 
arr_h = np.arange(10, 25)
print("Mảng arr_h theo thứ tự đảo ngược:", arr_h[::-1])

# Câu 3:
arr_k = np.array([1, 2, 0, 8, 2, 0, 1, 3, 0, 5, 0])
arr_1 = arr_k[arr_k != 0]
print("Mảng arr_1 (chỉ chứa các phần tử khác 0):", arr_1)

# Câu 4: 
arr_1 = np.append(arr_1, [10, 20])
print("Mảng sau khi thêm 10 và 20 vào cuối:", arr_1)

# Câu 5: 
arr_1 = np.insert(arr_1, 5, 100)
print("Mảng sau khi thêm 100 vào vị trí index 5:", arr_1)

# Câu 6:
arr_1 = np.delete(arr_1, [0, 1, 2])
print("Mảng sau khi xóa các phần tử tại index 0, 1, 2:", arr_1)


### Bài 3.5
import numpy as np

# Đọc dữ liệu từ các tập tin vào list
height = []
weight = []

# Giả sử bạn đã có dữ liệu từ các tập tin heights_1.txt và weights_1.txt
with open("heights_1.txt", "r") as file:
    height = [int(line.strip()) for line in file.readlines()]

with open("weights_1.txt", "r") as file:
    weight = [int(line.strip()) for line in file.readlines()]

# 1. Tạo numpy array arr_height từ list height.
arr_height = np.array(height)

# 2. Tạo numpy array arr_weight từ list weight.
arr_weight = np.array(weight)

# 3. Quy đổi từ inch sang m
conversion_factor_inch_to_m = 0.0254
arr_height_m = arr_height * conversion_factor_inch_to_m

# 4. Quy đổi từ pound sang kg
conversion_factor_pound_to_kg = 0.453592
arr_weight_kg = arr_weight * conversion_factor_pound_to_kg

# 5. Tính BMI
arr_bmi = arr_weight_kg / (arr_height_m ** 2)

# 6. Giá trị cân nặng ở vị trí index = 50 trong arr_weight_kg
weight_at_index_50 = arr_weight_kg[50]

# 7. Tạo arr_height_m_100 gồm các phần tử có vị trí index từ 100 đến 110
arr_height_m_100 = arr_height_m[100:111]

# 8. Các cầu thủ có BMI < 21
players_with_bmi_less_than_21 = arr_bmi[arr_bmi < 21]

# 9. Chiều cao và cân nặng trung bình
average_height = np.mean(arr_height_m)
average_weight = np.mean(arr_weight_kg)

# 10. Chiều cao và cân nặng lớn nhất
max_height = np.max(arr_height_m)
max_weight = np.max(arr_weight_kg)

# 11. Chiều cao và cân nặng nhỏ nhất
min_height = np.min(arr_height_m)
min_weight = np.min(arr_weight_kg)

# Hiển thị kết quả
print(f"Cân nặng tại index 50: {weight_at_index_50:.2f} kg")
print(f"Chiều cao từ index 100 đến 110: {arr_height_m_100}")
print(f"Các cầu thủ có BMI < 21: {players_with_bmi_less_than_21}")
print(f"Chiều cao trung bình: {average_height:.2f} m")
print(f"Cân nặng trung bình: {average_weight:.2f} kg")
print(f"Chiều cao lớn nhất: {max_height:.2f} m")
print(f"Cân nặng lớn nhất: {max_weight:.2f} kg")
print(f"Chiều cao nhỏ nhất: {min_height:.2f} m")
print(f"Cân nặng nhỏ nhất: {min_weight:.2f} kg")