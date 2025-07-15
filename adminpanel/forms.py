from django import forms
from products.models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['created_at']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'parent'] 