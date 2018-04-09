from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from .forms import SigninForm, RegisterForm
from .models import User

@csrf_exempt
def sign_in(request):
    user = None
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            results = User.objects.filter(email=form.cleaned_data['email'])
            if len(results) == 1:
                if results[0].check_password(form.cleaned_data['password']):
                    request.session['user'] = results[0].pk
                    return redirect('app:index')
                else:
                    form.addError('Incorrect email address or password')
            else:
                form.addError('Incorrect email address or password')
    else:
        form = SigninForm() 
    return render(request,'accounts/sign_in.html',{
        'form':form,
        'user':user
    })

def sign_out(request):
    del request.session['user']
    return redirect('app:index')

def register(request):
    user = None
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(request)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(form)
        if form.is_valid():
            user = User(
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
            )
            user.set_password(form.cleaned_data['password'])
            try:
                user.save()
            except IntegrityError:
                form.addError(user.email + 'is already a member')
            else:
                request.session['user'] = user.pk
                return redirect('app:index')
    else:
        form=RegisterForm()
    return render(request,'accounts/register.html',{
        'form':form,
        'user':user,
    })