from django import forms

class SearchCoursesForm(forms.Form):
    SUBJECTS = [
    ('WEB', 'Web Development'),
    ('DESIGN', 'Graphic Design'),
    ('MUSIC', 'Music'),
    ('BUSINESS', 'Business'),]
    
    LEVELS = [
    ('ALL', 'All Levels'),
    ('BEG', 'Beginner Level'),
    ('INTER', 'Intermediate Level'),
    ('EXPERT', 'Expert Level'),]


    search=forms.CharField(label="Search Courses",max_length=100)
    subject=forms.ChoiceField(label="Course Type",choices=SUBJECTS)
    level=forms.ChoiceField(label="Course Level",choices=LEVELS)