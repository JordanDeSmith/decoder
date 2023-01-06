import sys

def main():
    if (len(sys.argv) != 3):
        print("Usage: python shiftDecoder.py <shift count> <code>")
        return

    shiftBy = int(sys.argv[1])
    code = sys.argv[2]
    #97-122

    returnValue = ""
    for char in code:
        newChar = chr(ord(char) + shiftBy)
        if (ord(newChar) > 122):
            newChar = chr(ord(newChar) - 26)
        if (ord(newChar) < 97):
            newChar = chr(ord(newChar) + 26)
        returnValue += newChar

    print(returnValue)

if __name__ == "__main__":
    main()