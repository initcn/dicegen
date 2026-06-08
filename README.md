# Secure Diceware Passphrase Generator

A cross-platform Diceware passphrase generator that uses:

* Cryptographically secure randomness (`secrets`)
* Bias-free dice roll simulation
* EFF Diceware wordlists
* Deterministic entropy calculation
* Pure Python implementation (no external runtime dependencies)

Supports:

* Linux
* Windows
* macOS

Based on the Diceware methodology recommended by the Electronic Frontier Foundation (EFF).

## References

* [https://www.eff.org/dice](https://www.eff.org/dice)
* [https://www.eff.org/files/2025/08/19/diceware.pdf](https://www.eff.org/files/2025/08/19/diceware.pdf)
* [https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt](https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt)
* [https://www.eff.org/files/2016/09/08/eff_short_wordlist_2_0.txt](https://www.eff.org/files/2016/09/08/eff_short_wordlist_2_0.txt)
* [https://www.eff.org/wordlist](https://www.eff.org/wordlist)

## How It Works

1. Generate cryptographically secure random dice rolls (1–6)
2. Convert rolls into Diceware-style numeric codes
3. Map codes to words from the EFF wordlist
4. Join words into a passphrase
5. Compute theoretical entropy in bits

## Usage

```bash
python dicegen.py
```

### Options

| Flag              | Description                           |
| ----------------- | ------------------------------------- |
| `-w 4\|5`         | Select wordlist type (short or large) |
| `-n N`            | Number of words (default: 7)          |
| `--wordlist PATH` | Custom wordlist path                  |
| `-s SEP`          | Word separator (default: space)       |
| `-q`              | Quiet mode (passphrase only output)   |

## Security Model

This generator assumes:

* Cryptographically secure OS entropy sources
* Uniform random selection via `secrets`
* Full EFF wordlist coverage (no reduced entropy subsets)

### Entropy Guidance

* ~70 bits → weak / legacy baseline
* ~90 bits → recommended minimum
* 100+ bits → strong long-term resistance

**Recommendation:**
Use at least **7–8 words (EFF large list)** for strong offline attack resistance.

## Why Diceware?

Diceware passphrases are designed for:

* High entropy with memorability
* Resistance to brute-force attacks (when sufficiently long)
* Human usability compared to random character passwords

### Example

Diceware passphrase:

```text
lunar canyon velvet orbit fossil nectar
```

Traditional random password:

```text
X7$qP!2zL@
```

### Comparison

| Property             | Diceware | Random password |
| -------------------- | -------- | --------------- |
| Memorability         | High     | Low             |
| Typing ease          | High     | Low             |
| Security (long form) | High     | High            |
| Usability            | Strong   | Weak            |

## Recommended Usage

Diceware passphrases are especially suitable for:

* Password manager master passwords
* Disk encryption keys (e.g., LUKS, VeraCrypt)
* Backup recovery phrases
* Offline vault security
* High-value account protection

## Password Managers

Using a password manager is strongly recommended for day-to-day credential management.

Recommended options:

* Bitwarden
* Proton Pass
* KeePass

Password managers enable:

* Unique passwords per service
* Secure random password generation
* Protection against credential reuse
* Centralized encrypted storage

## Important Note

Diceware passphrases are not a replacement for a password manager.

They are best used for:

* **master passwords**
* **encryption keys**
* **recovery credentials**
