from django.db import models
from django.urls import reverse


class CourseManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query)
        )


#classe com os campos de cursos
class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    about = models.TextField('Sobre o Curso', blank=True)
    start_date = models.DateField(
        'Data de Início', null=True, blank=True
    )
    image = models.ImageField(
        upload_to='couses/images', verbose_name='Imagem',
        null=True, blank=True
    )
    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = CourseManager()

#função que mostra os nomes dos cursos cadastradosna tabela
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('course:details', args=[self.slug])

    class Meta:
        verbose_name = 'Curso' #muda o nome da "CURSO" para o plural "CURSOS"
        verbose_name_plural = 'Cursos'
        ordering = ['name'] #ordena por "NOME"

