def hamming_encode_4bit(data):
    """
    Encode 4-bit data using Hamming (7,4) code.
    """
    if len(data) != 4 or not all(bit in "01" for bit in data):
        raise ValueError("Input must be a 4-bit binary string.")

    d = [int(bit) for bit in data]  # Convert string to list of integers

    # Assign data bits (d1, d2, d3, d4)
    d1, d2, d3, d4 = d

    # Calculate parity bits
    p1 = d1 ^ d2 ^ d4  # Parity for bits 1, 2, 4
    p2 = d1 ^ d3 ^ d4  # Parity for bits 1, 3, 4
    p3 = d2 ^ d3 ^ d4  # Parity for bits 2, 3, 4

    # Encoded data: p1, p2, d1, p3, d2, d3, d4
    encoded = [p1, p2, d1, p3, d2, d3, d4]
    return ''.join(map(str, encoded))


data=input("Enter data: ")

print(hamming_encode_4bit(data))
