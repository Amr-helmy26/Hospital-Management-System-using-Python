
patients = {}
number_of_patients = 0
doctors = {1:{'name':'Amr Mosa','experence':7,'phone' :'01584578965','schules':'Monday', 'category':'cold'},
           2:{'name':'Omar Ahmed','experence':5,'phone' :'01244654141','schules':'Thursday', 'category':'dentistry'},
           3:{'name':'Ahemd Ali','experence':8,'phone' :'01054154557','schules':'Wednesday', 'category':'orthopedic'},
           4:{'name':'Mohamad Amar','experence':6,'phone' :'01184915415','schules':'Thursday', 'category':'cardiology'}}

number_of_doctors = 4
all_reservation ={1:[],2:[],3:[],4:[]}


while True:
    print('-'*60)
    print('          Hospital Management System')
    print('-'*60)
    print('1. Add New Patient')
    print('2. View All Patients')
    print('3. Search Patient')
    print('4. Book Appointment')
    print('5. View Doctor Schedule')
    print('6. Generate Bill')
    print('7. Exit')
    print('-'*60)
    choice = int(input('Enter your Choice :'))

    match(choice):
        case 1:
            name = input('Enter Name : ')
            genter = input('Enter Gender : ')
            age = int(input('Enter Age : '))
            address = input('Enter Address : ')
            disease = input('Enter Disease : ')
            chronic_diseases = input('Enter Chronic Diseases : ')
            
            patient_information = {'Name':name.capitalize(), 
                                   'Gender': genter, 
                                   'Age': age, 
                                   'Address': address, 
                                   'Disease':disease, 
                                   'Chronic_diseases':chronic_diseases}
            number_of_patients+=1
            patients[number_of_patients] = patient_information

        case 2:
            i = 1
            print('Total number of paitients :', number_of_patients)
            while i <= number_of_patients:
                patient = patients[i]
                print('-'*60)
                print('patient id : ', i)
                print('patient name : ', patient['Name'])
                print('patient age : ', patient['Age'])
                print('patient gender : ', patient['Gender'])
                print('patient id : ', patient['Address'])
                print('patient disease : ', patient['Disease'])
                print('patient chronic diseases : ', patient['Chronic_diseases'])
                print('-'*60)
                i+=1

        case 3:
            i = int(input('Enter Patient ID : '))
            patient = patients[i]
            print('-'*60)
            print('patient id : ', i)
            print('patient name : ', patient['Name'])
            print('patient age : ', patient['Age'])
            print('patient gender : ', patient['Gender'])
            print('patient id : ', patient['Address'])
            print('patient disease : ', patient['Disease'])
            print('patient chronic diseases : ', patient['Chronic_diseases'])
            print('-'*60)

        case 4: 
            
            i = 1
            print('Total number of doctors :', number_of_doctors)
            while i <= number_of_doctors:
                doctor = doctors[i]
                print('-'*60)
                print('dr. id :', i)
                print('dr. name :', doctor['name'])
                print('dr. phone :', doctor['phone'])
                print('dr. experence :', doctor['experence'])
                print('dr. schules:', doctor['schules'])
                print('dr. category:', doctor['category'])
                print('-'*60)
                i+=1

            dr_id = int(input('Enter Doctor ID: '))
            doctor = doctors[i]
            patient_id = int(input('Enter Patient ID: '))
            all_reservation[i].append(patient_id)

        case 5:
            i = 1
            print('Total number of doctors :', number_of_doctors)
            while i <= number_of_doctors:
                doctor = doctors[i]
                print('-'*60)
                print('dr. id :', i)
                print('dr. name :', doctor['name'])
                print('reservations : ')
                patient_list = all_reservation[i]
                for j in patient_list :
                    
                    print(j, patients[j]['Name'])
                i+=1

        case 6:
            i = int(input('Enter Patient ID : ')) 
            fee = int(input('Enter FEE cost : '))
            lab = int(input('Enter lab cost : '))
            total =fee+lab
            patient = patients[i]
            print('-'*60)
            print('BILL')
            print('-'*60)
            print('patient id: ', i)
            print('patient name: ', patient['Name'])
            print('patient age: ', patient['Age'])
            print('patient gender: ', patient['Gender'])
            print('-'*60)
            print('FEE :', fee)
            print("Lab cost :", lab)
            print('-'*60)
            print('Total : ', total)
            print('-'*60)

        case 7:
            break   





