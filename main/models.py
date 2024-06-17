from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.contrib.auth.models import AbstractUser
from parler.models import TranslatableModel, TranslatedFields
from hitcount.models import HitCountMixin, HitCount


class User(AbstractUser):
    phone = models.TextField(blank=True, null=True)


class Post(TranslatableModel, HitCountMixin):
    image = models.ImageField()
    date = models.DateField()
    translations = TranslatedFields(
        title=models.TextField(),
        content=models.TextField(),
        short=models.TextField()
    )
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Feedback(models.Model):
    name = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)


class Faq(TranslatableModel):
    translations = TranslatedFields(
        title=models.TextField(),
        content=models.TextField(),
    )
    image = models.ImageField()


class Testimonial(TranslatableModel):
    translations = TranslatedFields(
        name=models.TextField(),
        content=models.TextField(),
    )
    image = models.ImageField()
