# Secure Diceware Passphrase Generator

A cross-platform Diceware passphrase generator using:

* Cryptographically secure randomness (`secrets`)
* EFF Diceware wordlists
* Pure Python implementation (no dependencies)

Supports:

* Linux
* Windows
* macOS

Based on the Diceware methodology from the Electronic Frontier Foundation (EFF).

## How It Works

1. Generates cryptographically secure “dice rolls” (1–6)
2. Builds a numeric Diceware key
3. Maps keys to words from an EFF wordlist
4. Joins words into a passphrase
5. (Optional) estimates entropy

## Usage

```bash
python dicegen.py
```

### Options

| Flag     | Description                        |                                      |
| -------- | ---------------------------------- | ------------------------------------ |
| `-w 4    | 5`                                 | Wordlist type (4 = short, 5 = large) |
| `-n N`   | Number of words (default: 7)       |                                      |
| `-s SEP` | Word separator (default: space)    |                                      |
| `-q`     | Quiet mode (print only passphrase) |                                      |

## Example Output

```text
4 5 2 1 3 -> lunar
6 1 5 4 2 -> canyon
...
Passphrase:
lunar canyon velvet orbit fossil nectar
```

## Security Model

This generator assumes:

* OS-provided cryptographically secure randomness
* Uniform selection via `secrets`
* Full EFF wordlist coverage

## Why Diceware?

Diceware passphrases are designed for:

* High entropy with memorability
* Resistance to brute-force attacks
* Easier human recall than random strings

## Wordlists

Official EFF lists:

* [https://www.eff.org/dice](https://www.eff.org/dice)
* [https://www.eff.org/files/2025/08/19/diceware.pdf](https://www.eff.org/files/2025/08/19/diceware.pdf)
* [https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt](https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt)
* [https://www.eff.org/files/2016/09/08/eff_short_wordlist_2_0.txt](https://www.eff.org/files/2016/09/08/eff_short_wordlist_2_0.txt)
* [https://www.eff.org/wordlist](https://www.eff.org/wordlist)

## Installation Notes

Place wordlists in the same directory as the script:

```text
eff_large_wordlist.txt
eff_short_wordlist_2_0.txt
```
