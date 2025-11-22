#COMPUTER SCIENCE PROJECT 2019-20
#RESULT ANALYSIS
#Made by - Alok Maurya

from tkinter import *
import matplotlib.pyplot as m

window=Tk()
window.title("RESULT ANALYSIS")
window.configure(background='pink')

Label(window,text="GRADE-->",bg='mediumorchid',width=12).grid(row = 0, column = 0,columnspan = 2,sticky = W)
Label(window,text="S.NO.",bg='lightcoral').grid(row = 1, column = 0,sticky = W)
Label(window,text="SUBJECT",bg='orangered').grid(row = 1, column = 1, sticky = W)

Label(window,text="A1",bg='mediumslateblue',width=6).grid(row = 0, column = 2,sticky = W)
Label(window,text="A2",bg='mediumslateblue',width=6).grid(row = 0, column = 3,sticky = W)
Label(window,text="B1",bg='mediumslateblue',width=6).grid(row = 0, column = 4,sticky = W)
Label(window,text="B2",bg='mediumslateblue',width=6).grid(row = 0, column = 5,sticky = W)
Label(window,text="C1",bg='mediumslateblue',width=6).grid(row = 0, column = 6,sticky = W)
Label(window,text="C2",bg='mediumslateblue',width=6).grid(row = 0, column = 7,sticky = W)
Label(window,text="D1",bg='mediumslateblue',width=6).grid(row = 0, column = 8,sticky = W)
Label(window,text="D2",bg='mediumslateblue',width=6).grid(row = 0, column = 9,sticky = W)
Label(window,text="E",bg='mediumslateblue',width=6).grid(row = 0, column = 10,sticky = W)

Label(window,text="8",bg='powderblue',width=6).grid(row = 1, column = 2,sticky = W)
Label(window,text="7",bg='powderblue',width=6).grid(row = 1, column = 3,sticky = W)
Label(window,text="6",bg='powderblue',width=6).grid(row = 1, column = 4,sticky = W)
Label(window,text="5",bg='powderblue',width=6).grid(row = 1, column = 5,sticky = W)
Label(window,text="4",bg='powderblue',width=6).grid(row = 1, column = 6,sticky = W)
Label(window,text="3",bg='powderblue',width=6).grid(row = 1, column = 7,sticky = W)
Label(window,text="2",bg='powderblue',width=6).grid(row = 1, column = 8,sticky = W)
Label(window,text="1",bg='powderblue',width=6).grid(row = 1, column = 9,sticky = W)
Label(window,text="0",bg='powderblue',width=6).grid(row = 1, column = 10,sticky = W)

Label(window,text="TOTAL GRADE",bg='greenyellow',width=10,height=2).grid(row = 0, column = 11,rowspan=2,sticky = W)
Label(window,text="NXW",bg='greenyellow',width=10,height=2).grid(row = 0, column = 12,rowspan=2,sticky = W)
Label(window,text="PI",bg='greenyellow',width=10,height=2).grid(row = 0, column = 13,rowspan=2,sticky = W)

# FIRST SUBJECT

Label(window,text="1",bg='yellow',width=4,height=3).grid(row = 2, column = 0,rowspan=2,sticky = W)

S1=Entry(window,bg='gold',width=8)                        
S1.grid(row = 2, column = 1,rowspan=2,sticky = W)
            
S1M1=Entry(window,bg='palegreen',width=6)
S1M1.grid(row = 2, column = 2,sticky = W)
S1M2=Entry(window,bg='palegreen',width=6)
S1M2.grid(row = 2, column = 3,sticky = W)
S1M3=Entry(window,bg='palegreen',width=6)
S1M3.grid(row = 2, column = 4,sticky = W)
S1M4=Entry(window,bg='palegreen',width=6)
S1M4.grid(row = 2, column = 5,sticky = W)
S1M5=Entry(window,bg='palegreen',width=6)
S1M5.grid(row = 2, column = 6,sticky = W)
S1M6=Entry(window,bg='palegreen',width=6)
S1M6.grid(row = 2, column = 7,sticky = W)
S1M7=Entry(window,bg='palegreen',width=6)
S1M7.grid(row = 2, column = 8,sticky = W)
S1M8=Entry(window,bg='palegreen',width=6)
S1M8.grid(row = 2, column = 9,sticky = W)
S1M9=Entry(window,bg='palegreen',width=6)
S1M9.grid(row = 2, column = 10,sticky = W)
 
def Result1(a,b,c,d,e,f,g,h,i):
    global s1,t1,k1
    v1,v2,v3,v4,v5,v6,v7,v8,v9=int(a.get()),int(b.get()),int(c.get()),int(d.get()),int(e.get()),int(f.get()),int(g.get()),int(h.get()),int(i.get())
    s1=v1+v2+v3+v4+v5+v6+v7+v8+v9
    t1=v1*8+v2*7+v3*6+v4*5+v5*4+v6*3+v7*2+v8*1+v9*0
    r=t1*(12.5/s1)
    k1=round(r,2)
    Label(window,text=v1*8,width=5,bg='aquamarine').grid(row=3,column=2,sticky=W)
    Label(window,text=v2*7,width=5,bg='aquamarine').grid(row=3,column=3,sticky=W)
    Label(window,text=v3*6,width=5,bg='aquamarine').grid(row=3,column=4,sticky=W)
    Label(window,text=v4*5,width=5,bg='aquamarine').grid(row=3,column=5,sticky=W)
    Label(window,text=v5*4,width=5,bg='aquamarine').grid(row=3,column=6,sticky=W)
    Label(window,text=v6*3,width=5,bg='aquamarine').grid(row=3,column=7,sticky=W)
    Label(window,text=v7*2,width=5,bg='aquamarine').grid(row=3,column=8,sticky=W)
    Label(window,text=v8*1,width=5,bg='aquamarine').grid(row=3,column=9,sticky=W)
    Label(window,text=v9*0,width=5,bg='aquamarine').grid(row=3,column=10,sticky=W)

    Label(window,text=s1,bg="salmon",width=9).grid(row=2,column=11)
    Label(window,text=t1,bg="cornflowerblue",width=9).grid(row=3,column=12)
    Label(window,text=k1,bg="mediumspringgreen",width=9,height=2).grid(row=2,column=13,rowspan=2,sticky = W)

S1Btn=Button(window,text="Submit1",command=lambda:Result1(S1M1,S1M2,S1M3,S1M4,S1M5,S1M6,S1M7,S1M8,S1M9)).grid(row=2,column=14,rowspan=2,sticky=E)


#SECOND SUBJECT

Label(window,text="2",bg='yellow',width=4,height=3).grid(row = 4, column = 0,rowspan=2,sticky = W)

S2=Entry(window,bg='gold',width=8)                        
S2.grid(row = 4, column = 1,rowspan=2,sticky = W)
            
S2M1=Entry(window,bg='palegreen',width=6)
S2M1.grid(row = 4, column = 2,sticky = W)
S2M2=Entry(window,bg='palegreen',width=6)
S2M2.grid(row = 4, column = 3,sticky = W)
S2M3=Entry(window,bg='palegreen',width=6)
S2M3.grid(row = 4, column = 4,sticky = W)
S2M4=Entry(window,bg='palegreen',width=6)
S2M4.grid(row = 4, column = 5,sticky = W)
S2M5=Entry(window,bg='palegreen',width=6)
S2M5.grid(row = 4, column = 6,sticky = W)
S2M6=Entry(window,bg='palegreen',width=6)
S2M6.grid(row = 4, column = 7,sticky = W)
S2M7=Entry(window,bg='palegreen',width=6)
S2M7.grid(row = 4, column = 8,sticky = W)
S2M8=Entry(window,bg='palegreen',width=6)
S2M8.grid(row = 4, column = 9,sticky = W)
S2M9=Entry(window,bg='palegreen',width=6)
S2M9.grid(row = 4, column = 10,sticky = W)
  
def Result2(a,b,c,d,e,f,g,h,i):
    global s2,t2,k2
    v1,v2,v3,v4,v5,v6,v7,v8,v9=int(a.get()),int(b.get()),int(c.get()),int(d.get()),int(e.get()),int(f.get()),int(g.get()),int(h.get()),int(i.get())
    s2=v1+v2+v3+v4+v5+v6+v7+v8+v9
    t2=v1*8+v2*7+v3*6+v4*5+v5*4+v6*3+v7*2+v8*1+v9*0
    r=t2*(12.5/s2)
    k2=round(r,2)
    Label(window,text=v1*8,width=5,bg='aquamarine').grid(row=5,column=2,sticky=W)
    Label(window,text=v2*7,width=5,bg='aquamarine').grid(row=5,column=3,sticky=W)
    Label(window,text=v3*6,width=5,bg='aquamarine').grid(row=5,column=4,sticky=W)
    Label(window,text=v4*5,width=5,bg='aquamarine').grid(row=5,column=5,sticky=W)
    Label(window,text=v5*4,width=5,bg='aquamarine').grid(row=5,column=6,sticky=W)
    Label(window,text=v6*3,width=5,bg='aquamarine').grid(row=5,column=7,sticky=W)
    Label(window,text=v7*2,width=5,bg='aquamarine').grid(row=5,column=8,sticky=W)
    Label(window,text=v8*1,width=5,bg='aquamarine').grid(row=5,column=9,sticky=W)
    Label(window,text=v9*0,width=5,bg='aquamarine').grid(row=5,column=10,sticky=W)

    Label(window,text=s2,bg="salmon",width=9).grid(row=4,column=11)
    Label(window,text=t2,bg="cornflowerblue",width=9).grid(row=5,column=12)
    Label(window,text=k2,bg="mediumspringgreen",width=9,height=2).grid(row=4,column=13,rowspan=2,sticky = W)
 
S2Btn=Button(window,text="Submit2",command=lambda:Result2(S2M1,S2M2,S2M3,S2M4,S2M5,S2M6,S2M7,S2M8,S2M9)).grid(row=4,column=14,rowspan=2,sticky=E)


#THIRD SUBJECT

Label(window,text="3",bg='yellow',width=4,height=3).grid(row = 6, column = 0,rowspan=2,sticky = W)

S3=Entry(window,bg='gold',width=8)                       
S3.grid(row = 6, column = 1,rowspan=2,sticky = W)
            
S3M1=Entry(window,bg='palegreen',width=6)
S3M1.grid(row = 6, column = 2,sticky = W)
S3M2=Entry(window,bg='palegreen',width=6)
S3M2.grid(row = 6, column = 3,sticky = W)
S3M3=Entry(window,bg='palegreen',width=6)
S3M3.grid(row = 6, column = 4,sticky = W)
S3M4=Entry(window,bg='palegreen',width=6)
S3M4.grid(row = 6, column = 5,sticky = W)
S3M5=Entry(window,bg='palegreen',width=6)
S3M5.grid(row = 6, column = 6,sticky = W)
S3M6=Entry(window,bg='palegreen',width=6)
S3M6.grid(row = 6, column = 7,sticky = W)
S3M7=Entry(window,bg='palegreen',width=6)
S3M7.grid(row = 6, column = 8,sticky = W)
S3M8=Entry(window,bg='palegreen',width=6)
S3M8.grid(row = 6, column = 9,sticky = W)
S3M9=Entry(window,bg='palegreen',width=6)
S3M9.grid(row = 6, column = 10,sticky = W)
  
def Result3(a,b,c,d,e,f,g,h,i):
    global s3,t3,k3
    v1,v2,v3,v4,v5,v6,v7,v8,v9=int(a.get()),int(b.get()),int(c.get()),int(d.get()),int(e.get()),int(f.get()),int(g.get()),int(h.get()),int(i.get())
    s3=v1+v2+v3+v4+v5+v6+v7+v8+v9
    t3=v1*8+v2*7+v3*6+v4*5+v5*4+v6*3+v7*2+v8*1+v9*0
    r=t3*(12.5/s3)
    k3=round(r,2)
    Label(window,text=v1*8,width=5,bg='aquamarine').grid(row=7,column=2,sticky=W)
    Label(window,text=v2*7,width=5,bg='aquamarine').grid(row=7,column=3,sticky=W)
    Label(window,text=v3*6,width=5,bg='aquamarine').grid(row=7,column=4,sticky=W)
    Label(window,text=v4*5,width=5,bg='aquamarine').grid(row=7,column=5,sticky=W)
    Label(window,text=v5*4,width=5,bg='aquamarine').grid(row=7,column=6,sticky=W)
    Label(window,text=v6*3,width=5,bg='aquamarine').grid(row=7,column=7,sticky=W)
    Label(window,text=v7*2,width=5,bg='aquamarine').grid(row=7,column=8,sticky=W)
    Label(window,text=v8*1,width=5,bg='aquamarine').grid(row=7,column=9,sticky=W)
    Label(window,text=v9*0,width=5,bg='aquamarine').grid(row=7,column=10,sticky=W)

    Label(window,text=s3,bg="salmon",width=9).grid(row=6,column=11)
    Label(window,text=t3,bg="cornflowerblue",width=9).grid(row=7,column=12)
    Label(window,text=k3,bg="mediumspringgreen",width=9,height=2).grid(row=6,column=13,rowspan=2,sticky = W)
   
S3Btn=Button(window,text="Submit3",command=lambda:Result3(S3M1,S3M2,S3M3,S3M4,S3M5,S3M6,S3M7,S3M8,S3M9)).grid(row=6,column=14,rowspan=2,sticky=E)


#FOURTH SUBJECT

Label(window,text="4",bg='yellow',width=4,height=3).grid(row = 8, column = 0,rowspan=2,sticky = W)

S4=Entry(window,bg='gold',width=8)                       
S4.grid(row = 8, column = 1,rowspan=2,sticky = W)
           
S4M1=Entry(window,bg='palegreen',width=6)
S4M1.grid(row = 8, column = 2,sticky = W)
S4M2=Entry(window,bg='palegreen',width=6)
S4M2.grid(row = 8, column = 3,sticky = W)
S4M3=Entry(window,bg='palegreen',width=6)
S4M3.grid(row = 8, column = 4,sticky = W)
S4M4=Entry(window,bg='palegreen',width=6)
S4M4.grid(row = 8, column = 5,sticky = W)
S4M5=Entry(window,bg='palegreen',width=6)
S4M5.grid(row = 8, column = 6,sticky = W)
S4M6=Entry(window,bg='palegreen',width=6)
S4M6.grid(row = 8, column = 7,sticky = W)
S4M7=Entry(window,bg='palegreen',width=6)
S4M7.grid(row = 8, column = 8,sticky = W)
S4M8=Entry(window,bg='palegreen',width=6)
S4M8.grid(row = 8, column = 9,sticky = W)
S4M9=Entry(window,bg='palegreen',width=6)
S4M9.grid(row = 8, column = 10,sticky = W)
  
def Result4(a,b,c,d,e,f,g,h,i):
    global s4,t4,k4
    v1,v2,v3,v4,v5,v6,v7,v8,v9=int(a.get()),int(b.get()),int(c.get()),int(d.get()),int(e.get()),int(f.get()),int(g.get()),int(h.get()),int(i.get())
    s4=v1+v2+v3+v4+v5+v6+v7+v8+v9
    t4=v1*8+v2*7+v3*6+v4*5+v5*4+v6*3+v7*2+v8*1+v9*0
    r=t4*(12.5/s4)
    k4=round(r,2)
    Label(window,text=v1*8,width=5,bg='aquamarine').grid(row=9,column=2,sticky=W)
    Label(window,text=v2*7,width=5,bg='aquamarine').grid(row=9,column=3,sticky=W)
    Label(window,text=v3*6,width=5,bg='aquamarine').grid(row=9,column=4,sticky=W)
    Label(window,text=v4*5,width=5,bg='aquamarine').grid(row=9,column=5,sticky=W)
    Label(window,text=v5*4,width=5,bg='aquamarine').grid(row=9,column=6,sticky=W)
    Label(window,text=v6*3,width=5,bg='aquamarine').grid(row=9,column=7,sticky=W)
    Label(window,text=v7*2,width=5,bg='aquamarine').grid(row=9,column=8,sticky=W)
    Label(window,text=v8*1,width=5,bg='aquamarine').grid(row=9,column=9,sticky=W)
    Label(window,text=v9*0,width=5,bg='aquamarine').grid(row=9,column=10,sticky=W)

    Label(window,text=s4,bg="salmon",width=9).grid(row=8,column=11)
    Label(window,text=t4,bg="cornflowerblue",width=9).grid(row=9,column=12)
    Label(window,text=k4,bg="mediumspringgreen",width=9,height=2).grid(row=8,column=13,rowspan=2,sticky = W)
  
S4Btn=Button(window,text="Submit4",command=lambda:Result4(S4M1,S4M2,S4M3,S4M4,S4M5,S4M6,S4M7,S4M8,S4M9)).grid(row=8,column=14,rowspan=2,sticky=E)


#FIFTH SUBJECT

Label(window,text="5",bg='yellow',width=4,height=3).grid(row = 10, column = 0,rowspan=2,sticky = W)

S5=Entry(window,bg='gold',width=8)                        
S5.grid(row = 10, column = 1,rowspan=2,sticky = W)
            
S5M1=Entry(window,bg='palegreen',width=6)
S5M1.grid(row = 10, column = 2,sticky = W)
S5M2=Entry(window,bg='palegreen',width=6)
S5M2.grid(row = 10, column = 3,sticky = W)
S5M3=Entry(window,bg='palegreen',width=6)
S5M3.grid(row = 10, column = 4,sticky = W)
S5M4=Entry(window,bg='palegreen',width=6)
S5M4.grid(row = 10, column = 5,sticky = W)
S5M5=Entry(window,bg='palegreen',width=6)
S5M5.grid(row = 10, column = 6,sticky = W)
S5M6=Entry(window,bg='palegreen',width=6)
S5M6.grid(row = 10, column = 7,sticky = W)
S5M7=Entry(window,bg='palegreen',width=6)
S5M7.grid(row = 10, column = 8,sticky = W)
S5M8=Entry(window,bg='palegreen',width=6)
S5M8.grid(row = 10, column = 9,sticky = W)
S5M9=Entry(window,bg='palegreen',width=6)
S5M9.grid(row = 10, column = 10,sticky = W)
  
def Result5(a,b,c,d,e,f,g,h,i):
    global s5,t5,k5
    v1,v2,v3,v4,v5,v6,v7,v8,v9=int(a.get()),int(b.get()),int(c.get()),int(d.get()),int(e.get()),int(f.get()),int(g.get()),int(h.get()),int(i.get())
    s5=v1+v2+v3+v4+v5+v6+v7+v8+v9
    t5=v1*8+v2*7+v3*6+v4*5+v5*4+v6*3+v7*2+v8*1+v9*0
    r=t5*(12.5/s5)
    k5=round(r,2)
    Label(window,text=v1*8,width=5,bg='aquamarine').grid(row=11,column=2,sticky=W)
    Label(window,text=v2*7,width=5,bg='aquamarine').grid(row=11,column=3,sticky=W)
    Label(window,text=v3*6,width=5,bg='aquamarine').grid(row=11,column=4,sticky=W)
    Label(window,text=v4*5,width=5,bg='aquamarine').grid(row=11,column=5,sticky=W)
    Label(window,text=v5*4,width=5,bg='aquamarine').grid(row=11,column=6,sticky=W)
    Label(window,text=v6*3,width=5,bg='aquamarine').grid(row=11,column=7,sticky=W)
    Label(window,text=v7*2,width=5,bg='aquamarine').grid(row=11,column=8,sticky=W)
    Label(window,text=v8*1,width=5,bg='aquamarine').grid(row=11,column=9,sticky=W)
    Label(window,text=v9*0,width=5,bg='aquamarine').grid(row=11,column=10,sticky=W)

    Label(window,text=s5,bg="salmon",width=9).grid(row=10,column=11)
    Label(window,text=t5,bg="cornflowerblue",width=9).grid(row=11,column=12)
    Label(window,text=k5,bg="mediumspringgreen",width=9,height=2).grid(row=10,column=13,rowspan=2,sticky = W)
  
S5Btn=Button(window,text="Submit5",command=lambda:Result5(S5M1,S5M2,S5M3,S5M4,S5M5,S5M6,S5M7,S5M8,S5M9)).grid(row=10,column=14,rowspan=2,sticky=E)


#SIXTH SUBJECT

Label(window,text="6",bg='yellow',width=4,height=3).grid(row = 12, column = 0,rowspan=2,sticky = W)

S6=Entry(window,bg='gold',width=8)                        
S6.grid(row = 12, column = 1,rowspan=2,sticky = W)
            
S6M1=Entry(window,bg='palegreen',width=6)
S6M1.grid(row = 12, column = 2,sticky = W)
S6M2=Entry(window,bg='palegreen',width=6)
S6M2.grid(row = 12, column = 3,sticky = W)
S6M3=Entry(window,bg='palegreen',width=6)
S6M3.grid(row = 12, column = 4,sticky = W)
S6M4=Entry(window,bg='palegreen',width=6)
S6M4.grid(row = 12, column = 5,sticky = W)
S6M5=Entry(window,bg='palegreen',width=6)
S6M5.grid(row = 12, column = 6,sticky = W)
S6M6=Entry(window,bg='palegreen',width=6)
S6M6.grid(row = 12, column = 7,sticky = W)
S6M7=Entry(window,bg='palegreen',width=6)
S6M7.grid(row = 12, column = 8,sticky = W)
S6M8=Entry(window,bg='palegreen',width=6)
S6M8.grid(row = 12, column = 9,sticky = W)
S6M9=Entry(window,bg='palegreen',width=6)
S6M9.grid(row = 12, column = 10,sticky = W)
  
def Result6(a,b,c,d,e,f,g,h,i):
    global s6,t6,k6
    v1,v2,v3,v4,v5,v6,v7,v8,v9=int(a.get()),int(b.get()),int(c.get()),int(d.get()),int(e.get()),int(f.get()),int(g.get()),int(h.get()),int(i.get())
    s6=v1+v2+v3+v4+v5+v6+v7+v8+v9
    t6=v1*8+v2*7+v3*6+v4*5+v5*4+v6*3+v7*2+v8*1+v9*0
    r=t6*(12.5/s6)
    k6=round(r,2)
    Label(window,text=v1*8,width=5,bg='aquamarine').grid(row=13,column=2,sticky=W)
    Label(window,text=v2*7,width=5,bg='aquamarine').grid(row=13,column=3,sticky=W)
    Label(window,text=v3*6,width=5,bg='aquamarine').grid(row=13,column=4,sticky=W)
    Label(window,text=v4*5,width=5,bg='aquamarine').grid(row=13,column=5,sticky=W)
    Label(window,text=v5*4,width=5,bg='aquamarine').grid(row=13,column=6,sticky=W)
    Label(window,text=v6*3,width=5,bg='aquamarine').grid(row=13,column=7,sticky=W)
    Label(window,text=v7*2,width=5,bg='aquamarine').grid(row=13,column=8,sticky=W)
    Label(window,text=v8*1,width=5,bg='aquamarine').grid(row=13,column=9,sticky=W)
    Label(window,text=v9*0,width=5,bg='aquamarine').grid(row=13,column=10,sticky=W)

    Label(window,text=s6,bg="salmon",width=9).grid(row=12,column=11)
    Label(window,text=t6,bg="cornflowerblue",width=9).grid(row=13,column=12)
    Label(window,text=k6,bg="mediumspringgreen",width=9,height=2).grid(row=12,column=13,rowspan=2,sticky = W)
  
S6Btn=Button(window,text="Submit6",command=lambda:Result6(S6M1,S6M2,S6M3,S6M4,S6M5,S6M6,S6M7,S6M8,S6M9)).grid(row=12,column=14,rowspan=2,sticky=E)



#SEVENTH SUBJECT

Label(window,text="7",bg='yellow',width=4,height=3).grid(row = 14, column = 0,rowspan=2,sticky = W)

S7=Entry(window,bg='gold',width=8)                       
S7.grid(row = 14, column = 1,rowspan=2,sticky = W)
            
S7M1=Entry(window,bg='palegreen',width=6)
S7M1.grid(row = 14, column = 2,sticky = W)
S7M2=Entry(window,bg='palegreen',width=6)
S7M2.grid(row = 14,column = 3,sticky = W)
S7M3=Entry(window,bg='palegreen',width=6)
S7M3.grid(row = 14, column = 4,sticky = W)
S7M4=Entry(window,bg='palegreen',width=6)
S7M4.grid(row = 14, column = 5,sticky = W)
S7M5=Entry(window,bg='palegreen',width=6)
S7M5.grid(row = 14, column = 6,sticky = W)
S7M6=Entry(window,bg='palegreen',width=6)
S7M6.grid(row = 14, column = 7,sticky = W)
S7M7=Entry(window,bg='palegreen',width=6)
S7M7.grid(row = 14,column = 8,sticky = W)
S7M8=Entry(window,bg='palegreen',width=6)
S7M8.grid(row = 14, column = 9,sticky = W)
S7M9=Entry(window,bg='palegreen',width=6)
S7M9.grid(row = 14, column = 10,sticky = W)
  
def Result7(a,b,c,d,e,f,g,h,i):
    global s7,t7,k7
    v1,v2,v3,v4,v5,v6,v7,v8,v9=int(a.get()),int(b.get()),int(c.get()),int(d.get()),int(e.get()),int(f.get()),int(g.get()),int(h.get()),int(i.get())
    s7=v1+v2+v3+v4+v5+v6+v7+v8+v9
    t7=v1*8+v2*7+v3*6+v4*5+v5*4+v6*3+v7*2+v8*1+v9*0
    r=t7*(12.5/s7)
    k7=round(r,2)
    Label(window,text=v1*8,width=5,bg='aquamarine').grid(row=15,column=2,sticky=W)
    Label(window,text=v2*7,width=5,bg='aquamarine').grid(row=15,column=3,sticky=W)
    Label(window,text=v3*6,width=5,bg='aquamarine').grid(row=15,column=4,sticky=W)
    Label(window,text=v4*5,width=5,bg='aquamarine').grid(row=15,column=5,sticky=W)
    Label(window,text=v5*4,width=5,bg='aquamarine').grid(row=15,column=6,sticky=W)
    Label(window,text=v6*3,width=5,bg='aquamarine').grid(row=15,column=7,sticky=W)
    Label(window,text=v7*2,width=5,bg='aquamarine').grid(row=15,column=8,sticky=W)
    Label(window,text=v8*1,width=5,bg='aquamarine').grid(row=15,column=9,sticky=W)
    Label(window,text=v9*0,width=5,bg='aquamarine').grid(row=15,column=10,sticky=W)

    Label(window,text=s7,bg="salmon",width=9).grid(row=14,column=11)
    Label(window,text=t7,bg="cornflowerblue",width=9).grid(row=15,column=12)
    Label(window,text=k7,bg="mediumspringgreen",width=9,height=2).grid(row=14,column=13,rowspan=2,sticky = W)
 
S7Btn=Button(window,text="Submit7",command=lambda:Result7(S7M1,S7M2,S7M3,S7M4,S7M5,S7M6,S7M7,S7M8,S7M9)).grid(row=14,column=14,rowspan=2,sticky=E)


#OVERALL RESULT

Label(window,text="TOTAL-->",bg='mediumorchid',width=12).grid(row = 16, column = 0,columnspan = 2,sticky = W)

def makegraph():
    x=[S1.get(),S2.get(),S3.get(),S4.get(),S5.get(),S6.get(),S7.get()]
    y=[k1,k2,k3,k4,k5,k6,k7]
    c=['r','y','g','c','b','m','b']
    rects1=m.bar(x,y,width=0.5,color=c)
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            m.text(rect.get_x() + rect.get_width()/2., 1.05*height, '%2.2f' % float(height),ha='center', va='bottom')
    autolabel(rects1)
    m.xlabel("subject")
    m.ylabel("PI")
    m.title("Graph: PI vs Subject")
    m.show()
    
def Result():
    global N
    Label(window,text="Enter",bg='pink').grid(row=17,column=0,sticky=E)
    Label(window,text="number",bg='pink').grid(row=17,column=1)
    Label(window,text="of",bg='pink').grid(row=17,column=2,sticky=W)
    Label(window,text="Students:",bg='pink').grid(row=18,column=1)

    N=Entry(window,width=6)
    N.grid(row=17,column=3)
    
    lastbtn=Button(window,text="submit",command=lambda:Final_Result()).grid(row=17,column=5)
def Final_Result():
    T1=int(S1M1.get())+int(S2M1.get())+int(S3M1.get())+int(S4M1.get())+int(S5M1.get())+int(S6M1.get())+int(S7M1.get())
    T2=int(S1M2.get())+int(S2M2.get())+int(S3M2.get())+int(S4M2.get())+int(S5M2.get())+int(S6M2.get())+int(S7M2.get())
    T3=int(S1M3.get())+int(S2M3.get())+int(S3M3.get())+int(S4M3.get())+int(S5M3.get())+int(S6M3.get())+int(S7M3.get())
    T4=int(S1M4.get())+int(S2M4.get())+int(S3M4.get())+int(S4M4.get())+int(S5M4.get())+int(S6M4.get())+int(S7M4.get())
    T5=int(S1M5.get())+int(S2M5.get())+int(S3M5.get())+int(S4M5.get())+int(S5M5.get())+int(S6M5.get())+int(S7M5.get())
    T6=int(S1M6.get())+int(S2M6.get())+int(S3M6.get())+int(S4M6.get())+int(S5M6.get())+int(S6M6.get())+int(S7M6.get())
    T7=int(S1M7.get())+int(S2M7.get())+int(S3M7.get())+int(S4M7.get())+int(S5M7.get())+int(S6M7.get())+int(S7M7.get())
    T8=int(S1M8.get())+int(S2M8.get())+int(S3M8.get())+int(S4M8.get())+int(S5M8.get())+int(S6M8.get())+int(S7M8.get())
    T9=int(S1M9.get())+int(S2M9.get())+int(S3M9.get())+int(S4M9.get())+int(S5M9.get())+int(S6M9.get())+int(S7M9.get())
    S=s1+s2+s3+s4+s5+s6+s7
    T=t1+t2+t3+t4+t5+t6+t7
    n=int(N.get())
    R=T*(2.5/n)
    K=round(R,2)
    Label(window,text=T1,width=5,bg='lightcyan').grid(row=16,column=2,sticky=W)                                     
    Label(window,text=T2,width=5,bg='lightcyan').grid(row=16,column=3,sticky=W)
    Label(window,text=T3,width=5,bg='lightcyan').grid(row=16,column=4,sticky=W)
    Label(window,text=T4,width=5,bg='lightcyan').grid(row=16,column=5,sticky=W)
    Label(window,text=T5,width=5,bg='lightcyan').grid(row=16,column=6,sticky=W)
    Label(window,text=T6,width=5,bg='lightcyan').grid(row=16,column=7,sticky=W)
    Label(window,text=T7,width=5,bg='lightcyan').grid(row=16,column=8,sticky=W)
    Label(window,text=T8,width=5,bg='lightcyan').grid(row=16,column=9,sticky=W)
    Label(window,text=T9,width=5,bg='lightcyan').grid(row=16,column=10,sticky=W)

    Label(window,text=S,bg="lightskyblue",width=9).grid(row=16,column=11)
    Label(window,text=T,bg="lightskyblue",width=9).grid(row=16,column=12)
    Label(window,text=K,bg="lightskyblue",width=9,height=2).grid(row=16,column=13,sticky = W)

    
    Label(window,text="click",bg='pink').grid(row=19,column=0,sticky=E)
    Label(window,text="to display",bg='pink').grid(row=19,column=1)
    Label(window,text="graph",bg='pink').grid(row=19,column=2)
    Label(window,text="of:",bg='pink').grid(row=19,column=3,sticky=W)
    Label(window,text="PI vs",bg='pink').grid(row=19,column=4,sticky=E)
    Label(window,text="Subject",bg='pink').grid(row=19,column=5,sticky=W)
    btn=Button(window,text="Click",command=lambda:makegraph()).grid(row=19,column=7)
    
FinalBtn=Button(window,text="Overall RESULT",command=lambda:Result()).grid(row=16,column=14,sticky=E)

window.mainloop()

