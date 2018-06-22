from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from home.forms import HomeForm
from searchings.forms import ProfessorForm
from searchings.models import Post, Professor, School, Rating, College


def professor(request, professor_id, professor_name):
    if request.method == "GET":
        form = HomeForm()
        print(form)
        prof = Professor.objects.get(id=professor_id)
        ratings = Rating.objects.filter(prof_rating=prof).order_by('-date')
        total = len(ratings)
        overall_grade = 0.0
        for score in ratings:
            overall_grade += score.overall_rating
        if total == 0:
            overall_grade = 0
        else:
            overall_grade = overall_grade / total
        overall_grade = round(overall_grade, 2)
        total_rating_user = len(ratings)
        posts = Post.objects.filter(rating_post__in=ratings).order_by('-date')
        args = {'form': form,
                'posts': posts,
                'prof': prof,
                'ratings': ratings,
                'overall_grade': overall_grade,
                'total_rating_user': total_rating_user,
                }
        return render(request, 'searchings/professor.html', args)

    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            search = form.save(commit=False)
            search.save()
            school = form.cleaned_data['school']
            prof = form.cleaned_data['prof']
            college = form.cleaned_data['college']
            if school != '' and prof == '' and college == '':
                return HttpResponseRedirect(reverse('searchings:school_professor_filter', args=(school,)))
            elif school == '' and prof != '' and college == '':
                return HttpResponseRedirect(reverse('searchings:professor_filter', args=(prof,)))
            elif school == '' and prof == '' and college != '':
                return HttpResponseRedirect(reverse('searchings:college_professor_filter', args=(college,)))
            else:
                post = form.save(commit=False)
                post.user = request.user
                prof = Professor.objects.get(id=professor_id,
                                             prof_name=professor_name)

                ratings = Rating.objects.filter(prof_rating=prof).order_by('-date')
                for rating in ratings:
                    post.rating_post = rating
                post.save()
                args = {'form': form,
                        'prof': prof,
                        'ratings': ratings
                        }
                return render(request, 'searchings/professor.html', args)
        else:
            return redirect(reverse('searchings:professor', args=(professor_id, professor_name,)))


def professor_filter(request, professor_name):
    if request.method == "GET":
        form = HomeForm()
        profs = Professor.objects.filter(prof_name=professor_name)
        args = {'form': form,
                'profs': profs
                }
        if len(profs) == 0:
            profs = Professor.objects.filter(prof_name__startswith=professor_name)
            args = {'form': form,
                    'profs': profs,
                    }
            return render(request, 'searchings/professor_filter.html', args)
        if len(profs) > 1:
            return render(request, 'searchings/professor_filter.html', args)
        else:
            prof = Professor.objects.get(prof_name=professor_name)
            return HttpResponseRedirect(reverse('searchings:professor', args=(prof.id, professor_name,)))
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            search = form.save(commit=False)
            search.save()
            school = form.cleaned_data['school']
            prof = form.cleaned_data['prof']
            college = form.cleaned_data['college']
            if school != '' and prof == '' and college == '':
                return HttpResponseRedirect(reverse('searchings:school_professor_filter', args=(school,)))
            elif school == '' and prof != '' and college == '':
                return HttpResponseRedirect(reverse('searchings:professor_filter', args=(prof,)))
            elif school == '' and prof == '' and college != '':
                return HttpResponseRedirect(reverse('searchings:college_professor_filter', args=(college,)))
            else:
                return HttpResponseRedirect(reverse('searchings:professor_filter', args=(professor_name,)))


def school_filter(request, professor_school):
    if request.method == "GET":
        form = HomeForm()
        schools = School.objects.filter(school_name__startswith=professor_school)
        args = {'form': form,
                'schools': schools,
                }
        return render(request, 'searchings/school_filter.html', args)
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            search = form.save(commit=False)
            search.save()
            school = form.cleaned_data['school']
            prof = form.cleaned_data['prof']
            college = form.cleaned_data['college']
            if school != '' and prof == '' and college == '':
                return HttpResponseRedirect(reverse('searchings:school_professor_filter', args=(school,)))
            elif school == '' and prof != '' and college == '':
                return HttpResponseRedirect(reverse('searchings:professor_filter', args=(prof,)))
            elif school == '' and prof == '' and college != '':
                return HttpResponseRedirect(reverse('searchings:college_professor_filter', args=(college,)))
            else:
                return HttpResponseRedirect(reverse('searchings:school_filter', args=(professor_school,)))


def school_professor_filter(request, professor_school):
    if request.method == "GET":
        form = HomeForm()
        school = School.objects.filter(school_name__startswith=professor_school)
        profs = Professor.objects.filter(prof_school__in=school)
        args = {'form': form,
                'profs': profs
                }
        return render(request, 'searchings/professor_filter.html', args)
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            search = form.save(commit=False)
            search.save()
            school = form.cleaned_data['school']
            prof = form.cleaned_data['prof']
            college = form.cleaned_data['college']
            if school != '' and prof == '' and college == '':
                return HttpResponseRedirect(reverse('searchings:school_professor_filter', args=(school,)))
            elif school == '' and prof != '' and college == '':
                return HttpResponseRedirect(reverse('searchings:professor_filter', args=(prof,)))
            elif school == '' and prof == '' and college != '':
                return HttpResponseRedirect(reverse('searchings:college_professor_filter', args=(college,)))
            else:
                return HttpResponseRedirect(reverse('searchings:school_professor_filter', args=(professor_school,)))


def college_professor_filter(request, professor_college):
    if request.method == "GET":
        form = HomeForm()
        college = College.objects.filter(college_name__startswith=professor_college)
        profs = Professor.objects.filter(prof_college__in=college)
        args = {'form': form,
                'profs': profs
                }
        return render(request, 'searchings/professor_filter.html', args)
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            search = form.save(commit=False)
            search.save()
            school = form.cleaned_data['school']
            prof = form.cleaned_data['prof']
            college = form.cleaned_data['college']
            if school != '' and prof == '' and college == '':
                return HttpResponseRedirect(reverse('searchings:school_professor_filter', args=(school,)))
            elif school == '' and prof != '' and college == '':
                return HttpResponseRedirect(reverse('searchings:professor_filter', args=(prof,)))
            elif school == '' and prof == '' and college != '':
                return HttpResponseRedirect(reverse('searchings:college_professor_filter', args=(college,)))
            else:
                return HttpResponseRedirect(reverse('searchings:college_professor_filter', args=(professor_college,)))
