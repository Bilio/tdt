from django import forms

class TopicForm(forms.Form):
    topic_name = forms.CharField(label='Topic (No Special Characters):', max_length=100)