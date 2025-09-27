prices = [100, 180, 260, 310, 40, 535, 695]
k = 1 
i = 0
prof = 0
while k<=(len(prices)-1):
    if prices[i] >= prices[k] :
        prof+=prices[k-1] - prices[i]
        i = k
        k+=1
    if k == (len(prices)-1):
        prof+=prices[k] - prices[i]
        k+=1
    else :
        k+=1 
        
print(prof)