import datetime

from django.utils.timezone import utc
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from stories.models import Story
from stories.forms import StoryForm




def top_stories(request):
	user_id = request.GET.get('user', '')
	search = request.GET.get('search', '')
	print "here"
	print search
	if user_id.isdigit():
		return Story.objects.all().filter(moderator__id=user_id).order_by('-pk')
	elif len(search) > 3:
		print "here in search"
		return Story.objects.all().filter(
			Q(title__contains=search) | Q(url__contains=search)
		)
	else:
		return Story.objects.all().order_by('-pk')
	#lastest_stories = Story.objects.all().order_by('-created_at')[limit_start:limit_end]

def index(request, template='index.html', extra_context=None):
	stories_list = top_stories(request)
	links_per_page = 20
	list_numbering_start = 1
	paginator = Paginator(stories_list, links_per_page)
	
	page = request.GET.get('page')
	try:
		stories = paginator.page(page)
		list_numbering_start = int((int(page)-1) * links_per_page) + 1
	except PageNotAnInteger:
		stories = paginator.page(1)
		list_numbering_start = 1
	except EmptyPage:
		stories = paginator.page(paginator.num_pages)
		if(paginator.num_pages > 1):
			list_numbering_start = int((int(paginator.num_pages)-1) * int(links_per_page)) + 1

	get_parameters_without_page = request.GET.copy()
	if get_parameters_without_page.has_key('page'):
		del get_parameters_without_page['page']

	return render(request, template, {'stories': stories, 'list_numbering_start': list_numbering_start, 'get_parameters_without_page': get_parameters_without_page})

@login_required
def submit(request):
	if request.method == 'POST':
		form = StoryForm(request.POST)
		if form.is_valid():
			record = form.save(commit=False)
			record.moderator = request.user
			record.save()
			return HttpResponseRedirect('/')
	else:
		form = StoryForm()

	return render(request, 'stories/submit.html', {'form': form})

def story(request, id=0):
	try:
		s = Story.objects.get(pk=id)
	except Story.DoesNotExist:
		return HttpResponseRedirect('/')

	return render(request, 'stories/story.html', {'story': s})

@login_required
def delete(request, id=0):
	try:
		s = Story.objects.get(pk=id)
		diff = (datetime.datetime.utcnow().replace(tzinfo=utc) - s.created_at.replace(tzinfo=utc)).days
		if s.moderator.id == request.user.id and diff < 2:
			s.delete()
	except Story.DoesNotExist:
		return HttpResponseRedirect('/')	
	
	return HttpResponseRedirect(reverse("stories.index"))





