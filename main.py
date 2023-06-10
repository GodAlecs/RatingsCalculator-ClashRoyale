def calc_ratings(win_rate):
    number = (win_rate / 100) * (2000 - 1200) + 1200
    return int(number)

win_rate = int(input("Enter the win rate percentage: "))
ratings = calc_ratings(win_rate)
print("Your ratings: " + str(ratings))