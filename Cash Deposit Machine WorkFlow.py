Account_Details=[{'Name':'Thota Pavan kumar','Account_Number':123451,'Pin':1234,'Balance':50000},
                 {'Name':'Sasi Kumar','Account_Number':123452,'Pin':2172,'Balance':90000},
                 {'Name':'Babavali','Account_Number':123453,'Pin':7453,'Balance':20000},
                 {'Name':'Murali','Account_Number':123454,'Pin':3772,'Balance':150000},
                 {'Name':'Naveen','Account_Number':123455,'Pin':1223,'Balance':230000},
                 {'Name':'Harish','Account_Number':123456,'Pin':1574,'Balance':110000},
                 {'Name':'Punith','Account_Number':123457,'Pin':1874,'Balance':450000}]



while True:
    Pin_Number=0   
    Balance=0
    Name=''
    Name2=''
    
    try:
        Action=int(input('Enter 1 - Withdraw 2-Balance Transfer 3-credit: '))
        if Action in (1,2,3):
            if Action==1:
                Account_Number=int(input('Enter Account Number: '))
                for i in Account_Details:
                    if i['Account_Number']==Account_Number:
                        Pin_Number=i['Pin']
                        Balance=i['Balance']
                        Name=i['Name']
                if Name=='':
                    print('Account Number is Invalid please enter valid Account Number')
                    print('Current Transaction is terminated')
                else:
                    Amount=int(input('Enter Amount to be withdraw: '))
                    if Amount>Balance:
                        print('InSufficient Funds ')
                        print('Current Transaction is terminated')
                    else:
                        Pin=int(input('Please Enter PIN: '))
                        if Pin==Pin_Number:
                            for i in Account_Details:
                                if i['Account_Number']==Account_Number:
                                    i['Balance']=i['Balance']-Amount
                                    Current_Balance=i['Balance']
                                    print('Please Collect your Cash')
                                    Display=int(input('Enter 1 to display your balance: '))
                                    if Display==1:
                                        print('Your Current balance is '+str(Current_Balance)+' rs')
                                    print('Current Transaction is Completed')      
                        else:
                            print('Invalid PIN')
                            print('Current Transaction is terminated')

            elif Action==2:
                Account_Number=int(input('Enter your Account Number: '))
                CD_Account_Number=int(input('Enter credit Account Number: '))
                for i in Account_Details:
                    if i['Account_Number']==Account_Number:
                        Pin_Number=i['Pin']
                        Balance=i['Balance']
                        Name=i['Name']
                    if i['Account_Number']==CD_Account_Number:
                        Name2=i['Name']
                if Name=='':
                    print(' Account Number is Invalid please enter valid Account Number')
                    print('Current Transaction is terminated')
                elif Name2=='':
                    print('Credit Account Number is Invalid please enter valid Account Number')
                    print('Current Transaction is terminated')
                else:
                    Amount=int(input('Enter Amount to be transfer: '))
                    if Amount>Balance:
                        print('InSufficient Funds ')
                        print('Current Transaction is terminated')
                    else:
                        Pin=int(input('Please Enter PIN: '))
                        if Pin==Pin_Number:
                            for i in Account_Details:
                                if i['Account_Number']==Account_Number:
                                    i['Balance']=i['Balance']-Amount
                                    Current_Balance=i['Balance']
                            for i in Account_Details:
                                if i['Account_Number']==CD_Account_Number:
                                    i['Balance']=i['Balance']+Amount
                                    print('Amount sucessfully transfered')
                                    Display=int(input('Enter 1 to display your balance: '))
                                    if Display==1:
                                        print('Your Current balance is '+str(Current_Balance)+' rs')
                                    print('Current Transaction is Completed')

                        else:
                            print('Invalid PIN')
                            print('Current Transaction is terminated')
            elif Action==3:
                Account_Number=int(input('Enter Account Number: '))
                for i in Account_Details:
                    if i['Account_Number']==Account_Number:
                        Pin_Number=i['Pin']
                        Balance=i['Balance']
                        Name=i['Name']
                if Name=='':
                    print(' Account Number is Invalid please enter valid Account Number')
                    print('Current Transaction is terminated')
                else:
                    Amount=int(input('Enter Amount to credit: '))
                    for i in Account_Details:
                        if i['Account_Number']==Account_Number:
                            i['Balance']=i['Balance']+Amount
                            print('Current Transaction is Completed')
        else:
            print('Action must be 1,2 or 3')
            print('Current Transaction is terminated')

    except Exception as e:
        print(e)
        print('Current Transaction is terminated')

    print(Account_Details)

