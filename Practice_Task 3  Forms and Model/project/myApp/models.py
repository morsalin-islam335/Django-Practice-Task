from django.db import models

# Create your models here.



class Model1(models.Model):
    name = models.CharField(max_length = 50, null = True, blank = True)
    pk1 = models.AutoField(primary_key = True) # এটা অটো মেটিক ভাবে increase করবে
    big_number = models.BigIntegerField()
    Age = models.IntegerField(null = True, blank = True)

    binary_data = models.BinaryField(null = True, blank = True)
    isEmployee = models.BooleanField(null = True, blank = True)
    description = models.TextField(null  = True, blank = True)
    birth_day = models.DateField(null = True, blank = True)
    weight = models.DecimalField(max_digits = 5, decimal_places = 4, blank   = True, null = True)# dicimal places er maddhoma decimal point er por koyta digit thakba ta nirdesh kora.  ar max digit hoicha maximum digit with floating point
    EventTime = models.DateTimeField(null = True, blank =  True)
    duration = models.DurationField(blank = True, null = True)# eta time track rakhar jonno
    email = models.EmailField(blank = True, null = True)
    height = models.FloatField(blank = True, null = True)
    num1 = models.PositiveIntegerField(blank = True, null = True)
    num2 = models.PositiveBigIntegerField(blank = True, null = True,)
    num3 = models.SmallIntegerField(blank = True, null = True,)
    description = models.TextField(blank = True, null = True)
    time = models.TimeField(blank = True, null = True)
    linkedin_profile = models.URLField(blank = True, null = True)
    TermsAndCondition = models.BooleanField(null = True, blank =  True)  # NullBooleanField is not works


    file = models.FileField(upload_to='media/uploads', null = True, blank = True) # required false




    



class Model2(models.Model):
    pk2 = models.BigAutoField(primary_key= True) # এটা অটো মেটিক ভাবে increase করবে

class Model3(models.Model):
    description = models.TextField(null = True, blank = True)
    slug = models.SlugField(max_length = 300)


class Teacher(models.Model):
    name = models.CharField(max_length = 60, blank = True, null = True)
    subject = models.CharField(max_length = 40, blank = True, null =  True)
    teacher_id = models.BigIntegerField(blank = True, null =  True)

# যেখানে বেশি থাকবে সেইখানে foreign key set করতে হবে।
class Student(models.Model):
    name = models.CharField(max_length = 60, blank = True, null = True)
    roll = models.IntegerField(blank = True,  null = True)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE, related_name = 'Students')
    # related name এর জায়গায় নিজস্ব model এর plural name আর field এর জায়গায় foreign model এর নাম দিলে ভাল হয়।

    def __str__(self):
        return self.name



class Course(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'Course', blank = True, null = True)
    credit = models.IntegerField(null = True, blank = True)
    students  = models.ManyToManyField(Student, related_name="courses", blank = True, null = True)
    
