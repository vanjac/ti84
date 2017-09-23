#http://www.benryves.com/bin/bbcbasic/manual/Appendix_Tokeniser.htm
#http://www.benryves.com/bin/bbcbasic/manual/Appendix_Format_of_Program_and_Variables_in_Memory.htm

import sys

TOKENS = [
    # 0x80
    "AND", "DIV", "EOR", "MOD", "OR", "ERROR", "LINE", "OFF",
    "STEP", "SPC", "TAB(", "ELSE", "THEN", "!!LINE NUM!!", "OPENIN", "PTR",
    # 0x90
    "PAGE", "TIME", "LOMEM", "HIMEM", "ABS", "ACS", "ADVAL", "ASC",
    "ASN", "ATN", "BGET", "COS", "COUNT", "DEG", "ERL", "ERR",
    # 0xA0
    "EVAL", "EXP", "EXT", "FALSE", "FN", "GET", "INKEY", "INSTR",
    "INT", "LEN", "LN", "LOG", "NOT", "OPENUP", "OPENOUT", "PI",
    # 0xB0
    "POINT(", "POS", "RAD", "RND", "SGN", "SIN", "SQR", "TAN",
    "TO", "TRUE", "USR", "VAL", "VPOS", "CHR$", "GET$", "INKEY$",
    # 0xC0
    "LEFT$(", "MID$(", "RIGHT$(", "STR$", "STRING$(", "EOF", "AUTO", "DELETE",
    "LOAD", "LIST", "NEW", "OLD", "RENUMBER", "SAVE", "PUT", "PTR",
    # 0xD0
    "PAGE", "TIME", "LOMEM", "HIMEM", "SOUND", "BPUT", "CALL", "CHAIN",
    "CLEAR", "CLOSE", "CLG", "CLS", "DATA", "DEF", "DIM", "DRAW",
    # 0xE0
    "END", "ENDPROC", "ENVELOPE", "FOR", "GOSUB", "GOTO", "GCOL", "IF",
    "INPUT", "LET", "LOCAL", "MODE", "MOVE", "NEXT", "ON", "VDU",
    # 0xF0
    "PLOT", "PRINT", "PROC", "READ", "REM", "REPEAT", "REPORT", "RESTORE",
    "RETURN", "RUN", "STOP", "COLOUR", "TRACE", "UNTIL", "WIDTH", "OSCLI"
]

def detokenize(src, dest, enableLineNumbers=True):
    with open(src, "rb") as readFile:
        with open(dest, "w") as writeFile:
            readFile.read(73) # header
            firstByte = True
            while True:
                nextByte = readFile.read(1)
                if nextByte == None or len(nextByte) == 0:
                    break
                nextByte = nextByte[0]
                if nextByte == ord('\r') or firstByte:
                    if not firstByte:
                        writeFile.write('\n')
                    firstByte = False
                    readFile.read(1) # line length byte
                    lineNum = readFile.read(2)
                    lineNum = lineNum[0] + lineNum[1] * 256
                    if lineNum == 65535:
                        break
                    if enableLineNumbers:
                        writeFile.write(str(lineNum) + " ")
                elif nextByte < 128:
                    writeFile.write(chr(nextByte))
                else:
                    writeFile.write(TOKENS[nextByte - 0x80])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Arguments: source.8xp dest.txt")
        sys.exit(1)

    detokenize(sys.argv[1], sys.argv[2], enableLineNumbers=False)
