from time import sleep
import argparse
import pyautogui


def write_string():
    pyautogui.write(args.user_string, interval=args.delay)


def main():
    print(f'String "{args.user_string}" will be typed in: ')
    for i in reversed(range(args.wait)):
        print(f"{i + 1}", end=" ")
        sleep(1)
    print("TYPING...")
    write_string()
    print("Done!")
    exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--string", dest="user_string",
                        help="String to type", type=str, required=True)
    parser.add_argument("-w", "--wait", dest="wait",
                        help="Wait time in seconds (default: 5)", type=int, default=5)
    parser.add_argument("-d", "--delay", dest="delay",
                        help="Delay between letters in seconds (default: 0)", type=int, default=0)
    args = parser.parse_args()
    main()
