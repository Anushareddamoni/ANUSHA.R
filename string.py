m=int(input("marks in maths: "))
s=int(input("marks in science: "))
e=int(input("marks in english: "))
total_marks=m+s+e
average=(total_marks)/3
percentage=(total_marks/300)*100
grade=""
if(percentage>90):
    grade="A"
elif(percentage>80 and percentage<=90):
    grade="B"
elif(percentage>70 and percentage<=80):
    grade="C"
else:
    grade="f"
print(f"Total marks:{total_marks}\nAvarage marks:{average}\nGrade:{grade}")    
                
    
