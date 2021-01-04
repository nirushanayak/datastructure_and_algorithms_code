def stockBuySell(stocks):
    max_p=0
    max_profit=0
    cp=0
    sellBuy=[]
    for i in range(1,len(stocks)):
        if stocks[i]<stocks[i-1]:
            if max_profit==0:
                cp=i
            else:
                sellBuy.append((cp ,max_p))
                cp=i
                max_profit=0

        else:
            local_profit=stocks[i]-stocks[cp]
            if local_profit>max_profit:
                max_profit=local_profit
                max_p=i
    if max_profit!=0:
        sellBuy.append((cp,max_p))

    if len(sellBuy):
        for i in sellBuy:
            a=' '.join(map(str,i))
            print('('+a+')',end=' ')
        print()
    else:
        print("No Profit")

test_num=int(input())
for i in range(test_num):
    n=int(input())
    stocks=list(map(int,input().split()))
    stockBuySell(stocks)
