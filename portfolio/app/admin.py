from django.contrib import admin
from app.models import About, Experience, Education, Project, Skill, Image


# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline')


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('employer_name', 'job_title',
                    'from_date', 'to_date', 'to_display')


class EducationAdmin(admin.ModelAdmin):
    list_display = ('college', 'degree', 'from_date',
                    'to_date', 'to_display')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'to_display')


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'to_display')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'created_at')

admin.site.register(About, AboutAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Image, ImageAdmin)
