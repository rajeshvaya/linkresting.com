from django.shortcuts import render

from stories.models import Story

def top_stories(limit_start=0, limit_end=30):
	lastest_stories = Story.objects.all().order_by('-created_at')[limit_start:limit_end]
	return lastest_stories

def index(request):
	stories = top_stories()

	return render('index.html', {'stories': stories})


