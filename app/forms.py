from django import forms
from .models import Producto

# El formulario hereda las validaciones definidas en el modelo.
class ProductoForm(forms.ModelForm):
    # Aplicar cambios en inputs del formulario (Otra forma)
    # fecha = forms.DateField(
    #     widget=forms.DateInput(attrs={'type': 'date'})  # widget=forms.SelectDateWidget()
    # )

    class Meta:
        model = Producto
        fields = '__all__'
        # fields = ['descripcion', 'categoria', 'fecha', 'precio', 'stock']  # Otra forma
        # Aplicar cambios en inputs del formulario
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'})
        }

    # Este es el método __init__ del formulario.
    # Este método se llama cuando se crea una instancia del formulario.
    def __init__(self, *args, **kwargs):

        # Aquí llamamos al método __init__ de la superclase forms.ModelForm, que inicializa el formulario con los argumentos *args y **kwargs que se pasan al constructor del formulario.
        # En Python 3.x y posteriores, puedes usar la sintaxis más corta de super(), que no requiere pasar el nombre de la clase o el objeto de la instancia. Esto es posible porque Python 3.x y posteriores infieren automáticamente la clase y el objeto de la instancia.
        super().__init__(*args, **kwargs)

        # Aquí estamos accediendo al campo categoria del formulario y estableciendo su etiqueta vacía con el texto "Seleccione una categoría".
        # El campo categoria es un campo de selección que se genera automáticamente a partir de la relación de clave externa en el modelo Producto.
        self.fields['categoria'].empty_label = "Seleccione una categoría"
