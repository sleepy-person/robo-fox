def packarray(arr,filename):
    assert len(arr) == 128 and all(len(row) == 128 for row in arr), "Array must be 128x128"
    flat_arr = [val for row in arr for val in row]
    packed_bytes = bytearray()
    for i in range(0, len(flat_arr), 2):
        first_val = flat_arr[i] & 0xF
        second_val = flat_arr[i + 1] & 0xF
        
        packed_byte = (first_val << 4) | second_val # left shift to cram
        packed_bytes.append(packed_byte)
    with open(filename, "wb") as f:
        f.write(packed_bytes)
        
def unpackarray(filename):
    with open(filename, "rb") as f:
        packed_bytes = f.read()
    flat_arr = []

    for byte in packed_bytes:
        first_val = (byte >> 4) & 0xF # gotta right shift back
        second_val = byte & 0xF
        flat_arr.extend([first_val, second_val]) # no I didn't know extend existed existed
        
    return [flat_arr[i:i+128] for i in range(0, len(flat_arr), 128)]

if __name__ == "__main__":
    yeet=input("Enter p for pack and u for unpack.").lower()
    if (yeet=="p"):
        packarray(input("> "),input(">> "))
    elif (yeet=="u"):
        unpackarray(input(">> "))
    else:
        exit()