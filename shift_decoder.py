"""A decoder for shift ciphers."""

import sys

def main():
    """The main function for running the decoeer."""
    if len(sys.argv) < 3:
        print("Usage: python shiftDecoder.py <shift_count_1,shift_count_2...> <code>")
        return

    shifts = sys.argv[1].split(',')
    i = 0
    while i < len(shifts):
        try:
            if (shifts[i] == "" or shifts[i] == ''):
                shifts.remove(shifts[i])
                continue
            int(shifts[i])
            i += 1
        except ValueError:
            print("Usage: python shiftDecoder.py <shift_count_1,shift_count_2...> <code>")
            return
    current_shift = 0
    #97-122

    return_value = ""
    for i in range(2, len(sys.argv)):

        code = sys.argv[i]
        for char in code:
            new_char = chr(ord(char) + int(shifts[current_shift]))
            current_shift = (current_shift + 1) % len(shifts)
            if ord(new_char) > 122:
                new_char = chr(ord(new_char) - 26)
            if ord(new_char) < 97:
                new_char = chr(ord(new_char) + 26)
            return_value += new_char
        return_value += " "

    print(return_value)

if __name__ == "__main__":
    main()
    