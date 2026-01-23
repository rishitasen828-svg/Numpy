import numpy as np
marks=np.array([40,44,50,52,60])
print("The Marks of the students are:")
print(marks)
marks[marks<50]=marks[marks<50]+5
print("The Updated marks of the students are:")
print(marks)
print("The Mean score of the class is:")
mean=sum(marks)/len(marks)
print(mean)

