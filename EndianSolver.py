def hex_to_bytes(hex_str):
    """Convert a hex string to bytes."""
    return bytes.fromhex(hex_str)

def bytes_to_hex(byte_data):
    """Convert bytes to a hex string."""
    return byte_data.hex().upper()

def little_endian_to_big_endian(little_endian_hex):
    """Convert little-endian hex to big-endian hex."""
    byte_data = hex_to_bytes(little_endian_hex)
    return bytes_to_hex(byte_data[::-1])

def big_endian_to_little_endian(big_endian_hex):
    """Convert big-endian hex to little-endian hex."""
    byte_data = hex_to_bytes(big_endian_hex)
    return bytes_to_hex(byte_data[::-1])

def string_to_little_endian(word):
    """Convert a string to little-endian hex."""
    return bytes_to_hex(word.encode()[::-1])

def string_to_big_endian(word):
    """Convert a string to big-endian hex."""
    return bytes_to_hex(word.encode())

def is_valid_hex(hex_str):
    """Check if the string is a valid hexadecimal string."""
    try:
        int(hex_str, 16)
        return True
    except ValueError:
        return False

def main():
    print("Endian Converter")
    print("1. Convert Little Endian Hex to Big Endian Hex")
    print("2. Convert Big Endian Hex to Little Endian Hex")
    print("3. Convert String to Little Endian Hex")
    print("4. Convert String to Big Endian Hex")
    
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        little_endian_hex = input("Enter Little Endian Hex: ").strip()
        if is_valid_hex(little_endian_hex):
            big_endian_hex = little_endian_to_big_endian(little_endian_hex)
            print(f"Big Endian Hex: {big_endian_hex}")
        else:
            print("Invalid Little Endian Hex input.")

    elif choice == '2':
        big_endian_hex = input("Enter Big Endian Hex: ").strip()
        if is_valid_hex(big_endian_hex):
            little_endian_hex = big_endian_to_little_endian(big_endian_hex)
            print(f"Little Endian Hex: {little_endian_hex}")
        else:
            print("Invalid Big Endian Hex input.")

    elif choice == '3':
        word = input("Enter a string: ").strip()
        little_endian_hex = string_to_little_endian(word)
        print(f"Little Endian Hex: {little_endian_hex}")

    elif choice == '4':
        word = input("Enter a string: ").strip()
        big_endian_hex = string_to_big_endian(word)
        print(f"Big Endian Hex: {big_endian_hex}")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
