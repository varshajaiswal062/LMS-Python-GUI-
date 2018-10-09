from tkinter import *
import tkinter.messagebox
import datetime
from tkinter import filedialog



class project():
    password="x"
    identity="x"

    def __init__(self,master,a):
        self.login=master
        self.e3=a

        def Login():

            username = entry1.get()
            password = entry2.get()
            if (username == "varshakjssc@somaiya.edu" and password == "varsha12345") or (
                    username == "yuvrajkjssc@somaiya.edu" and password == "yuvraj12345"):
                pass

            else:
                invalid = Tk()
                invalid.geometry("300x200")
                label = Label(invalid, text="Invalid login").pack()
                invalid.mainloop()

    rootA = Tk()
    rootA.title("Login")
    rootA.geometry("300x200")

    username = StringVar()
    password = StringVar()

    label1 = Label(rootA, text="Enter the Username")
    label1.grid(row=2, column=1, sticky=W)
    entry1 = Entry(rootA)
    entry1.grid(row=2, column=2)
    entry1.focus()

    label2 = Label(rootA, text="Enter the Password")
    label2.grid(row=4, column=1, sticky=W)
    entry2 = Entry(rootA, show="*")
    entry2.grid(row=4, column=2)
    entry2.focus()

    LoginB = Button(rootA, text="Login", font=20, command=Login)
    LoginB.grid(row=6, column=2, sticky=W)

    rootA.mainloop()


def hompage(self):

        self.homepage.title("K.J.SOMAIYA COLLEGE OF SCIENCE AND COMMERES")
        self.homepage.geometry("800x800")

        self.menubar = Menu(homepage)
        self.listone = Menu(homepage)
        self.listtwo = Menu(homepage)
        self.listthree = Menu(homepage)

        self.menubar.add_cascade(label="DIRECTORIES", menu=self.listone)
        self.listone.add_command(label="CATEGORY", command=self.categories)
        self.listone.add_command(label="OPEN",command=self.open)
        self.listone.add_command(label="EXIT",command=self.quit)

        self.menubar.add_cascade(label="TRASCATIONS", menu=self.listtwo)
        self.listtwo.add_command(label="FINE",command=self.fine)


        self.menubar.add_cascade(label="LOGGEDIN_INFO", menu=self.listthree)
        self.listthree.add_command(label="STUDENT")


        self.homepage.config(menu=self.menubar)
        ''''label = Label(homepage, text="To issue a book follow simple steps", font=("arial", 16, "bold")).grid(row=0, column=2)
        label = Label(homepage, text="Step1.Go to Directories ", font=("arial", 16, "bold")).grid(row=1, column=2)
        label = Label(homepage, text="Step2.Click on category", font=("arial", 16, "bold")).grid(row=2, column=2)
        label = Label(homepage, text="Step3.select the book", font=("arial", 16, "bold")).grid(row=3, column=2)'''
        photo=PhotoImage(file="svv_(2).png")
        label=Label(homepage,image=photo).pack()
    def categories(self):
        cat=Tk()
        cat.geometry("300x300")
        cat.title("Categories of boosks")
        self.btn1=Button(cat,text="1.Physics",relief="flat",cursor="circle",command=self.physics).grid(row=0,column=1,sticky=W)
        self.btn2=Button(cat,text="2.Chemistry",relief="flat",cursor="circle",command=self.chemistry).grid(row=1,column=1,sticky=W)
        self.btn3=Button(cat,text="3.Biology",relief="flat",cursor="circle",command=self.biology).grid(row=2,column=1,sticky=W)
        self.btn4=Button(cat,text="4.Information technology",relief="flat",cursor="circle",command=self.information_tech).grid(row=3,column=1,sticky=W)
        self.btn5=Button(cat,text="5.Novel",relief="flat",cursor="circle",command=self.novel).grid(row=4,column=1,sticky=W)
        cat.mainloop()

    def physics(self):
        phy=Tk()
        phy.geometry("400x400")
        phy.title("Physics books")
        self.btn1=Button(phy,text="1.Circular motion",cursor="circle",relief="flat",command=self.issue).grid(row=0,column=1,sticky=W)
        self.btn2=Button(phy,text="2.Gravitation",cursor="circle",relief="flat",command=self.issue).grid(row=1,column=1,sticky=W)
        self.btn3=Button(phy,text="3.Rotational motion",cursor="circle",relief="flat",command=self.issue).grid(row=2,column=1,sticky=W)
        self.btn4=Button(phy,text="4.Elasticity",cursor="circle",relief="flat",command=self.issue).grid(row=3,column=1,sticky=W)
        self.btn5=Button(phy,text="5.Surface tension",cursor="circle",relief="flat",command=self.issue).grid(row=4,column=1,sticky=W)
        self.btn6 =Button(phy, text="6.Wave motion", cursor="circle", relief="flat", command=self.issue).grid(row=5,column=1,sticky=W)
        self.btn7 =Button(phy, text="7.Stationary waves", cursor="circle", relief="flat", command=self.issue).grid(row=6,column=1,sticky=W)
        self.btn8 =Button(phy, text="8.Magnetisum", cursor="circle", relief="flat", command=self.issue).grid(row=7,column=1,sticky=W)
        self.btn9 =Button(phy, text="9.Semiconductor", cursor="circle", relief="flat", command=self.issue).grid(row=8,column=1,sticky=W)
        self.btn10 =Button(phy, text="10.Electrostatics", cursor="circle", relief="flat", command=self.issue).grid(row=9,column=1,sticky=W)
        phy.mainloop()

    def chemistry(self):
        chem=Tk()
        chem.geometry("400x400")
        chem.title("Chemistry books")
        self.btn1=Button(chem,text="1.Halogen derivatives of alkenes",cursor="circle",relief="flat",command=self.issue).grid(row=0,column=1,sticky=W)
        self.btn2=Button(chem,text="2.Nature od chemical bonding",cursor="circle",relief="flat",command=self.issue).grid(row=1,column=1,sticky=W)
        self.btn3=Button(chem,text="3.Thermodynamics",cursor="circle",relief="flat",command=self.issue).grid(row=2,column=1,sticky=W)
        self.btn4=Button(chem,text="4.Electrochemistry",cursor="circle",relief="flat",command=self.issue).grid(row=3,column=1,sticky=W)
        self.btn5=Button(chem,text="5.Alcohol,Phenol,Aldehyde",cursor="circle",relief="flat",command=self.issue).grid(row=4,column=1,sticky=W)
        self.btn6=Button(chem, text="6.Co-ordinate geometry", cursor="circle", relief="flat", command=self.issue).grid(row=5,column=1,sticky=W)
        self.btn7=Button(chem, text="7.P-block", cursor="circle", relief="flat", command=self.issue).grid(row=6,column=1,sticky=W)
        self.btn8=Button(chem, text="8.Solid state", cursor="circle", relief="flat", command=self.issue).grid(row=7, column=1, sticky=W)
        self.btn9=Button(chem, text="9.Chemical kinetics", cursor="circle", relief="flat", command=self.issue).grid(row=8, column=1, sticky=W)
        self.btn10=Button(chem, text="10.Collegative properties", cursor="circle", relief="flat", command=self.issue).grid(row=9, column=1, sticky=W)
        self.btn11=Button(chem, text="11.Ethers ", cursor="circle", relief="flat", command=self.issue).grid(row=10, column=1, sticky=W)
        chem.mainloop()

    def biology(self):
        bio=Tk()
        bio.geometry("400x400")
        bio.title("Biology books")
        self.btn1=Button(bio,text="1.Photosynthesis",cursor="circle",relief="flat",command=self.issue).grid(row=0,column=1,sticky=W)
        self.btn2=Button(bio,text="2.Flower morphology",cursor="circle",relief="flat",command=self.issue).grid(row=1,column=1,sticky=W)
        self.btn3=Button(bio,text="3.Kingdom animalia",cursor="circle",relief="flat",command=self.issue).grid(row=2,column=1,sticky=W)
        self.btn4=Button(bio,text="4.Human reproduction",cursor="circle",relief="flat",command=self.issue).grid(row=3,column=1,sticky=W)
        self.btn5=Button(bio,text="5.Human bones",cursor="circle",relief="flat",command=self.issue).grid(row=4,column=1,sticky=W)
        self.btn6=Button(bio, text="6.Origin of species", cursor="circle", relief="flat", command=self.issue).grid(row=5, column=1, sticky=W)
        self.btn7=Button(bio, text="7.The cell", cursor="circle", relief="flat", command=self.issue).grid(row=6,column=1,sticky=W)
        self.btn5=Button(bio, text="8.Parasite", cursor="circle", relief="flat", command=self.issue).grid(row=7, column=1, sticky=W)
        self.btn5=Button(bio, text="9.The selfish gene", cursor="circle", relief="flat", command=self.issue).grid(row=8, column=1, sticky=W)
        self.btn5=Button(bio, text="10.Kingdom plante", cursor="circle", relief="flat", command=self.issue).grid(ow=9, column=1, sticky=W)
        bio.mainloop()

    def information_tech(self):
        info=Tk()
        info.geometry("400x400")
        info.title("Information technology")
        self.btn1=Button(info,text="1.Python",cursor="circle",relief="flat",command=self.issue).grid(row=0,column=1,sticky=W)
        self.btn2=Button(info,text="2.Let us C++",cursor="circle",relief="flat",command=self.issue).grid(row=1,column=1,sticky=W)
        self.btn3=Button(info,text="3.Java script",cursor="circle",relief="flat",command=self.issue).grid(row=2,column=1,sticky=W)
        self.btn4=Button(info,text="4.Programmming with C",cursor="circle",relief="flat",command=self.issue).grid(row=3,column=1,sticky=W)
        self.btn5=Button(info,text="5.Kotlin",cursor="circle",relief="flat",command=self.issue).grid(row=4,column=1,sticky=W)
        self.btn6=Button(info,text="6.PHP the server side language",cursor="circle",relief="flat",command=self.issue).grid(row=5,column=1,sticky=W)
        self.btn7=Button(info,text="7.Ruby", cursor="circle", relief="flat", command=self.issue).grid(row=6,column=1,sticky=W)
        self.btn8=Button(info,text="8.Core java", cursor="circle", relief="flat", command=self.issue).grid(row=7,column=1,sticky=W)
        self.btn9=Button(info,text="9.HTML/CSS", cursor="circle", relief="flat", command=self.issue).grid(row=8,column=1,sticky=W)
        self.btn10=Button(info,text="10.Rust", cursor="circle", relief="flat", command=self.issue).grid(row=9,column=1,sticky=W)
        info.mainloop()

    def novel(self):
        nov=Tk()
        nov.geometry("400x400")
        nov.title("Novel")
        self.btn1=Button(nov,text="1.Anna karenina",cursor="circle",relief="flat",command=self.issue).grid(row=0,column=1,sticky=W)
        self.btn2=Button(nov,text="2.To kill a mock-ingbird",cursor="circle",relief="flat",command=self.issue).grid(row=1,column=1,sticky=W)
        self.btn3=Button(nov,text="3.The great gatsby", cursor="circle",relief="flat",command=self.issue).grid(row=2,column=1,sticky=W)
        self.btn4=Button(nov,text="4.Stranger things",cursor="circle",relief="flat",command=self.issue).grid(row=3,column=1,sticky=W)
        self.btn5=Button(nov,text="5.The load of the ring",cursor="circle",relief="flat",command=self.issue).grid(row=4,column=1,sticky=W)
        self.btn6=Button(nov,text="6.Beloved", cursor="circle", relief="flat", command=self.issue).grid(row=5,column=1,sticky=W)
        self.btn7=Button(nov,text="7.Suicide squad", cursor="circle", relief="flat", command=self.issue).grid(row=6,column=1,sticky=W)
        self.btn8=Button(nov,text="8.Narcos", cursor="circle", relief="flat", command=self.issue).grid(row=7,column=1,sticky=W)
        nov.mainloop()


    def issue(self):
        issue = Tk()
        issue.geometry("300x200")
        issue.title("Issuing a book")

        label=Label(issue,text="Username")
        label.grid(row=0,column=0,sticky=W)
        self.mail= Entry(issue)
        self.mail.grid(row=0,column=1)

        labe11=Label(issue,text="Password").grid(row=1,column=0,sticky=W)
        self.passw=Entry(issue)
        self.passw.grid(row=1,column=1)

        self.sub = Button(issue, text="Submit",command= self.checkinfo).grid(row=5, column=2, sticky=W)

        #self.forpass=Button(issue,text="Forgot password",command=self.forgot).grid(row=6,column=1,sticky=W)

        issue.mainloop()

    def checkinfo(self):
        identity=self.mail.get()
        password=self.passw.get()





        d1 = {"1420101": {"email_id": "varsha", "password": "12345"},
              "1420102": {"email_id": "jerry", "password": "34567"},
              "1420103": {"email_id": "tommy", "password": "143567"},
              "1420104": {"email_id": "harley", "password": "12513783"}}
        for i in d1:
            if (identity == d1[i]['email_id']) and (password == d1[i]['password']):
                log=Tk()
                log.geometry("200x80")
                log.title("BOKK ISSUED")
                label=Label(log,text="BOOK ISSIUED!!!!!!!",font=("arial",8,"bold")).pack()
                log.mainloop()
                break

            else :
                wrong=Tk()
                wrong.geometry("200x80")
                label=Label(wrong,text="Wrong password or username",font=("arial",8,"bold")).pack()
                wrong.mainloop()

    def open(self):
        filename=filedialog.askopenfilename()


    def quit(self):
        answer=tkinter.messagebox.askyesno(title="Quit",message="Are you sure you want to exit")
        if answer:
            homepage.quit()

    #def display(self):
        #with open("datasave.txt","a")as f:
            #f.write(identity)


    def fine(self):
        fine=Tk()
        fine.geometry("300x150")
        fine.title("Fine Rules")
        label=Label(fine,text="1.From te date of issue the due is after 7 day").grid()
        label=Label(fine,text="2.After 7th day the library fine will be applied").grid()
        label=Label(fine,text="3.Fine per day is 2rs, so kindly return the book  ").grid()

        fine.mainloop()




login=Tk()
login.geometry("300x300")
p=project(login,0)
login.mainloop()



