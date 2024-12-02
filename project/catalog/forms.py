from django import forms 
 
 
class UserForm(forms.Form): 
    """
    name = forms.CharField(label="Имя клиента", max_length=15, help_text="ФИО не более 15 символов")      
    age = forms.IntegerField(label="Возраст клиента") 
    basket = forms.BooleanField(label="Положить товар в корзину", required=False) 
    ling = forms.ChoiceField(label="Выберите язык", choices=((1, "Английский"), (2, "Немецкий"), (3, "Французский"))) 
    date = forms.DateField(label="Введите дату") 
    date_time = forms.DateTimeField(label="Введите дату и время") 
    num = forms.DecimalField(label="Введите десятичное число", decimal_places=2) 
    email = forms.EmailField(label="Электронный адрес", help_text="Обязательный символ - @")

    """
   
    file_path = forms.FilePathField(label="choose file", path="C:/", allow_files="True", allow_folders="True")
    num = forms.FloatField(label="Enter number")
    ip_address = forms.GenericIPAddressField(label="ip address", help_text="for example 192.0.2.0")
    file = forms.ImageField(label="image") 