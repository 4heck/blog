from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.urls import reverse
from .models import Post, Tag
from .utils import *
from .forms import TagForm, PostForm
from django.contrib.auth.decorators import login_required

def posts_list(request):
	posts = Post.objects.all()
	return render(request, 'blog/index.html', context={'posts': posts})

def tags_list(request):
	tags = Tag.objects.all()
	return render(request, 'blog/tags_list.html', context={'tags': tags})

class PostDetail(ObjectDetailMixin, View):
	model = Post
	template = 'blog/post_detail.html'

class TagDetail(ObjectDetailMixin, View):
	model = Tag
	template = 'blog/tag_detail.html'

class PostCreate(ObjectCreateMixin, View):
	model_form = PostForm
	template = 'blog/post_create.html'
	template_index = 'blog/post_create.html'

class TagCreate(ObjectCreateMixin, View):
	model_form = TagForm
	template = 'blog/tag_create.html'
	template_index = 'blog/tags_list.html'
	
class PostUpdate(ObjectUpdateMixin, View):
	model = Post
	model_form = PostForm
	template = 'blog/post_update.html'

class TagUpdate(ObjectUpdateMixin, View):
	model = Tag
	model_form = TagForm
	template = 'blog/tag_update.html'

class PostDelete(ObjectDeleteMixin, View):
	model = Post
	template = 'blog/post_delete.html'
	redirect_url = 'posts_list_url'

class TagDelete(ObjectDeleteMixin, View):
	model = Tag
	template = 'blog/tag_delete.html'
	redirect_url = 'tags_list_url'

