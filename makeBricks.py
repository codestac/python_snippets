def make_bricks(small, big, goal):
    #failure 1 - not enough bricks
    if (goal > 5*big + small):
        return False
    #failure 2 - not enough small bricks
    elif (goal > 5%big):
        return False
			
    return True

print(make_bricks(5, 6, 12))