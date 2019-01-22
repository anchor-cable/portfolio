from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from stdimage.models import StdImageField


class AboutList(models.Model):  # Todolist able name that inherits models.Model
    title = models.CharField(max_length=250)  # a varchar
    content = MarkdownxField(blank=True)  # a text field
    created = models.DateField(
        default=timezone.now().strftime("%Y-%m-%d"))  # a date

    class Meta:
        ordering = ["-created"]  # ordering by the created field

    def __str__(self):
        return self.title  # name to be shown when called

    def content2html(self):
        return markdownify(self.content)


class Category(models.Model):  # The Category table name that inherits models.Model
    name = models.CharField(max_length=100)  # Like a varchar
    created = models.DateField(
        default=timezone.now().strftime("%Y-%m-%d"))  # a date

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name  # name to be shown when called


class WorksList(models.Model):
    title = models.CharField(max_length=250)  # a varchar
    content = MarkdownxField(blank=True)  # a text field_
    link = MarkdownxField(blank=True)  # a text field_
    created = models.DateField(
        default=timezone.now().strftime("%Y-%m-%d"))  # a date
    category = models.ForeignKey(
        Category, default="general", on_delete=models.CASCADE)  # a foreignkey
    image = StdImageField(upload_to='path/works', blank=True, variations={
        'large': (600, 400),
        'thumbnail': (300, 200, True),
    })

    def content2html(self):
        return markdownify(self.content)

    def link2html(self):
        return markdownify(self.link)


# Create your models here.
