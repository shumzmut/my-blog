from django.contrib import admin
from .models import Question, Choice

# Register your models here.

# admin.site.register(Question)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    list_display = ['pub_date', 'question_text']
    # fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     #('Date information', {'fields': ['pub_date']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    inlines = [ChoiceInline]
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
