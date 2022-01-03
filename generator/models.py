from django.db import models
from .utils import *


class Image(models.Model):
    image = models.ImageField(blank=True, upload_to='images')
    result = models.ImageField(blank=True, upload_to='results')
    gen_type = models.CharField(max_length=20)
    text_fields = models.CharField(max_length=120, blank=True)
    params = models.CharField(max_length=20, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.gen_type

    def sava(self, *args, **kwargs):
        if self.gen_type == 'checks':
            self.result = process_checks(self.image, self.text_fields)
        else:
            self.result = self.image


    def action(self):
        if self.result is True:
            return
        if self.gen_type == "checks":
            self.result = process_checks(self.image, self.text_fields)
        if self.gen_type == 'high_article':
            fields = self.text_fields.split(';')
            color = self.params.split('=')[1]
            self.result = process_high_article(fields[0], fields[1], color)
        if self.gen_type == "triangle_mask":
            color = self.params.split('=')[1]
            self.result = process_triangle_mask(self.image, self.text_fields, color)
        if self.gen_type == "typography":
            color = self.params.split('=')[1]
            self.result = process_typography(self.text_fields, color)

