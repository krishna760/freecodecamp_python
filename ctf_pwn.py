
import pwn
import re
host, port = '2018shell2.picoctf.com', 3000
s = pwn.remote(host, port)
prompt = s.recv()
print(prompt)

binary = re.findall('the (.*) as a word', prompt)[0]
print(hex(int(binary.replace(' ', ''), 2)))[2:].decode('hex')
s.sendline(answer)
s.close()