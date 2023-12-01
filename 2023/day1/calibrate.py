sum = 0
with open("calibration.txt", "r") as f:
    for line in f:
        i, j = 0, 0
        for i, char in enumerate(line):
            num = ""
            if char.isnumeric():
                num += char
                break
        for j, char in enumerate(line[::-1]):
            if char.isnumeric():
                num += char
                break
        
        sum += int(num)

print(f"sum is {sum}")
            