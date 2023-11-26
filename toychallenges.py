def convert_to_24_hour(hour, minute, period):
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0

    return f"{hour:02d}{minute:02d}"



def two_positive(a, b, c):
    positive_count = 0

    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    return positive_count == 2

def solve(word):
    consonant_values = [ord(char) - ord('a') + 1 for char in word if char not in 'aeiou']
    return sum(consonant_values)
# Test for Challenge 1
print(convert_to_24_hour(8, 30, "am"))  # Expected output: "0830"
print(convert_to_24_hour(8, 30, "pm"))  # Expected output: "2030"

# Test for Challenge 2
print(two_positive(2, 4, -3))  # Expected output: True
print(two_positive(-4, 6, 8))  # Expected output: True
print(two_positive(4, -6, 9))  # Expected output: True
print(two_positive(-4, 6, 0))  # Expected output: False
print(two_positive(4, 6, 10))  # Expected output: False
print(two_positive(-14, -3, -4))  # Expected output: False

# Test for Challenge 3
print(solve("zodiacs"))  # Expected output: 26
print(solve("strength"))  # Expected output: 57
