''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''


student_pet_count_list = [0, 1, 2, 3, 5, 4, 2, 0, 1, 3]

# 2.4 updating an index
student_pet_count_list[2] = 4
student_pet_count_list[3] = student_pet_count_list[3] + 1
student_pet_count_list[-1] = student_pet_count_list[-1] + 2

#2.4 add a number to the back of the list (array)
student_pet_count_list.append(4)

#2.2 checking indexes within the list (array)
ITEM_AT_INDEX_THREE = student_pet_count_list[3]
#print(student_pet_count_list[6])
ITEM_THREE_FROM_BACK = student_pet_count_list[-3]
#print(student_pet_count_list[-3])

#2.3 checking the length of the array
NUM_OF_STUDENTS = len(student_pet_count_list)
print(NUM_OF_STUDENTS)

#2.3 doing the average = sum / number of items
SUM = 0
for INDIVIDUAL_PET_COUNT in student_pet_count_list:
  SUM = SUM + INDIVIDUAL_PET_COUNT
print(SUM)

AVERAGE = SUM / NUM_OF_STUDENTS
print(AVERAGE)
