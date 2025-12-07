from django import forms
from .models import Post, Comment, Tag
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from taggit.forms import TagWidget

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post title', 'class': 'form-input'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your post here...', 'class': 'form-textarea', 'rows': 10}),
            'tags': TagWidget(),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        if not title:
            raise forms.ValidationError("Title cannot be empty.")
        return title

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    """
    Simple ModelForm for comments. Only exposes 'content'.
    """
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment...'}),
        }

    def clean_content(self):
        content = self.cleaned_data.get('content', '').strip()
        if not content:
            raise forms.ValidationError("Comment cannot be empty.")
        return content
    

class PostForm(forms.ModelForm):
    # Text input for tags: comma-separated, e.g. "django, api, tutorial"
    tags_input = forms.CharField(
        required=False,
        help_text="Comma-separated tags (e.g. django, python, tutorial).",
        widget=forms.TextInput(attrs={'placeholder': 'tag1, tag2, tag3'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags_input']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'rows': 10, 'class': 'form-textarea'}),
        }

    def __init__(self, *args, **kwargs):
        # If instance exists, populate tags_input with the current tags
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['tags_input'].initial = ', '.join([t.name for t in self.instance.tags.all()])

    def clean_tags_input(self):
        tags_input = self.cleaned_data.get('tags_input', '')
        # normalize: remove duplicate commas/spaces
        tags = [t.strip() for t in tags_input.split(',') if t.strip()]
        # Optional: limit tag length or number
        return tags

    def save(self, commit=True):
        # Save Post first, then handle tags
        tags = self.cleaned_data.pop('tags_input', [])
        post = super().save(commit=commit)
        # Clear existing tags
        post.tags.clear()
        for tag_name in tags:
            tag_obj, created = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag_obj)
        return post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
