from django.shortcuts import render, redirect
from django.urls import reverse

from searchings.forms import ProfessorForm
from searchings.models import Professor, Rating, Post, School
from ratings.forms import RatingForm


def professor_rating(request, professor_id, professor_name):
    if request.method == "GET":
        form = RatingForm()
        prof = Professor.objects.get(id=professor_id,
                                     prof_name=professor_name)
        args = {'form': form,
                'prof': prof,
                }
        return render(request, 'ratings/professor_rating.html', args)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            prof = Professor.objects.get(id=professor_id)
            rating.prof_rating = prof
            rating.save()
            ratings = Rating.objects.filter(prof_rating=prof).order_by('-date')
            posts = Post.objects.filter(rating_post__in=ratings).order_by('-date')
            form = ProfessorForm()
            args = {'form': form,
                    'posts': posts,
                    'prof': prof,
                    'ratings': ratings,
                    }
            return redirect(reverse('searchings:professor', args=(professor_id, professor_name,)))
        else:
            return redirect(reverse('searchings:professor', args=(professor_id, professor_name,)))
