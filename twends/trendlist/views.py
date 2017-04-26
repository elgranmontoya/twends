from django.shortcuts import render
from .models import TrendList
from .forms import TrendDate

def search(request):
	trendlist = []
	final_list = []

	if request.method == 'POST':
		form = TrendDate(request.POST)
		if form.is_valid():
			# print("Valid Form!!")
			form_year = form.cleaned_data['year']
			form_month = form.cleaned_data['month']
			form_day = form.cleaned_data['day']

			print("making form")
			trendlist = list(TrendList.objects.filter(requested_year=form_year).filter(requested_month=form_month).filter(requested_day=form_day).first())['tag_counts']
			for item in trendlist:
				final_list.append(str(item))

	else:
		form = TrendDate()
	return render(request, 'trendlist/index.html', {'form': form, 'trendlist': trendlist, 'final_list': final_list})