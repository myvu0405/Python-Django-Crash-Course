from email import message
from django.shortcuts import redirect,render
from django.views.generic.edit import FormView

from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import *
from django.contrib.auth import authenticate,login,logout

#=============
def registerPage(request):
    form = UserRegisterForm()

    if request.method=='POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            if not request.POST['username'].isalpha():
                messages.error(request, 'Username should only contain letters.')
                return render(request, 'user_auth/register.html',{'form':form})
            else:
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created and saved to database for '+user)
                return redirect('login')

    context = {'form':form}

    return render(request, 'user_auth/register.html',context)

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('posts')

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            try: 
                next_url = request.GET['next']
                next_url=next_url.replace('/','')
                if next_url!= '':
                    return redirect(next_url)
                else:
                    return redirect('posts')
                
            except:
                return redirect('posts')

        else:
            messages.info(request,'Username or Password is incorrect!')

    context ={}

    return render(request,'user_auth/login.html',context)

def logoutUser(request):

    logout(request)
    return redirect('login')


#=============
'''
class CustomLoginView(LoginView):
    template_name= 'user_auth/login.html'
    fields='__all__'
    redirect_authenticated_user= True

    def get_success_url(self):
        
        # if self.request.GET['next']=='/' or not self.request.GET['next']:
        #     return reverse_lazy('posts')
        try: 
            next_url = self.request.GET['next']
            next_url=next_url.replace('/','')
            if next_url!= '':
                return reverse_lazy(next_url)
            else:
                return reverse_lazy('posts')
                
        except:
            return reverse_lazy('posts')


class RegisterPage(FormView):
    template_name='user_auth/register.html'
    form_class=UserCreationForm
    redirect_authenticated_user= True
    success_url=reverse_lazy('posts')

    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)


    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('posts')
        return super(RegisterPage, self).get(*args, **kwargs)

'''