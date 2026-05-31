from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Field
from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'name', 'gender', 'generation', 'role',
            'birth_year', 'birth_date', 'parent', 'spouse',
            'photo', 'photo_url', 'is_alive', 'notes'
        ]
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'person-form'
        self.helper.attrs = {
            'hx-post': '',
            'hx-target': '#form-response',
            'hx-swap': 'outerHTML',
        }
        self.helper.layout = Layout(
            Row(
                Column(Field('name', css_class='form-control'), css_class='col-md-6'),
                Column(Field('gender', css_class='form-select'), css_class='col-md-3'),
                Column(Field('generation', css_class='form-select'), css_class='col-md-3'),
            ),
            Row(
                Column(Field('role', css_class='form-select'), css_class='col-md-4'),
                Column(Field('birth_year', css_class='form-control'), css_class='col-md-4'),
                Column(Field('birth_date', css_class='form-control'), css_class='col-md-4'),
            ),
            Row(
                Column(Field('parent', css_class='form-select'), css_class='col-md-6'),
                Column(Field('spouse', css_class='form-select'), css_class='col-md-6'),
            ),
            Row(
                Column(Field('photo_url', css_class='form-control'), css_class='col-md-8'),
                Column(Field('is_alive', css_class='form-check-input'), css_class='col-md-4 d-flex align-items-center'),
            ),
            Field('notes'),
            Submit('submit', 'Save Person', css_class='btn btn-success px-4 mt-2'),
        )
