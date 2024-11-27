def calculate_parity_bits(hamming_code):
    """
    Calculate the parity check for error detection.
    :param hamming_code: List of 7 integers (0 or 1) representing the Hamming code.
    :return: The position of the error (0 means no error).
    """
    p1 = hamming_code[0] ^ hamming_code[2] ^ hamming_code[4] ^ hamming_code[6]  # Parity 1
    p2 = hamming_code[1] ^ hamming_code[2] ^ hamming_code[5] ^ hamming_code[6]  # Parity 2
    p4 = hamming_code[3] ^ hamming_code[4] ^ hamming_code[5] ^ hamming_code[6]  # Parity 4

    # Combine parity bits to find the error position
    error_position = (p4 << 2) | (p2 << 1) | p1
    return error_position


def correct_error(hamming_code, error_position):
    """
    Correct a single-bit error in the Hamming code.
    :param hamming_code: List of 7 integers (0 or 1) representing the Hamming code.
    :param error_position: Position of the error (1-indexed, 0 means no error).
    :return: Corrected Hamming code.
    """
    if error_position > 0:
        print(f"Error detected at position {error_position}. Correcting...")
        hamming_code[error_position - 1] ^= 1  # Flip the bit at the error position
    else:
        print("No error detected.")
    return hamming_code


def extract_data_bits(hamming_code):
    """
    Extract the 4 data bits from the 7-bit Hamming code.
    :param hamming_code: List of 7 integers (0 or 1) representing the Hamming code.
    :return: List of 4 integers representing the original data bits.
    """
    return [hamming_code[2], hamming_code[4], hamming_code[5], hamming_code[6]]


def main():
    # Input a 7-bit Hamming code
    print("Enter the 7-bit Hamming code (0 or 1) , Enter Space-Seperated Input: ")
    hamming_code = list(map(int, input().strip().split()))
    hamming_code=hamming_code[::-1]

    if len(hamming_code) != 7 or any(bit not in [0, 1] for bit in hamming_code):
        print("Invalid input. Please enter exactly 7 bits (0 or 1).")
        return

    # Detect and correct errors
    error_position = calculate_parity_bits(hamming_code)
    corrected_code = correct_error(hamming_code, error_position)

    # Extract original data bits
    data_bits = extract_data_bits(corrected_code)

    print("Corrected Hamming Code:", corrected_code)
    print("Extracted Data Bits:", data_bits[::-1])
    


if __name__ == "__main__":
    main()
