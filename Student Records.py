import os
path="C:\\Student Reports"

while True:
    
    try:
        Name=input('Enter Student Name: ')
        Student_Name=Name.capitalize()
        if os.path.exists(path+'\\'+Student_Name+'.txt'):
            print(Student_Name+' record already present in the folder')
            Rem=int(input('To remove existing record enter 1: '))
            if Rem==1:
                os.remove(path+'\\'+Student_Name+'.txt')
        else:
            file=open(path+'\\'+Student_Name+'.txt','w')
            file.write("--------------------------------------------\n")
            file.write(Student_Name+' Annual Report \n')
            Subjects=['Telugu ','Hindi  ','English','Maths  ','Science','Social ']
            Marks=[]
            for i in range(0,6):
                Score=int(input('Enter Marks for '+Subjects[i]+': '))
                Marks.append(Score)
            count=0
            Total=sum(Marks)
            file.write("--------------------------------------------\n")
            for i in range(6):
                if Marks[i]>=90:
                    file.write(Subjects[i]+"    :- "+str(Marks[i])+'/100 '+' | '+"Grade - "+"A+ \n")
                elif Marks[i]>=80:
                    file.write(Subjects[i]+"    :- "+str(Marks[i])+'/100 '+' | '+"Grade - "+"A \n")
                elif Marks[i]>=70:
                    file.write(Subjects[i]+"    :- "+str(Marks[i])+'/100 '+' | '+"Grade - "+"B \n")
                elif Marks[i]>=60:
                    file.write(Subjects[i]+"    :- "+str(Marks[i])+'/100 '+' | '+"Grade - "+"C \n")
                elif Marks[i]>=50:
                    file.write(Subjects[i]+"    :- "+str(Marks[i])+'/100 '+' | '+"Grade - "+"D \n")
                elif Marks[i]>=40:
                    file.write(Subjects[i]+"    :- "+str(Marks[i])+'/100 '+' | '+"Grade - "+"E \n")
                else:
                    count=count+1
                    file.write(Subjects[i]+"   :-   "+str(Marks[i])+'/100 '+' | '+"Grade - "+"Fail \n")
            file.write("--------------------------------------------\n")
            file.write('Total Marks = '+str(Total)+'/600 | Percentage :- '+str(round(Total/6,1))+"\n")
            file.write("--------------------------------------------\n")
            if count==0:
                if Total>=550:
                    file.write('Verdict :- Excellent \n')
                elif Total>=500:
                    file.write('Verdict :- Very Good \n')
                elif Total>=450:
                    file.write('Verdict :- Good \n')
                elif Total>=400:
                    file.write('Verdict :- OK \n')
                elif Total>=350:
                    file.write('Verdict :- Average \n')
                elif Total>=300:
                    file.write('Verdict :- Need Improvement \n')
                else:
                    file.write('Verdict :- Bad \n')
            else:
                file.write('Verdict :- Fail \n')
            file.write("--------------------------------------------\n")
            file.close()
            Exit=int(input('Enter 1 to exit 0 to Continue: '))
            if Exit==1:
                break
           
    except Exception as e:
        print(e)
        print('Again start with student name')
