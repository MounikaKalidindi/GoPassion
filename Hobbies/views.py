from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
#from library.models import Myclass
from Hobbies.models import Categories, Categories_Sub_Categories_Mapping, Sub_Categories
from django.views import generic
from django.template import loader

# Create your views here.
def index(request) :
	#templates = loader.get_template("Hobbies/category_list.html")
	#return HttpResponse(templates.render())
	return HttpResponse( "Mouniii")


def categories_list(request):	
	#cat = Categories.objects.all().order_by('id')[:3]
	category_obj = get_list_or_404(Categories)
	category_map_obj = get_list_or_404(Categories_Sub_Categories_Mapping)
	sub_category_obj = get
	sub_category_map_obj = get_list_or_404(Sub_Categories_Sub_Categories1_Mapping)
	#c_id = getCategoryId(cat_name)
	#sub_c_obj = get_list_or_404(Categories_Sub_Categories_Mapping, category_id = c_id)
	return render(
		request,
		'Hobbies/category_list.html',
		context = {'categories':category_obj, 'categories_map':category_map_obj, '':, 'sub_categories_map':sub_category_map_obj}
	)

def getCategoryId(cat_name):
	#c_obj = get_list_or_404(Categories)
	c_id = get_object_or_404 (Categories, category = cat_name)
	return (c_id.id)
def getSub_Categories(request, cat_name):
	c_id = getCategoryId(cat_name)
	sub_c_obj = get_list_or_404(Categories_Sub_Categories_Mapping, category_id = c_id)
	
	return render(
		request,
		'Hobbies/sub_category_list.html',
		context = {'cat_name': cat_name, 'sub_cat':sub_c_obj}
	)

	
"""
class CategoriesListView(generic.ListView):
	model = Categories

	def get_context_data(self):
		context = super(CategoriesListView, self).get_context_data()
		return context
		
"""

		

