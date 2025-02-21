Questions=[{'ID':1,'Question':'How Single Line Comments are comments are represented in python','A':'#','B':'@','C':'%','D':'/',
            'AP':'A','PAF':'A','E':'A','DP':'A or D','PriceAmount':1000,'ActualAmount':0,'Answer':'A'},
           {'ID':2,'Question':'Which of the following is not a Arthematic Operator','A':'*','B':'%','C':'@','D':'/',
            'AP':'C','PAF':'C','E':'C','DP':'A or C','PriceAmount':5000,'ActualAmount':0,'Answer':'C'},
           {'ID':3,'Question':'Which keyword used to define function in python','A':'super','B':'__init__','C':'class','D':'def',
            'AP':'D','PAF':'D','E':'D','DP':'B or D','PriceAmount':10000,'ActualAmount':0,'Answer':'D'},
           {'ID':4,'Question':'Which keyword used to define class ','A':'super','B':'__init__','C':'class','D':'def',
            'AP':'C','PAF':'C','E':'C','DP':'C or D','PriceAmount':20000,'ActualAmount':0,'Answer':'C'},
           {'ID':5,'Question':'Which is not a feature of python','A':'dynamically typed','B':'case insensitive','C':'zero indexing','D':'interpreted',
            'AP':'B','PAF':'B','E':'B','DP':'B or D','PriceAmount':40000,'ActualAmount':40000,'Answer':'B'},
           {'ID':6,'Question':'Which function used to display output ','A':'output()','B':'input()','C':'printf()','D':'print()',
            'AP':'D','PAF':'C','E':'D','DP':'C or D','PriceAmount':80000,'ActualAmount':40000,'Answer':'D'},
           {'ID':7,'Question':'Which is unordered sequence ','A':'Tuple','B':'String','C':'Set','D':'List',
            'AP':'D','PAF':'C','E':'C','DP':'C or D','PriceAmount':160000,'ActualAmount':40000,'Answer':'C'},
           {'ID':8,'Question':'Which of the following is not a set function ','A':'discard()','B':'add()','C':'update()','D':'index()',
            'AP':'D','PAF':'D','E':'D','DP':'C or D','PriceAmount':320000,'ActualAmount':40000,'Answer':'D'},
           {'ID':9,'Question':'Which of the following is not related to OOP ','A':'file','B':'polymorphism','C':'Inheritance','D':'Abstraction',
            'AP':'A','PAF':'C','E':'A','DP':'A or D','PriceAmount':640000,'ActualAmount':40000,'Answer':'A'},
           {'ID':10,'Question':'Which of the following is not a parameter passing type in functions ','A':'Default','B':'Positional','C':'Conditional','D':'Keyword',
            'AP':'D','PAF':'C','E':'C','DP':'C or A','PriceAmount':1250000,'ActualAmount':1250000,'Answer':'C'},
           {'ID':11,'Question':'Which of the follwoing is not a file opening mode ','A':'a','B':'w','C':'r','D':'z',
            'AP':'D','PAF':'C','E':'D','DP':'C or D','PriceAmount':2500000,'ActualAmount':1250000,'Answer':'D'},
           {'ID':12,'Question':'Which o the following is not a built in data type in python ','A':'Array','B':'int','C':'float','D':'string',
            'AP':'A','PAF':'C','E':'A','DP':'A or D','PriceAmount':5000000,'ActualAmount':1250000,'Answer':'A'},
           {'ID':13,'Question':'Which of the following is not a sequence object ','A':'String','B':'Class','C':'List','D':'Tuple',
            'AP':'B','PAF':'A','E':'B','DP':'C or B','PriceAmount':10000000,'ActualAmount':10000000,'Answer':'B'}]

Won_Prize_Money=0
count1=0
count2=0
count3=0
count4=0
count=0
LifeLines=['1-Audiance pole','2-Phone a Friend','3-Expert','4-Double Dip']
try:
    for i in Questions:
        print(str(i['ID'])+' '+i['Question'])
        print('  A. '+i['A'])
        print('  B. '+i['B'])
        print('  C. '+i['C'])
        print('  D. '+i['D'])
        print('Avalible LifeLines')
        for i in LifeLines:
            print(i)
        Option=int(input(' Enter 1 to use Audiance pole 2 to use Phone a Friend 3 to Use Expert 4 to use Double Dip[50:50] 0 to skip life line: '))
        if Option in (1,2,3,4):
            if Option==1 and count1==0:
                print(' Audiance suggesting '+i['AP']+' as answer')
                LifeLine.remove('1-Audiance pole')
                count1=count1+1
            elif Option==2 and count2==0:
                print(' Your friend suggesting '+i['PAF']+' as answer')
                LifeLine.remove('2-Phone a Friend')
                count2=count2+1
            elif Option==3 and count3==0:
                print(' Expert suggesting '+i['E']+' as answer')
                LifeLine.remove('3-Expert')
                count3=count3+1
            elif Option==4 and count4==0:
                print(' Answer is among '+i['DP'])
                LifeLine.remove('4-Double Dip')
                count4=count4+1
            else:
                print('Inavalid option or you already used this life line')
        answer=input('Enter the Answer A,B,C or D: ')
        Answer=answer.upper()
        if Answer!=i['Answer']:
            print('Sorry Wrong answer')
            print('Congrats you won '+str(Won_Prize_Money)+' rs')
            break
        else:
            count=count+1
            if i['ID']%5==0 and count!=13:
                print('You reached '+str(i['ID']/5)+' Save point you won '+str(i['ActualAmount']))
                Won_Prize_Money=i['ActualAmount']
            con=int(input('Enter 1 for continue 0 to exit: '))
            if con==0:
                print('Congrats you won '+str(i['PriceAmount'])+' rs')
                break


except Exception as e:
    print(e)
    print('please again start game from starting')

if count==13:
    print('Congrats you won '+str(Won_Prize_Money)+' rs')




                      
