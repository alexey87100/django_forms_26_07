from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

MAX_LEN_FOR_STR = 50


class Skill(models.Model):
    """Модель навыка."""
    name = models.CharField(max_length=218,
                            verbose_name="Название навыка",
                            )
    value = models.IntegerField(validators=[
                            MinValueValidator(1, "Минимальное зачение-1"),
                            MaxValueValidator(10, "Максимальное значение-10"),
                            ],
                            default=1,
                            verbose_name="Важность навыка",
                            )
    slug = models.SlugField(unique=True,
                            verbose_name="Уникальное имя навыка",
                            )

    class Meta:
        ordering = ("name",)
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.name[:MAX_LEN_FOR_STR]


class Profile(models.Model):
    """Модель профиля сотрудника."""
    name = models.CharField(max_length=218,
                            verbose_name="Полное имя",
                            )
    age = models.IntegerField(default=18,
                              verbose_name="Возраст",
                              )
    skill = models.ForeignKey(Skill,
                              on_delete=models.SET_NULL,
                              null=True,
                              related_name="profiles",
                              )

    class Meta:
        ordering = ("name",)
        verbose_name = "Профиль сотрудника"
        verbose_name_plural = "Профили сотрудников"

    def __str__(self):
        return self.name[:MAX_LEN_FOR_STR]
