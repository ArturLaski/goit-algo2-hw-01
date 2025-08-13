my_list = [10, 1, 84, 65, 5, 2, 45, 89, 11, 3, 9]


def find_min_max(arr):
    # Przypadek bazowy: tablica z jednym elementem
    if len(arr) == 1:
        return (arr[0], arr[0])

    # Przypadek bazowy: tablica z dwoma elementami
    if len(arr) == 2:
        return (min(arr[0], arr[1]), max(arr[0], arr[1]))

    # Znajdujemy środek tablicy
    mid = len(arr) // 2

    # Rekurencyjnie znajdujemy min/max dla lewej i prawej części
    left_min, left_max = find_min_max(arr[:mid])   # Lewa połowa tablicy
    right_min, right_max = find_min_max(arr[mid:]) # Prawa połowa tablicy

    # Zwracamy ogólny minimum i maksimum
    return (min(left_min, right_min), max(left_max, right_max))


if __name__ == "__main__":
    print(find_min_max(my_list))
