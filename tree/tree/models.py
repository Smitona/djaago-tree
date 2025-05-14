from django.db import models


class Menu(models.Model):
    """
        Модель меню.
        title: str - название
    """
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ('title',)

    def __str__(self):
        return self.title[:30]


class Ancestor(models.Model):
    """
        Модель веток (наследников) меню (дерева).
    """
    title = models.CharField(max_length=200)
    menu = models.ForeignKey(
            Menu, blank=True,
            related_name='ancestors',
            on_delete=models.CASCADE
        )

    class Meta:
        verbose_name = 'Наследник'
        verbose_name_plural = 'Наследники'
        ordering = ('title',)
