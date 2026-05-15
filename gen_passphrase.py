import subprocess
import argparse
import os
import sys


def load_wordlist(path):

    words = {}

    try:

        with open(path, "r", encoding="utf-8") as f:

            for line in f:

                parts = line.strip().split()

                if len(parts) >= 2:

                    code = parts[0]
                    word = parts[1]

                    words[code] = word

    except FileNotFoundError:
        print(f"[ERROR] Wordlist file not found: {path}")
        sys.exit(1)

    except PermissionError:
        print(f"[ERROR] Permission denied reading: {path}")
        sys.exit(1)

    except Exception as e:
        print(f"[ERROR] Failed to load wordlist: {e}")
        sys.exit(1)

    if not words:
        print("[ERROR] Wordlist is empty or invalid")
        sys.exit(1)

    return words


def get_code(binary, width):

    try:

        result = subprocess.check_output(
            [binary, str(width)],
            stderr=subprocess.STDOUT
        )

        code = result.decode().strip()

        return code

    except FileNotFoundError:
        print(f"[ERROR] RNG binary not found: {binary}")
        sys.exit(1)

    except PermissionError:
        print(f"[ERROR] Permission denied executing: {binary}")
        sys.exit(1)

    except subprocess.CalledProcessError as e:
        print("[ERROR] RNG binary execution failed")
        print(e.output.decode(errors="ignore"))
        sys.exit(1)

    except Exception as e:
        print(f"[ERROR] Failed running RNG binary: {e}")
        sys.exit(1)


def main():

    parser = argparse.ArgumentParser(
        description="Secure Diceware passphrase generator"
    )

    parser.add_argument(
        "-w",
        type=int,
        default=5,
        help="digits per code"
    )

    parser.add_argument(
        "-n",
        type=int,
        default=6,
        help="number of words"
    )

    parser.add_argument(
        "-source",
        required=True,
        help="wordlist file"
    )

    parser.add_argument(
        "-bin",
        default="./dicegen",
        help="C RNG binary"
    )

    args = parser.parse_args()

    # Validate width
    if args.w <= 0:
        print("[ERROR] Width must be greater than 0")
        sys.exit(1)

    # Validate word count
    if args.n <= 0:
        print("[ERROR] Number of words must be greater than 0")
        sys.exit(1)

    # Check binary exists
    if not os.path.isfile(args.bin):
        print(f"[ERROR] Binary file does not exist: {args.bin}")
        sys.exit(1)

    # Check source exists
    if not os.path.isfile(args.source):
        print(f"[ERROR] Wordlist file does not exist: {args.source}")
        sys.exit(1)

    wordlist = load_wordlist(args.source)

    passphrase = []

    print("\nGenerated values:\n")

    for _ in range(args.n):

        code = get_code(args.bin, args.w)

        print(code, end="")

        word = wordlist.get(code)

        if word:

            print(f" -> {word}")

            passphrase.append(word)

        else:

            print(" -> missing")

    if passphrase:

        print("\nPassphrase:\n")

        print(" ".join(passphrase))

    else:

        print("\n[ERROR] No valid passphrase generated")


if __name__ == "__main__":
    main()