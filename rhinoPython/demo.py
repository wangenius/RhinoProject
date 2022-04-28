#coding=utf-8
import rhinoscriptsyntax as rs
import math,random

#行数
i=20
#列数
j=12
#间距
k=4
#定义存储线段的列表
line=[]
for aa in range(i):
   line.append([])
   for bb in range(j):
       line[aa].append(None)

#remap函数
def fx(a,b,t):
   res=a*(1-t)+b*t
   return res

#在线段上按比例取点
def linediv(line,t):
   point1,point2=line
   x1,y1=point1
   x2,y2=point2
   x3=fx(x1,x2,t)
   y3=fx(y1,y2,t)
   point_res=(x3,y3)
   return point_res

#将两线段按数量均分点进行连接
def drawline(line1,line2,num):
   dr_t=0
   for dr_i in range(num+1):
       dr_t=dr_i*(1/num)
       p1=linediv(line1,dr_t)
       p2=linediv(line2,dr_t)
       rs.AddLine(p1,p2)

#主函数
for item in range(i):
   for value in range(j):
       x=value*k+random.uniform(-k/2,k/2)
       y=item*k+random.uniform(-k/2,k/2)
       if value==0:
           pointa=(x,y)
           #rs.AddPoint(x,y)
           continue
       #rs.AddPoint(x,y)
       pointb=(x,y)
       line[item][value]=(pointa,pointb)
       rs.AddLine(pointa,pointb)
       pointa=(x,y)
       if item==0:
           continue
       drawline(line[item][value],line[item-1][value],item)