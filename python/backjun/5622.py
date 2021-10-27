import sys

dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
input_sentense = sys.stdin.readline()
total_time = 0
for character in input_sentense:
    for dial_number in dial:
        if character in dial_number:
            total_time += dial.index(dial_number) + 3
print(total_time)
