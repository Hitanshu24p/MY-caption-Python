
import csv
def write_into_csv(info_list):
    with open('student_info.csv','a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            write.writerow({"Name", "Age", "Contact Numbaer", "E-mail ID"})
            
        write.writerow(info_list)


if __name__=='__main__':
    condition = true
    student_num = 1 

    while(condition):
        student_info = input("enter student information in the following format (Name Age Contact_Number E-mail_ID):".format(student_num))

        
        #split
        student_info_list = student_info.split(' ')
        print("Enter split up information is: " + str(student_info_list))

        print("\n The entered information is -\n Name: {}\n Age: {}\n Contact_Number: {}\n E-mail_ID: {}"
              .format(student_info.list{0}, student_info_list{1}, student_info_list{2}, student_indo_list{3}))
        choice_check = input("Is the entered information correct? (yes/no):")

        if choice_check == "yes":
             write_into_csv(student_info_list)
              condition_check = input("Enter (yes/no) if you want to enter the information for another student: ")
              if condition_check == "yes":
                  condition = True
                  student_num = student_num + 1
                elif condition_check == "no":
                    condition = False
        elif choice_check == "no":
            print("\n please re-enter the values!")
