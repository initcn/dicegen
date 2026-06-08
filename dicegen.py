import sys
import argparse
import secrets
import math
from pathlib import Path

MINIMUM_SAFE_ENTROPY = 90.0 

def get_secure_code(width: int) -> str:
    """Generates a diceware code of the specified width using uniform RNG."""
    return "".join(str(secrets.randbelow(6) + 1) for _ in range(width))

def load_wordlist(path: Path, width: int) -> dict:
    """Loads, validates format, and verifies full coverage of the Diceware wordlist."""
    words = {}
    expected_coverage = 6 ** width
    
    if not path.exists():
        raise FileNotFoundError(f"Wordlist not found: {path.absolute()}")

    with open(path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
                
            parts = line.split(maxsplit=1)
            
            if len(parts) != 2 or not parts[1].strip():
                raise ValueError(f"Malformed entry at line {line_num}: '{line}'")
                
            code, word = parts
            if len(code) != width or not all(c in '123456' for c in code):
                raise ValueError(f"Invalid code format at line {line_num}: {code}")
            
            if code in words:
                raise ValueError(f"Duplicate code found: {code}")
                
            words[code] = word

    if len(words) != expected_coverage:
        raise ValueError(f"Incomplete wordlist coverage: Expected {expected_coverage}, got {len(words)}.")
        
    return words

def main():
    parser = argparse.ArgumentParser(
        description="Secure Diceware passphrase generator",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-w', '--width', type=int, choices=[4, 5], default=5, help="Wordlist width")
    parser.add_argument('-n', '--num-words', type=int, default=7, help="Number of words")
    parser.add_argument('-s', '--sep', default=' ', help="Passphrase word separator")
    parser.add_argument('-q', '--quiet', action='store_true', help="Output only the passphrase")

    args = parser.parse_args()

    # Resolve Wordlist locally
    filename = "eff_short_wordlist_2_0.txt" if args.width == 4 else "eff_large_wordlist.txt"
    target_path = Path(__file__).resolve().parent / filename

    try:
        wordlist = load_wordlist(target_path, args.width)
    except Exception as e:
        print(f"[FATAL ERROR] {e}", file=sys.stderr)
        return 1

    # Generate Passphrase
    words = [wordlist[get_secure_code(args.width)] for _ in range(args.num_words)]
    passphrase = args.sep.join(words)

    # Output
    if not args.quiet:
        bits_per_word = math.log2(len(wordlist))
        total_entropy = bits_per_word * args.num_words
        print(f"\nPassphrase:\n{passphrase}\n")
        print(f"[ Security: {total_entropy:.1f} bits | Wordlist size: {len(wordlist)} ]")
        
        if total_entropy < MINIMUM_SAFE_ENTROPY:
            print(f"[WARNING] Entropy below {MINIMUM_SAFE_ENTROPY} bits. Consider 8+ words for stronger offline resistance.")
        print()
    else:
        print(passphrase)

    return 0

if __name__ == '__main__':
    sys.exit(main())