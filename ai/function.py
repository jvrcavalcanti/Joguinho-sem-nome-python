def d_two_points(x1, x2, y1, y2):
    cat1 = (x1 - x2) ** 2
    cat2 = (y1 - y2) ** 2
    return (cat1 + cat2) * 1 / 2

if __name__ == "__main__":
    print(d_two_points(2, 0, 1, 1))