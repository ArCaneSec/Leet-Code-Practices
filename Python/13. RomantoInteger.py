roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

x = "IVI"
previous_char = ""
nums = []

for i in x:
    if previous_char == "":
        previous_char = i
        nums.append(roman[i])
        continue
    if roman[i] > roman[previous_char]:
        num = roman[previous_char] - roman[i]
        nums.append(num)
    else:
        nums.append(roman[i])
    
print(sum(nums))

