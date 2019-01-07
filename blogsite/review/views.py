from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Artist, Album
from .forms import ListForm
from django.views import generic
from django.views.generic.edit import FormMixin
from django.db.models.functions import Lower
from django.db.models.functions import Cast
from django.db.models import IntegerField
from django.utils.text import slugify
import urllib

import operator


class IndexView(generic.ListView, FormMixin):
	template_name = 'review/index.html'
	context_object_name = 'AlbumList'
	form_class = ListForm
		
	def get_queryset(self):
		query = self.request.GET.get('listselect')
		#query = ListForm(self.request.GET)
		#print(query)
		result = Album.objects.all()
		if query == '1':
			result = Album.objects.order_by('title')[:5]
		if query == '2':
			result = Album.objects.order_by(Lower('author__name'))[:5]
			#print (result)
		if query == '3':
			result = Album.objects.order_by('-pubdate')[:5]
		return result
		
		
		
def detail(request,title):    
	#album = Album.objects.get(title=title.replace("Deathscapes", "Staff Only"))
	album = Album.objects.get(title=urllib.parse.unquote(title))
	context = {'album': album}
	return render(request,'review/detail.html',context)
	

	
	
	
# def detail(request):
    # return HttpResponse("You're looking at title .")
	
# def index(request):
    # AlbumList = Album.objects.all()
    # form = ListForm()
    # context = {'AlbumList': AlbumList, 'form' : form}
    # return render(request, 'review/index.html', context)
	
# def newlist(request):	
	# if request.method == 'POST':
		# form = ListForm(request.POST)
		# if form.is_valid():
			# #print ("The Choice Was %s") % form
			# #print('test')
			# return HttpResponseRedirect('detail/',form)
			# #return render(request,'detail/', {'form': form})
	# else:
		# form = ListForm()
	# return render(request,'', {'form': form})
	