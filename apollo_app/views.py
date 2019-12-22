from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from apollo_app.forms import Task_Models_Form
from apollo_app.models import Task_Models
from task_manager import settings


def base(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == "POST":
        name = request.POST["name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        re_pass = request.POST["confirm_password"]
        if password == re_pass:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email ID already Exist')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already Someone using')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    first_name=name, username=username, password=password, email=email)
                user.save()
                messages.info(request, 'Registered Successfully, Please Login ')
                return redirect('login')
        else:
            messages.info(request, 'Password does not Match')
            return redirect('signup')
    else:
        return render(request, "sign_up.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid User Details')
            return redirect('login')
    else:
        return render(request, 'login.html')


def log_out(request):
    auth.logout(request)
    return redirect('/')


def my_task(request):
    task_data = Task_Models.objects.all()
    return render(request, 'my_taks.html', {'task_data': task_data})


@login_required()
def new_takk_create(request):
    if request.method == 'POST':
        med = Task_Models()
        form = Task_Models_Form(request.POST or None, instance=med)
        email = User.objects.get(email__contains=request.POST['assigning_to']).email
        send_mail('Task You have to do', 'You have received New task', settings.EMAIL_HOST_USER, [email])
        if form.is_valid():
            form.save()
            messages.info(request, 'Task Created')
            return redirect('home')
    else:
        users = User.objects.all()
        user_data = []
        for x in users:
            user_data.append(x)
        return render(request, 'new_takk_create.html', {'user_data': user_data})


def update(request):
    if request.method == 'POST':

        return redirect('my_task')
    else:
        return redirect('new_takk_create')