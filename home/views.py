from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from searchings.models import School, Professor
from .models import Search
from .forms import HomeForm
from django.urls import reverse


class HomeView(TemplateView):
    template_name = "home/index.html"

    def get(self, request):
        form = HomeForm()
        searches = Search.objects.all()
        args = {'form': form,
                'searches': searches,
                }
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            search = form.save(commit=False)
            search.save()
            school = form.cleaned_data['school']
            prof = form.cleaned_data['prof']
            if school == '' and prof == '':
                return redirect('home:index')
            elif school == '':
                return HttpResponseRedirect(reverse('searchings:professor_filter', args=(search.prof,)))
            elif prof == '':
                return HttpResponseRedirect(reverse('searchings:school_filter', args=(search.school,)))
            else:
                school = School.objects.filter(school_name=school)
                profs = Professor.objects.filter(prof_school__in=school, prof_name=prof)
                if len(profs) == 1:
                    return HttpResponseRedirect(reverse('searchings:professor', args=(profs[0].id, search.prof,)))
                elif len(profs) == 0:
                    return HttpResponseNotFound('<h1>We have no result</h1>')
                else:
                    return HttpResponseRedirect(reverse('searchings:professor_filter', args=(search.prof,)))
