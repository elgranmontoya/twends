from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet

# A home page for tweets which lists out all current tweets
def index(request):
	first_tweet = Tweet.objects.all()[0]

	return render(request, 'tweet/first.html', {
		'first_tweet': first_tweet,
		})