from django.shortcuts import render
from django.http import HttpResponseRedirect

from stories.models import Story
from stories.forms import StoryForm

def top_stories(limit_start=0, limit_end=30):
	lastest_stories = Story.objects.all().order_by('-created_at')[limit_start:limit_end]
	return lastest_stories

def index(request):
	stories = top_stories()
	return render(request, 'index.html', {'stories': stories})

def story(request):
	if request.method == 'POST':
		form = StoryForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = StoryForm()

	return render(request, 'stories/story.html', {'form': form})
