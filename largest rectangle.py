#посмотреть как это работает
# @param height, a list of integer
# @return an integer
def largest_histogram(height):
    increasing, area, i = [], 0, 0
    while i <= len(height):
        if not increasing or (i < len(height) and height[i] > height[increasing[-1]]):
            increasing.append(i)
            i += 1
        else:
            last = increasing.pop()
            if not increasing:
                area = max(area, height[last] * i)
            else:
                area = max(area, height[last] * (i - increasing[-1] - 1 ))
    return area


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert largest_histogram([5]) == 5, "one is always the biggest"
    #assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
   # assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
   # assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")
