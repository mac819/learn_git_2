import argparse

def square_operator(x):
    return x**2

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    # parser.add_argument("echo", help="Returns the string which you feed as argument")
    # parser.add_argument("square", help="Returns the square of provided argument", type=int)
    parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true")
    args = parser.parse_args()

    if args.verbosity:
        print(args.verbosity)

    # print(square_operator(args.square))

