import os
a = input("""input Doctor name >>> """)
##lec name
if a:
    file = open("lec.txt","w")
    file.write(a)
    file.close()
else:
    print(" no names said ")
    quit()
##file name
b = input("""input your test file name >>> """)
if b:
    file = open("file_name.txt", "w")
    file.write(b)
    file.close()
else:
    print(" no files name said ")
    quit()
##foldername
c = input("""input your group name >>> """)
if c:
    if os.path.exists("..\\DhQ\\{}".format(c)):
        print("this group existed before")
        quit()
    file=open("group.txt","w")
    file.write("{}".format(c))
    os.mkdir("..\\DhQ\\{}".format(c))
    print("your new quiz is ready")

    quit()
