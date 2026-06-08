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

## References

- [EFF Diceware Guide](https://www.eff.org/dice)
- [EFF Diceware PDF](https://www.eff.org/files/2025/08/19/diceware.pdf)
- [EFF Large Wordlist](https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt)
- [EFF Short Wordlist](https://www.eff.org/files/2016/09/08/eff_short_wordlist_2_0.txt)
- [EFF Wordlist Methodology](https://www.eff.org/wordlist)

## How It Works

1. Generate secure dice rolls.
2. Convert rolls into Diceware codes.
3. Map codes to EFF words.
4. Build a passphrase.

## Compile

```shell
gcc dicegen.cpp -o dicegen.exe
```

## Password Managers

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
