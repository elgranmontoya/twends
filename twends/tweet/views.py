from django.shortcuts import render
from django.http import HttpResponse
from .models import GeoTweet

# A home page for tweets which lists out all current tweets
def list(request):
	tweets_from_date = GeoTweet.objects\
	.filter(created_at_year=2017)\
	.filter(created_at_month=4)\
	.filter(created_at_day=22)


	return render(request, 'tweet/list.html', {
		'tweets_from_date': tweets_from_date
		})