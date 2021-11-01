from django import forms

class SearchCoursesForm(forms.Form):
    SUBJECTS = [
    ('IT and Web Development', 'IT and Web Development'),
    ('Graphic Design', 'Graphic Design'),
    ('Music', 'Music'),
    ('Business', 'Business'),]
    
    LEVELS = [
    ('All Levels', 'All Levels'),
    ('Beginner Level', 'Beginner Level'),
    ('Intermediate Level', 'Intermediate Level'),
    ('Expert Level', 'Expert Level'),]


    search=forms.CharField(label="Search Courses",max_length=100)
    subject=forms.ChoiceField(label="Course Type",choices=SUBJECTS)
    level=forms.ChoiceField(label="Course Level",choices=LEVELS)