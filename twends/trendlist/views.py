from operator import itemgetter
from django.shortcuts import render
from .models import TrendList
from .forms import TrendDate

class Hashtag:
	def __init__(self, hashtag_string, hashtag_count):
		self.text = hashtag_string
		self.count = hashtag_count

def search(request):
	trend_list = []

	if request.method == 'POST':
		form = TrendDate(request.POST)
		if form.is_valid():
			form_year = form.cleaned_data['year']
			form_month = form.cleaned_data['month']
			form_day = form.cleaned_data['day']

			query_item = TrendList.objects.filter(requested_year=form_year).filter(requested_month=form_month).filter(requested_day=form_day)[0]
			hash_counts = (query_item['tag_counts'])

			for hash_count in hash_counts:
				hashtag_text = hash_count[1:hash_count.find(",")]
				hashtag_count = int(hash_count[hash_count.find(",") + 1:hash_count.find(")")])
				trend_list.append(Hashtag(hashtag_text, hashtag_count))

			trend_list.sort(key=lambda h: h.count, reverse=True)

	else:
		form = TrendDate()
	return render(request, 'trendlist/index.html', {'form': form, 'trend_list': trend_list})