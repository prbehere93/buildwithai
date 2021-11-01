import re
from django.shortcuts import render
from django.utils.functional import empty
from django.views.generic import TemplateView
from django.views.generic.base import View
import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from .forms import SearchCoursesForm
from django.conf import settings
from django.contrib import messages

file_path=os.path.join(settings.BASE_DIR,"courses.csv")
# Create your views here.
data=pd.read_csv(file_path)

def StudyGroup(request):
    if request.method=='POST':
        messages.add_message(request, messages.SUCCESS,'Form Submitted')
          
    return render(request, 'courses/study_group.html')
    
def HomePageView(request):
    courses={}
    urls={}
    levels={}
    def create_similarity_matrix(new_description, overall_descriptions):
        #Append the new description to the overall set
        overall_descriptions=list(overall_descriptions)
        overall_descriptions.append(new_description)
        # Define a tfidf vectorizer and remove all stopwords.
        tfidf = TfidfVectorizer(stop_words="english")
        #Convert tfidf matrix by fitting and transforming the data.
        tfidf_matrix = tfidf.fit_transform(overall_descriptions)
        # output the shape of the matrix.
        tfidf_matrix.shape
        # calculating the cosine similarity matrix.
        cosine_sim = linear_kernel(tfidf_matrix,tfidf_matrix)
        return cosine_sim
    
    def get_recommendations(new_description,overall_descriptions):
        cosine_sim = create_similarity_matrix(new_description,overall_descriptions)
        # Get pairwise similarity scores of all the courses with new search
        sim_scores = list(enumerate(cosine_sim[-1]))
        
        sim_scores = sorted(sim_scores,key =lambda x:x[1],reverse= True)
        # Get the scores of top 10 best fit courses
        sim_scores = sim_scores[1:11]
        # getting the original indices from the data
        indices = [i[0]for i in sim_scores]
        return data[['title','url','instructionalLevel','Subject','source','institution','isPaid']].iloc[indices]

    if request.method=='POST':
        search_form=SearchCoursesForm(request.POST)
        if search_form.is_valid():
            search=search_form.cleaned_data['search']
            subject=search_form.cleaned_data['subject']
            level=search_form.cleaned_data['level']

            result_dict=get_recommendations(search+" "+subject+" "+level,data['corpus'])
            # result_dict=result_dict[result_dict['Subject']==subject]
            if level!="All Levels":
                result_dict=result_dict[result_dict['instructionalLevel']==level]
            if result_dict.empty:
                messages.add_message(request, messages.INFO,'If you find no courses, try changing course levels. To display all relevant courses, select course level as "All Levels"')
            courses=result_dict.to_dict('records')
    else:
        search_form=SearchCoursesForm()
    return render (request, 'courses/home.html',{'search_form':search_form,
                                                        'courses':courses,
                                                        'urls':urls,
                                                        'levels':levels})