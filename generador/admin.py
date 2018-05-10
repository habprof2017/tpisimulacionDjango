from django.contrib import admin
from .models import VariableLote1, VariableLote2
from .forms import VariableL1ModelForm, VariableL2ModelForm


class AdminVariableL1(admin.ModelAdmin):
    class Meta:
        form = VariableL1ModelForm

    list_display = ['valor']
    search_fields = ["valor"]
    fields = ['valor']


class AdminVariableL2(admin.ModelAdmin):
    class Meta:
        form = VariableL2ModelForm

    list_display = ['valor']
    search_fields = ["valor"]
    fields = ['valor']


admin.site.register(VariableLote1, AdminVariableL1)
admin.site.register(VariableLote2, AdminVariableL2)
