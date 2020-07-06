from django.shortcuts import render
from random import *

# Create your views here.

def main(request):
    return render(request, 'main.html')

def result(request):
    a=[]
    dirty_bit=[0,0,0,0,0]
    ran_num=randint(1,7)
    for i in range(5):
        while ran_num in a:
            ran_num=randint(1,7)
        a.append(ran_num)
    b=[int(request.GET['num1']),int(request.GET['num2']),int(request.GET['num3']),int(request.GET['num4']),int(request.GET['num5'])]
    count=0
    ranking="꽝 입니다^^"

    for i in b:
        for j in range(0,len(a)):
            if  i==a[j] and dirty_bit[j]==0:
                count=count+1
                dirty_bit[j]=1
                break

    if count==5:
        ranking="1등입니다"
    elif count==4:
        ranking="2등입니다"
    elif count==3:
        ranking="3등입니다"
    else:
        pass
    return render(request, 'result.html',{'lotto_num':a,'check_num':b, 'count':count,'ranking':ranking})