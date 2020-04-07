# coding:utf-8
import os
import sys
from Crypto.Cipher import AES

#函数的俩参数长度都得是16的倍数
def aes_encrypt(msg, key = "wisdomtetestAES", iv="B1D8D3D0BBD8CFEC"):
    length = len(msg)
    mod = 16 - length%16
    msg += " " * mod
    aes = AES.new(key, AES.MODE_CBC, iv)
    block = aes.encrypt(msg)
    return block

def aes_decrypt(crypto, key="wisdomtetestAES", iv="B1D8D3D0BBD8CFEC"):
    aes = AES.new(key,AES.MODE_CBC, iv)
    block = aes.decrypt(crypto)
    return block.strip()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("python ./des_tool -d filepath")
        print("python ./des_tool -e filepath")
        exit()
    if sys.argv[1] == "-d": #调用解密函数逐行解密
        if not os.path.isfile(sys.argv[2]):
            print(sys.argv[2] + " is not vailable file")
            exit()
        decfile = sys.argv[2] + ".decode"
        decfd = open(decfile, "w")
        f = open(sys.argv[2])
        line = f.readline()
        index = 0
        while line:
            line = line.strip("\n")
            line = line.replace("confencoding", "\n")	#由于加密的时候，加密完的块有可能带有换行符，写文件后再读出来解密一行就读不完整（非16的倍数），会出错
            msg = aes_decrypt(line, "wisdomtetestAES", iv = "B1D8D3D0BBD8CFEC")
            decfd.write(msg + "\n")
            line = f.readline()
            index += 1
            if index%10000 == 0:
                print("decoding file line: " + str(index))	#每解密1w行打印一次信息
        print(str(index) + " lines decode finished")
        decfd.close()
        f.close()

    if sys.argv[1] == "-e":
        if not os.path.isfile(sys.argv[2]):
            print(sys.argv[2] + " is not vailable file")
            exit()
        encfile = sys.argv[2] + ".encode"
        encfd = open(encfile, "w")
        f = open(sys.argv[2])
        line = f.readline()
        index = 0
        while line:
            msg = aes_encrypt(line, "wisdomtetestAES", iv = "B1D8D3D0BBD8CFEC")
            msg = msg.replace("\n", "confencoding")
            encfd.write(msg + "\n")
            line = f.readline()
            index += 1
            if index%10000 == 0:
                print("encoding file line: " + str(index))
        print(str(index) + " lines encode finished")
        encfd.close()
        f.close()