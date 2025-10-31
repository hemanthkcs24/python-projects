dividend=1
divisor=2
if (dividend>0 and divisor >0) or (dividend<0 and divisor<0):
    reminder=dividend-divisor
    if abs(reminder)>=abs(divisor):
        q=1
    else: q=0
    while abs(reminder)>=abs(divisor):
        q+=1
        dividend=reminder
        reminder=dividend-divisor
    print (q)
elif dividend<0 or divisor<0:
    reminder=dividend+divisor
    if abs(reminder)>=abs(divisor):
        q=-1
    else: q=0
    while abs(reminder)>=abs(divisor):
        q-=1
        dividend=reminder
        reminder=dividend+divisor
    print(q)

           

