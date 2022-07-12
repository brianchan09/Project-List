def main():
    print('--<Basic function>--')
    print('1.Add new item(s)\n')
    print('2.Display Item record(s)\n')
    print('3.Search Item Information\n')
    print('4.Modify Item Record(s)\n')
    print('5.Delete Item Record(s)') 

    choice=int(input('please enter the function you want to operate'))

    if choice==0 or choice >=5:
          print('Wrong input, please choose again.')
          return main()
    if choice==1:
        adddata()
    if choice ==2:
        displaydata()
    if choice ==3:
        searchdata()
    if choice ==4:
        modifydata()
    if choice==5:
        deleteitem()

def adddata():
    appfile=open('inventory.txt','a')
    recnumber=input('Please enter Record number:')
    itemname=input('Please enter Item name:')
    itemnum=input('Please enter Item number:')
    category=input('Please enter Category:')
    quantity=input('Please enter Quantity:')
    weight=input('Please enter Weight:')
    recipent=input('Please enter Recipent:')
    finDes=input('Please enter Final Destinaton:')
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
    while contin != 'y'and contin !='n':
        print('It is a wrong input.Please input again.')
        contin=input('Do you want to add another new item?(y/n):')
    if contin=='y':
        return adddata()
    if contin=='n':
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
    disfile=open('inventory.txt','r')
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
        weight[i]= weights
        reci[i]= recip
        fianl_des[i]=fianldes
        deli_stat[i]=delistat
        i=i+1
        Recnum=disfile.readline()
        
    disfile.close()
    a=0
    while Rec_num[a] != 0:
        print(Rec_num[a])
        print(item_nam[a])
        print(item_num[a])
        print(cate[a])
        print(quant[a])
        print(weight[a])
        print(reci[a])
        print(fianl_des[a])
        print(deli_stat[a])
        print('\n')
        a=a+1
    return main() 
main()
