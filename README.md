# Secure Diceware Passphrase Generator

Cross-platform Diceware passphrase generator using:

- Cryptographically secure OS randomness
- Bias-free dice generation
- EFF Diceware wordlists
- C entropy backend
- Python automation

Supports:
- Linux
- Windows

Based on the Diceware methodology recommended by the EFF.

# References

EFF Diceware Guide  
https://www.eff.org/dice

EFF Diceware PDF  
https://www.eff.org/files/2025/08/19/diceware.pdf

EFF Large Wordlist  
https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt

EFF Short Wordlist  
https://www.eff.org/files/2016/09/08/eff_short_wordlist_2_0.txt

EFF Wordlist Methodology  
https://www.eff.org/wordlist

# How It Works

1. Generate secure dice rolls.
2. Convert rolls into Diceware codes.
3. Map codes to EFF words.
4. Build a passphrase.

Example:

```text
43463 -> panoramic
21563 -> fossil
63142 -> nectar
```

Generated passphrase:

```text
panoramic-fossil-nectar
```

A 6-word passphrase using the EFF large wordlist provides approximately:

```text
~77 bits entropy
```

# Project Structure

```text
dicegen.c
gen_passphrase.py
eff_large_wordlist.txt
eff_short_wordlist_2_0.txt
```

# Security

Uses:
- Linux `getrandom()`
- Windows `BCryptGenRandom()`
- Rejection sampling to remove modulo bias
- Cryptographically secure operating system entropy

Does NOT use:
- `rand()`
- pseudo-random generators
- time-based seeds

# Compile

## Linux

```bash
gcc dicegen.c -o dicegen
```

## Windows (MinGW GCC)

```powershell
gcc dicegen.c -lbcrypt -o dicegen.exe
```

# Manual Diceware

Generate a Diceware code manually:

## Linux

```bash
./dicegen 5
```

## Windows

```powershell
.\dicegen.exe 5
```

Example output:

```text
43463
```

Look up the code in the EFF wordlist.

# Automatic Passphrase Generation

## Large EFF Wordlist

```bash
python3 gen_passphrase.py -w 5 -n 6
```

Windows:

```powershell
python gen_passphrase.py -w 5 -n 6
```

## Short EFF Wordlist

```bash
python3 gen_passphrase.py -w 4 -n 6
```

Windows:

```powershell
python gen_passphrase.py -w 4 -n 6
```

# Parameters

| Parameter | Description |
|---|---|
| `-w` | 4 = short wordlist, 5 = large wordlist |
| `-n` | Number of words |

# Recommended Settings

| Wordlist | Words |
|---|---|
| EFF Large | 6–8 |
| EFF Short | 7–9 |

# Example Output

```text
52316 -> lunar
11452 -> canyon
66125 -> velvet
34211 -> orbit
21563 -> fossil
63142 -> nectar

Passphrase:

lunar-canyon-velvet-orbit-fossil-nectar
```

Example mnemonic:

```text
A lunar canyon covered in velvet orbited a fossil filled with nectar.
```

Creating a memorable sentence or mental image can help remember long Diceware passphrases without reducing entropy.

# Password Managers

It is strongly recommended to use a password manager instead of reusing passwords or memorizing many passwords manually.

Recommended password managers:

- Bitwarden
- Proton Pass
- KeePass

Diceware passphrases work especially well as master passwords for password managers because they provide high entropy while remaining easier to remember than short complex passwords.

Example Diceware master password:

```text
lunar-canyon-velvet-orbit-fossil-nectar
```

Compared to a traditional password like:

```text
X7$qP!2zL@
```

a Diceware passphrase is:
- easier to remember
- easier to type
- harder to brute-force when sufficiently long

Using a password manager allows:
- unique passwords for every account
- secure password storage
- strong random password generation
- reduced password reuse
- safer long-term credential management

Diceware passphrases are especially useful for:
- password manager master passwords
- encryption passwords
- recovery keys
- offline vault passwords
- full-disk encryption passwords

# Notes

- The C program only generates secure Diceware codes.
- The Python script handles word lookup and passphrase generation.
- All randomness originates from the operating system cryptographic RNG.
- Modulo bias is removed using rejection sampling.

# License

MIT License