
def count(lst):
    order = 1
    print(order)
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            order += 1
        print order


if __name__ == "__main__":
    lst = []
    count(lst)
