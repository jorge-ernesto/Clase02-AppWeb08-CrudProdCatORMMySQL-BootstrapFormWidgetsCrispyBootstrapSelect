
from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    #fecha = forms.DateField(widget=forms.SelectDateWidget())
    class Meta:
        model=Producto
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super(ProductoForm,self).__init__(*args, **kwargs)
        self.fields['categoria'].empty_label = "Select"
       

