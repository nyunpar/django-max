from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render

monthly_challenges = {
    "january": "Eat no meat for entire month",
    "february": "Walk fro at least 20 minutes every day",
    "march": "Learn Django for at least 20 minutes everyday",
    "april": "Practice mindfulness or meditation: Set aside time each day to focus on the present moment, reduce stress, and increase self-awareness.",
    "may": "Read books: Reading expands your knowledge, enhances your vocabulary, and stimulates your imagination. Choose books that inspire and motivate you.",
    "june": "Learn a new skill: Invest time in acquiring a new skill or hobby that interests you. It can broaden your horizons, boost your confidence, and provide a sense of accomplishment.",
    "july": "Cultivate gratitude: Practice gratitude by keeping a gratitude journal or expressing gratitude to others. It can increase positive emotions and improve overall happiness.",
    "august": "Spend quality time with loved ones: Foster meaningful connections with family and friends. Engage in activities together and create lasting memories.",
    "september": "Set goals and prioritize tasks: Establish clear goals and break them down into actionable steps. Prioritize tasks based on importance and focus on completing them one at a time.",
    "october": "Volunteer or help others: Engage in acts of kindness and contribute to your community. Helping others not only makes a positive impact but also promotes personal growth and fulfillment.",
    "november": "Take care of your mental health: Prioritize self-care activities such as getting enough sleep, managing stress, and seeking professional help when needed.",
    "december": None
}

def index(request): 
    months = list(monthly_challenges.keys())
    return render(request,"challenges/index.html",{
        "months":months
    })
 
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    try:
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("Invalid month" )

def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request ,"challenges/challenge.html",{
            "text":challenge_text,
            "month_name":month
        })
    except:
        raise Http404()