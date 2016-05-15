import  re
rest="1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
res=re.sub(r' ', '', rest)#去掉所有的空格
print(eval(res))
def zhaokuohao(zhi):#找括号
    a=re.search("\([^()]*\)",zhi).group()#找到内层小括号
    a1=a.strip('()')
    tmp=[]
    for i in a1:
        if i!=a1[0]:
            tmp.append(i)
    if ('-' or '+')not in tmp:#如果没有加减就算乘除
        jieguo=chengchu(a1)

    res=zhi.replace(a,'%s'%jieguo)
    return res

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

def format_string(string):
    string = string.replace("--", "+")
    string = string.replace("-+", "-")
    string = string.replace("++", "+")
    string = string.replace("+-", "-")
    string = string.replace("*+", "*")
    string = string.replace("/+", "/")
    string = string.replace(' ', '')
    return string

def handle_special_occactions(plus_and_minus_operators,multiply_and_dividend):
    '''有时会出现这种情况 , ['-', '-'] ['1 ', ' 2 * ', '14969036.7968254'],2*...后面这段实际是 2*-14969036.7968254,需要特别处理下,太恶心了'''
    for index,i in enumerate(multiply_and_dividend):
        i = i.strip()
        if i.endswith("*") or i.endswith("/"):
            multiply_and_dividend[index] = multiply_and_dividend[index] + plus_and_minus_operators[index] + multiply_and_dividend[index+1]
            del multiply_and_dividend[index+1]
            del plus_and_minus_operators[index]
    return plus_and_minus_operators,multiply_and_dividend
def compute(formula):
    '''这里计算是的不带括号的公式'''

    formula = formula.strip("()") #去除外面包的拓号
    formula = format_string(formula) #去除外重复的+-号
    plus_and_minus_operators = re.findall("[+-]", formula)
    multiply_and_dividend = re.split("[+-]", formula) #取出乘除公式
    if len(multiply_and_dividend[0].strip()) == 0:#代表这肯定是个减号
        multiply_and_dividend[1] = plus_and_minus_operators[0] + multiply_and_dividend[1]
        del multiply_and_dividend[0]
        del plus_and_minus_operators[0]

    plus_and_minus_operators,multiply_and_dividend=handle_special_occactions(plus_and_minus_operators,multiply_and_dividend)
    for index,i in enumerate(multiply_and_dividend):
        if re.search("[*/]" ,i):
            sub_res = chengchu(i)
            multiply_and_dividend[index] = sub_res

    #开始运算+,-
    print(multiply_and_dividend, plus_and_minus_operators)
    total_res = None
    for index,item in enumerate(multiply_and_dividend):
        if total_res: #代表不是第一次循环
            if plus_and_minus_operators[index-1] == '+':
                total_res += float(item)
            elif plus_and_minus_operators[index-1] == '-':
                total_res -= float(item)
        else:
            total_res = float(item)
    print("\033[32;1m[%s]运算结果:\033[0m" %formula,total_res)
    return total_res

#a=re.search("\([^()]*\)",res).group()#找到内层小括号
#a=a.strip("()")#去掉外层括号
#a=re.split("[/*]",a)#以乘除号为分割
#a1=float(a[0])/float(a[1])
res=zhaokuohao(res)#算出了第一个小括号里面的值
#res=res.replace(re.search("\([^()]*\)",res).group(),'%s'%a1)

#res="1 - 2 * ( (60-30 +%s * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"%a
#b=re.search("\([^()]*\)",res).group()#继续找到内层小括号
#b=zhaokuohao(res)

b=b.strip("()")#去掉外层括号
b=re.split("[-+]",b)#以加减号分割
tmp=[]
for i,v in enumerate(b):
    val=re.split("[/*]",v)
    if len(v)<2:
        tmp.append(v)
    if i==1:
        val=re.split("[*/]",v)
        v1=float(val[0])*float(val[1])
        v2=v1/float(val[2])
        tmp.append(v2)
    if i==2:
        val=re.split("[*/]",v)
        v1=float(val[0])/float(val[1])
        v2=v1*float(val[2])
        v3=v2/float(val[3])
        v4=v3*float(val[4])
        tmp.append(v4)
    if i==3:
        val=re.split("[*/]",v)
        v1=float(val[0])*float(val[1])
        v2=v1/float(val[2])
        tmp.append(v2)
b=float(tmp[0])-float(tmp[1])+float(tmp[2])+float(tmp[3])#算出了第2个小括号里面的值

res=res.replace(re.search("\([^()]*\)",res).group(),'%s'%b)

#res="1 - 2 * ( (60-30 +%s * %s) - (-4*3)/ (16-3*2) )"%(a,b)
c=re.search("\([^()]*\)",res).group()#继续找到内层小括号
c=re.sub(r'[+]-', '-', c)#把+-替换成-
c=c.strip("()")#去掉外层括号

c=re.split("[+-]",c)#以加减号分割

tmp1=[]
for k,v in enumerate(c):
    val=re.split("[*/]",v)
    if len(val)<2:
        tmp1.append(float(v))
    elif k==2:
        valu=float(val[0])*float(val[1])
        tmp1.append(valu)

c=tmp1[0]-tmp1[1]-tmp1[2]#算出了第3个小括号里面的值

res=res.replace(re.search("\([^()]*\)",res).group(),'%s'%c)

#res="1 - 2 * ( %s - (-4*3)/ (16-3*2) )"%(c)

d=re.search("\([^()]*\)",res).group()#继续找到内层小括号

d=d.strip("()")#去掉外层括号
d=re.split("[/*]",d)#以乘除号为分割

d=float(d[0])*float(d[1])#算出了第4个小括号里面的值
res=res.replace(re.search("\([^()]*\)",res).group(),'%s'%d)
print(res)
#res="1 - 2 * ( %s - %s/ (16-3*2) )"%(c,d)

e=re.search("\([^()]*\)",res).group()#继续找到内层小括号
e=e.strip("()")#去掉外层括号
tmp2=[]
if '-' or '+' in e:
    e=re.split("[+-]",e)#以加减号分割
    for k,v in enumerate(e):
        val=re.split("[/*]",v)#以乘除号为分割
        if len(val)<2:
            tmp2.append(float(v))
        else:
            val1=float(val[0])*float(val[1])
            tmp2.append(val1)

e=tmp2[0]-tmp2[1]#算出了第5个小括号里面的值
res=res.replace(re.search("\([^()]*\)",res).group(),'%s'%e)
print(res)
#res="1 - 2 * ( %s - %s/ %s )"%(c,d,e)

f=re.search("\([^()]*\)",res).group()#继续找到内层小括号
f=f.strip("()")#去掉外层括号
f=re.sub(r'--', '+', f)#把--替换成+
print(f)
tmp3=[]
if '-' or '+' in f:
    f=re.split("[+-]",f)#以加减号分割

    for k,v in enumerate(f):
        val=re.split("[/*]",v)#以乘除号为分割

        if len(val)<2:
            tmp3.append(v)

        else:
            val1=float(val[0])/float(val[1])
            tmp3.append(val1)
tmp4=[]
print(tmp3)
for k,v in enumerate(tmp3):
    if  tmp3[k-1]=='':
        t='-%s'%tmp3[k]
        tmp4.append(t)
    else:
        if v!='':
            tmp4.append(tmp3[k])
print(tmp4)
f=float(tmp4[0])+float(tmp4[1])#算出了第6个小括号里面的值
res=res.replace(re.search("\([^()]*\)",res).group(),'%s'%f)
#res="1 - 2 * %s"%(f)
print(res)


