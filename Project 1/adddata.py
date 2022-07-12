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
