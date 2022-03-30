from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render,redirect

from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='user-auth/login')

# Create your views here.
def allPosts(request):

    # if not request.user.is_authenticated:
    #     return redirect('user-auth/login')

    posts = Post.objects.all().order_by('-createdAt')
    comments=Comment.objects.all().order_by('-createdAt')
    count= posts.count()
        
    form = PostForm()
    formComment=Comment()

    if request.method=='POST':
        # Create a form instance with POST data
        form=PostForm(request.POST)        

        if form and form.is_valid():
            # Create, but don't save the new post instance.
            new_post=form.save(commit=False)
            #update user for the post
            new_post.user=request.user
            #save the post to db
            new_post.save()

        elif request.POST['detail']:
            detail=request.POST['detail']
            post=Post.objects.filter(id=request.POST['post'])[0]
            user=request.user
            formComment=Comment(detail=detail,post=post,user=user)
            
            formComment.save()

        return redirect('/')

    context={'posts': posts,'count': count,'comments':comments,'form':form, 'formComment': formComment}

    return render(request,'post/post_list.html',context)

# class PostList(LoginRequiredMixin, ListView):
#     model = Post
#     context_object_name = 'posts'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['posts']=context['posts'].filter(user=self.request.user)
#         context['count']=context['posts'].count()

#         return context
