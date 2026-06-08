import sys
import argparse
import secrets
from pathlib import Path

def get_secure_code(width: int) -> str:
    """Generates a diceware code of the specified width using uniform RNG."""
    return "".join(str(secrets.randbelow(6) + 1) for _ in range(width))

def load_wordlist(path: Path) -> dict:
    """Loads and validates wordlist; ignores comments and empty lines."""
    words = {}
    if not path.exists():
        raise FileNotFoundError(f"Wordlist not found: {path.absolute()}")
    
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split(maxsplit=1)
            if len(parts) == 2:
                words[parts[0]] = parts[1]
    return words

def main():
    parser = argparse.ArgumentParser(description="Secure Diceware generator")
    parser.add_argument('-w', '--width', type=int, choices=[4, 5], default=5)
    parser.add_argument('-n', '--num-words', type=int, default=7)
    parser.add_argument('-s', '--sep', default=' ')
    parser.add_argument('-q', '--quiet', action='store_true')
    args = parser.parse_args()

    # Resolve wordlist path
    filename = "eff_short_wordlist_2_0.txt" if args.width == 4 else "eff_large_wordlist.txt"
    wordlist = load_wordlist(Path(__file__).resolve().parent / filename)

    # Generate results
    results = []
    for _ in range(args.num_words):
        code = get_secure_code(args.width)
        word = wordlist.get(code)
        if not word:
            print(f"[FATAL ERROR] Code {code} missing in wordlist.", file=sys.stderr)
            return 1
        results.append((code, word))

    # Output
    passphrase = args.sep.join(word for _, word in results)
    
    if not args.quiet:
        for code, word in results:
            print(f"{code} -> {word}")
        print(f"\nPassphrase:\n{passphrase}")
    else:
        print(passphrase)

if __name__ == '__main__':
    main()