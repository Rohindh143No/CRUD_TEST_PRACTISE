from django.shortcuts import render ,redirect
from crudApp.models import Student
from crudApp.forms import StudentForm

# Create your views here.
def retrieve_view(request):
    student=Student.objects.all()
    return render(request,'crudApp/index.html',{'student':student})

def create_view(request):
    form=StudentForm() 
    if request.method=='POST':
        form=StudentForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/check') #NEW LINE TO REDIRECT (/ ) to return the previous page
        
    return render(request,'crudApp/create.html',{'form':form})

def delete_view(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('/check')

def update_view(request,id): #to define this littile bit combination of delete and create
    student=Student.objects.get(id=id)
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST,instance=student) #adding instance to update the old value
    if form.is_valid():
        form.save() 
        return redirect('/check')
    return render(request,'crudApp/update.html',{'student':student})
    