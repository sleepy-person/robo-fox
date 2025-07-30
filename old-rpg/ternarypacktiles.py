def packarray(arr,filename):
    assert len(arr) == 128 and all(len(row) == 128 for row in arr), "Array must be 128x128"
    flat_arr = [val for row in arr for val in row]
    packed_bytes = bytearray()
    bit_buffer = 0
    bit_count = 0

    for val in flat_arr:
        val &= 0x7  # Ensure only 3 bits are used
        bit_buffer |= (val << bit_count)  # Insert at correct position
        bit_count += 3  # Move bit counter

        while bit_count >= 8:  # If we filled a byte, store it
            packed_bytes.append(bit_buffer & 0xFF)  # Store 8 bits
            bit_buffer >>= 8  # Shift out stored bits
            bit_count -= 8  # Update bit count
        
    # If there are remaining bits, store them in the last byte
    if bit_count > 0:
        packed_bytes.append(bit_buffer & 0xFF)
    with open(filename, "wb") as f:
        f.write(packed_bytes)
        
def unpackarray(filename):
    with open(filename, "rb") as f:
        packed_bytes = f.read()
    
    flat_arr = []
    bit_buffer = int.from_bytes(packed_bytes, 'little')  # Convert bytes to an integer
    bit_count = len(packed_bytes) * 8  # Total bits available
    pos = 0  # Bit position

    while pos + 3 <= bit_count:  # Extract while at least 3 bits remain
        flat_arr.append((bit_buffer >> pos) & 0b111)  # Get 3 bits
        pos += 3  # Move bit position

    return [flat_arr[i:i + 128] for i in range(0, len(flat_arr), 128)]

if __name__ == "__main__":
    yeet=input("Enter p for pack and u for unpack.").lower()
    if (yeet=="p"):
        packarray(input("> "),input(">> "))
    elif (yeet=="u"):
        unpackarray(input(">> "))
    else:
        exit()
