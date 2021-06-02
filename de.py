import os
import base64
from Crypto.Cipher import AES

#AES对称加密算法
#str不是16的倍数就补足为16的倍数
def get_file(_dir):
	_file = []
	tmp = os.listdir(_dir)
	print("遍历文件夹"+_dir)
	for i in tmp:
		i = _dir +'\\'+ i
		if os.path.isdir(i):
			_file += get_file(i)
		else:
			_file.append(i)
	return _file

def add_to_16(message):
	while len(message) % 16 != 0:
		message += b'\x00'
	return message

#加密方法
def babyencode(message,key='1234567890123456'.encode()):
	key = add_to_16(key)
	message = add_to_16(message)
	mode = AES.MODE_ECB
	aes = AES.new(key,mode)
	encrypt = aes.encrypt(message)
	return encrypt

#解密方法
def babydecode(message,key='1234567890123456'.encode()):
	mode = AES.MODE_ECB
	key = add_to_16(key)
	message = add_to_16(message)
	aes = AES.new(key,mode)
	decrypt = aes.decrypt(message)
	return decrypt

def jiami_file(_file):
	if '.py' in _file:
		pass
	else:
		with open(_file,'rb') as f:
			content = f.read()
		content = babyencode(content)
		with open(_file,'wb') as f:
			f.write(content)

def jiemi_file(_file):
	if '.py' in _file:
		pass
	else:
		with open(_file,'rb') as f:
			content = f.read()
		content = babydecode(content)
		with open(_file,'wb') as f:
			f.write(content)

key = '1234567890123456'
_dir = os.getcwd()  #获取当前位置
_file = get_file(_dir) #获取当前所有文件名
print(_file)
for i in _file:
	print("正在处理:" +i)
	jiemi_file(i)
