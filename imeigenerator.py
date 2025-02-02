# Written by Jeff Steveanus
# Date: 2024-10-20
#
# Usage:
# python imeigenerator.py --tac <8 digits> --total <total generated imei>
# Example: python imeigenerator.py --tac 12345678 --total 10

import random
import argparse

def calculate_luhn(imei_partial):
    imei_digits = [int(d) for d in str(imei_partial)]
    total_sum = 0

    for i in range(14):
        digit = imei_digits[i]
        if i % 2 == 1:
            doubled = digit * 2
            if doubled > 9:
                total_sum += doubled - 9
            else:
                total_sum += doubled
        else:
            total_sum += digit

    check_digit = (10 - (total_sum % 10)) % 10
    return check_digit

def generate_imei(tac):
    serial_number = f"{random.randint(0, 999999):06d}"
    imei_partial = tac + serial_number
    checksum = calculate_luhn(imei_partial)
    return f"{imei_partial}{checksum}"

def main():
    parser = argparse.ArgumentParser(description="Generate valid IMEI numbers based on TAC.")
    parser.add_argument('--tac', type=str, required=True, help="TAC number (8 digits)")
    parser.add_argument('--total', type=int, required=True, help="Total number of IMEI numbers to generate")
    
    args = parser.parse_args()
    
    tac = args.tac
    total = args.total
    
    if len(tac) != 8 or not tac.isdigit():
        print("Error: TAC must be an 8-digit number.")
        return
    
    imeis = [generate_imei(tac) for _ in range(total)]
    for imei in imeis:
        print(imei)

if __name__ == "__main__":
    main()
