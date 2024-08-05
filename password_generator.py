import random
import string
import math
import time

def generate_password(length=12, use_upper=True, use_numbers=True, use_special=True):
    """Generate a random password."""
    
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_upper else ''
    numbers = string.digits if use_numbers else ''
    special_chars = string.punctuation if use_special else ''

    # Combine all character sets
    all_chars = lowercase + uppercase + numbers + special_chars

    if not all_chars:
        raise ValueError("At least one character set must be enabled")

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

def calculate_entropy(password):
    """Calculate the entropy of the password."""
    charset_size = 0
    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(c in string.punctuation for c in password):
        charset_size += 32

    entropy = len(password) * math.log2(charset_size)
    return entropy

def estimate_crack_time(entropy):
    """Estimate crack time based on entropy."""
    attempts_per_second = 1e12  # 1 trillion attempts per second (hypothetical)
    seconds_to_crack = 2**entropy / attempts_per_second
    
    # Convert to a more readable format
    time_units = [
        ('years', 60 * 60 * 24 * 365),
        ('days', 60 * 60 * 24),
        ('hours', 60 * 60),
        ('minutes', 60),
        ('seconds', 1)
    ]
    
    for unit, seconds_in_unit in time_units:
        if seconds_to_crack >= seconds_in_unit:
            return f"{seconds_to_crack / seconds_in_unit:.2f} {unit}"

    return "Less than a second"

def main():
    """Main function to execute the password generator."""
    print("Welcome to the Password Generator")
    length = int(input("Enter the desired length of the password: "))
    use_upper = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
    
    password = generate_password(length, use_upper, use_numbers, use_special)
    entropy = calculate_entropy(password)
    crack_time = estimate_crack_time(entropy)
    
    print(f"Generated Password: {password}")
    print(f"Password Strength (Entropy): {entropy:.2f} bits")
    print(f"Estimated Time to Crack: {crack_time}")

if __name__ == "__main__":
    main()
