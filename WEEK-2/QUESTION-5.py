def dataDisplay():
   dataList=[]
   dataDictionary={}
  #this question seemed difficult but was quiet easy , the only problem i faced was (look belo)
   for i in range(3):
    name=input("Enter name of student no-{} :".format(i+1))
    age=input("Enter age of student no-{} :".format(i+1))
    grade=input("Enter grade of studnet no-{} :" .format(i+1))
    dataTuple=(name,int(age),grade.upper())
     #in the line below i was first trying to add values in datalist by datalist[i]=datatuple because of my experience in js, but after a quick query i found out we use append in python .
    dataList.append(dataTuple)

    for key ,value, extra in dataList:
      dataDictionary[key]=value,extra
    
   for key,(value,extra) in dataDictionary.items():
      print(f"The name of {key} is {value} years old and grade is : {extra}")


dataDisplay()

#approach was simple
#1. take data rom user through a loop 3 times
#2. add data to tupple in each iteration and then from tupple to list 
#the iterate over dictionary to unpack all the values
