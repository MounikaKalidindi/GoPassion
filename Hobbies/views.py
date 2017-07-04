from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
# from library.models import Myclass
from models import *
from django.views import generic
from django.template import loader
from forms import *
from django import forms;


# Create your views here.
def index(request):
    # templates = loader.get_template("Hobbies/category_list.html")
    # return HttpResponse(templates.render())
    return HttpResponse("Mouniii")


<<<<<<< HEAD
"""
def categories_list(request):	
	#cat = Categories.objects.all().order_by('id')[:3]
	category_obj = get_list_or_404(Categories)
	category_map_obj = get_list_or_404(Categories_Sub_Categories_Mapping)
	sub_category_obj = get_list_or_404(Sub_Categories)
	sub_category_map_obj = get_list_or_404(Sub_Categories_Sub_Categories1_Mapping)
	#c_id = getCategoryId(cat_name)
	#sub_c_obj = get_list_or_404(Categories_Sub_Categories_Mapping, category_id = c_id)
	return render(
		request,
		'Hobbies/category_list.html',
		context = {'categories':category_obj, 'categories_map':category_map_obj, 'sub_categories':sub_category_obj, 'sub_categories_map':sub_category_map_obj}
	)
"""
=======
def categories_list(request):
    # cat = Categories.objects.all().order_by('id')[:3]
    category_obj = get_list_or_404(Categories)
    category_map_obj = get_list_or_404(Categories_Sub_Categories_Mapping)
    sub_category_obj = get_list_or_404(Sub_Categories)
    sub_category_map_obj = get_list_or_404(Sub_Categories_Sub_Categories1_Mapping)
    # c_id = getCategoryId(cat_name)
    # sub_c_obj = get_list_or_404(Categories_Sub_Categories_Mapping, category_id = c_id)
    return render(
        request,
        'Hobbies/category_list.html',
        context={'categories': category_obj, 'categories_map': category_map_obj, 'sub_categories': sub_category_obj,
                 'sub_categories_map': sub_category_map_obj}
    )


def getCategoryId(cat_name):
    # c_obj = get_list_or_404(Categories)
    c_id = get_object_or_404(Categories, category=cat_name)
    return (c_id.id)

>>>>>>> 346e5c9ee0a0e02544daa693bcf9c0fb109fee25

def nav_cat_list(request):
    category_obj = get_list_or_404(Categories)
    category_map_obj = get_list_or_404(Categories_Sub_Categories_Mapping)
    sub_category_obj = get_list_or_404(Sub_Categories)
    return render(
        request,
        'Hobbies/cat_list.html',
        context={'categories': category_obj, 'categories_map': category_map_obj, 'sub_categories': sub_category_obj}
    )


def getDifferentOptions(request, category_name, sub_category_name):
<<<<<<< HEAD
	posts_obj = get_list_or_404(Posts)
	return render(
		request,
		'Hobbies/options.html',
		context = {'category_name': int(category_name), 'sub_category_name' : sub_category_name, 'posts':posts_obj}
		)

"""
class CategoriesListView(generic.ListView):
	model = Categories
=======
    return render(
        request,
        'Hobbies/options.html',
        context={'category_name': category_name, 'sub_category_name': sub_category_name}
    )

>>>>>>> 346e5c9ee0a0e02544daa693bcf9c0fb109fee25

def getDifferentOptions1(request):
    category_obj = get_list_or_404(Categories)
    category_map_obj = get_list_or_404(Categories_Sub_Categories_Mapping)
    #	sub_category_obj = get_list_or_404(Sub_Categories)
    posts_obj = get_list_or_404(Posts)
    return render(
        request,
        'Hobbies/options.html',
        context={'categories': category_obj, 'categories_map': category_map_obj, 'posts': posts_obj}
    )


def addpost(request, cat_id, sub_cat_id):
    name = 'ADD POST FORM'
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            src = form['src'].value()
            post_adv = form['post_adv'].value()
            descr = form['description'].value()
            post = Posts()
            post.src = src
            post.user_id = request.user
            post.description = descr
            post.likes = 0
            post.post_adv = post_adv
            post.category_map_id = get_object_or_404(Categories_Sub_Categories_Mapping, category_id= cat_id, sub_category_id = sub_cat_id)
            post.save()
            return HttpResponse("<h1>thanks for the post" + descr + src + str(post_adv)+ str(post.user_id.id) + "</h1>")
    else:
        form = PostForm()
    return render(request, 'Hobbies/form.html', {'form': form, 'form_name': name})
