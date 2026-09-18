from django import forms
from django.core.exceptions import ValidationError

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    website = forms.CharField(required=False, widget=forms.HiddenInput)
    form_started = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Your name",
                    "autocomplete": "name",
                    "maxlength": "120",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "you@example.com",
                    "autocomplete": "email",
                }
            ),
            "subject": forms.TextInput(
                attrs={
                    "placeholder": "How can I help?",
                    "maxlength": "180",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "placeholder": "Share a short overview of the role, project, or question.",
                    "rows": 6,
                    "maxlength": "4000",
                }
            ),
        }

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if len(name) < 2:
            raise ValidationError("Please enter your name.")
        return name

    def clean_subject(self):
        subject = self.cleaned_data["subject"].strip()
        if len(subject) < 3:
            raise ValidationError("Please enter a subject.")
        return subject

    def clean_message(self):
        message = self.cleaned_data["message"].strip()
        if len(message) < 12:
            raise ValidationError("Please write a slightly more detailed message.")
        if message.count("http") > 4:
            raise ValidationError("This message looks like spam.")
        return message

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("website"):
            raise ValidationError("Spam detected.")
        return cleaned
