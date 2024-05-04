import subprocess
import time

# 定义你想要执行代码的特定时间点（24小时制）
特定时间点 = "08:10:00"

while True:
    # 获取当前时间
    当前时间 = time.strftime("%H:%M:%S", time.localtime())
    
    # 如果当前时间等于特定时间点，执行代码
    if 当前时间 == 特定时间点:
        # 执行外部脚本
        subprocess.run(["python", "qiandao.py"])
        
        # 等待下一个特定时间点
        continue
    
    # 如果当前时间不等于特定时间点，让脚本休眠一段时间（比如每秒检查一次）
    time.sleep(1)
