from django import forms

class SearchCoursesForm(forms.Form):
    SUBJECTS = [
    ('Web Development', 'Web Development'),
    ('Graphic Design', 'Graphic Design'),
    ('Music', 'Music'),
    ('Business', 'Business'),
    ('Data Science', 'Data Science'),
    ('Computer Programming', 'Computer Programming')]
    
    LEVELS = [
    ('Beginner Level', 'Beginner Level'),
    ('Intermediate Level', 'Intermediate Level'),
    ('Expert Level', 'Expert Level'),
    ('All Levels', 'All Levels'),]


    search=forms.CharField(label="Search Courses",max_length=100)
    subject=forms.ChoiceField(label="Course Type",choices=SUBJECTS)
    level=forms.ChoiceField(label="Course Level",choices=LEVELS)