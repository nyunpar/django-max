from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .forms import ReviewForm
from .models import Review
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView


# Create your views here.

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank-you'


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        request.session['favorite_review'] = review_id
        return HttpResponseRedirect('/reviews/' + review_id)


"""     def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request, 'reviews/review.html', {"form": form})
 """

""" def review(request):

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
             review = Review(user_name=form.cleaned_data['user_name'],
                            review_text=form.cleaned_data['review_text'],
                            rating=form.cleaned_data['rating']) 

            form.save()

            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()

    return render(request, 'reviews/review.html', {"form": form}) """


class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["messages"] = 'This works!'
        return context


class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = 'reviews'

    """ def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=4)
        return data """


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
