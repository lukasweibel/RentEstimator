import re

def extract_zip_code(text):
    # Regular expression pattern for Swiss zip codes: 4 digits
    pattern = r'\b\d{4}\b'
    # Find the first match in the text
    match = re.search(pattern, text)
    if match:
        return int(match.group(0))  # Return the matched zip code
    return None  # Return None if no zip code is found

def extract_number(text):
    # Split the text by spaces
    parts = text.split()
    # Look for the part that contains the digit(s) right after "CHF"
    for part in parts:
        if part.isdigit() or (part[0].isdigit() and any(char.isdigit() for char in part[1:])):
            # Once found, remove any non-digit characters and convert to an integer
            amount = int(''.join(filter(str.isdigit, part)))
            return amount
    return None

def mixed_number_to_decimal(text):
    # Mapping of common fraction characters to their decimal equivalents
    fraction_to_decimal = {
        '½': 0.5,
        '⅓': 1/3,
        '⅔': 2/3,
        '¼': 0.25,
        '¾': 0.75,
        '⅕': 0.2,
        '⅖': 0.4,
        '⅗': 0.6,
        '⅘': 0.8,
        '⅙': 1/6,
        '⅚': 5/6,
        '⅛': 0.125,
        '⅜': 0.375,
        '⅝': 0.625,
        '⅞': 0.875,
    }

    # Split the input text by space
    parts = text.split()
    
    # Initialize the decimal number with the integral part if present
    decimal_number = float(parts[0]) if parts[0].isdigit() else 0.0
    
    # If there is a fractional part, add its decimal equivalent
    if len(parts) > 1 and parts[1] in fraction_to_decimal:
        decimal_number += fraction_to_decimal[parts[1]]
    
    return decimal_number




