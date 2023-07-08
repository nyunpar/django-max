from django import forms
from .models import Review


""" class ReviewForm (forms.Form):
    user_name = forms.CharField(label="Namamu: ", max_length=100, error_messages={
        "required": "Namamu tidak boleh kosong",
        "max_length": "Masukkan nama yang lebih pendek"
    })
    review_text = forms.CharField(
        label="Your Feedback: ", widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(
        label="Your Rating: ", min_value=1, max_value=5) """


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        # exclude=['']
        labels = {
            'user_name': 'Namamu:',
            'review_text': "Ulasan Anda:",
            'rating': "Penilaian Anda:"
        }
        error_messages = {
            'user_name': {
                'required': "Namamu tidak boleh kosong",
                'max_length': "Masukkan nama yang lebih pendek"
            }
        }
