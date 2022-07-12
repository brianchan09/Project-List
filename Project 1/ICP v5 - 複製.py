import sys

def main():
    print('--<Basic function>--')
    print('1.Add new item(s)\n')
    print('2.Display Item record(s)\n')
    print('3.Search Item Information\n')
    print('4.Modify Item Record(s)\n')
    print('5.Delete Item Record(s)\n') 
    print('6.Exit program\n')
    while (True):
        try:
            choice=int(input('Please enter the function you want to operate (1-6): '))
            break
        except:
            print("Please input integer only!")
    if choice<=0 or choice >6:
          print('Wrong input, please choose again.')
          return main()
    if choice == 1:
        adddata()
    if choice == 2:
        displaydata()
    if choice == 3:
        searchdata()
    if choice == 4:
        modifydata()
    if choice == 5:
        deleteitem()
    if choice == 6:
        sys.exit()

def adddata():
    appfile=open('inventory.txt','a')
    recnumber=input('Please enter Record number:')
    itemname=input('Please enter Item name:')
    itemnum=input('Please enter Item number:')
    category=input('Please enter Category:')
    quantity=input('Please enter Quantity:')
    weight=input('Please enter Weight:')
    recipent=input('Please enter Recipent:')
    finDes=input('Please enter Final Destination:')
    deli=input('Please enter Delivery status:')

    appfile.write(recnumber+'\n')
    appfile.write(itemname+ '\n')
    appfile.write(itemnum+ '\n')
    appfile.write(category+ '\n')
    appfile.write(quantity+ '\n')
    appfile.write(weight+ '\n')
    appfile.write(recipent+ '\n')
    appfile.write(finDes+'\n')
    appfile.write(deli+ '\n\n')
    appfile.close()

    contin=input('Do you want to add another new item?(y/n)')
    while contin.lower() != 'y'and contin.lower() !='n':
        print('It is a wrong input.Please input again.')
        contin=input('Do you want to add another new item?(y/n):')
    if contin.lower() == 'y':
        return adddata()
    if contin.lower() == 'n':
        return main()
        

def displaydata():
    Rec_num=[0]*1000
    item_nam=[0]*1000
    item_num=[0]*1000
    cate=[0]*1000
    quant=[0]*1000
    weight=[0]*1000
    reci=[0]*1000
    fianl_des=[0]*1000
    deli_stat=[0]*1000
    newline=[0]*1000
    try:
        disfile=open('inventory.txt','r')
    except:
        print("File not exist. Please add data before display them.")
        return main()
    Recnum=disfile.readline()
    i=0
    while Recnum != '':
        itemnam=disfile.readline()
        itemnum=disfile.readline()
        categ= disfile.readline()
        quanti= disfile.readline()
        weights= disfile.readline()
        recip= disfile.readline()
        fianldes= disfile.readline()
        delistat= disfile.readline()
        newlines= disfile.readline()

        Rec_num[i]=Recnum
        item_nam[i]=itemnam
        item_num[i]= itemnum
        cate[i]= categ
        quant[i]= quanti
        weight[i]= weights[:-1]
        reci[i]= recip
        fianl_des[i]=fianldes
        deli_stat[i]=delistat
        i=i+1
        Recnum=disfile.readline()
        
    disfile.close()
    a=0
    while Rec_num[a] != 0:
        print("Record Number:",Rec_num[a])
        print("Item Name:",item_nam[a])
        print("Item Number:",item_num[a])
        print("Category:",cate[a])
        print("Quantity:",quant[a])
        print("Weight:",weight[a],"kg\n")
        print("Recipent:",reci[a])
        print("Final destination:",fianl_des[a])
        print("Delivery:",deli_stat[a])
        print('\n')
        a=a+1
    return main() 



def searchdata():
    """
        Variable list for modifydata:
            # b => input of continue function
            # num => the record number 
            # name => item name
            # item_num => item number
            # cate => category of item 
            # c => quantity
            # w => weight
            # buyer => recipient 
            # dst => final destination 
            # stat => status of delivery
            # f => file name
            # confirm => user to confirm 
            # leave => boolean for leave the funcation
            # i,j,k,l is use for looping
            # s_list => all data into that list
    """
    
    ###################################################################################################     READ DATA FROM TXT FILE    ################################################################################################
    try:
        f = open("inventory.txt","r")
        f.close()
    except:
        print("\"inventory.txt\" is not exist.")
        return 0;
    with open("inventory.txt") as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    j = 0
    num = [""]
    name = [""]
    item_num = [""]
    cate = [""]
    c = [""]
    w = [""]
    buyer = [""]
    dst = [""]
    stat = [""]
    max = len(data)//9
    for i in range(max):
        num.append(str(data[j]))
        name.append(str(data[j+1]))
        item_num.append(str(data[j+2]))
        cate.append(str(data[j+3]))
        c.append(str(data[j+4]))
        w.append(str(data[j+5]))
        buyer.append(str(data[j+6]))
        dst.append(str(data[j+7]))
        stat.append(str(data[j+8]))
        j+=9
    num.remove("")
    name.remove("")
    item_num.remove("")
    cate.remove("")
    c.remove("")
    w.remove("")
    buyer.remove("")
    dst.remove("")
    stat.remove("")
    f.close()
    ####################################################################################################################################################################################################################################
    leave_1 = True
    if max == 0: print("----------------------------------------------------------------------\nThe file \"inventory.txt\" is empty.\n----------------------------------------------------------------------\n");pause();return
    ########################################################################################################    SEARCH    ##############################################################################################################
    s_list = [""]
    s_list_2 = [""]
    for s_x in range(max):
        s_list.append(num[s_x])
        s_list.append(name[s_x])
        s_list.append(item_num[s_x])
        s_list.append(cate[s_x])
        s_list.append(c[s_x])
        s_list.append(w[s_x])
        s_list.append(buyer[s_x])
        s_list.append(dst[s_x])
        s_list.append(stat[s_x])
    s_list.remove("")
    confirm = False
    skip = False
    s_search = input("Search (Case Sensitive): ")
    for i in range(len(s_list)):
        if s_search in s_list[i] and i//9 not in s_list_2:
            if not skip: print("Search result of \"",s_search,"\": ",sep='')
            s_list_2.append(i//9)
            print("\n---------------------------------------------------------")
            print("Record Number:",num[i//9])
            print("Item Name:",name[i//9])
            print("Item Number:",item_num[i//9])
            print("Category:",cate[i//9])
            print("Weight:",c[i//9])
            print("Recipient:",buyer[i//9])
            print("Final Destination:",dst[i//9])
            print("Delivery Status:",stat[i//9])
            confirm = True
            skip = True
    if not confirm:
        print("You search -- \"",s_search,"\" did not match anything in \"inventory.txt\".",sep='')
        while True:
            b = input("Do you want to search again?(y/n) ")
            if b.lower() == 'y' or b.lower() == 'n': break
            else: print("Please input \"y\" or \"n\" only.");
    print("---------------------------------------------------------\n")
    while True and confirm:
        b = input("Do you want to search again?(y/n) ")
        if b.lower() == 'y' or b.lower() == 'n': break
        else: print("Please input \"y\" or \"n\" only.");
    if b.lower() == 'y': searchdata();
    if b.lower() == 'n': return;
        
def modifydata():
    try:
        g = open("inventory.txt","r")
        g.close()
    except:
        print("\"inventory.txt\" is not exist.")
        return 0;
    g=open("inventory.txt","r")
    text=g.readlines()
    length=len(text)
    text=[x.strip() for x in text]
    g.close()
    mod=input("Please enter the record number of the data you want to modify:")
    count1=length
    global index_a
    index_a=0
    for ii in text:
        if ii!=mod:
            index_a+=1
            if index_a+1 >length:
                print("No this record number")
                return modifydata()
        else:
            index_a+=1
            break
    import linecache
    linecache.clearcache()
    theline1=linecache.getline("inventory.txt",index_a)
    theline2=linecache.getline("inventory.txt",index_a+1)
    theline3=linecache.getline("inventory.txt",index_a+2)
    theline4=linecache.getline("inventory.txt",index_a+3)
    theline5=linecache.getline("inventory.txt",index_a+4)
    theline6=linecache.getline("inventory.txt",index_a+5)
    theline7=linecache.getline("inventory.txt",index_a+6)
    theline8=linecache.getline("inventory.txt",index_a+7)
    theline9=linecache.getline("inventory.txt",index_a+8)
    global list1
    list1=str("\n"+theline1+theline2+theline3+theline4+
               theline5+theline6+theline7+theline8+theline9)
    print("A.Record number:",theline1,end="")
    print("B.Item name:",theline2,end="")
    print("C.Item number:",theline3,end="")
    print("D.Category:",theline4,end="")
    print("E.Quantity:",theline5,end="")
    print("F.Weight:",theline6,end="")
    print("G.Recipient:",theline7,end="")
    print("H.Final Destination:",theline8,end="")
    print("I.Deliver Status:",theline9,end="")
    modify()

def modify():
    import linecache
    modi=input("Which item do you want to modify?(A-I):")
    if modi!="A" and modi!="B" and modi!="C" and modi!="D" and modi!="E" \
       and modi!="F" and modi!="G" and modi!="H" and modi!="I" :
        print("Please input A-I")
        return modify()
    newitem=input("input new data:")
    x=ord(modi)-64
    f=open("inventory.txt","r")
    a=f.read()
    lins=linecache.getline("inventory.txt",index_a-1+x)
    ff=open("inventory.txt","r+")
    import re
    list2 = re.sub(r'[^.]\b(%s)\b'%lins,"\n"+newitem+"\n",list1,0)
    ff.write(re.sub(list1,list2,a,0))
    ff.close()

    contin=input('Do you want to modify another new item?(y/n): ')
    while contin.lower() != 'y'and contin.lower() !='n':
        print('It is a wrong input.Please input again.')
        contin = input('Do you want to modify another new item?(y/n): ')
    if contin.lower() == 'y':
        return modifydata()
    if contin.lower() == 'n':
        return main()


def deleteitem():
    search = input("What are you want to delete? ")
    try: 
        f = open("inventory.txt",mode="r")
    except:
        print("There is not data on \"inventory.txt\".")
        return 0
    nums = []
    for lines in f:
        lines = lines.strip()
        if len(lines)>0:
            nums.append(lines)
    group = len(nums) // 9
    multiple = len(nums) % 9
    mylist = [list(nums[x*9:(x+1)*9]) for x in range(group)]
    f.seek(0,0)
    line = f.readlines()
    f.seek(0,0)

    while line:
        line = f.readline()
        if line.find(search) >= 0:
            for i,j in enumerate(mylist):
                for k,l in enumerate(j):
                    if l == search:
                        f_w = open("inventory.txt",mode="w")
                        if i != 0:
                            for y in range(i):
                                for z in range(9):
                                    index = mylist[y][z]
                                    f_w.write(index+"\n")
                                    q = y + 1
                                f_w.write("\n")
                        else:
                            q = 0


            break

    for y in range(q+1,i+1):
        for z in range(9):
            index = mylist[y][z]
            f_w.write(index+"\n")
        f_w.write("\n")    

    f_w.close()

    contin=input('Do you want to delete another new item?(y/n): ')
    while contin.lower() != 'y'and contin.lower() !='n':
        print('It is a wrong input.Please input again.')
        contin = input('Do you want to delete another new item?(y/n): ')
    if contin.lower() == 'y':
        return deleteitem()
    if contin.lower() == 'n':
        return main()

while True:
    main()
