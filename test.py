import time

# 获取当前时间的13位时间戳（毫秒级）
timestamp = int(round(time.time() * 1000))
print(timestamp)