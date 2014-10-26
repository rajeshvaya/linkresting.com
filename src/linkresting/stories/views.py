from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
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
	paginator = Paginator(stories_list, 25)
	
	page = request.GET.get('page')
	try:
		stories = paginator.page(page)
	except PageNotAnInteger:
		stories = paginator.page(1)
	except EmptyPage:
		stories = paginator.page(paginator.num_pages)

	return render(request, template, {'stories': stories})

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
	
