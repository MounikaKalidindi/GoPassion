from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
#from library.models import Myclass
from Hobbies.models import Categories
from django.views import generic
from django.template import loader

# Create your views here.
def index(request) :
	#templates = loader.get_template("Hobbies/category_list.html")
	#return HttpResponse(templates.render())
	return HttpResponse( "Mouniii")


def categories(request):	
	#cat = Categories.objects.all().order_by('id')[:3]
	c_name = get_list_or_404(Categories)
	#return HttpResponse(cat_name + "haii")
	return render(
		request,
		'Hobbies/category_list.html',
		context = {'category_name':c_name}
	)

"""class CategoriesListView(generic.ListView):
	model = Categories

	def get_context_data(self):
		context = super(CategoriesListView, self).get_context_data()
		return context
		
"""

		

