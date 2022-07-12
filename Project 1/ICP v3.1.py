import sys,os

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



def modifydata():
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
    if g_max == 0: print("----------------------------------------------------------------------\nThe file \"inventory.txt\" is empty.\n----------------------------------------------------------------------\n");pause();return
    ########################################################################################################    SEARCH    ##############################################################################################################
    m_search = input("Search (Case Sensitive): ")
    for x in range(max):
        
 
    
    
    














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
os.system("color 0a")
while True:
    main()
