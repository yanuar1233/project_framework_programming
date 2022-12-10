from django.forms import ModelForm, TextInput, SelectMultiple
from landingpage.models import Barang

class FromBarang(ModelForm):
    class Meta :
        model=Barang
        fields='__all__'
        widgets = {
            'kodebrg' : TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Kode Barang'
                }),
            'nama' : TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Kode Barang'
                }),
            'stok' : TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Kode Barang'
                }),
            'harga' : TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Kode Barang'
                }),
            'link_gbr' : TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Kode Barang'
                }),
            'jenis_id_id' : SelectMultiple(attrs={
                'class': "form-control",
                }),
        }