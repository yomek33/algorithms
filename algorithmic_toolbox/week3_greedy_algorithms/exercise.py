# 質問 1
# Distribute 60 black balls among 10 boxes so that every two boxes have
# different number of balls (you can put 0 balls in some box if you want
# to). Fill in numbers of black balls in each box below.
def BallsinBoxes(num):
    box = []
    balls_left = num
    for i in range(10):
        a = min(balls_left, 10 - i)
        box.append(a)
        balls_left -= a
    return box


balls_60 = 60
print(BallsinBoxes(balls_60))
