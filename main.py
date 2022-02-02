
def division_by_10(number):

    if not number // 10 == 0:
        return number


if __name__ ==  "__main__":
    list_number = [1,5,23,89,11,84,5]

    results = list()
    for n in list_number:
        d= division_by_10(n)
        if d != None:
            results.append(d)

    print(results)