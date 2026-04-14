import sleep_sort

def main():
    print("Enter a list of integers seperated by a space to be sorted (WARNING: large numbers will take a while):")
    nums = list(map(int, input("").split()))
    sorted = sleep_sort.sort(nums)
    print(f"Your sorted list is: {sorted}")

if __name__ == "__main__":
    main()
