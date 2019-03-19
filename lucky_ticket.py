n = input()
begining = n[:3]
end = n[3:]
b = int(begining[0]) + int(begining[1]) + int(begining[2])
e = int(end[0]) + int(end[1]) + int(end[2])
if b == e:
    print("Счастливый")
else:
    print("Обычный")

