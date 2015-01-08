#-*- coding: utf-8 -*-
from django import forms
from contacts.models import Comment, Contact, UserProfile, Articles
class DocumentForm(forms.Form):

    docfile = forms.FileField(
                        label='Select a file',
                        help_text='max. 42 megabytes'
                        )


class UserForm(forms.ModelForm):

    location = forms.CharField(max_length=140, help_text="Location")
    gender = forms.CharField(max_length=140, help_text="Gender")

    class Meta:
        model = UserProfile
        exclude = ("user","profile_picture","reputation")

class PostArticleForm(forms.ModelForm):

    link = forms.CharField(max_length=255, help_text="URL of article")
    description = forms.CharField(max_length=255, help_text="Description")

    class Meta:
        model = Articles
        exclude = ("user","votes","uploader","time_stamp")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('user','article', 'date')
