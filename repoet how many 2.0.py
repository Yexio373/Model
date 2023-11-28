import sys

if __name__ == '__main__':
    args = sys.argv[1:]
    shortest_arg = sorted(args, key=len)[0]
    print(f"The shortest argument is: {shortest_arg}")