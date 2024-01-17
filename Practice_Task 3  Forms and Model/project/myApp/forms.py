from django import forms


#  Form API
choice = (
    ('1','*'),
    ('2','**'),
    ('3','***'),
    ('4','****'),
    ('5','*****'),
)
class User(forms.Form):
    name = forms.CharField(max_length= 50)
    email = forms.EmailField(help_text= 'Enter your email correctly', required=False)
    password = forms.CharField(widget= forms.PasswordInput(), help_text = 'Enter a strong password')
 
    rating = forms.ChoiceField(choices = choice)
    rating2 = forms.TypedChoiceField(choices = choice, coerce = str) # ami jokhon backend theke access korta jabo tokhon etaka string hisabai pabo.
    date = forms.DateField(help_text= 'Provide data with this format year-month-day(YY-MM-DD)') # data format will be year-month-day(YY-MM-DD)
    date_time = forms.DateTimeField(help_text = "Provide a date with time", required = False, error_messages={'invalid':'Your provided date format is not correct'})
    age = forms.DecimalField(max_value= 20)
    income_per_capital = forms.DecimalField()
    duration = forms.DurationField(help_text= 'input duration in second unit')# it takes duration in second unit # we can access this through timedelta 
    weight = forms.FloatField()
    Working_hour = forms.IntegerField()

    file = forms.FileField(required = False)
    choice = (
        ('Hd', "Hardware"),
        ("Sft", 'Software'),
        ('Nt','Networking'),
        ("Db", 'Database'),
        ("CP", "Competitive Programming")
    )

    hobbies =forms.MultipleChoiceField(choices =choice)
    hobbies2 =forms.TypedMultipleChoiceField(choices =choice)

    isAddult = forms.NullBooleanField()
    regex =  forms.RegexField(help_text="Fill this regex field", regex =r'^[a-zA-Z0-9]*$')

    url = forms.URLField()
    time = forms.TimeField()




    # termsAndCondition = forms.BooleanField(label= 'terms and condition')




# Model Form
    
from .models import Model1, Model2
class ModelForm1(forms.ModelForm):
    class Meta:
        model = Model1
        fields = "__all__"
        
