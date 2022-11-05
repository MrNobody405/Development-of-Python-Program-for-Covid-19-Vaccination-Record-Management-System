#WONG CHEE SHENG
#TP060635
"""
   Vaccine code    Dosage required    Intervals between doses    Age group
-----------------------------------------------------------------------------
        AF                2             2 weeks (or 14 days)     12 & above
        BV                2             2 weeks (or 21 days)     18 & above
        CZ                2             3 weeks (or 21 days)     12 - 45
        DM                2             4 weeks (or 28 days)     12 & above
        EC                1                      -               18 & above

Two vaccination centres: 1. VC1 2.VC2

         |     |
         |     |                - code: 3 (AF, DM, BV, EC)
  -------------------45
   |     |     |
   |     |     |                - code: 2 (CZ, AF, DM, BV, EC)
  -------------------18 
   |     |                      - code: 1 (CZ, AF, DM)
  -------------------12
   CZ    AF    BV               - code: 0 (ineligible)
         DM    EC
"""

from datetime import date, timedelta

#some functions---------
def backtomainmenu():
    while True:                                                                                                                                                        #a while loop for users to enter [Y] to get back to main menu.
        ans = input("\nPress [Y] to go back to main menu: ").upper()
        if ans == "Y":
            break

def print_vc1():
    waiting_for_dose2 = 0                                                                                                                    #variable waiting_for_dose2 is set to 0
    completed = 0                                                                                                                            #variable completed is set to 0
    vc_count = 0                                                                                                                             #variable vc_count is set to 0
    with open("vaccination.txt", "r") as file:
        for line in file:                                                                                                                    #loop each line in file 
            if line.startswith("Vaccination centre: 1"):                                                                                     #check if lines starts with "Vaccination centre: 1"
                next(file)                                                                                                                   #skip vaccine line, which vaccine is not needed
                if next(file).startswith("Dose 1            : Completed"):                                                                   #check if lines starts with "Dose 1            : Completed"
                    waiting_for_dose2 = waiting_for_dose2 + 1                                                                                #if dose 1 is completed, waiting_for_dose2 will + 1
                next(file)                                                                                                                   #skip dose 2 line as it is not needed                                         
                if next(file).startswith("Completion        : Completed"):                                                                   #check if lines starts with "Completion        : Completed"
                    completed = completed + 1                                                                                                #if completed vaccination, completed variable will + 1
                    waiting_for_dose2 = waiting_for_dose2 - 1                                                                                #if not completed vaccination, waiting_for_dose2 variable will - 1 
                vc_count += 1                                                                                                                #each loop, if there's a line starts with "Vaccination centre: 1", then vc_count variable will + 1
    print(f"""
----------------------------------------------------------
Total people in vaccination centre 1: {vc_count}
\nTotal people waiting for dose 2: {waiting_for_dose2}
\nTotal people completed vaccination: {completed}
----------------------------------------------------------
    """) #this print(f) function is able to print string and placeholder(variable) more efficiently
#explanation: if dose 1 is completed, EC vaccination will be completed hence completed variable + 1 and waiting_for_dose2 variable - 1. If dose 1 of other vaccine is completed, waiting_for_dose2 will + 1 and completion if statement will not execute as dose 2 have not been administered.

def print_vc2():
    waiting_for_dose2 = 0
    completed = 0
    vc_count = 0
    with open("vaccination.txt", "r") as file:
        for line in file:
            if line.startswith("Vaccination centre: 2"):
                next(file)
                if next(file).startswith("Dose 1            : Completed"):
                    waiting_for_dose2 = waiting_for_dose2 + 1
                next(file)
                if next(file).startswith("Completion        : Completed"):
                    completed = completed + 1
                    waiting_for_dose2 = waiting_for_dose2 - 1
                vc_count += 1
    print(f"""
----------------------------------------------------------
Total people in vaccination centre 2: {vc_count}
\nTotal people waiting for dose 2: {waiting_for_dose2}
\nTotal people completed vaccination: {completed}
----------------------------------------------------------
    """)
#print_vc2() have the same principle as print_vc1()

def get_staff():
    staff_list = []
    with open("staff.txt", "r") as file:                                                                                                                 #opens staff.txt file in read mode
        for line in file:                                                                                                                                #loops each line in file
            login = line[0:6]                                                                                                                            #index of 0 to 6 in line is stored in variable called login
            password = line[7:15]                                                                                                                        #index of 7 to 15 in line is stored in variable called password
            staff_list.append(login)                                                                                                                     #appending login and password into staff_list
            staff_list.append(password)
    #login      :   staff1              staff2              staff3              staff4       
    #password   :   20406080            30507090            40608010            50709020
    while True:
        lg = input("\nPlease enter staff ID: ")
        pw = input("\nPlease enter password: ")
        if (lg == staff_list[0] and pw == staff_list[1]) or (lg == staff_list[2] and pw == staff_list[3]) or (lg == staff_list[4] and pw == staff_list[5]) or (lg == staff_list[6] and pw == staff_list[7]):   #checks for corresponding login and password from staff_list
            break
        else:
            print("\nInvalid ID or password. Please ensure both ID and password is correct.")

def dose_administration(vaccine, dose1, dose2, completion, id_line):
    valid = 0
    while valid == 0:
        dose = input("\nPlease enter the dosage of vaccination: ")
        if vaccine == "EC":
            if dose == "1" and dose1 == "-":                                                                                                                         #if dose input == "1" and dose1 in file is "-", then patient entered a valid dose
                print("\nCongratulations for your vaccination. You EC vaccination have been completed.")
                dose1_complete(id_line)                                                                                                                                     #change the status of dose1 and completion in file from "-" to "Completed"
                completion_complete(id_line)
                valid = 1
            elif dose == "2" and dose1 == "-":                                                                                                                       #if dose input == "2" and dose1 in file is "-", program will prompt user that dose one have not been administered.
                print("\nThe dose that you entered is invalid. Your vaccine (EC) only have only dose. Please enter '1' to get your vaccine administered.")
            elif dose == "2" or completion == "Completed":                                                                                                            #if dose input == "2" or completion in file is "Completed", the program will prompt user that EC vaccine have been completed and there is no second dose for EC vaccine.
                print("\nYour only dosage of EC vaccine have been administered hence you have completed your vaccination. You will be redirected back to main menu.")
                valid = 1
            else:
                print("\nThe dose that you entered is invalid. Your vaccine (EC) only have only dose. Please enter '1' to get your vaccine administered.")           #if user enter other than 1 or 2
        elif vaccine == "CZ":
            if dose == "1":
                if dose1 == "-" and completion == "-":                                                                                                              #if dose input == "1" and the completion in file is "-", user have successfully entered a valid vaccine dose hence will be administered and assigned a date for second dose
                    print("\nCongratulations for your vaccination. Your first dosage have been administered.")
                    dose1_complete(id_line)                                                                                                                                #change the status of dose1 in file from "-" to "Completeed"
                    dose1_date = date.today()                                                                                                                       #It gets the date of the registration day
                    datefordose2 = dose1_date + timedelta(21)                                                                                                       #It assigns a specific date(after 21 days) for second dosage of vaccine
                    print("\nThe date for your vaccine second dosage is on " + str(datefordose2) + ".")
                    valid = 1
                else:                                                                          
                    print("\nYour first dosage of vaccine have been administered. Please enter '2' to get your second dosage or to check if you have completed vaccination.")
            
            elif dose == "2":
                if dose1 == "-" and completion == "-":
                    print("\nYour first dosage have not been administered. Please enter '1' to get your first dosage.")
                elif dose1 == "Completed" and dose2 == "-":
                    print("\nCongratulations for your vaccination. Your second dosage have been administered.")
                    dose2_complete(id_line)
                    completion_complete(id_line)
                    valid = 1
                else:
                    print("You have completed both of your vaccination. Please return to main menu.")
                    valid = 1
            else:
                    print("\nThe dose that you entered is invalid. Plase enter 1 or 2 to get your vaccine administered.")
        elif vaccine == "AF":
            if dose == "1":
                if dose1 == "-" and completion == "-":                                                                                                              #if dose input == 1 and the completion in file is "-", user have successfully entered a valid vaccine dose hence will be administered and assigned a date for second dose
                    print("\nCongratulations for your vaccination. Your first dosage have been administered.")
                    dose1_complete(id_line)                                                                                                                                #change the status of dose1 in file from "-" to "Completeed"
                    dose1_date = date.today()                                                                                                                       #It gets the date of the registration day
                    datefordose2 = dose1_date + timedelta(14)                                                                                                       #It assigns a specific date(after 14 days) for second dosage of vaccine
                    print("\nThe date for your vaccine second dosage is on " + str(datefordose2) + ".")
                    valid = 1
                else:                                                                          
                    print("\nYour first dosage of vaccine have been administered. Please enter '2' to get your second dosage or to check if you have completed vaccination.")
            
            elif dose == "2":
                if dose1 == "-" and completion == "-":
                    print("\nYour first dosage have not been administered. Please enter '1' to get your first dosage.")
                elif dose1 == "Completed" and dose2 == "-":
                    print("\nCongratulations for your vaccination. Your second dosage have been administered.")
                    dose2_complete(id_line)
                    completion_complete(id_line)
                    valid = 1
                else:
                    print("You have completed both of your vaccination. Please return to main menu.")
                    valid = 1
            else:
                    print("\nThe dose that you entered is invalid. Plase enter 1 or 2 to get your vaccine administered.")
        elif vaccine == "DM":
            if dose == "1":
                if dose1 == "-" and completion == "-":                                                                                                              #if dose input == 1 and the completion in file is "-", user have successfully entered a valid vaccine dose hence will be administered and assigned a date for second dose
                    print("\nCongratulations for your vaccination. Your first dosage have been administered.")
                    dose1_complete(id_line)                                                                                                                                #change the status of dose1 in file from "-" to "Completeed"
                    dose1_date = date.today()                                                                                                                       #It gets the date of the registration day
                    datefordose2 = dose1_date + timedelta(28)                                                                                                       #It assigns a specific date(after 14 days) for second dosage of vaccine
                    print("\nThe date for your vaccine second dosage is on " + str(datefordose2) + ".")
                    valid = 1
                else:                                                                          
                    print("\nYour first dosage of vaccine have been administered. Please enter '2' to get your second dosage or to check if you have completed vaccination.")
            
            elif dose == "2":
                if dose1 == "-" and completion == "-":
                    print("Y\nour first dosage have not been administered. Please enter '1' to get your first dosage.")
                elif dose1 == "Completed" and dose2 == "-":
                    print("\nCongratulations for your vaccination. Your second dosage have been administered.")
                    dose2_complete(id_line)
                    completion_complete(id_line)
                    valid = 1
                else:
                    print("You have completed both of your vaccination. Please return to main menu.")
                    valid = 1
            else:
                    print("\nThe dose that you entered is invalid. Plase enter 1 or 2 to get your vaccine administered.")                            
        elif vaccine == "BV":
            if dose == "1":
                if dose1 == "-" and completion == "-":                                                                                                              #if dose input == 1 and the completion in file is "-", user have successfully entered a valid vaccine dose hence will be administered and assigned a date for second dose
                    print("\nCongratulations for your vaccination. Your first dosage have been administered.")
                    dose1_complete(id_line)                                                                                                                                #change the status of dose1 in file from "-" to "Completeed"
                    dose1_date = date.today()                                                                                                                       #It gets the date of the registration day
                    datefordose2 = dose1_date + timedelta(21)                                                                                                       #It assigns a specific date(after 14 days) for second dosage of vaccine
                    print("\nThe date for your vaccine second dosage is on " + str(datefordose2) + ".")
                    valid = 1
                else:                                                                          
                    print("\nYour first dosage of vaccine have been administered. Please enter '2' to get your second dosage or to check if you have completed vaccination.")
            
            elif dose == "2":
                if dose1 == "-" and completion == "-":
                    print("\nYour first dosage have not been administered. Please enter '1' to get your first dosage.")
                elif dose1 == "Completed" and dose2 == "-":
                    print("\nCongratulations for your vaccination. Your second dosage have been administered.")
                    dose2_complete(id_line)
                    completion_complete(id_line)
                    valid = 1
                else:
                    print("You have completed both of your vaccination. Please return to main menu.")
                    valid = 1
            else:
                print("\nThe dose that you entered is invalid. Plase enter 1 or 2 to get your vaccine administered.")

#statistical information on patient vaccinated function
def statistical_information_on_patient_vaccinated():
    print("---------------------------------------------------------------------------")
    print("               Statistical Information On Patient Vaccinated               ")
    print("---------------------------------------------------------------------------")
    while True:
        vc_centre = input("\nPlease enter which vaccination centre you want to print: ")
        if vc_centre == "1":                                                                                                                        #staff choose which vaccination centre to print
            print_vc1()
            break
        elif vc_centre == "2":
            print_vc2()
            break
        else:
            print("Invalid input. Please enter 1 or 2 only.")

def get_id():                                                                                                                                                          #check ID of patient and store other needed information in variables
    valid_id = 0
    id_line = 1
    while valid_id == 0:
        patient_id = input("\nPlease enter your patient ID: ")                                                                                                             
        with open("vaccination.txt", "r") as file3:
            for number, line in enumerate(file3):                                                                                                                      #The enumerate() function allows you to loop over an iterable object and keep track of how many iterations have occurred.
                if line.startswith("ID                : "):                                                                                                            #only gets the line that starts with "ID                : "
                    id_check = line[20:26]                                                                                                                             #id_check will store the value from that specific line from index 20:26
                    if patient_id == id_check:                                                                                                                         #if patient_id entered is the same as id_check(which is in the file), the patient is valid and will perform functions below
                        id_line = number + 1                                                                                                                           #id_line will plus 1 to keep track of which line which will be used later
                        vaccination_centre = (next(file3).strip()).removeprefix("Vaccination centre: ")    
                        vaccine = (next(file3).strip()).removeprefix("Vaccine           : ")                                                        
                        dose1 = (next(file3).strip()).removeprefix("Dose 1            : ")
                        dose2 = (next(file3).strip()).removeprefix("Dose 2            : ")
                        completion = (next(file3).strip()).removeprefix("Completion        : ")
                        valid_id = 1
            if valid_id == 0:                                                                                                                                          #if patient_id entered is not in the file, valid_id will say 0 and while loop will continue to loop the user input
                print("Invalid ID. Please ensure ID entered is valid/registered.")
    return patient_id, vaccination_centre, vaccine, dose1, dose2, completion, id_line

def get_details():                                                                                                                                                     #check ID of patient and store other needed information in variables
    patient_id, vaccination_centre, vaccine, dose1, dose2, completion, id_line = get_id()
    with open("patient.txt", "r") as file:
        for line in file:
            if ("ID                : " + patient_id) in line:                                                                                                          #if patient id can be found in the file, it will set other variables to values under the patient id and removing the prefix to only contain the value needed
                patient_name = (next(file).strip()).removeprefix("Patient name      : ")
                patient_age = (next(file).strip()).removeprefix("Patient age       : ")
                vaccination_centre = (next(file).strip()).removeprefix("Vaccination centre: ")
                vaccine = (next(file).strip()).removeprefix("Vaccine           : ")
                contact_number = (next(file).strip()).removeprefix("Contact number    : ")
                email_address = (next(file).strip()).removeprefix("Email address     : ")
                height = (next(file).strip()).removeprefix("Height            : ")
                weight = (next(file).strip()).removeprefix("Weight            : ")
    return patient_id, vaccination_centre, vaccine, dose1, dose2, completion, id_line, patient_name, patient_age, contact_number, email_address, height, weight

def dose1_complete(id_line):
    with open("vaccination.txt", "r") as file:
        list_of_lines = file.readlines()                                                                                                     #it reads all the line in file then store each line into array called "list_of_line"
        list_of_lines[id_line + 2] = "Dose 1            : Completed\n"                                                                       #in the array, the position of dose 1 which is id_line + 2 is appended

    with open("vaccination.txt", "w") as file:                                                                                               #open file in write mode to rewrite the file
        file.writelines(list_of_lines)                                                                                                       #overwrite the file with list_of_lines with new information appended

def dose2_complete(id_line):
    with open("vaccination.txt", "r") as file:
        list_of_lines = file.readlines()
        list_of_lines[id_line + 3] = "Dose 2            : Completed\n"
    
    with open("vaccination.txt", "w") as file:
        file.writelines(list_of_lines)                                                                                                       #overwrite the file with list_of_lines with new information appended

def completion_complete(id_line):
    with open("vaccination.txt", "r") as file:
        list_of_lines = file.readlines()
        list_of_lines[id_line + 4] = "Completion        : Completed\n"

    with open("vaccination.txt", "w") as file:
        file.writelines(list_of_lines)               

#patient record and vaccination status function
def patient_record_and_vaccination_status():
    print("---------------------------------------------------------------------------")
    print("                Search Patient Record And Vaccination Status               ")
    print("---------------------------------------------------------------------------")
    patient_id, vaccination_centre, vaccine, dose1, dose2, completion, id_line, patient_name, patient_age, contact_number, email_address, height, weight = get_details()            #obtains all the information of patient from file
    print("\nBelow is your details.")                                                                                                              #this part will display the patient record from patient.
    print("-------------------------------------------------------")
    print("ID                : " + patient_id)
    print("Name              : " + patient_name)
    print("Age               : " + patient_age)
    print("Vaccination centre: VC" + vaccination_centre)
    print("Vaccine           : " + vaccine)
    print("Contact number    : " + contact_number)
    print("Email address     : " + email_address)
    print("Height            : " + height + "cm")
    print("Weight            : " + weight + "kg")
    print("\nBelow is your vaccination status.")                                                                                                   #this part will display the vaccination status from patient.
    print("-------------------------------------------------------")
    print("Vaccine Code      : " + vaccine)
    if vaccine == "EC":                                                                                                                            #if patient's vaccine is "EC" then their dosage required is two while the others are one
        dosage_required = "1"
    else:
        dosage_required = "2"
    print("Dosage required   : " + dosage_required)
    print("Before dose 1     : New")
    print("After dose 1      : " + dose1)
    print("After dose 2      : " + dose2)

#registration functions
def get_vc():
    print("---------------------------------------------------------------------------")
    print("                          New Patient Registration                         ")
    print("---------------------------------------------------------------------------")
    print("\nPlease select one of the vaccination centre.")
    print("1 : Vaccination centre 1            2: Vaccination centre 2")

    vaccination_centre = 0                                                                                                                     #initializing vaccination_centre variable to 0
    while (vaccination_centre != "1" or vaccination_centre != "2"):
        vaccination_centre = input("\nPlease enter the corresponding number for your preferred vaccination centre:")
        if (vaccination_centre == "1" or vaccination_centre == "2"):
            break
        else: 
            print("Invalid input. Please enter 1 or 2 for corresponding preferred vaccination centre.")
    #this while loop allows patient to only register for integer 1 or 2 for the corresponding vaccination centre. It then stores the input in variable "vaccination_centre"
    return vaccination_centre

def get_age():
    while True:
        try:                                                                                                                              #only accepts onteger value.
            patient_age = int(input("\nPlease enter your age:"))                                                                          #depending on the age, vaccine selection is assigned for later to provide a selection of vaccine available according to their age group
            if patient_age < 12:
                vaccine_selection = 0
                break
            elif patient_age < 18:    
                vaccine_selection = 1
                break
            elif patient_age <= 45:
                vaccine_selection = 2
                break
            else:
                vaccine_selection = 3
                break
        except ValueError:
            print("Invalid input. Please enter a valid age.")
    return patient_age, vaccine_selection

def get_vaccine():
    patient_age, vaccine_selection = get_age()                                                                                          #calling get_age() and store the value of patient_age and vaccine_selection
    
    if vaccine_selection == 0:
        pass
    elif vaccine_selection == 1:                                                                                                        #age group between 12 to 18.
        print("\nPlease select a vaccine to be administered.")
        print("1 : CZ         2 : AF         3 : DM")
        print("\n")
        while True:
            vaccine_code = input("Please enter the corresponding number for your preferred vaccine: ")
            if vaccine_code == "1":
                vaccine = "CZ"
                break
            elif vaccine_code == "2":
                vaccine = "AF"
                break
            elif vaccine_code == "3":
                vaccine = "DM"
                break
            else:
                print("Invalid input. Please enter a valid vaccine selection.")
        #this while loop allows patient from vaccine selection "1" to choose only vaccine "CZ", "AF" or "DM". It then stores the input into variable "vaccine"
    elif vaccine_selection == 2:                                                                                                      #age group between 18 to 45.
        print("\nPlease select a vaccine to be administered.")
        print("1 : CZ         2 : AF         3 : DM         4 : BV         5 : EC")
        print("\n")

        while True:
            vaccine_code = input("Please enter the corresponding number for your preferred vaccine: ")
            if vaccine_code == "1":
                vaccine = "CZ"
                break
            elif vaccine_code == "2":
                vaccine = "AF"
                break
            elif vaccine_code == "3":
                vaccine = "DM"
                break
            elif vaccine_code == "4":
                vaccine = "BV"
                break
            elif vaccine_code == "5":
                vaccine = "EC"
                break
            else:
                print("Invalid input. Please enter a valid vaccine selection")
        #this while loop allows patient from vaccine selection "2" to choose only vaccine "CZ", "AF", "DM", "BV" or "EC". It then stores the input into variable "vaccine"
    elif vaccine_selection == 3:                                                                                                                             #age group from 46 and above
        print("\nPlease select a vaccine to be administered.")
        print("1 : AF         2 : DM         3 : BV         4 : EC")
        print("\n")

        while True:
            vaccine_code = input("Please enter the corresponding number for your preferred vaccine: ")
            if vaccine_code == "1":
                vaccine = "AF"
                break
            elif vaccine_code == "2":
                vaccine = "DM"
                break
            elif vaccine_code == "3":
                vaccine = "BV"
                break
            elif vaccine_code == "4":
                vaccine = "EC"                            
                break
            else:
                print("Invalid input. Please enter a valid vaccine selection")
        #this while loop allows patient from vaccine selection "3" to choose only vaccine "AF", "DM", "BV" or "EC". It then stores the input into variable "vaccine"
    return patient_age, vaccine

def get_patient_details():
    print("\n")
    print("Please enter details about yourself below.\n")

    while True:
        name = input("\nPlease enter your name: ").upper()
        if (any(character.isdigit() for character in name)):                                                                              #to check if any of the characters in name containes integer.
            print("Invalid input. Please enter a name without any number.")
        else:
            break
    #asking patient to enter name. Input cannot have integer. Valid input will be stored in variable "name".

    while True:
        contact_number = input("\nPlease enter your contact number: ")
        if contact_number.isdigit() == True:                                                                                             #The isdigit() method returns “True” if all characters in the string are digits, Otherwise, It returns “False”.
            a_string = str(contact_number)                                                                                               #create a new variable to hold the string of the input and perform length checking.
            if len(a_string) >= 7 and len(a_string) <= 11:
                break
            else:
                print("Invalid contact number. It should contain seven to eleven digits.")
        else:
            print("Invalid input. Please ensure contact number does not contain any characters.")
    #asking patient to enter contact number. Contact number should only consists of string and not string. Valid input will be stored in variable "contact_number"

    while True:
        email_address = input("\nPlease enter your email address: ")                                                                      
        if "@" in email_address and ".com" in email_address:
            break
        else:
            print("Email address provided is not valid.")
    #asking patient to enter email_address. Email address is validated where it must contains "@" and ".com"

    while True:
        height = input("\nPlease enter your height in centimeter and it should not have decimal number: ")
        if height.isdigit() == True:                                                                                                     #The isdigit() method returns “True” if all characters in the string are digits, Otherwise, It returns “False”.
            a_string = str(height)                                                                                                       #reusing a_string variable to hold the string of the input and perform length checking. Height in centimter should contain only 2 or 3 digits however there are no limit to height as dwarfism exists.
            if len(a_string) == 2 or len(a_string) == 3:
                break
            else:
                print("Invalid height. Please ensure height entered is in centimeter.")
        else:
            print("Invalid input. Please ensure height does not contain any characters or height does not contain any decimal number.")
    #asking patient to enter height. Height should not contain characters and decimal number for the ease of recording patient detail. 

    while True:
        weight = input("\nPlease enter your weight in kilogram and it should not have decimal number: ")
        if weight.isdigit() == True:                                                                                                     #The isdigit() method returns “True” if all characters in the string are digits, Otherwise, It returns “False”.
            a_string = str(weight)                                                                                                       #reusing a_string variable to hold the string of the input and perform length checking. Weight in kilogram should contain only 2 or 3 digits.
            if len(a_string) == 2 or len(a_string) == 3:
                break
            else:
                print("Invalid weight. Please ensure weight entered is in kilogram.")
        else:
            print("Invalid input. Please ensure weight does not contain any characters or weight does not contain any decimal number.")
    #asking patient to enter weight. Weight should not contain characters and decimal number for the ease of recording patient detail. 
    return name, contact_number, email_address, height, weight

def file_input(name, patient_age, vaccination_centre, vaccine, contact_number, email_address, height, weight):  
    file = open("patient.txt", "r")                                                                                                              #open to read patient.txt file
    for line in file:                                                                                                                            #for loop to check the criteria of lines in file 
        if line.startswith('ID                : '):                                                                                              #checking for lines that starts with 'ID                : '
            ids = line[21:27]                                                                                                                    #abstracting the values in line from [21:27] to obtain the patient IDs
            prev_id = [ids]                                                                                                                      #place the IDs into an list called "prev_id"

    latest_id = (prev_id[-1])                                                                                                                   #take the latest ID and put it in variable "latest_id"
    patient_id = int(latest_id) + 1                                                                                                             #change the type to int first then assign the latest_id by plus 1 to itself
    patient_id =  str(patient_id).zfill(6)     
    file.close()
    #read and assign patient ID

    file = open("patient.txt", "a")
    file.write("\n")
    file.write("\nID                : " + str(patient_id))                                                                                       #writing all the details into the file(patient.txt) accordingly, str() is used to change int to string. This is to allow values to be written into file.
    file.write("\nPatient name      : " + name)
    file.write("\nPatient age       : " + str(patient_age))
    file.write("\nVaccination centre: " + str(vaccination_centre))
    file.write("\nVaccine           : " + vaccine)
    file.write("\nContact number    : " + str(contact_number))
    file.write("\nEmail address     : " + str(email_address))
    file.write("\nHeight            : " + str(height))
    file.write("\nWeight            : " + str(weight))
    file.close()
    #append information into patient.txt file

    file2 = open("vaccination.txt", "a")                                                                                                         #open to append the information in vaccination.txt file
    file2.write("\n")
    file2.write("\nID                : " + str(patient_id))                                                                                      #writing some details that is needed into file(vaccination.txt)
    file2.write("\nVaccination centre: " + str(vaccination_centre))
    file2.write("\nVaccine           : " + vaccine)
    file2.write("\nDose 1            : -")
    file2.write("\nDose 2            : -")
    file2.write("\nCompletion        : -")
    file2.close()
    #append information into vaccination.txt file

    return patient_id, name, patient_age, vaccination_centre, vaccine, contact_number, email_address, height, weight

def display(patient_id, name, patient_age, vaccination_centre, vaccine, contact_number, email_address, height, weight):
    print("\nBelow is your details.\n")
    print("ID                : " + patient_id)                                                                                                     #this function will display all the input from patient as well as showing them their ID.
    print("Name              : " + name)
    print("Age               : " + str(patient_age))
    print("Vaccination centre: VC" + str(vaccination_centre))
    print("Vaccine           : " + vaccine)
    print("Contact number    : " + str(contact_number))
    print("Email address     : " + str(email_address))
    print("Height            : " + str(height) + "cm")
    print("Weight            : " + str(weight) + "kg")

def dose1_date():
    registration_date = date.today()                                                                                                                                  #It gets the date of the registration day
    datefordose1 = registration_date + timedelta(7)                                                                                                                   #It assigns a specific date(after a week of registration) for first dosage of vaccine
    print("\nThe date for your vaccine first dosage is on " + str(datefordose1) + ".")

def registration():
    vaccination_centre = get_vc()
    patient_age, vaccine = get_vaccine()
    if patient_age < 12:
        print("You are not eligible for vaccination.")
    else: 
        name, contact_number, email_address, height, weight = get_patient_details()                                                                   #lastly, it executes get_patient_details to get user details
        print("\nThank you for registering!")    
        patient_id, name, patient_age, vaccination_centre, vaccine, contact_number, email_address, height, weight = file_input(name, patient_age, vaccination_centre, vaccine, contact_number, email_address, height, weight)                                     #It executes file_input() to get patient a new ID as well as inputting the details into the file called "new patient registration file.txt"
        display(patient_id, name, patient_age, vaccination_centre, vaccine, contact_number, email_address, height, weight)
        dose1_date()
#----------------------- 

def vaccine_administration():
    print("---------------------------------------------------------------------------")
    print("                           Vaccine Administration                          ")
    print("---------------------------------------------------------------------------")
    patient_id, vaccination_centre, vaccine, dose1, dose2, completion, id_line = get_id()                                                        #calling get_id() function to validate patient_id
    dose_administration(vaccine, dose1, dose2, completion, id_line)

def staff_administration():
    while True:                                                                                                                                         #staff only interface, where they have full access to the functions
        ans = input("\nThis is an authorized access only. Please enter [Y] to continue or [N] to go back to main menu: ").upper()
        if ans == "N":
            break
        elif ans == "Y":
            get_staff()
            while True:
                print("---------------------------------------------------------------------------")
                print("                            Staff Aministration                            ")
                print("---------------------------------------------------------------------------")
                print("               1. New Patient Registration")
                print("               2. Vaccine Administration")
                print("               3. Search Patient Record and Vaccination Status")
                print("               4. Statistical information on patient vaccinated")
                print("               5. exit")
                ans1 = input("\nPlease enter your option: ")
                if ans1 == "1":
                    registration()
                    backtomainmenu()
                elif ans1 == "2":
                    vaccine_administration()
                    backtomainmenu()
                elif ans1 == "3":
                    patient_record_and_vaccination_status()
                    backtomainmenu()
                elif ans1 == "4":
                    statistical_information_on_patient_vaccinated()
                    backtomainmenu()
                elif ans1 == "5":
                    break
                else:
                    print("Invalid input. Please enter the available numbers to proceed with the program.")
            break
        else:
            print("Invalid input. Please enter [Y] or [N] to proceed.")

def main_menu():
    while True:                                                                                                                                #loops main menu until users input a valid number to proceed with program or entered "5" to exit program.
        print("---------------------------------------------------------------------------")
        print("                                 Main Menu                                 ")
        print("---------------------------------------------------------------------------")
        print("               1. New Patient Registration")
        print("               2. Staff Administration")
        print("               3. Search Patient Record and Vaccination Status")
        print("               4. Exit")
        option = input("\nPlease enter your option: ")
        if option == "1":
            registration()
            backtomainmenu()
        elif option == "2":
            staff_administration()
        elif option == "3":
            patient_record_and_vaccination_status()
            backtomainmenu()
        elif option == "4": 
            break
        else:
            print("\nInvalid input. Please enter the available numbers to proceed with the program.")

#main execution---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
main_menu()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------