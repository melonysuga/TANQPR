from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr,Global


def wolfsession():
    wolfpath = 'C:\\Program Files\\Wolfram Research\\Mathematica\\11.3\\WolframKernel.exe'
    sess=WolframLanguageSession(wolfpath)
    # exp=wlexpr(commands)
    # sess.evaluate(exp)
    return sess

# 计算后所得变量保存在Global里,同样需要计算来获得实际值
# dist = sess.evaluate(Global.dist2)  # 输出元组类型数据
# e_d = sess.evaluate([Global.e, Global.d])  # 输出元组类型数据
# print("结果分布:",dist) #此处按照mathematica语法输出新的分布
# print("期望:",e_d[0],"方差:",e_d[1]) #输出新分布的期望和方差

