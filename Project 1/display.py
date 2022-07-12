def displaydata():
    Rec_num=[0]*1000
    item_name=[0]*1000
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
        itemnum=disfile.readline()
        categ= disfile.readline()
        quanti= disfile.readline()
        weights= disfile.readline()
        recip= disfile.readline()
        fianldes= disfile.readline()
        delistat= disfile.readline()
        newlines= disfile.readline()

        Rec_num[i]=Recnum
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
displaydata()
