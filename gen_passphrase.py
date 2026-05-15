import subprocess
import argparse
import os
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

BINARY = (
    os.path.join(BASE_DIR, "dicegen.exe")
    if os.name == "nt"
    else os.path.join(BASE_DIR, "dicegen")
)

WORDLISTS = {
    4: os.path.join(BASE_DIR, "eff_short_wordlist_2_0.txt"),
    5: os.path.join(BASE_DIR, "eff_large_wordlist.txt"),
}


def error(message):
    print(f"[ERROR] {message}")
    sys.exit(1)


def load_wordlist(path):

    words = {}

    try:

        with open(path, "r", encoding="utf-8") as f:

            for line in f:

                code, word = line.strip().split(maxsplit=1)

                words[code] = word

    except FileNotFoundError:
        error(f"Wordlist not found: {path}")

    except Exception as e:
        error(f"Failed loading wordlist: {e}")

    return words


def get_code(width):

    try:

        result = subprocess.check_output(
            [BINARY, str(width)],
            stderr=subprocess.STDOUT
        )

        return result.decode().strip()

    except FileNotFoundError:
        error(f"RNG binary not found: {BINARY}")

    except subprocess.CalledProcessError as e:
        error(e.output.decode(errors="ignore"))

    except Exception as e:
        error(f"Failed running RNG binary: {e}")


def main():

    parser = argparse.ArgumentParser(
        description="Secure Diceware passphrase generator"
    )

    parser.add_argument(
        "-w",
        type=int,
        default=5,
        choices=[4, 5],
        help="4 = short list, 5 = large list"
    )

    parser.add_argument(
        "-n",
        type=int,
        default=6,
        help="number of words"
    )

    args = parser.parse_args()

    if args.n <= 0:
        error("Number of words must be greater than 0")

    if not os.path.isfile(BINARY):
        error(f"Missing RNG binary: {BINARY}")

    wordlist_path = WORDLISTS[args.w]

    if not os.path.isfile(wordlist_path):
        error(f"Missing wordlist: {wordlist_path}")

    wordlist = load_wordlist(wordlist_path)

    words = []

    print("\nGenerated values:\n")

    for _ in range(args.n):

        code = get_code(args.w)

        word = wordlist.get(code, "missing")

        print(f"{code} -> {word}")

        words.append(word)

    print("\nPassphrase:\n")

    print("-".join(words))


if __name__ == "__main__":
    main()