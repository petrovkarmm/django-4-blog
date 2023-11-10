from django.contrib import admin
from .models import Post, Comment

# Добавление фулл модели.
# admin.site.register(Post)


# Адаптация внешнего вида моделей
# под конкретно-прикладную задачу
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Отображение полей
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    # Лист фильтрация справа
    list_filter = ['status', 'created', 'publish', 'author']
    # Строка поиска
    search_fields = ['title', 'body']
    # Автоматическое заполнение слаг во время ввода title
    prepopulated_fields = {'slug': ('title',)}
    # Поле author отображается поисковым виджетом,
    # который будет более приемлемым, чем выбор из выпадающего списка, когда у вас
    # тысячи пользователей.
    raw_id_fields = ['author']
    # Навигация по иерархии дат
    date_hierarchy = 'publish'
    # Сортировка по стобцам по умолчанию
    ordering = ['status', 'publish']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']