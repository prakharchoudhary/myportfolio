from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import requires_csrf_token
from .models import About, Experience, Education, Project, Skill
import json


# Create your views here.
def main(request):
    '''
    Renders the SPA.
    '''
    about = About.objects.get()
    education = Education.objects.filter(to_display=True)
    experience = Experience.objects.filter(to_display=True)
    projects = Project.objects.filter(to_display=True)
    context = {
        'name': about.name,
        'tagline': about.tagline,
        'about': about.about,
        'cv': about.cv,
        'github': about.github,
        'linkedin': about.linkedin,
        'facebook': about.facebook,
        'skills': [skill.name for skill in about.skills.all()],
        'education': education,
        'experience': experience,
        'projects': projects
    }
    return render(request, 'portfolio.html', context)


@requires_csrf_token
def send_email(request):
    print(request.POST)
    if request.method == 'POST':
        try:
            send_mail('Regarding a contact from visitor',
                      request.POST['message'],
                      request.POST['_replyto'],
                      ['prakhar2397@gmail.com'])
            return HttpResponse(json.dumps({'status': 'success'}))
        except Exception as e:
            raise
    else:
        print("Get method!")
