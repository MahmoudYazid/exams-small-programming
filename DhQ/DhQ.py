import tkinter as tk
from PIL import ImageTk as imgtk
from PIL import Image as img
import easygui
import pyexcel_xls as xls
import pyexcel.ext.xls
import pyexcel.ext.xlsx
import pyexcel as exel
import os
import xlsxwriter
from datetime import datetime
main = tk.Tk()
main.title("DHQ - Main")
def Quiz():
    if not os.path.exists("..\\DhQ\\ids.xls"):
        easygui.msgbox("may there is a problem in ids.xlsx file that you put or there is no file at all so if its exist check that the file is .xlsx not .xls")
        return 0

    if not os.path.exists("file_name.txt"):
        easygui.msgbox("there is no exams Yet")
        return 0
    check = open("group.txt", "r")
    if not os.path.exists("..\\DhQ\\{}".format(check.read())):
        easygui.msgbox("There is no exam Yet")
        return 0
    check.close()
    check=open("group.txt","r")
    if os.path.exists("..\\DhQ\\{}\\{}.xlsx".format(check.read(),id.get())):
        easygui.msgbox("you made this exam before")
        return 0
    check.close()

    confirm = open("lec.txt","r")
    if confirm.read() == "":
        easygui.msgbox("there is no lec. now pls wait")
        main.quit()
    confirm.close()
    fname = open("file_name.txt","r")
    sheet = exel.load("{}.xls".format(fname.read()))
    ##ids check
    ids_sheets = exel.load("ids.xls")
    print(ids_sheets.number_of_rows())
    for n in ids_sheets.row_range():
        if id.get() == str(ids_sheets[n,0]):
            easygui.msgbox("Your id is confirmed")
            break
        else:
            easygui.msgbox("no id like this")
            return 0
    ##Quiz
    for i in sheet.row_range():
        choice = [sheet[i,1],sheet[i,2],sheet[i,3],sheet[i,4]]
        cc = easygui.choicebox(title="Quiz",choices=choice,msg=sheet[i,0])
        if cc == sheet[i,5]:
            i = i+1
            degree = open("dg_of_{}.txt".format(name.get()), "w")
            degree.write("{} of {}".format(i,sheet.number_of_rows()))
            degree.close()
        else:
            easygui.msgbox("the right answer was {}".format(sheet[i,5]))

    conferm_d = open("dg_of_{}.txt".format(name.get()),"r")
    easygui.msgbox("your degree is {}".format(conferm_d.read()))
    conferm_d.close()
    _quizlec = open("lec.txt","r")
    lec_name = easygui.enterbox("call the lecturer to confirm your result","confirm")

    if lec_name == _quizlec.read():
        ####inseert the info in exel result
        _get=open("group.txt","r")
        wb=xlsxwriter.Workbook("..\\DhQ\\{}\\{}.xlsx".format(_get.read(),id.get()))
        ws=wb.add_worksheet()
        ws.write(0,0,"name")
        ws.write(1,0,"id")
        ws.write(2,0,"time of Quiz")
        ws.write(3,0,"degree")
        ws.write(0,1,"{}".format(name.get()))
        ws.write(1,1,"{}".format(id.get()))
        ws.write(2,1, "{}".format(datetime.today()))
        dg=open("dg_of_{}.txt".format(name.get()),"r")
        ws.write(3,1,"{}".format(dg.read()))
        dg.close()
        wb.close()
        _get.close()
        ############
        easygui.msgbox("Your Quiz done you can stand up now")


    else:
        easygui.msgbox("you try to steal if you are the doctor you ha just one more time")
        _quizlec = open("lec.txt", "r")
        lec_name2 = easygui.enterbox("call the lecturer to confirm your result", "confirm")

        if lec_name2 == _quizlec.read():
            ####inseert the info in exel result
            _get = open("group.txt", "r")
            wb = xlsxwriter.Workbook("..\\DhQ\\{}\\{}.xlsx".format(_get.read(),id.get()))
            ws = wb.add_worksheet()
            ws.write(0, 0, "name")
            ws.write(1, 0, "id")
            ws.write(2, 0, "time of Quiz")
            ws.write(3, 0, "degree")
            ws.write(0, 1, "{}".format(name.get()))
            ws.write(1, 1, "{}".format(id.get()))
            ws.write(2, 1, "{}".format(datetime.today()))
            dg = open("dg_of_{}.txt".format(name.get()), "r")
            ws.write(3, 1, "{}".format(dg.read()))
            dg.close()
            wb.close()
            _get.close()
            ############
            easygui.msgbox("Your Quiz done you can stand up now")

        else:
            easygui.msgbox("in correct answer")
            main.quit()
        _quizlec.close()
    os.remove("dg_of_{}.txt".format(name.get()))
    fname.close()
#name and year
##back
img1 = img.open("main.jpg")
img1_show = imgtk.PhotoImage(img1)
tk.Label(image=img1_show).pack(expand=True)
#sub_back
img3 = img.open("Free_Sample_By_Wix (1).jpg")
img3_show = imgtk.PhotoImage(img3)
tk.Label(image=img3_show).place(x=700,y=0)
##login btm
img2 = img.open("Background.png")
img2_show = imgtk.PhotoImage(img2)
tk.Button(image=img2_show, border=0, command=Quiz).place(x=1000,y=450)

##name
tk.Label(text="Your Name",font=20).place(x=860,y=205)
name = tk.Entry(width=30,font=33)
name.bind("<Return>",Quiz)
name.place(x=1000,y=200)
##year in collage
tk.Label(text="Year in collage", font=20, border=0, bg="white").place(x=850,y=300)
Year = tk.Entry(width=30,font=33)
Year.bind("<Return>",Quiz)
Year.place(x=1000,y=300)
#id
tk.Label(text="ID", font=20, border=0, bg="white").place(x=900,y=400)
id = tk.Entry(width=30,font=33)
id.bind("<Return>",Quiz)
id.place(x=1000,y=400)
main.mainloop()