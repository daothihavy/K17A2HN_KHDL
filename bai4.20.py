

# Đọc file CSV và tạo DataFrame
euro12 = pd.read_csv("euro12.csv")

# In kiểu dữ liệu, kích thước, và danh sách các cột
print("Type:", type(euro12))
print("Shape:", euro12.shape)
print("Columns:", euro12.columns)

# 1. In giá trị cột Goals
print("\nCột Goals:")
print(euro12["Goals"])


# 2. Có bao nhiêu đội tham gia Euro 2012?
num_teams = euro12["Team"].nunique()
print("\nSố đội tham gia Euro 2012:", num_teams)

# 3. In thông tin của Euro2012
print("\nThông tin chi tiết của Euro2012:")
print(euro12.info())

# 4. Tạo DataFrame mới chỉ chứa 3 cột: 'Team', 'Yellow Cards', 'Red Cards'
discipline = euro12[["Team", "Yellow Cards", "Red Cards"]]

# 5. Sắp xếp discipline giảm dần theo 'Red Cards' và sau đó 'Yellow Cards'
discipline_sorted = discipline.sort_values(by=["Red Cards", "Yellow Cards"], ascending=False)
print("\nDiscipline DataFrame sau khi sắp xếp:")
print(discipline_sorted)

# 6. a) Tính trung bình Yellow Cards
avg_yellow_cards = euro12["Yellow Cards"].mean()
print("\nTrung bình Yellow Cards:", avg_yellow_cards)

# 6. b) Lọc các đội đã ghi hơn 6 bàn thắng
teams_more_than_6_goals = euro12[euro12["Goals"] > 6]
print("\nCác đội ghi hơn 6 bàn thắng:")
print(teams_more_than_6_goals)

# 7. In các đội mà tên bắt đầu bằng 'G'
teams_starting_with_g = euro12[euro12["Team"].str.startswith("G")]
print("\nCác đội bắt đầu bằng chữ 'G':")
print(teams_starting_with_g)

# 8. In 7 cột đầu của euro12
print("\n7 cột đầu của euro12:")
print(euro12.iloc[:, :7])

# 9. In tất cả các cột, trừ 3 cột cuối
print("\nTất cả các cột trừ 3 cột cuối:")
print(euro12.iloc[:, :-3])

# 10. In các cột Team, Goals, Shooting Accuracy, Yellow Cards, Red Cards
print("\nCác cột: Team, Goals, Shooting Accuracy, Yellow Cards, Red Cards:")
print(euro12[["Team", "Goals", "Shooting Accuracy", "Yellow Cards", "Red Cards"]])

# 11. In các cột Team và Shooting Accuracy của 'England', 'Italy', 'Russia'
selected_teams = euro12[euro12["Team"].isin(["England", "Italy", "Russia"])]
print("\nCột Team và Shooting Accuracy của England, Italy, Russia:")
print(selected_teams[["Team", "Shooting Accuracy"]])
