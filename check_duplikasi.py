def check_duplikasi(data):
    duplikat = set()
    for item in data:
        if data.count(item) > 1:
            duplikat.add(item)
    return list(duplikat)


data = [1, 2, 3, 2, 4, 1, 5]

print(check_duplikasi(data))
