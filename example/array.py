N_MAX = 15

def read_array():
    n = int(input("Enter number of elements: "))
    if n > N_MAX:
        print(f"Max elements is {N_MAX}")
        n = N_MAX
    arr = []
    print("Enter elements:")
    for _ in range(n):
        arr.append(int(input()))
    return arr

def print_array(arr):
    print("Array:")
    for x in arr:
        print(x, end=" ")
    print()

if __name__ == "__main__":
    arr = read_array()
    print_array(arr)
