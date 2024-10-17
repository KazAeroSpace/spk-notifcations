from django.db import models
from django.contrib.auth.models import AbstractUser, Group


class User(AbstractUser):
    tg_username = models.CharField(
        verbose_name='Логин в тг',
        max_length=128,
        blank=True, null=True,
    )
    patronymic = models.CharField(
        verbose_name='Отчество',
        max_length=50,
        blank=True, null=True,
    )
    iin = models.CharField(
        max_length=15,
        verbose_name="ИИН",
        null=True,
        blank=True,
    )
    session_hash = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Хэш сессии"
    )
    last_password_change = models.DateTimeField(
        verbose_name='Последнее изменения пароля',
        editable=False,
        null=True,
        blank=True
    )
    tg_chat_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Chat ID'
    )
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Уникальное имя для обратной ссылки
        blank=True
    )
    is_blocked = models.BooleanField(
        default=False,
        verbose_name="Заблокирован"
    )
    phone = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Номер телефона'
    )

    @property
    def groups_names(self):
        groups = self.groups.all()
        if groups.count() > 0:
            groups_arr = []
            for group in groups:
                groups_arr.append(group.name)
            groups_str = ', '.join(groups_arr)
            return groups_str
        return ""

    def __str__(self):
        if self.last_name:
            return f"{str(self.last_name)} {str(self.first_name)} [{str(self.id)}]"
        else:
            if self.first_name:
                return f"{str(self.first_name)} [{str(self.id)}]"
            return str(self.username)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class MessageType(models.TextChoices):
    START = 'START', "Старт"
    TICKET = 'TICKET', "Запрос на создание тикета"
    ASK_CONTRACT_NUMBER = 'ASK_CONTRACT_NUMBER', "Запрос номера договора"


class TgMessageHistory(models.Model):
    message_type = models.CharField(
        verbose_name="Тип сообщения",
        choices=MessageType.choices,
        max_length=256
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Пользователь",
        null=True,
        blank=True
    )
    message_id = models.IntegerField(
        verbose_name="ID сообщения",
        null=True,
        blank=True
    )
    is_deleted = models.BooleanField(
        default=False,
        verbose_name="Удалено",
    )
    deleted_at = models.DateTimeField(
        verbose_name='Удалено',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        verbose_name='Создано',
        auto_now_add=True,
        editable=False,
        db_index=True,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "История сообщений"
        verbose_name_plural = "История сообщений"
