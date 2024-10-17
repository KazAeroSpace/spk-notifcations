from django.db import models


class Contract(models.Model):
    oid = models.IntegerField(
        verbose_name="ARCGIS OBJ ID",
        null=True,
        blank=True
    )
    num = models.CharField(
        max_length=256,
        verbose_name="Номер договора",
        null=True,
        blank=True
    )
    exp_date = models.DateField(
        verbose_name="Дата истечения договора",
        null=True,
        blank=True
    )
    location = models.CharField(
        max_length=256,
        verbose_name="Локация",
        null=True,
        blank=True
    )
    area = models.FloatField(
        verbose_name="Площадь",
        null=True,
        blank=True)
    price_1sq = models.IntegerField(
        verbose_name="Стоимость 1 кв м",
        null=True,
        blank=True
    )
    montly = models.IntegerField(
        verbose_name="Оплата за месяц",
        null=True,
        blank=True
    )
    tenant = models.CharField(
        max_length=512,
        verbose_name="Владелец",
        null=True,
        blank=True
    )
    purpose = models.CharField(
        max_length=512,
        verbose_name="Назначение",
        null=True,
        blank=True
    )
    num_date_agg = models.CharField(
        max_length=512,
        verbose_name="Номер и дата договора",
        null=True,
        blank=True
    )
    subrent = models.CharField(
        max_length=512,
        verbose_name="Субаренда",
        null=True,
        blank=True
    )
    owner_ddu = models.CharField(
        max_length=512,
        verbose_name="",
        null=True,
        blank=True
    )
    note = models.CharField(
        max_length=512,
        verbose_name="Примечание",
        null=True,
        blank=True
    )
    region = models.CharField(
        max_length=512,
        verbose_name="Регион",
        null=True,
        blank=True
    )
    globalid = models.CharField(
        max_length=128,
        verbose_name="GLOBAL ID",
        null=True,
        blank=True
    )
    phone_num = models.CharField(
        max_length=64,
        verbose_name="Номер телефона владельца",
        null=True,
        blank=True
    )
    user = models.ForeignKey(
        'user.User',
        on_delete=models.DO_NOTHING,
        verbose_name="Пользователь",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Договор"
        verbose_name_plural = "Договора"
