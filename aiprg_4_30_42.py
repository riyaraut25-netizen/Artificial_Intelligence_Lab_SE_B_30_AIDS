print("The subjects to be entered are : PHYSICS,CHEMISTRY,MATHS,BIOLOGY,PROGRAMMING,STATISTICS,CIRCUITS,AI CONCEPTS,GRAPHICS,CONSTRUCTION ")
print("\nEnter the 2 subjectS to get the career options :\n")
sub1=input("Enter a subject 1 : ") 
sub2=input("Enter a subject 2 : ")
if(sub1=="MATHS" and sub2=="PHYSICS") or (sub1=="PHYSICS" and sub2=="MATHS"):
 print("\nSuggested career option is : MECHANICAL ENGINEERING ")
elif(sub1=="PROGRAMMING" and sub2=="MATHS") or (sub1=="MATHS" and sub2=="PROGRAMMING"):
 print("\nSuggested career option is : COMPUTER ENGINEERING ")
elif(sub1=="BIOLOGY" and sub2=="CHEMISTRY") or (sub1=="CHEMISTRY" and sub2=="BIOLOGY"):
 print("\nSuggested career option is : BIOTECNOLOGY")
elif(sub1=="CIRCUITS" and sub2=="MATHS") or (sub1=="MATHS" and sub2=="CIRCUITS"):
 print("\nSuggested career option is : ELECTRONICS ENGINEERING")
elif(sub1=="PROGRAMMING" and sub2=="STATISTICS") or (sub1=="STATISTICS" and sub2=="PROGRAMMING"):
 print("\nSuggested career option is : AIDS")
elif(sub1=="PROGRAMMING" and sub2=="AI CONCEPTS") or (sub1=="AI CONCEPTS" and sub2=="PROGRAMMING"):
 print("\nSuggested career option is : AIML")
elif(sub1=="GRAPHICS" and sub2=="CONSTRUCTION") or (sub1=="CONSTRUCTION" and sub2=="GRAPHICS"):
 print("\nSuggested career option is : 'CIVIL ENGINEERING' ")
else:
 print("\nDid Not Entered Valid Subjects")
