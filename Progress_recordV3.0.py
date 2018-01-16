import time
x = open(recordtimes.txt')
num = int(x.read(-1)[::-1][:2][::-1])
t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#调用当前时间
f = open('progress.txt','a',encoding='utf-8')
f.write('\n')
f.write(str(t))
f.write('\n')
zifu = ['看到第%d个视频 '%num]
f.write(str(zifu))
f.write('\n')
num += 1
m = open('recordtimes.txt','a')
m.write(str(num))
f.write('\n')
f.close()
x.close()
