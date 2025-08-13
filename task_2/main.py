my_list = [10, 1, 84, 65, 5, 2, 45, 89, 11, 3, 9]

def quick_select(arr, k):
    # Sprawdzenie poprawności danych wejściowych
    if k < 1 or k > len(arr):
        raise ValueError("ValueError - k musi być pomiędzy 1 a długością tablicy")

    if len(arr) == 1:
        return arr[0]

    # Wybór elementu pivot
    pivot = arr[len(arr) // 2]

    # Podział tablicy na 3 części
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if k <= len(left):  # k-ty element znajduje się w lewej części
        return quick_select(left, k)
    elif k > len(left) + len(middle):  # k-ty element znajduje się w prawej części
        return quick_select(right, k - len(left) - len(middle))
    else:  # k-ty element znajduje się w części środkowej
        return pivot


if __name__ == "__main__":
    # Znajdźmy np. 6-ty najmniejszy element
    print(quick_select(my_list, 6))  # To wypisze 6-ty najmniejszy element w liście
