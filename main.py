# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cmath
import json
from fractions import Fraction
import re
import sympy
from sympy import *
import numpy as np
import math

from wolframclient.language import Global, wlexpr

from wolf import wolfsession


def file2array(path, delimiter=' '):  # delimiter是数据分隔符
    fp = open(path, 'r', encoding='utf-8')
    string = fp.read()  # string是一行字符串，该字符串包含文件所有内容
    fp.close()
    row_list = string.splitlines()  # splitlines默认参数是‘\n’
    data_list = [[float(i) for i in row.strip().split(delimiter)] for row in row_list]
    return np.array(data_list)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def outputdata(V, outfile):
    for i in V:
        for j in range(len(i)):
            outfile.write(str(i[j]))
            outfile.write(' ')
        outfile.write('\n')
    outfile.flush()


def ReachableSpaceI(E, M, p, d):
    # Input: E -> list, the set of super-operator E_i E_i -> list  E_ij -> matrix
    #        M -> list, the set of measure operators M_0 = M_t, M_1 = M_nt
    #        p -> the initial state
    # Output: an orthonormal basis B
    # compute F(p)
    # compute the arithmetic average of E
    F = []
    for i in range(len(E)):
        for j in range(len(E[i])):
            F.append(np.matrix(E[i][j]) * np.matrix(M[1]))
    outfile = open('wolf/outdata.dat', 'w+')
    sess = wolfsession()
    exp = wlexpr('''
                P=Import["wolf/data.dat","Table"];
                vector = Eigenvectors[P];
                ortho = Orthogonalize[vector]
    ''')
    sess.evaluate(exp)
    res = sess.evaluate(Global.ortho)  # 输出元组类型数据
    print(res)
    B = []
    for i in res:
        B.append(list(i))
    B0 = []
    for i in range(d - 1):
        B1 = B.copy()
        for phi in B:
            if not (phi in B0):
                V = []
                for f in F:
                    print(np.c_[phi])
                    V.append(np.mat(f) * np.mat(np.c_[phi]))
                outputdata(V, outfile)
                exp = wlexpr('''
                    P=Import["wolf/outdata.dat","Table"];
                    vector=Eigenvectors[P];
                    ortho = Orthogonalize[vector]
                                    ''')
                sess.evaluate(exp)
                orthr = set(sess.evaluate(Global.ortho))
                B_ = []
                for i in orthr:
                    B_.append(list(i))
                B1.extend(B_)
                if B1 == B:
                    break
                B0 = B.copy()
                B = B1.copy()
        return B

    print('ReachableSpaceI')


if __name__ == '__main__':
    print_hi('PyCharm')
    with open("wolf/E.data",'r') as f:
        sqn=f.read()
    sqn.split('{*}')

    E = []
    E1 = []

    a = cmath.sqrt(3)
    e1 = np.mat([[1, 1, 0, -1], [1, -1, 1, 0], [0, 1, 1, 1], [1, 0, -1, 1]])
    e1 = 1 / a * e1
    e2 = np.mat([[1, 1, 0, 1], [-1, 1, -1, 0], [0, 1, 1, -1], [1, 0, -1, -1]])
    e2 = 1 / a * e2
    E1.append(e1)
    E1.append(e2)
    E.append(E1)
    M = []
    M0 = np.mat([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]])
    M1 = np.eye(4) - M0
    M.append(M0)
    M.append(M1)
    p = np.mat([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    d = 4
    ReachableSpaceI(E, M, p, d)
