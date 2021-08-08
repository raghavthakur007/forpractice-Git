name=input("Enter your name")
print("Enter the marks obtained in following subjects :-")
de=int(input("Enter your marks in Digital electronics :"))
bse=int(input("Enter your marks obtained in compurt science :"))
English=int(input("Enter yur marks in English :"))
matlab=int(input("Enter your marks in matlab :"))
percentage=((de+bse+English+matlab)*100)/400
print("The name of the student is :",name)
print("The marks obtained in the Digital Electronics %d,CSE %d,English %d and matlab %d are :",de,bse,English,matlab)
print("percentage : ",percentage) 
        
