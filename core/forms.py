from django.forms import ModelForm
from .models import ModulesEnrollment


class ModulesEnrollmentForm(ModelForm):
    class Meta:
        model = ModulesEnrollment
        fields = ['final_test_answer']
