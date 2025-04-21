from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginUserForm ,ContactForm, UpdateForm # Fixed incorrect import

# for login user
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from .models import Record

def home(request):
    return render(request, 'pages/home.html')

# Create user account
def create_account(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')  

    context = {'form': form}
    return render(request, 'pages/create-account.html', context)

# login user
def my_login(request):
    form = LoginUserForm()
    if request.method=="POST":
        form= LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username= request.POST.get('username')
            password= request.POST.get('password')

            user = authenticate(request, username= username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")
                
    context = {'form': form}
    return render (request, 'pages/my-login.html', context)


# dashboard view
@login_required(login_url='my-login')

def dashboard(reuest):
    my_contacts = Record.objects.all()
    context = {'records':my_contacts}

    return render(reuest,'pages/dashboard.html', context)

# ==========CRUD=========
# crete conact 
@login_required(login_url='my-login')
def create_contact(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)    
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to dashboard after saving

    context = {'form2': form}
    return render(request, 'pages/create-contact.html', context)

# Update_contact
@login_required(login_url='my-login')
def update_contact(request, pk):

    record = Record.objects.get(id = pk)
    form = UpdateForm(instance = record)
    if request.method == "POST":
        form =UpdateForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    context = {'form3':form}
    return render(request, 'pages/update-contact.html', context)


# read singule  contact
@login_required(login_url='my-login')

def singular_contact(request, pk):

    all_records = Record.objects.get(id=pk)

    context= {'record': all_records}

    return render(request, "pages/view-contact.html", context =context)    


@login_required(login_url='my-login')

def delete_contact(request, pk):

        
        record = Record.objects.get(id=pk)
        
        record.delete()
        

        return redirect('dashboard')

    







# user logout
def logout_user(request):
    auth.logout(request)
    return redirect('my-login')





