import  re
rest="1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
res=re.sub(r' ', '', rest)#去掉所有的空格

def format_string(string):
    string = string.replace("--", "+")
    string = string.replace("-+", "-")
    string = string.replace("++", "+")
    string = string.replace("+-", "-")
    string = string.replace("*+", "*")
    string = string.replace("/+", "/")
    string = string.replace(' ', '')
    string = string.replace('- -', '+')
    return string

def chengchu(formula):#'''算乘除,'''

    operators = re.findall("[*/]", formula )
    calc_list = re.split("[*/]", formula )
    res = None
    for index,i in enumerate(calc_list):
        if res:
            if operators[index-1] == "*":
                res *= float(i)
            elif operators[index-1] == "/":
                res /= float(i)
        else:
            res = float(i)

    print("\033[31;1m[%s]运算结果=\033[0m" %formula, res  )
    return res

def jiajian(formula):#'''算+-,'''

    operators = re.findall("[+-]", formula )
    calc_list = re.split("[+-]", formula )
    res = None
    for index,i in enumerate(calc_list):
        if res:
            if operators[index-1] == "+":
                res += float(i)
            elif operators[index-1] == "-":
                res -= float(i)
        else:
                res = float(i)

    print("\033[31;1m[%s]运算结果=\033[0m" %formula, res  )
    return res


def zhaokuohao(zhi):#找括号
    a=re.search("\([^()]*\)",zhi).group()#找到内层小括号
    a1=a.strip('()')#去掉外层括号
    return a1
#print(zhaokuohao(res))


#a=re.search("\([^()]*\)",res).group()#找到内层小括号
#a=a.strip("()")#去掉外层括号
a=zhaokuohao(res)
#a=re.split("[/*]",a)#以乘除号为分割
#a=float(a[0])/float(a[1])#算出了第一个小括号里面的值
a=chengchu(a)
#print(a)
res=res.replace(re.search("\([^()]*\)",res).group(),'%s'%a)
#b=re.search("\([^()]*\)",res).group()#继续找到内层小括号
#b=b.strip("()")#去掉外层括号
b=zhaokuohao(res)
b_jiajian=re.findall("[+-]",b)
b=re.split("[-+]",b)#以加减号分割
tmp=[]
for i,v in enumerate(b):
    val=re.split("[/*]",v)
    if len(v)<2:
        tmp.append(float(v))
    if i==1:
        #val=re.split("[*/]",v)
        #v1=float(val[0])*float(val[1])
        #v2=v1/float(val[2])
        v2=chengchu(v)
        tmp.append(v2)
    if i==2:
        #val=re.split("[*/]",v)
        #v1=float(val[0])/float(val[1])
        #v2=v1*float(val[2])
        #v3=v2/float(val[3])
        #v4=v3*float(val[4])
        v4=chengchu(v)
        tmp.append(v4)
    if i==3:
        #val=re.split("[*/]",v)
        #v1=float(val[0])*float(val[1])
        #v2=v1/float(val[2])
        v2=chengchu(v)
        tmp.append(v2)
print(tmp,b_jiajian)
b='%s%s%s%s%s%s%s'%(tmp[0],b_jiajian[0],tmp[1],b_jiajian[1],tmp[2],b_jiajian[2],tmp[3])
b=jiajian(b)#算出了第2个小括号里面的值
#print(b)
res=res.replace(re.search("\([^()]*\)",res).group(),'%s'%b)
#c=re.search("\([^()]*\)",res).group()#继续找到内层小括号
#c=re.sub(r'[+]-', '-', c)#把+-替换成-
#c=c.strip("()")#去掉外层括号
c=zhaokuohao(res)#把+-替换成-
c=format_string(c)
c_jiajian=re.findall("[+-]",c)
c=re.split("[+-]",c)#以加减号分割

tmp1=[]
for k,v in enumerate(c):
    val=re.split("[*/]",v)
    if len(val)<2:
        tmp1.append(float(v))
    elif k==2:
        #valu=float(val[0])*float(val[1])
        valu=chengchu(v)
        tmp1.append(valu)
#print(tmp1,c_jiajian)
c='%s%s%s%s%s'%(tmp1[0],c_jiajian[0],tmp1[1],c_jiajian[1],tmp1[2])#算出了第3个小括号里面的值
#print(c)
c=jiajian(c)
res=res.replace(re.search("\([^()]*\)",res).group(),'%s'%c)

#d=re.search("\([^()]*\)",res).group()#继续找到内层小括号
#d=d.strip("()")#去掉外层括号
d=zhaokuohao(res)
#d=re.split("[/*]",d)#以乘除号为分割
#d=float(d[0])*float(d[1])#算出了第4个小括号里面的值
d=chengchu(d)
#print(d)
res=res.replace(re.search("\([^()]*\)",res).group(),'%s'%d)

#e=re.search("\([^()]*\)",res).group()#继续找到内层小括号
#e=e.strip("()")#去掉外层括号
e=zhaokuohao(res)
tmp2=[]
if '-' or '+' in e:
    e_jiajian=re.findall("[+-]",e)
    e=re.split("[+-]",e)#以加减号分割
    for k,v in enumerate(e):
        val=re.split("[/*]",v)#以乘除号为分割
        if len(val)<2:
            tmp2.append(float(v))
        else:
            #val1=float(val[0])*float(val[1])
            val1=chengchu(v)
            tmp2.append(val1)

e='%s%s%s'%(tmp2[0],e_jiajian[0],tmp2[1])#算出了第5个小括号里面的值
e=jiajian(e)
#print(e)

res=res.replace(re.search("\([^()]*\)",res).group(),'%s'%e)

#f=re.search("\([^()]*\)",res).group()#继续找到内层小括号
#f=f.strip("()")#去掉外层括号
f=zhaokuohao(res)
#f=re.sub(r'- -', '+', f)#把--替换成+
f=format_string(f)
tmp3=[]
if '-' or '+' in f:

    f_jiajian=re.findall("[+-]",f)
    f=re.split("[+-]",f)#以加减号分割
    for k,v in enumerate(f):
        val=re.split("[/*]",v)#以乘除号为分割

        if len(val)<2:
            tmp3.append(v)

        else:
            #val1=float(val[0])/float(val[1])
            val1=chengchu(v)
            tmp3.append(val1)
tmp4=[]
for k,v in enumerate(tmp3):
    if  tmp3[k-1]=='':
        t='-%s'%tmp3[k]
        tmp4.append(t)
    else:
        if v!='':
            tmp4.append(tmp3[k])
#print(tmp4,f_jiajian)
f='%s%s%s'%(float(tmp4[0]),f_jiajian[1],str(tmp4[1]))#算出了第6个小括号里面的值
#f=float(tmp4[0])+tmp4[1]
#f=jiajian(f)
#print(f)
res=res.replace(re.search("\([^()]*\)",res).group(),'%s'%f)
#print(res)
g_jiajian=re.findall("[+-]",res)
g=re.split("[+-]",res)#以加减号分割
#print(g)
tmp5=[]
for k,v in enumerate(g):
    if v.strip().endswith("*") or v.strip().endswith("/"):
        tmp5.append(" %s-%s"%(g[k],g[k+1]))
    elif ("*" or "/")  in v:
        tmp5.append(v)
    else:
        tmp5.append(v)
#print(tmp5)
for k,v in enumerate(tmp5):
    if ("*" or '/') in tmp5[k-1]:
        tmp5.remove(v)
tmp6=[]
for k,v in enumerate(tmp5):
    val=re.split("[*/]",v)
    if len(val)<2:
        tmp6.append(float(v))
    else:
        #valu=float(val[0])*float(val[1])
        valu=chengchu(v)
        tmp6.append(valu)
#print('tmp6',tmp6,g_jiajian)
#g=tmp6[0]-tmp6[1]
g='%s%s%s%s%s%s%s'%(0,g_jiajian[0],tmp6[0],g_jiajian[1],tmp6[1],g_jiajian[2],tmp6[2])

g=format_string(g)

g=jiajian(g)
print('本程序计算出的结果',g)
