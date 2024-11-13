### Bài 3.6
import numpy as np

# 1. Tạo array art có kích thước 3x3 với các giá trị True
art = np.full((3, 3), True)
print("Array art:\n", art)

# 2. Tạo array arr_ID và tạo array 2 chiều arr_2D từ nó
arr_ID = np.array([0, 12345678, 0])  # Thêm một giá trị nữa để đủ 3 cột
arr_2D = np.tile(arr_ID, (3, 1))     # Tạo kích thước 3x3
print("\nArray arr_2D ban đầu:\n", arr_2D)

# Chuyển cột 1 sang cột 3 và ngược lại
arr_2D[:, [0, 2]] = arr_2D[:, [2, 0]]
print("\nArray arr_2D sau khi đổi thứ tự cột:\n", arr_2D)


# 3. Chuyển dòng 1 sang dòng 2 và ngược lại
arr_2D[[0, 1]] = arr_2D[[1, 0]]
print("\nArray arr_2D sau khi đổi thứ tự dòng:\n", arr_2D)

# 4. Đảo ngược các dòng của arr_2D
arr_2D = arr_2D[::-1]
print("\nArray arr_2D sau khi đảo ngược các dòng:\n", arr_2D)

# 5. Đảo ngược các cột của arr_2D
arr_2D = arr_2D[:, ::-1]
print("\nArray arr_2D sau khi đảo ngược các cột:\n", arr_2D)

# 6. Kiểm tra giá trị null trong arr_2D_null
arr_2D_null = np.array([[1, 2, 3], [np.NaN, 5, 6], [7, np.NaN, 9], [4, 5, 6]])
has_nan = np.isnan(arr_2D_null).any()
print("\nArray arr_2D_null:\n", arr_2D_null)
print("Có giá trị null trong arr_2D_null không?", has_nan)

# 7. Thay thế giá trị null bằng 0
arr_2D_null[np.isnan(arr_2D_null)] = 0
print("\nArray arr_2D_null sau khi thay thế giá trị null bằng 0:\n", arr_2D_null)


#### Bài 3.7
import numpy as np

# 1. Đọc dữ liệu từ tập tin vào danh sách baseball
with open('baseball_2D.txt', 'r') as file:
    baseball = [list(map(float, line.strip().split())) for line in file]

# Tạo mảng numpy 2D từ baseball
np_baseball = np.array(baseball)

# Kiểm tra kiểu dữ liệu và kích thước của np_baseball
print("Dữ liệu np_baseball:\n", np_baseball)
print("Kiểu dữ liệu của np_baseball:", np_baseball.dtype)
print("Kích thước của np_baseball:", np_baseball.shape)

# 2. In các giá trị của dòng thứ 50 trong np_baseball
print("\nDòng thứ 50 trong np_baseball:", np_baseball[49])

# 3. Tạo numpy array np_weight từ cột hai của np_baseball
np_weight = np_baseball[:, 1]
print("\nMảng np_weight (cột cân nặng):\n", np_weight)

# 4. Chiều cao của vận động viên thứ 124
print("\nChiều cao của vận động viên thứ 124:", np_baseball[123, 0])

# 5. Tính chiều cao trung bình và cân nặng trung bình của các cầu thủ
mean_height = np.mean(np_baseball[:, 0])
mean_weight = np.mean(np_baseball[:, 1])
print("\nChiều cao trung bình của các cầu thủ:", mean_height)
print("Cân nặng trung bình của các cầu thủ:", mean_weight)

# 6. Tính tương quan giữa chiều cao và cân nặng
correlation = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])[0, 1]
print("\nHệ số tương quan giữa chiều cao và cân nặng của các cầu thủ:", correlation)

# Nhận xét về mối tương quan
if correlation > 0:
    print("Nhận xét: Chiều cao và cân nặng có mối tương quan thuận.")
elif correlation < 0:
    print("Nhận xét: Chiều cao và cân nặng có mối tương quan nghịch.")
else:
    print("Nhận xét: Chiều cao và cân nặng không có mối tương quan.")



### Bài 3.8
import numpy as np

# 1. Đọc dữ liệu từ hai tệp heights.txt và positions.txt
with open('heights.txt', 'r') as file:
    heights = [float(line.strip()) for line in file]

with open('positions.txt', 'r') as file:
    positions = [line.strip() for line in file]

# a) Tạo numpy array np_positions từ list positions
np_positions = np.array(positions)
print("Dữ liệu np_positions:\n", np_positions)
print("Kiểu dữ liệu của np_positions:", np_positions.dtype)

# b) Tạo numpy array np_heights từ list heights
np_heights = np.array(heights)
print("\nDữ liệu np_heights:\n", np_heights)
print("Kiểu dữ liệu của np_heights:", np_heights.dtype)

# 2. Tính chiều cao trung bình của các GK
gk_heights = np_heights[np_positions == 'GK']
mean_gk_height = np.mean(gk_heights)
print("\nChiều cao trung bình của các GK:", mean_gk_height)

# 3. Tính chiều cao trung bình của những vị trí khác (Không phải là GK)
non_gk_heights = np_heights[np_positions != 'GK']
mean_non_gk_height = np.mean(non_gk_heights)
print("Chiều cao trung bình của những vị trí khác (Không phải GK):", mean_non_gk_height)

# 4. Tạo mảng dữ liệu có cấu trúc tự định nghĩa players
players = np.array(list(zip(np_positions, np_heights)), dtype=[('position', 'U5'), ('height', 'float')])
print("\nMảng players:\n", players)

# 5. Sắp mảng players theo chiều cao, tìm vị trí có chiều cao cao nhất và thấp nhất
sorted_players = np.sort(players, order='height')
print("\nMảng players sau khi sắp xếp theo height:\n", sorted_players)
print("\nVị trí có chiều cao thấp nhất:", sorted_players[0]['position'], "- Chiều cao:", sorted_players[0]['height'])
print("Vị trí có chiều cao cao nhất:", sorted_players[-1]['position'], "- Chiều cao:", sorted_players[-1]['height'])



### Bài 3.9
import pandas as pd

# Tạo data frame từ tệp CSV
euro12 = pd.read_csv('euro2012.csv')

# In kiểu dữ liệu, kích thước và danh sách các cột
print("Kiểu dữ liệu của euro12:", type(euro12))
print("Kích thước của euro12:", euro12.shape)
print("Danh sách các cột của euro12:", euro12.columns.tolist())

# 1. In giá trị cột Goals
print("\nCột Goals:\n", euro12['Goals'])

# 2. Có bao nhiêu đội tham gia Euro 2012?
num_teams = euro12['Team'].nunique()
print("\nSố đội tham gia Euro 2012:", num_teams)

# 3. In thông tin của Euro 2012
print("\nThông tin của Euro 2012:")
print(euro12.info())

# 4. Tạo data frame mới từ euro12 tên là discipline chỉ chứa các cột "Team", "Yellow Cards", "Red Cards"
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
print("\nDataFrame discipline:\n", discipline)

# 5. Sắp xếp discipline giảm dần theo 'Red Cards', 'Yellow Cards'
discipline_sorted = discipline.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=False)
print("\nDataFrame discipline sau khi sắp xếp:\n", discipline_sorted)

# 6a. Tính trung bình số thẻ vàng (Yellow Cards)
mean_yellow_cards = euro12['Yellow Cards'].mean()
print("\nTrung bình số thẻ vàng:", mean_yellow_cards)

# 6b. Lọc các đội đã ghi hơn 6 bàn thắng
teams_more_than_6_goals = euro12[euro12['Goals'] > 6]
print("\nCác đội đã ghi hơn 6 bàn thắng:\n", teams_more_than_6_goals[['Team', 'Goals']])

# 7. In các đội mà tên bắt đầu bằng 'G'
teams_start_with_G = euro12[euro12['Team'].str.startswith('G')]
print("\nCác đội có tên bắt đầu bằng 'G':\n", teams_start_with_G[['Team']])

# 8. In 7 cột đầu của euro12
print("\n7 cột đầu của euro12:\n", euro12.iloc[:, :7])

# 9. In tất cả các cột, trừ 3 cột cuối
print("\nTất cả các cột trừ 3 cột cuối:\n", euro12.iloc[:, :-3])

# 10. In các cột Team, Goals, Shooting Accuracy, Yellow Cards, Red Cards
print("\nCác cột Team, Goals, Shooting Accuracy, Yellow Cards, Red Cards:\n",
      euro12[['Team', 'Goals', 'Shooting Accuracy', 'Yellow Cards', 'Red Cards']])

# 11. In các cột 'Team', 'Shooting Accuracy' từ các đội 'England', 'Italy', 'Russia'
selected_teams = euro12[euro12['Team'].isin(['England', 'Italy', 'Russia'])]
print("\nCác cột 'Team', 'Shooting Accuracy' từ các đội 'England', 'Italy', 'Russia':\n",
      selected_teams[['Team', 'Shooting Accuracy']])