from django.shortcuts import render

# Create your views here.

# Create your views here.
from django.shortcuts import render
from datetime import datetime
#Example 1
def student1(request):
  return render(request, 'studentpage.html', {'nm':'shalini'})


#Example 2
def student2(request):
    s_name = 'ravi'
    roll_no = '105'
    address = 'Hyderabad'
    student_details = {'name':s_name, 'roll':roll_no, 'address':address}
    return render(request, 'studentpage1.html', student_details)

#Example 3
def student3(request):
    return render(request, 'studentpage2.html', {'cap':'welcome to ojas'})

#Example 4
def student4(request):
    date=datetime.now()
    return render(request, 'studentpage3.html', {'dt':date})


#Example 5
def student5(request):
    return render(request, 'studentpage4.html', {'f1':4564.4654, 'f2':897.0000, 'f3':953.35700})

#Example 6
def student6(request):
    st='hello all welcome to 10th class'
    return render(request, 'studentpage5.html', {'st':st})
#Example 7
def student7(request):
    st='welcome to school'
    return render(request, 'studentpage6.html', {'nm':st})
#Example 8
def student8(request):
    return render(request, 'studentpage7.html', {'nm':'Electronic and communication Engg','st':10})

#Example 9
def student9(request):
  student = {'names': ['kumar', 'laxmi', 'sreeja','shravya']}
  return render(request, 'studentpage8.html', student)

#Example 10
def student10(request):
    stu = {'stu1': {'name': 'bargav', 'roll':1002},
            'stu2': {'name': 'Sai ram', 'roll':102},
            'stu3': {'name': 'mukesh', 'roll':103},
            'stu4': {'name': 'Amulya', 'roll':104},
          }
    students = {'student':stu}
    return render(request, 'studentpage9.html', students)

#Example 11
def student11(request):
    details = {'name': 'Akhil', 'roll':502}
    return render(request, 'studentpage10.html', {'data':details})

#Example 12
def student12(request):
    details = {'student1': {'name': 'shiva', 'roll':101, 'Address':'Hyd'},
              'student2': {'name': 'Soniya', 'roll':102, 'Address':'pune'},
              'student3': {'name': 'divya', 'roll':103, 'Address':'Chennai'},
              'student4': {'name': 'srividya', 'roll':104,'Address':'Mumbai'},
            }
    return render(request, 'studentpage11.html', {'data':details})