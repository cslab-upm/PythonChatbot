#import os #to delete files

FAIL=2
SUCCES=1
#Global
Messages=[]

def TrimString(input):
    SingleQuote="'"
    DoubleQuote='"'
    if input.startswith(SingleQuote) and input.endswith(SingleQuote):
        result=input.replace(SingleQuote,"")
    elif input.startswith(DoubleQuote) and input.endswith(DoubleQuote):
        result=input.replace(DoubleQuote,"")
    else:
        result=input
    return result

def Message_Tag(messages,tag):
    for m in messages:
        #print(m)
        if m[0]==tag:
            #print("Tag:",tag," found:",m[1]) 
            return m[1] # return list
    print("Tag:",tag," not found!")
    return None

def Process_Line(messages,line,lineno):
    #print("reading textfile line ",lineno," = ",line)
    # now split line in tag + list of alternative strings, ignore if comment
    if (line.startswith("#")):
        return FAIL
    else:
        tags=line.split(":",1)
        tag=tags[0].strip()
        if (tag!=""):
            if (len(tags)>1):
                messageslist = tags[1].strip()
                list1=[]
                for m in messageslist.split(";"):
                    list1.append(TrimString(m.strip()))
                tagmesg = (tag,list1)
                messages.append(tagmesg)
            else:
                print("*** Text Input format error in file on line",lineno," ':' expected!  tag =",tag)
    return SUCCES

def ReadFile_Messages(filename):
    Messages = []
    file = open(filename, "r")
    if (file!=None):
        lineno=1
        for line in file:
            if line!="":
                Process_Line(Messages,line.strip(),lineno)
            # else skip empty lines
            lineno=lineno+1
        file.close()
    return Messages

def Read_results(filename):
    list1 = []
    file = open(filename, "r")
    if (file!=None):
        for line in file:
            list2 = line.split(",")
            last = list2[-1]
            if last[-1] == "\n":
                list2[-1] = last[:-1] #because the last string from a line includes an \n = Enter which should not be read
            list1.append(list2)
        file.close()
    return list1
def Write_results(list1,filename):
    file = open(filename, "w")
    if (file):
        for line in list1:
            for x in range(0,len(line)-1):
                file.write(line[x])
                file.write(",")
            file.write(line[-1]) #print without comma
            file.write("\n")
        file.close()
def Reset_results():
    list1 = [["category","1","2","3","4","5","other"]]
    return list1
def Add_result(name,category_number,list1):
    for r in list1:
        if r[0] == name:
            r[category_number] = str(int(r[category_number])+1)
            return
    new = [name,"0","0","0","0","0","0"]
    new[category_number] = "1"
    list1.append(new)
if __name__ == "__main__":
    x = input("Are you sure that you want to delete the solution file? Click stop run")
    result_list = Read_results("solutions.txt")
    if result_list == []:
        result_list = Reset_results()
        print("resetting")
    else:
        print (result_list)
    sound = "sound123.wav"
    answer = 1
    Add_result(sound,answer,result_list)
    print("write now")
    Write_results(result_list,"solutions.txt")
# print("Example reading file messages.txt:")
# Messages = []
# ReadFile_Messages("messages.txt")
# print("Example searching for tag: Andre")
# AndreMessages = Message_Tag(Messages,"Andre") # not found!
# # nu kun je dus iets gaan doen als:
# print("Example searching and returning options for tag 'Answers1'")
# Answers1 = Message_Tag(Messages,"Answers1") # found
# #AM=random.choice(AndreMessages)
# #Speak(AM)