__author__ = 'dennis'

def PrintSheet(prefix):
    startNum = 253
    endNum = startNum +(28*5) -1

    f = open("./klantkaarten.txt","w")
    f.write("nummer;\r\n")

    for num in range(startNum, endNum + 1):
        f.write("\"KK{0:0>5}\";\r\n".format(num))
        f.write("\"KK{0:0>5}\";\r\n ".format(num))

    f.close()

if __name__ == '__main__':
    PrintSheet("KK")