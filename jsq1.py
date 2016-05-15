#!/usr/bin/env python
# -*- coding:utf-8 -*-

import  re
rest="1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
res=re.sub(r' ', '', rest)#去掉所有的空格
print(res)

def zhaokuohao(zhi):
    a=re.search("\([^()]*\)",zhi).group()#找到内层小括号
    print(a)
    res=zhi.replace(a,'-8')
    return res

res=zhaokuohao(res)

print(res)

