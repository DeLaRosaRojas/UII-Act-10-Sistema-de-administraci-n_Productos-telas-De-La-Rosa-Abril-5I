from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio', 'stock', 'unidad_medida']
        labels = {
            'nombre': 'Nombre del Producto',
            'categoria': 'Categoría',
            'precio': 'Precio',
            'stock': 'Cantidad en Stock',
            'unidad_medida': 'Unidad de Medida',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'unidad_medida': forms.TextInput(attrs={'class': 'form-control'}),
        }