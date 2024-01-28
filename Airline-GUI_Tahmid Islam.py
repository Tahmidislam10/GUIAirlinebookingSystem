from tkinter import*
from tkinter import messagebox

tahmid=Tk()

tahmid.geometry("700x700")
tahmid.title("Tahmid's Airline")
tahmid.resizable(False,False)

seats_available = 152
adult_ticket = 120
child_ticket = 60
all_adult = 0
all_child = 0
all_adultp = 0
all_childp = 0
all_price = 0
all_seats = 0
seat = 0


def Cal():
    
    global seats_available
    global adult_price
    global all_adult
    global all_child
    global all_adultp
    global all_childp
    global all_price
    global all_seats

 

    adult = int(adult_num.get())
    child = int(child_num.get())

 


    if adult + child > seats_available:
        
        result=messagebox.showerror(title="Overbooked",message="You have reached max booking capacity")

 

    elif adult + child <= seats_available:

 

        
        adult_price = adult * (adult_ticket)
        child_price =  child * (child_ticket)
        total = adult_price + child_price
        seat = child + adult
        
        all_adult = all_adult + adult
        all_child = all_child + child
        all_adultp = all_adultp + adult_price
        all_childp = all_childp + child_price
        all_price = all_price + (adult_price + child_price)
        all_seats = all_seats + (adult + child)
        

 
        labe7=Label(tahmid,text="------------------------------------------",fg='blue').grid(row=8,column=1)
        labe7=Label(tahmid,text="Session Summary: ",fg='red').grid(row=9,column=1)

        labe7=Label(tahmid,text="Your Forename: %s"%forname.get(),fg='green').grid(row=10,column=1)
        labe7=Label(tahmid,text="Your Surname: %s"%surname.get(),fg='green').grid(row=11,column=1)
        labe7=Label(tahmid,text="Adult tickets booked: %.F"%adult,fg='green').grid(row=12,column=1)
        labe8=Label(tahmid,text="Price for adult tickets booked £%.2F"%adult_price,fg='green').grid(row=13,column=1)
        labe9=Label(tahmid,text="Child tickets booked: %.F"%child,fg='green').grid(row=14,column=1)
        labe10=Label(tahmid,text="Price for child tickets booked £%.2F"%child_price,fg='green').grid(row=15,column=1)
        labe11=Label(tahmid,text="Total price: £%.2F"%total,fg='blue').grid(row=16,column=1)
        seats_available = seats_available - seat
        labe3=Label(tahmid,text="Seats left: %.F"%seats_available,fg='blue').grid(row=17,column=1)
        
        
        labe11=Label(tahmid,text="Seats booked: %.F"%seat,fg='blue').grid(row=18,column=1)



def final():
    global adult_price
    global all_adult
    global all_child
    global all_adultp
    global all_childp
    global all_price
    global all_seats

    labe7=Label(tahmid,text="------------------------------------------",fg='blue').grid(row=19,column=1)
    
    labe7=Label(tahmid,text="Final Summary:",fg='red').grid(row=20,column=1)
    labe7=Label(tahmid,text="Total adult tickets booked: %.2F"%all_adult,fg='green').grid(row=21,column=1)
    labe9=Label(tahmid,text="Total child ticket booked: %.2F"%all_child,fg='green').grid(row=22,column=1)
    labe10=Label(tahmid,text="Price for adult tickets booked: £%.2F"%all_adultp,fg='green').grid(row=23,column=1)
    labe10=Label(tahmid,text="Price for child tickets booked: £%.2F"%all_childp,fg='green').grid(row=24,column=1)
    labe11=Label(tahmid,text="Total Price: £%.2F"%all_price,fg='blue').grid(row=25,column=1)
    labe11=Label(tahmid,text="Total Seats booked: %.F"%all_seats,fg='blue').grid(row=26,column=1)



    

   
    

     




    
        

adult_num=StringVar()
child_num=StringVar()
forname=StringVar()
surname=StringVar()

labe1=Label(tahmid,text="✈Welcome to Tahmid Airlines✈",fg='red').grid(row=0,column=1)
labe2=Label(tahmid,text="💸Price: Adult £120 Child £60",fg='green').grid(row=1,column=1)

labe8=Label(tahmid,text="Please enter your Forename",fg='blue').grid(row=3,column=0)
labe9=Label(tahmid,text="Please enter your Surname",fg='blue').grid(row=4,column=0)
labe4=Label(tahmid,text="Please enter your Adult Seats",fg='blue').grid(row=5,column=0)
labe5=Label(tahmid,text="Please enter your Child Seats",fg='blue').grid(row=6,column=0)
labe3=Label(tahmid,text="🪑Seats Available: 152",fg='red').grid(row=2,column=1)
labe6=Label(tahmid,text="Reservations:",fg='red').grid(row=7,column=1)

entry1=Entry(tahmid,textvariable=forname).grid(row=3,column=1)
entry1=Entry(tahmid,textvariable=surname).grid(row=4,column=1)
entry1=Entry(tahmid,textvariable=adult_num).grid(row=5,column=1)
entry2=Entry(tahmid,textvariable=child_num).grid(row=6,column=1)

button=Button(tahmid,text="Calculate",command=Cal,fg='red').grid(row=3,column=3)
button=Button(tahmid,text="Final Summary",command=final,fg='red').grid(row=4,column=3)
button=Button(tahmid,text="Clear",command=tahmid.destroy,fg='red').grid(row=5,column=3)

menubar=Menu(tahmid)

filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New file")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save as")
filemenu.add_command(label="Print")
filemenu.add_command(label="Close",command=tahmid.destroy)
menubar.add_cascade(label='File',menu=filemenu)
tahmid.config(menu=menubar)                 

filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="Undo")
filemenu.add_command(label="Redo")
filemenu.add_command(label="Cut")
filemenu.add_command(label="Copy")
filemenu.add_command(label="Paste")
menubar.add_cascade(label='Edit',menu=filemenu)
tahmid.config(menu=menubar)                 

filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="Format Paragraph")
filemenu.add_command(label="Indent Region")
filemenu.add_command(label="Dedent Region ")
filemenu.add_command(label="Comment Out Region")
filemenu.add_command(label="Uncomment Region")
filemenu.add_command(label="Toggle Tabs")
menubar.add_cascade(label='Format',menu=filemenu)
tahmid.config(menu=menubar)

filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="Run Module")
filemenu.add_command(label="Run Customized ")
filemenu.add_command(label="Check Module")
filemenu.add_command(label="Python Shell")
menubar.add_cascade(label='Run',menu=filemenu)
tahmid.config(menu=menubar)                 

filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="Configure IDLE")
filemenu.add_command(label="Show Code Content")
filemenu.add_command(label="Show line Numbers")
filemenu.add_command(label="Zoom Height")
menubar.add_cascade(label='Options',menu=filemenu)
tahmid.config(menu=menubar)

filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="About IDLE")
filemenu.add_command(label="IDLE Help")
filemenu.add_command(label="Python Docs F1")
filemenu.add_command(label="Turtle Demo")
menubar.add_cascade(label='Help',menu=filemenu)
tahmid.config(menu=menubar)    

