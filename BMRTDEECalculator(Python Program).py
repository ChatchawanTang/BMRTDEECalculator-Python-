from tkinter import *
import csv
import time
import os.path

Genderlist = ['Male','Female',]
Exercisedayslist = ['Little to no exercise',
                    'Light exercise (1-3 days / week)',
                    'Moderate exercise (3-5 days / week)',
                    'Heavy exercise (6-7 days / week)',
                    'Very heavy exercise (2x / day)',]


EZ = Tk()
EZ.title('BMR & TDEE Calculator')


myinputH1=StringVar()
myinputW1=StringVar()
myinputA1=StringVar()
myinputD1=StringVar()
display1=StringVar()
display2=StringVar()
display3=StringVar()
myinputN1=StringVar()


variable = StringVar(EZ)
variable.set('Select your gender')
variable1=StringVar(EZ)
variable1.set('Choose your activity')



GD=OptionMenu(EZ,variable,*Genderlist)
GD.config(width=17, bg='#fff1ea') 
GD.grid(row = 2, column = 1, sticky = W, padx = 40, pady = 2)
EX=OptionMenu(EZ,variable1,*Exercisedayslist)
EX.config(width=17, bg='#fff1ea')
EX.grid(row = 8, column = 1, sticky = W, padx = 40, pady = 2)



Welcome = Label(EZ, text = 'BMR & TDEE Calculator')
Welcome.grid(row = 0, column = 1, sticky = W, pady = 2)
wc_font = ("Comic Sans MS", 20, "bold")
Welcome.config(font = wc_font)



Name   = Label(EZ, text = 'Name ')  
height = Label(EZ, text = 'Height ')   
weight = Label(EZ, text = 'Weight ')
age    = Label(EZ, text = 'Age    ')
gender = Label(EZ, text = 'Gender ')
BMR    = Label(EZ, text = 'BMR :    ')
BMR_result =Label(EZ,textvariable = display1)
DAYS   = Label(EZ, text = 'Activity')
TD     = Label(EZ, text = 'TDEE :  ')
TD_result =Label(EZ,textvariable = display2)
save = Label(EZ,textvariable = display3)



EZ['background']='#FFC8A2'
Welcome['background']='#FFC8A2'
Name['background']='#FFC8A2'
height['background']='#FFC8A2'
weight['background']='#FFC8A2'
gender['background']='#FFC8A2'
age['background']='#FFC8A2'
BMR['background']='#FFC8A2'
BMR_result['background']='#FFC8A2'
DAYS['background']='#FFC8A2'
TD['background']='#FFC8A2'
TD_result['background']='#FFC8A2'
save['background']='#FFC8A2'



Name.grid(row = 1, column = 0, sticky = W, padx = 10, pady = 2)
gender.grid(row = 2, column = 0, sticky = W, padx = 10, pady = 2)
save.grid(row = 12, column = 2, sticky = W, padx = 4, pady = 2)
height.grid(row = 3, column = 0, sticky = W, padx = 10, pady = 2)
weight.grid(row = 4, column = 0, sticky = W, padx = 10, pady = 2)
age.grid(row = 5, column = 0, sticky = W, padx = 10, pady = 2)
BMR.grid(row = 6, column = 0, sticky = W, padx = 10, pady = 2)
BMR_result.grid(row = 6, column = 1, sticky = W, padx = 40, pady = 2)
DAYS.grid(row = 8, column = 0, sticky = W, padx = 10, pady = 2)
TD.grid(row = 9, column = 0, sticky = W, padx = 10, pady = 2)
TD_result.grid(row = 9, column = 1, sticky = W, padx = 40, pady = 2)



H1 = Entry(EZ,textvariable=myinputH1)
W1 = Entry(EZ,textvariable=myinputW1)
A1 = Entry(EZ,textvariable=myinputA1)
N1 = Entry(EZ,textvariable=myinputN1)



H1.grid(row = 3, column = 1, sticky = W, padx = 40,pady = 2)
W1.grid(row = 4, column = 1, sticky = W, padx = 40,pady = 2)
A1.grid(row = 5, column = 1, sticky = W, padx = 40,pady = 2)
N1.grid(row = 1, column = 1, sticky = W, padx = 40,pady = 2)



H1['background']='#FFD8BE'
W1['background']='#FFD8BE'
A1['background']='#FFD8BE'
N1['background']='#FFD8BE'


#ปุ่ม Calc BMR
def cal(): 
    try:
        print('Your Gender :' +variable.get())
        print('Your Height :' +H1.get())
        print('Your Weight :' +W1.get())
        print('Your Age    :' +A1.get())
        height=eval(myinputH1.get())
        weight=eval(myinputW1.get())
        age   =eval(myinputA1.get())                
        
        global BMR
    
        if (variable.get()) == 'Male':
            if weight < 0:
                print('Oops! We can not calculate BMR for you. (Input can not be negative)')
                BMR = ('Not calculate BMR')
                display1.set('Value must be positive')
                return BMR
            if height < 0:
                print('Oops! We can not calculate BMR for you. (Input can not be negative)')
                BMR = ('Not calculate BMR')
                display1.set('Value must be positive')
                return BMR
            if age < 0:
                print('Oops! We can not calculate BMR for you. (Input can not be negative)')
                BMR = ('Not calculate BMR')
                display1.set('Value must be positive')
                return BMR
            else:
                BMR = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
                print('Your BMR are : {0:.2f}'.format(BMR))
                
       
        if (variable.get()) == 'Female':
            if weight < 0:
                print('Oops! We can not calculate BMR for you. (Input can not be negative)')
                BMR = ('Not calculate BMR')
                display1.set('Value must be positive')
                return BMR
            if height < 0:
                print('Oops! We can not calculate BMR for you. (Input can not be negative)')
                BMR = ('Not calculate BMR')
                display1.set('Value must be positive')
                return BMR
            if age < 0:
                print('Oops! We can not calculate BMR for you. (Input can not be negative)')
                BMR = ('Not calculate BMR')
                display1.set('Value must be positive')
                return BMR
            else:
                BMR = 665 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
                print('Your BMR are : {0:.2f}'.format(BMR)) 
                
                
        if BMR == 'Not calculate BMR':
            display1.set('Value must be positive')
            
        else:
            display1.set('{0:.2f}'.format(BMR))
            
        
    except TypeError as te1:
        display1.set('Please select gender')
        print('Oops! We can not calculate BMR for you. (Please select gender)')

    except SyntaxError as se1:
        display1.set('Please Input value')
        print('Oops! We can not calculate BMR for you. (Please Input value)')

    except NameError as ne1:
        display1.set('Input must be number')
        print('Oops! We can not calculate BMR for you. (Input must be number)')

        #TypeError = ยังไม่เลือกเพศ
        #SyntaxError = มี Input ว่างอยู่
        #NameError = Input ไม่ใช่เลข


#ปุ่มคำนวณ TDEE
def CalTDEE():

    global TDEE

    if (variable1.get()) == 'Little to no exercise':
        TD = 1.2
    if (variable1.get()) == 'Light exercise (1-3 days / week)':
        TD = 1.375
    if (variable1.get()) == 'Moderate exercise (3-5 days / week)':
        TD = 1.55
    if (variable1.get()) == 'Heavy exercise (6-7 days / week)':
        TD = 1.725
    if (variable1.get()) == 'Very heavy exercise (2x / day)':
        TD = 1.9
        
    try:
        TDEE = BMR * TD
        display2.set('{0:.2f}'.format(TDEE))
        print('Your TDEE are : {0:.2f}'.format(TDEE))
        
    except TypeError as te2:
        display2.set('Calculate BMR first!')
        print("Oops! We can not calculate TDEE for you. (Haven't calculate BMR yet)")

    except UnboundLocalError as uble2:
        display2.set('Please select activity level!')
        print("Oops! We can not calculate TDEE for you. (Haven't select activity yet!)")
        
        #TypeError = ยังไม่มีค่า BMR
        #UnboundLocalError = ยังไม่เลือก Activity


header=['Month/Day', 'Year', 'Time', 'Name', 'Height', 'Weight', 'Age', 'Gender', 'BMR', 'Activity', 'TDEE']
global big_lst
big_lst=[]


#ปุ่ม Save ข้อมูลลง CSV
def saveCSV():
    if not os.path.exists("BMRdata.csv"):
        with open('BMRdata.csv', 'w',encoding='UTF-8-sig') as wt1:
                writer = csv.writer(wt1)
                writer.writerow(header)
                print('New file create')
                pass

    if os.path.exists("BMRdata.csv"):
        print('file exist')
        BMRfile = open("BMRdata.csv", "r",encoding='UTF-8-sig')
        BMRfile_reader = csv.reader(BMRfile)
        lists_from_OLDbiglst = []
        for row in BMRfile_reader:
            lists_from_OLDbiglst.append(row)
        big_lst = lists_from_OLDbiglst

    try:
        time_get = time.localtime()
        time_MD = time.strftime('%m/%d',time_get)
        time_Y = time.strftime('%Y',time_get)
        time_HMS = time.strftime('%H:%M:%S',time_get)
        name=str(myinputN1.get())
        if (myinputN1.get()) == '':
            name='NO NAME'
        height=eval(myinputH1.get())
        weight=eval(myinputW1.get())
        age   =eval(myinputA1.get())
        gender=str(variable.get())
        activity = str(variable1.get())
        TDEE=str(display2.get())

        if (display2.get()) == '':
            TDEE = 'No Calculate TDEE'

        if (variable1.get()) == 'Choose your activity':
            activity = 'No activity selected'

        if type(BMR) != float:
            print('Save failed!')
            display3.set("Haven't calc BMR")
            
        else:
            lst=[time_MD,time_Y,time_HMS,name,height,weight,age,gender,BMR,activity,TDEE]
            big_lst.append(lst)
            with open('BMRdata.csv', 'w', encoding='UTF-8-sig', newline='') as wt2:
                writer = csv.writer(wt2)
                writer.writerows(big_lst)
            display3.set('Save succuess!')
            print('Save succuess!')
            

    except PermissionError as PE:
        display3.set('Close running CSV file and try again!')
        print('CSV currently running! Close and try again!')
    except SyntaxError as Se3:
        display3.set('No input!')
        print('Save failed')
    except NameError as Ne3:
        display3.set("Haven't Calc BMR")
        print('Save failed')

        #PermissionError = ไฟล์ CSV ยังเปิดอยู่ให้ปิดก่อน
        #SyntaxError = ไม่มี Input ไม่ให้ Save
        #NameError = ใส่ Input แล้วแต่ยังไม่กดคำนวณ BMR


#สร้างหน้าต่าง Log
def New_windows():
    
    EZ1=Tk()
    EZ1.title("Log")
    newlabel = Label(EZ1, text = "History")
    window_font = ("Comic Sans MS", 20, "bold")
    newlabel.config(font = window_font)
    newlabel.pack()
    EZ1['background']='#FFC8A2'
    newlabel['background']='#FFC8A2'

    try:
        BMRfile = open("BMRdata.csv", "r",encoding='UTF-8-sig')
        BMRfile_reader = csv.reader(BMRfile)
        lists_from_OLDbiglst = []
        for row in BMRfile_reader:
            lists_from_OLDbiglst.append(row)
        big_lst = lists_from_OLDbiglst

        EIEI=Text(EZ1,width=70,height=20)
        HELLO=open("BMRdata.csv","r",encoding="UTF-8")
        HI=HELLO.read()
        EIEI.insert(END,HI)
        EIEI['background']='#FFD8BE'
        HELLO.close()
        EIEI.pack()

    except FileNotFoundError as FnFE:
        FNF=Label(EZ1, text = 'Flie not Found!')
        FNF['background']='#FFD8BE'
        FNF.pack()


#ปุ่มต่างๆ
buttonOK = Button(EZ,text='Calc BMR',command=cal,width=10)
buttonOK.grid(row = 7, column = 0, sticky = W, padx = 10, pady = 2)
buttonClose = Button(EZ,text = 'Close' , command=EZ.destroy,width=10)
buttonClose.grid(row = 10, column = 2, sticky = W, padx = 10, pady = 2)
buttonCal = Button(EZ,text='Calc TDEE',command=CalTDEE,width=10)
buttonCal.grid(row = 10, column = 0, sticky = W, padx = 10, pady = 2)
buttonSave =Button(EZ,text='Save',command=saveCSV,width=10)
buttonSave.grid(row = 9, column = 2, sticky = W, padx = 10, pady = 2)
buttonNew_windows = Button(EZ,text='Open Log',command=New_windows,width=10)
buttonNew_windows.grid(row = 8, column = 2, sticky = W, padx = 10, pady = 2)


buttonOK['background']='#FFD8BE'
buttonClose['background']='#FFD8BE'
buttonCal['background']='#FFD8BE'
buttonSave['background']='#FFD8BE'
buttonNew_windows['background']='#FFD8BE'


EZ.mainloop()

