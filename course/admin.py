from django.contrib import admin

from .models import Course


#classe que lista os "CURSOS" com itens descritos e permite pesquisa por determinada palavra chave
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Course, CourseAdmin)