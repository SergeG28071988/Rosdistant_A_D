from django.db import models

# Create your models here.


class Person(models.Model):

    last_name = models.CharField(max_length=100, verbose_name="Фамилия автора")
    first_name = models.CharField(max_length=100, verbose_name="Имя автора")    
    date_of_birth = models.DateField(verbose_name="Дата рождения", null=True, blank=True)   
    class Meta:
        abstract = True 

    def __str__(self):
        return self.last_name      


class Author(Person):
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"    


class Language(models.Model):
    name = models.CharField( help_text="Введите язык", verbose_name="Язвк статьи",
                            max_length=100, null=True, blank=True)
    
    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = "Языки"     

    def __str__(self):
        return self.name  
    

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название статьи")
    content = models.TextField(verbose_name="Содержание статьи")
    language = models.ForeignKey(Language, verbose_name="Язык статьи", on_delete=models.CASCADE)
    date_published = models.DateField(verbose_name="Дата публикации")
    author = models.ForeignKey(Author, verbose_name="Автор", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title    
    
    