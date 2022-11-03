from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from user.models import User
from csvs.forms import CsvModelForm
from csvs.models import Csv
import csv


def main(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'home.html')


def profile(request):
    return render(request, 'profile.html')


def data(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    users = User.objects.all()
    context = {'form': form,
                'users': users}
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f, skipinitialspace=True)
            next(reader)
            
            for row in reader:
                if len(row[0]) or len(row[1]) != 0:       
                    user = User(username=row[0],
                        password=row[1],
                        )
                    user.save()
                    '''It should not adds users with empty username or password into db but
                    it adds. Not sure why'''
                else:
                    print('Else row', row)
  
            obj.activated = True
            obj.save()
    return render(request, 'data.html', context)


def signup(request):

    if request.method == "POST":
        username = request.POST['Username']
        first_name = request.POST['First_name']
        last_name = request.POST['Last_name']
        password = request.POST['password']
        password2 = request.POST['password']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('/')
            else:
                User.objects.create_user(username=username, first_name=first_name, last_name=last_name,  password=password)

                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                return redirect('/')
        else:
            messages.info(request, 'Password not matching')
            return redirect('signup/')
    else:
        return render(request, 'signup.html')

def login(request):

    if request.method == 'POST':
        print('request.method: ', request.method)
        print('request.POST: : ', request.POST)
        username = request.POST['username']
        print('username: ', username)
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print('user: ', user)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials invalid')
            print('message', messages.info(request, 'Credentials invalid'))
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')



@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('/')
