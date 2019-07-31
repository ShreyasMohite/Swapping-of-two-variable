import tkinter
from tkinter import *
import tkinter.messagebox



class swap:
     def __init__(self,root):
          self.root=root
          self.root.title("Swapping")
          self.root.geometry("1250x650")


          A=IntVar( )
          B=IntVar( )
          C=IntVar( )
          D=IntVar( )
          E=IntVar( )
          F=IntVar( )

#===========================def=========================
          def iExit( ):
              iExit=tkinter.messagebox.askyesnocancel("Question","confirm if you want to exit")
              if iExit > 0:
                  root.destroy( )
                  return

          def SW( ):
                W=int(self.AA.get( ))
                X=int(self.BB.get( ))
                if int(W)%3==0 & int(X)%3==0:
                     temp=W
                     W=X
                     X=temp
                     D.set(W)
                     E.set(X)
                elif int(W)%3!=0 & int(X)%3==0:
                     e=tkinter.messagebox.askretrycancel("question","The given input is not divisible by 3 retry if you want",icon="error")
                     if e==True:
                          W=int(self.AA.get( ))
                          X=int(self.BB.get( ))
                         
                elif int(X)%3!=0 & int(W)%3==0:
                      e=tkinter.messagebox.askretrycancel("question",'the number is not divisible by 3 retry if you want',icon="error")
                      if e==True:
                          W=int(self.AA.get( ))
                          X=int(self.BB.get( ))
                     
                else:
                          pass
                         
                
          def display( ):
               TXT.insert(END,"BEFORE SWAPPING \t\t\t AFTER SWAPPING \n\n ")
               TXT.insert(END,'A=\t' +  self.AA.get( )+'\t\t'+'A=\t'+  self.AA1.get() + "\n\n",END,'B=\t' +  self.BB.get( )+'\t\t'+'B=\t' + self.BB1.get( ) +"\n\n")
               
          def clear( ):
               self.AA.delete(0,END)
               self.AA1.delete(0,END)
               self.BB.delete(0,END)
               self.BB1.delete(0,END)
               

          def cont( ):
               no=0
               w=int(self.E1.get( ))
               while True:
                     W=int(self.AA.get( ))
                     X=int(self.BB.get( ))
                     if int(W)%3==0 & int(X)%3==0:
                          temp=W
                          W=X
                          X=temp
                          D.set(W)
                          E.set(X)
                          TXT.insert(END,"THE ATTEMTS ARE\t:"+self.E1.get( )+"\n\n")
                          TXT.insert(END,"BEFORE SWAPPING          AFTER SWAPPING\n\n")
                          TXT.insert(END,'A=\t'+ self.AA.get( )+'\t\tA=\t'+self.AA1.get( )+"\n\n",END,'B=\t'+ self.BB.get ( )+'\t\tB=\t'+ self.BB1.get ( )+"\n\n")
                          w=int(w)-1
                          F.set(w)
                          C.set(w)
                          TXT.insert(END,"attempt remanin:"+ self.E2.get( )+"\n\n")
                          self.AA.delete(0,END)
                          self.AA1.delete(0,END)
                          self.BB.delete(0,END)
                          self.BB1.delete(0,END)
                          if int(w)==int(no):
                                e=tkinter.messagebox.askyesno("question","your all attempts are over do you want to continue",icon="question")
                                if e==True:
                                    w=int(self.E1.get( ))
                                    self.AA.delete(0,END)
                                    self.AA1.delete(0,END)
                                    self.BB.delete(0,END)
                                    self.BB1.delete(0,END)
                                    self.E1.delete(0,END)
                                    self.E2.delete(0,END)
                                else:
                                    break
                         
                     elif int(W)%3!=0 & int(X)%3==0:
                          e=tkinter.messagebox.askretrycancel("question",'The given input is not divisible by 3 retry if you want',icon="error")
                          if e==False:
                              w=int(self.E1.get( ))
                              w=int(w)-1
                              F.set(w)
                              TXT.insert(END,"attempt remanin:"+ self.E2.get( )+"\n\n")
                              C.set(w)
                              self.AA.delete(0,END)
                              self.AA1.delete(0,END)
                              self.BB.delete(0,END)
                              self.BB1.delete(0,END)
                              if int(w)==int(no):
                                  e=tkinter.messagebox.askyesno("Question","Your all attempts are over do you want to continue",icon="question")
                                  if e==True:
                                    w=int(self.E1.get( ))
                                    self.AA.delete(0,END)
                                    self.AA1.delete(0,END)
                                    self.BB.delete(0,END)
                                    self.BB1.delete(0,END)
                                    self.E1.delete(0,END)
                                    self.E2.delete(0,END)
                                  else:
                                      break
                          else:
                               break
                     elif int(W)%3==0 & int(X)%3!=0:
                          e=tkinter.messagebox.askretrycancel("question",'The given input is not divisible by 3 retry if you want',icon="error")
                          if e==False:
                              w=int(self.E1.get( ))
                              w=int(w)-1
                              F.set(w)
                              TXT.insert(END,"attempt remanin are:"+ self.E2.get( )+"\n\n")
                              C.set(w)
                              self.AA.delete(0,END)
                              self.AA1.delete(0,END)
                              self.BB.delete(0,END)
                              self.BB1.delete(0,END)
                              if int(w)==int(no):
                                  e=tkinter.messagebox.askyesno("Question","Your all attempts are over do you want to continue",icon="question")
                                  if e==True:
                                    w=int(self.E1.get( ))
                                    self.AA.delete(0,END)
                                    self.AA1.delete(0,END)
                                    self.BB.delete(0,END)
                                    self.BB1.delete(0,END)
                                    self.E1.delete(0,END)
                                    self.E2.delete(0,END)
                                  else:
                                      break
                                
                          else:
                            break
                              
          def erase( ):
              TXT.delete("1.0",END)
                

#===================Frame================================
          F1=Frame(self.root,relief=RIDGE,bg="yellow")
          F1.pack( )
          F2=Frame(F1,relief=RIDGE,bg="honeydew2",bd=18,width=1350,height=110)
          F2.pack( )
          F3=Frame(F1,relief=RIDGE,bg="cornsilk2",bd=18,width=950,height=650,padx=40,pady=60)
          F3.pack(side=LEFT)
          F4=Frame(F1,relief=RIDGE,bg="snow2",bd=22,width=550,height=650,padx=30,pady=40)
          F4.pack(side=RIGHT)
          F5=Frame(F3,relief=RIDGE,bd=18,width=550,height=150,bg="grey",padx=50,pady=10)
          F5.pack(side=TOP)
          F6=Frame(F3,relief=RIDGE,bd=18,width=550,height=150,padx=30,pady=20,bg="powder blue")
          F6.pack(side=BOTTOM)
          
#====================Label==================================
          LAb=Label(F2,text="                            SWAPPING OF TWO VARAIBLE                      ",font=("arial",36),bg="honeydew2")
          LAb.pack( )
          La1=Label(F5,text="          A         "  ,font=("arial",16,"bold"),fg="black",bg="red")
          La1.grid(row=0,column=0)
          La2=Label(F5,text="          A         "  ,font=("arial",16,"bold"),fg="black",bg="snow")
          La2.grid(row=0,column=2)
          Lc=Label(F5,bg="grey")
          Lc.grid(row=1,column=0)
          Lc=Label(F5,bg="grey")
          Lc.grid(row=2,column=0)
          Lb1=Label(F5,text="         B           ",font=("arial",16,"bold"),fg="black",bg="gold")
          Lb1.grid(row=3,column=0)
          Lb2=Label(F5,text="         B           ",font=("arial",16,"bold"),fg="black",bg="snow")
          Lb2.grid(row=3,column=2)
          Lc=Label(F5,bg="grey")
          Lc.grid(row=4,column=0)
          Lc=Label(F5,bg="grey")
          Lc.grid(row=5,column=0)
          LAT=Label(F5,text="       ATTEMPT       ",font=("arial",16,"bold"),fg="black",bg="silver")
          LAT.grid(row=6,column=0)
          LAT=Label(F5,text="      REMAIN       ",font=("arial",16,"bold"),fg="black",bg="silver")
          LAT.grid(row=6,column=2)
          Lc=Label(F5,bg="grey")
          Lc.grid(row=7,column=0)
          Lc=Label(F5,bg="grey")
          Lc.grid(row=8,column=0)
          
          
#========================Entry================================
          self.AA=Entry(F5,textvariable=A,fg="red",width=20,relief=RIDGE,bd=12,font=("arial",10,"bold"),bg="powder blue")
          self.AA.grid(row=0,column=1)
          self.AA1=Entry(F5,textvariable=D,fg="black",width=20,relief=RIDGE,bd=12,font=("arial",10,"bold"),bg="powder blue")
          self.AA1.grid(row=0,column=3)
          self.BB=Entry(F5,textvariable=B,fg="black",width=20,relief=RIDGE,bd=12,font=("arial",10,"bold"),bg="powder blue")
          self.BB.grid(row=3,column=1)
          self.BB1=Entry(F5,textvariable=E,fg="red",width=20,relief=RIDGE,bd=12,font=("arial",10,"bold"),bg="powder blue")
          self.BB1.grid(row=3,column=3)
          self.E1=Entry(F5,textvariable=C,fg="black",width=20,relief=RIDGE,bd=12,font=("arial",10,"bold"),bg="powder blue")
          self.E1.grid(row=6,column=1)
          self.E2=Entry(F5,textvariable=F,fg="black",width=20,relief=RIDGE,bd=12,font=("arial",10,"bold"),bg="powder blue")
          self.E2.grid(row=6,column=3)


#=========================Button==============================
          B1=Button(F6,text="Look out",command=SW,font=("arial",12,"bold"),width=10,height=3,relief='raise',bd=5,bg="light cyan")
          B1.grid(row=0,column=1)
          Lc=Label(F6)
          Lc.grid(row=0,column=2)
          B2=Button(F6,text="DISPLAY",command=display,font=("arial",12,"bold"),width=10,height=3,relief='raise',bd=5,bg="light cyan")
          B2.grid(row=0,column=3,sticky=W)
          Lc=Label(F6)
          Lc.grid(row=0,column=4)
          B3=Button(F6,text="Swap",command=cont,font=("arial",12,"bold"),width=10,height=3,relief='raise',bd=5,bg="light cyan")
          B3.grid(row=0,column=5,sticky=W)
          Lc=Label(F6)
          Lc.grid(row=0,column=6)
          B4=Button(F6,text="CLEAR",command=clear,font=("arial",12,"bold"),width=10,height=3,relief='raise',bd=5,bg="light cyan")
          B4.grid(row=0,column=7,sticky=W)
          Lc=Label(F6)
          Lc.grid(row=0,column=8)
          B5=Button(F6,text="Erase",command=erase,font=("arial",12,"bold"),width=10,height=3,relief='raise',bd=5,bg="light cyan")
          B5.grid(row=0,column=9,sticky=W)
          Lc=Label(F6)
          Lc.grid(row=0,column=10)
          B6=Button(F6,text="EXIT",command=iExit,font=("arial",12,"bold"),width=10,height=3,relief='raise',bd=5,bg="light cyan")
          B6.grid(row=0,column=11,sticky=W)


#==============================TEXT & scrollbar=================================
          scroll=Scrollbar(F4)
          scroll.pack(side=RIGHT,fill=Y)
          ab=Label(F4,font=('arial',14,'bold'),text="     SWAPPING    ",fg='peachpuff4').pack( )
          TXT=Text(F4, width=45,height=29,font=('arial',9,'bold'),bd=8,bg="gray95",relief=RIDGE,fg="red",yscrollcommand=scroll.set)
          TXT.pack( )
          scroll.config(command=TXT.yview)

          




if __name__=='__main__':
     root=Tk( )
     application=swap(root)
     root.mainloop( )
