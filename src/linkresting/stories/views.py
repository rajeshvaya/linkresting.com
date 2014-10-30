from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from stories.models import Story
from stories.forms import StoryForm


def top_stories(limit_start=0, limit_end=30):
	return Story.objects.all().order_by('-pk')
	lastest_stories = Story.objects.all().order_by('-created_at')[limit_start:limit_end]
	return lastest_stories

def index(request, template='index.html', extra_context=None):
	stories_list = top_stories()
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

	return render(request, template, {'stories': stories, 'list_numbering_start': list_numbering_start})

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

def delete(request, id=0):
	return HttpResponseRedirect(reverse("stories.index"))
