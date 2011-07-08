__author__ = 'dennis'

def PrintSheet(prefix):
    startNum = 113
    endNum = 168

    f = open("./klantkaarten.txt","w")
    f.write("nummer;\r")

    for num in range(startNum, endNum + 1):
        f.write("\"KK{0:0>5}\";\r".format(num))
        f.write("\"KK{0:0>5}\";\r".format(num))

    f.close()

if __name__ == '__main__':
    PrintSheet("KK")
  