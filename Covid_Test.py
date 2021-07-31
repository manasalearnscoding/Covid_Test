#GLOBAL VARIABLES
from IPython.display import clear_output
name_values = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")
import os 
import time
from termcolor import colored

def clear():
  
    os.system('cls')

clear()

class intro():
        print('Hi! Welcome to the Covid-19 test!\n')
        print('The DNA sequence of chromosome 3 will be checked for the presence of Covid-19, by comparing it to specific COVID-19 genome sequences present in an infected person.\n')
        print('\nYou will be asked to enter your symptoms, name, age, and sex. Please enter all appropriate values.')
        print('\n\nTHIS MESSAGE WILL AUTOMATICALLY DISAPPEAR IN 30 SECONDS')

time.sleep(30)
clear()

class symptoms():
                
    def check():
        
        check=True
        
        high_fever=''
        dry_cough=''
        sore_throat=''
        dib=''
        
        while check:
            high_fever=input('Do you have high fever? Enter Y or N: ').upper()
            if high_fever=='Y' or high_fever=='N':
                clear()
                break
            else:
                print('Enter Y or N only please')
         
        while check:
            dry_cough=input('Do you have dry cough? Enter Y or N: ').upper()
            if dry_cough=='Y' or dry_cough=='N':
                clear()
                break
            else:
                print('Enter Y or N only please')
         
        while check:
            sore_throat=input('Do you have sore throat? Enter Y or N: ').upper()
            if sore_throat=='Y' or sore_throat=='N':
                clear()
                break
            else:
                print('Enter Y or N only please')
                 
        while check:       
            dib=input('Do you have difficulty in breathing? Enter Y or N: ').upper()
            if dib=='Y' or dib=='N':
                clear()
                break
            else:
                print('Enter Y or N only please')
                    
        symptom_dict={'High Fever':high_fever,'Dry Cough':dry_cough,'Sore Throat':sore_throat,'Difficulty in breathing':dib}
                
        symptoms.check.variable=symptom_dict
    
class person():
        
    def name_ask():
        name=input('Enter your name: ')
        for item in name:
            if item not in name_values:
                name = name.replace(item, "")
        clear()
        person.name_ask.variable=name
     
    def age_ask():
        s=True
    
        while s:
    
            try:
                age=int(input('Enter your age: '))

            except ValueError:
                clear()
                print('Enter appropriate value please')
        
            else:
                clear()
                s=False
    
        person.age_ask.variable=age  
        
    def sex_ask():
            
        on=True
        
        while on:
        
            gender=input('Enter your sex (M or F): ').upper()


            if gender=='M' or gender=='F':
                clear()
                on=False
                                    
            else:
                clear()
                print('Enter appropriate value please')
                on=True
            
        person.sex_ask.variable=gender

class blood_match:
        
    def blood_compare():
        covid_result=''
        covid1='AGGTAACAAACCAACCAACTT'
        covid2='CACGAGTAACTCGTCTATCTT'
                
        seq= open('myfile.txt','r')
        Dnaseq=seq.read()
        
        #positive only if person has cough, difficulty in breathing, AND the file has covid+ve sequence
        if (Dnaseq.find(covid1))>-1 or (Dnaseq.find(covid2))>-1 :
            for (key,value) in symptoms.check.variable.items():
                if symptoms.check.variable.get('Dry Cough')=='Y' and symptoms.check.variable.get('Difficulty in breathing')=='Y':
                    covid_result=(colored('POSIIVE', 'red'))
                else:
                    covid_result=(colored('NEGATIVE', 'green'))
        else:
            covid_result=(colored('NEGATIVE', 'green'))
        blood_match.blood_compare.variable=covid_result


'''The program'''

#ASKING PATIENT DETAILS

run=True

while run:

    on=True

    while on:
        symptoms.check()
        person.name_ask()
        person.age_ask()
        person.sex_ask()
        blood_match.blood_compare()
    
    #CONFIRMING IF PATIENT DETAILS ENTERED ARE CORRECT

        print(f'Name: {person.name_ask.variable}\nAge: {person.age_ask.variable}\nSex: {person.sex_ask.variable}')

        confirm=input('Are these the correct details? Press Y or N').upper()
    
        if confirm=='Y':
            clear()
            break
    
        elif confirm=='N':
            clear()
            print('Re-enter all details')
            person.name_ask.variable=''
            person.sex_ask.variable=''
            person.age_ask.variable=0
            
        else:
            clear()
            break
        
    #IF PATIENT DETAILS ARE CORRECT, STORING THEM AS RECORDS
    
    def Records():
        details_list=[]
        records= open('records.txt', 'a+') 
        records.write('\nNAME        AGE        GENDER        COVID RESULT')
        details_list.append((person.name_ask.variable, person.age_ask.variable, person.sex_ask.variable))
        string=' '.join([str(blood_match.blood_compare.variable)])
        #details_list.append(string)
        records.write(f'\n{details_list} {string}')
        records.close()

    def Records_read():
        records = open("records.txt")
        lines = records.readlines()
        for line in lines:
            print(line)
        pass
    

    #OUTPUT
         
    print('\nPersonal Details')
    print(f'Name: {person.name_ask.variable}\nAge: {person.age_ask.variable}\nSex: {person.sex_ask.variable}')
    print('\nWhich symptoms are present?')
    for (key,value) in symptoms.check.variable.items():
        if symptoms.check.variable.get(key)=='Y':
            print (key)
        else:
            pass

    print(f'\n\nCOVID RESULT: {blood_match.blood_compare.variable}')


    #ASKING IF PATEINT RECORDS WANT TO BE ACCESSED
    
    record_access=input('\nDo you want to access all patient records? Enter Y or N: ').upper()

    while True:
        if record_access=='Y':
            clear()
            Records()
            print('\n')
            Records_read()
            break
         
        elif record_access=='N':
            clear()
            break
        
        else:
            clear()
            print('Enter Y or N only please')
        
    #ASKING IF PATIENT WANTS TO RUN PROGRAM AGAIN
    run_again=input('\nDo you want to run program again? Enter Y or N: ').upper()
    while True:
        if run_again=='Y':
            clear()
            person.name_ask.variable=''
            person.sex_ask.variable=''
            person.age_ask.variable=0
            blood_match.blood_compare.variable=''
            break
         
        elif run_again=='N':
            clear()
            print('Thank you for using this program.')
            run=False
            break
        
        else:
            clear()
            print('Enter Y or N only please')