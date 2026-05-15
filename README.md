# Secure Diceware Passphrase Generator

A cross-platform secure Diceware passphrase generator using:

- Cryptographically secure randomness
- Bias-free dice generation
- EFF Diceware wordlists
- C-based entropy generation
- Python-based passphrase generation

Supports:
- Linux
- Windows

The project follows the Diceware methodology recommended by the Electronic Frontier Foundation (EFF).

# References

EFF Diceware Guide

https://www.eff.org/dice

EFF Diceware PDF

https://www.eff.org/files/2025/08/19/diceware.pdf

EFF Large Wordlist

https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt

EFF Short Wordlist

https://www.eff.org/files/2016/09/08/eff_short_wordlist_2_0.txt

The creator of the EFF wordlists, Joseph Bonneau, has written a detailed explanation of passphrase security and the methodology used to create the EFF Diceware wordlists:

https://www.eff.org/wordlist

# How Diceware Works

For most applications, EFF recommends generating a six-word passphrase using the large EFF wordlist.

Generation method:

1. Roll five dice.
2. Record the results left to right.
3. Example:

```text
43463
```
4. Look up `43463` in the EFF wordlist.
5. You may get a word like:

```text
panoramic
```

6. Repeat the process six times.

Example passphrase:

```text
panoramic nectar precut smith banana handclap
```

This method produces approximately:

```text
2^77
```

possible combinations for a six-word passphrase using the large EFF wordlist.

This provides strong resistance against brute-force attacks.

# Project Structure

```text
dicegen.c
gen_passphrase.py
eff_large_wordlist.txt
eff_short_wordlist_2_0.txt
```

# Security Properties

This project uses:

- Linux `getrandom()`
- Windows `BCryptGenRandom()`
- Rejection sampling to remove modulo bias
- Cryptographically secure operating system entropy

This project does NOT use:

- `rand()`
- pseudo-random generators
- time-based seeding

# Compile the C RNG Generator

## Linux

Compile:

```bash
gcc dicegen.c -o dicegen
```

Run manually:

```bash
./dicegen 5
```

Example output:

```text
43463
```

## Windows (MinGW GCC)

Compile:

```bash
gcc dicegen.c -lbcrypt -o dicegen.exe
```

Run manually:

```powershell
.\dicegen.exe 5
```

Example output:

```text
43463
```

# Manual Diceware Workflow

You can use the C program manually.

Example:

```bash
./dicegen 5
```

Output:

```text
43463
```

Open the EFF wordlist and look up:

```text
43463
```

You may get:

```text
panoramic
```

Repeat six times to generate a secure passphrase.

# Automatic Passphrase Generation

The Python script automates:

- dice generation
- word lookup
- passphrase assembly

The Python script uses the C RNG binary as its entropy source.

# Python Requirements

Python 3 required.

No third-party libraries needed.

# Usage

## Large EFF Wordlist

Recommended for maximum security.

Linux:

```bash
python3 gen_passphrase.py -w 5 -n 6 -source eff_large_wordlist.txt -bin dicegen
```

Windows:

```powershell
python gen_passphrase.py -w 5 -n 6 -source eff_large_wordlist.txt -bin dicegen.exe
```

Example output:

```text
52316 -> lunar
11452 -> canyon
66125 -> velvet
34211 -> orbit
21563 -> fossil
63142 -> nectar

Passphrase:

lunar canyon velvet orbit fossil nectar
```

## Short EFF Wordlist

Uses 4 dice rolls per word.

Linux:

```bash
python3 gen_passphrase.py -w 4 -n 6 -source eff_short_wordlist_2_0.txt -bin dicegen
```

Windows:

```powershell
python gen_passphrase.py -w 4 -n 6 -source eff_short_wordlist_2_0.txt -bin dicegen.exe
```

# Parameters

| Parameter | Description |
|---|---|
| `-w` | Digits per code |
| `-n` | Number of words |
| `-source` | Wordlist file |
| `-bin` | RNG binary |

# Recommended Settings

| Wordlist | Width | Recommended Words |
|---|---|---|
| EFF Large | 5 | 6–8 |
| EFF Short | 4 | 7–9 |

# Entropy

EFF Large Wordlist:

```text
7776 words
~12.9 bits entropy per word
```

Six-word passphrase:

```text
~77 bits entropy
```

# Example Mnemonic

Example passphrase:

```text
panoramic nectar precut smith banana handclap
```

Example mnemonic:

```text
The panoramic view, as I tasted the nectar of a precut granny smith apple and banana, deserved a handclap.
```

# Notes

- The C program only generates secure dice codes.
- The Python script handles word lookup and passphrase generation.
- Keeping entropy generation separate improves simplicity and auditability.
- All randomness originates from the operating system cryptographic RNG.

# License

MIT License