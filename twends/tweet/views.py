from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet

def index(request):
	all_tweets = Tweet.objects.all()
	first_tweet = all_tweets[0]
	return HttpResponse(len(all_tweets))