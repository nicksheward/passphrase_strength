# Passphrase Strength Calculator

This Python module calculates the entropy of a passphrase to decide how strong it is. It also performs validation beforehand to ensure it meets the typical requirements.

## How To Use

Install and run `passphrase_strength.py`.

You will be asked to input a passphrase. If the validation is successful, the entropy of your passphrase is displayed and if it is either weak, reasonable or strong.

## Function Explanations

### Validate

This confirms that the passphrase has at least one of each:
- Lowercase characters
- Uppercase characters
- Special characters
- Digits

This is achieved by looping through the passphrase and incrementing counters for each character type. If any of the counters remain at 0, then the passphrase is invalid.

### Entropy

This calculates the entropy of the passphrase using the passphrase length, size of the character pool and log base 2. The size of the character pool is guaranteed to be 95 due to validation of the passphrase for each character type.

The entropy value is then used to display how strong the passphrase is using SSH's recommendations.

## References

- **Password Special Characters** - OWASP. Available at: https://owasp.org/www-community/password-special-characters
- **How complex does a passphrase need to be?** - SSH. Available at: https://www.ssh.com/academy/ssh/passphrase-generator#how-complex-does-a-passphrase-need-to-be
