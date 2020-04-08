#!/bin/sh

# 首先需要使用 openssl 生成一个 2048 位的密钥 rsa.key 文件 (rsa.key 密钥文件中包含了私钥和公钥)
openssl genrsa -out rsa.key 2048

# 然后从 rsa.key 密钥文件中提取出公钥 pub.key
openssl rsa -in rsa.key -pubout -out pub.key

# 使用 pub.key 公钥加密一个文件 (fxb.txt 为原始文件，fxb.txt.rsa 为加密之后的文件)
openssl rsautl -encrypt -inkey pub.key -pubin -in fxb.txt -out fxb.txt.rsa

# 使用 rsa.key 私钥解密一个文件 (fxb.txt.rsa 为加密的文件，fxb.txt.resp 为解密之后的文件)
openssl rsautl -decrypt -inkey rsa.key -in fxb.txt.rsa -out fxb.txt.resp