from django import forms
from .models import Post
from catalog.models import Tag
from Django.core.exceptions import ValidationError

class SearchForm(forms.Form):
    search = forms.CharField(help_text="Add search terms")
    
    def clean_search(self):
        terms = self.cleaned_data['search']
        
        result = []
        current = 0
        for i in len(terms):
            if terms[i] == " ":
                result.append(terms[current:i])
                current = i + 1
                
        return result
    
    def get_results(self):
        result = clean_search(self)
        filtered = Topic.object.all
        for i in result:
            filtered = filtered.filter(result[i])
        
        return filtered