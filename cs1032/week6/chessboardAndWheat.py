def chessboardAndWheat(): #time (s): 0.0955335
    total = 0
    for i in range(1, 65): total += 2 ** (i - 1)
    return total

# or more efficiently:
def wheatAndChessboard(): #time (s): 0.0002867
    return 2 ** 64 - 1

print(chessboardAndWheat())
print(wheatAndChessboard())