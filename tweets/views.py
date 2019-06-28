from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import yearSearch
import sys
from . import script
import matplotlib.pyplot as plt


# Create your views here.

def search(request):
    positive = []
    negative = []
    neutral = []
    percent = []

    if request.method == 'POST':
        videotitle=request.POST['videoname']
        x = script.main(videotitle)

     #for getting positive tweets   
    for tweet in x:
        if tweet['sentiment']=='positive':
            p = tweet['text']
            positive.append(p)

    #for getting Negative tweets
    for tweet in x:
        if tweet['sentiment']=='negative':
            p = tweet['text']
            negative.append(p)

    #for getting neutral tweets
    for tweet in x:
        if tweet['sentiment']=='neutral':
            p = tweet['text']
            neutral.append(p)

     #calculating the percentages of positive, negative and neutral tweets
    percent.append(100*len(positive)/len(x))
    percent.append( 100*len(negative)/len(x))
    percent.append(100*len(neutral)/len(x))

    #Creating a pie chart with the help of matplotlib
    labels = 'positive', 'Negative', 'Neutral'
    sizes = [percent[0],percent[1], percent[2]]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
    shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    #saving the pie chart as a png image.
    plt.savefig('tweets/templates/tweets/plot.png', bbox_inches='tight')

    #passing the data to html page
    context = {'positive': positive, 'negative':negative, 'neutral':neutral}
    return render(request,'tweets/search.html',context)

def home(request):
    if request.method == 'POST':
        form = yearSearch(request.POST)

        if form.is_valid():
            return redirect('search')
    else:
        form = yearSearch()

    context = {'form':form}

    return render(request,'tweets/home.html', context)