t = int(input()) # number of test case

for x in range(1, t + 1):
    s = input()
    y = ''
    num = 0
    anterior = 0
    posterior = 0
        
    for n in range(0, len(s)):
        num = int(s[n])
        
        if len(s)==1:
            if num == 0:
                y += '0'
            else:
                y += '('*num + str(num) + ')'*num
        
        elif n == 0 and num == 0:
            y += '0'
        
        elif num > 0 and n == 0:
            y += '('*num + str(num)
        
        elif n == len(s) - 1 :
            anterior = int(s[n-1])

            if num == 0 and anterior == 0:
                y += '0'
            elif num == 0 and anterior > 0:
                y += ')'*anterior + '0'
            elif anterior == 0 and num > 0:
                y += '('*num + str(num) + ')'*num
            elif anterior > num and num > 0:
                y += ')' * (anterior - num) + str(num) + ')'* num
            elif anterior < num and num > 0:
                y += '(' * (num - anterior) + str(num) + ')'* num
            else:
                y += str(num) + ')' * num   
        
        else:
            anterior = int(s[n-1])
            posterior = int(s[n+1])

            if anterior == num :
                y += str(num)
            elif anterior == 0 and num > 0:
                y += '('*num + str(num)
            elif anterior > 0 and num == 0 :
                y += ')' * anterior + '0'
            elif anterior > num and num > 0:
                y += ')' * (anterior - num) + str(num)
            elif anterior < num and num > 0:
                y += '(' * (num - anterior) + str(num)
            
    print("Case #{}: {}".format(x, y))