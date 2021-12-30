from django import forms

class ContactUsForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)


class BlockForm(forms.Form):
   height = forms.IntegerField(min_value=0, required=True)
   length = forms.IntegerField(min_value=0, required=True)
   blackpix = forms.IntegerField(min_value=0, required=True)
   blackand = forms.IntegerField(min_value=0, required=True)
   wb_trans = forms.IntegerField(min_value=0, required=True)