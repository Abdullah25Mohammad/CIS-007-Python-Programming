#5.17
#Display the ASCII character table
#Abdullah Mohammad
#1/5/23

# ! is 33
# ~ is 126

for i in range(33,127):
    if (i-32)%10 != 0:                      #detect if ASCII letter is not the 10th
        print(chr(i), end=' ')              #if not 10th, then print with space after
    else:
        print(chr(i), end='\n')             #if is 10th, then print with new line after
