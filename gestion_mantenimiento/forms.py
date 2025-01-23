from django import forms

class ExcelUploadForm(forms.Form):
    archivo_excel = forms.FileField(label="Selecciona un archivo Excel", required=True)
