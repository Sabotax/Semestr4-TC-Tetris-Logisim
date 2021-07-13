
input_file = open("gpumanrom.txt", "r")
output_file = open("result", "w")
output_file.write("v2.0 raw" + "\n")
for line in input_file.readlines():
    line = str(line)
    number = int(line[0]) * 8 + int(line[2]) * 4 + int(line[4]) * 2 + int(line[6]) * 1
    number = str(hex(number))
    if len(number) == 3:
        output_file.writelines(number[2] + "\n")
    else:
        output_file.writelines(number[2] + " " + number[3] + "\n")
input_file.close()
output_file.close()