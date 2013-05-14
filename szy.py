# -*- coding: UTF-8 -*-

p=["底","高","长半轴","短半轴"]
size=[]
squ=[]
def size():
    print '请分别输入底，高，长半轴，短半轴，如无该种尺寸以0代替'
    for i in range(0,4):
        a=input(p[i])
        size.append(a)
    print size
def rectangle():
    print "矩形面积："
    b= size[0]*size[1]
    squ.append(b)
    print b
def square():
    print "正方形面积："
    b= size[0]*size[1]
    squ.append(b)
    print b
def parallelogram():
    print "平行四边形面积："
    b= size[0]*size[1]
    squ.append(b)
    print b
def rt():
    print "直角三角形面积："
    b= 0.5*size[0]*size[1]
    squ.append(b)
    print b
def et():
    print "等边三角型面积："
    b= 0.5*size[0]*size[1]
    squ.append(b)
    print b
def riangle ():
    print "等边三角型面积："
    b= 0.5*size[0]*size[1]
    squ.append(b)
    print b
def circle():
    print "圆形面积："
    b= 3.14*size[2]*size[3]
    squ.append(b)
    print b
def ellipse():
    print "椭圆形面积："
    b= 3.14*size[2]*size[3]
    squ.append(b)
    print b

size()
rectangle()
size()
square()
size()
parallelogram()
size()
rt()
size()
et()
size()
riangle ()
size()
circle()
size()
ellipse()
c=0
print "图形面积之和："
for i in range(0,8):
    c=c+squ[i]
print c
print "平均面积："
print c/8
