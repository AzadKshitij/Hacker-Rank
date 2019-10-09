n= int(input())
num_candle = list(map(int,input().split(sep = " ", maxsplit=n)))
high_candle = max(num_candle)
candles = 0
for i in range(0,n):
    if num_candle[i] == high_candle:
        candles += 1
        continue
print(candles)
