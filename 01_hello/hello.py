import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description="Say hello"
    )
    parser.add_argument(
        "-n", "--name",
        default="World",
        help="Name to greet"
    )
    return parser.parse_args()


def main():
    args = get_args()
    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()