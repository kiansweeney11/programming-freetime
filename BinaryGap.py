# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

## 86% task score
def solution(N):
    # Implement your solution here
    # convert to binary
    binary = bin(N)
    seq = 0
    consec = []
    for i in range(len(binary)):
        # find first 1
        if binary[i] == "1":
            for j in range(len(binary) - 1):
                # count one ahead of pointer (which is the 1)
                # if this is a zero increment 1
                if binary[j + 1] == "0":
                    seq += 1
                else:
                # if next number is a 1, save this count of sequence to list and reset to 0
                    consec.append(seq)
                    seq = 0
        else:
            continue
    # return max value in list of sequence scores
    return max(consec)