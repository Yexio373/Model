import sys

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0:
        print("No temperature readings provided.")
    else:
        temps = list(map(float, args))
        print(f"Maximum temperature: {max(temps)}")
        print(f"Minimum temperature: {min(temps)}")
        print(f"Average temperature: {sum(temps) / len(temps)}")