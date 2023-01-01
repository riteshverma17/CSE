#This project makes acronym of given line 
#KOC-42
#Team Members:  (1)Ritesh Verma
#               (2)Hariesh Ragavendhar
#               (3)Nityadev Singh 


a = input().replace('of','').split()
for i in a:
  acronym=i[0].upper()
  print(acronym, end="")



