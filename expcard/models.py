from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class AttForm(models.Model):
    name = models.CharField(null=False, max_length = 50, verbose_name="Форма аттестации")
    
    def __str__(self):
        return self.name
    
    objects = models.Manager()
    
    class Meta:
        verbose_name = 'Форма аттестации'
        verbose_name_plural = 'Формы аттестации'


class periods(models.Model):
    name_period = models.CharField(null=False, max_length = 30, verbose_name="Название периода")
    date_start = models.DateField(verbose_name="Дата начала периода", null=False)
    date_end = models.DateField(verbose_name="Дата окончания периода", null=False)
    
    def __str__(self):
        return self.name_period
    
    objects = models.Manager()
    
    class Meta:
        verbose_name = "Период"
        verbose_name_plural = "Периоды"


class criteria(models.Model):
    name_criteria = models.CharField(null=False, max_length=50, verbose_name="Критерий")

    def __str__(self):
        return self.name_criteria

    objects = models.Manager()

    class Meta:
        verbose_name = "Критерий"
        verbose_name_plural = "Критерии"


class MunObr(models.Model):
    name_MO = models.CharField(null=False, max_length=250, verbose_name="Наименование МО")
    type_MO = models.CharField(null=False, default="Муниципалитет", max_length=100, verbose_name="Тип МО")

    def __str__(self):
        return self.name_MO

    objects = models.Manager()

    class Meta:
        verbose_name = "МО"
        verbose_name_plural = "МО"


class Position(models.Model):
    name_pos = models.CharField(null=False, max_length=250, verbose_name="Название должности аттестуемого")
    type_pos = models.CharField(null=False, default="Специалист", max_length=20, verbose_name="Тип должности")

    def __str__(self):
        return self.name_pos

    objects = models.Manager()

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"


class ExpLevel(models.Model):
    name_level = models.CharField(null=False, max_length=250, verbose_name="Этап всестороннего анализа")

    def __str__(self):
        return self.name_level

    objects = models.Manager()

    class Meta:
        verbose_name = "Этап всестороннего анализа"
        verbose_name_plural = "Этапы всестороннего анализа"


class certified(models.Model):
    period = models.ForeignKey(periods, on_delete=models.CASCADE, null=False, default=0, verbose_name="Период")
    att_code = models.CharField(null=False, max_length=25, verbose_name="Код аттестуемого", unique=True)
    MO = models.ForeignKey(MunObr, on_delete=models.CASCADE, null=False, related_name="attMOcert",
                               verbose_name="Муниципальное образование")
    FIO = models.CharField(null=False, max_length=100, verbose_name="ФИО")
    Organization = models.CharField(null=False, max_length=300, verbose_name="Образовательная организация")
    Position = models.ForeignKey(Position, on_delete=models.CASCADE, null=False,
                                     verbose_name="Должность")
    att_form = models.ForeignKey(AttForm, on_delete=models.CASCADE, null=False, default=0,
                                     verbose_name="Форма аттестации")
    Category = models.ForeignKey('AttCategories', on_delete=models.CASCADE, null=False,
                                 verbose_name="Заявленная категория")
    target = models.CharField(null=False, max_length=10, default="Нет", verbose_name="Назначения")
    result = models.CharField(null=False, max_length=20, default="Нет результата", verbose_name="Итоговый результат")

    def __str__(self):
        return self.FIO

    objects = models.Manager()

    class Meta:
        verbose_name = "Аттестуемый"
        verbose_name_plural = "Аттестуемые"


class delegates(models.Model):
    period = models.ForeignKey(periods, on_delete=models.CASCADE, null=False, default=0, verbose_name="Период")
    MO = models.ForeignKey(MunObr, on_delete=models.CASCADE, null=False, related_name="delegatesMO",
                           verbose_name="Муниципальное образование")
    FIO = models.CharField(null=False, max_length=100, verbose_name="ФИО")
    Organization = models.CharField(null=False, max_length=300, verbose_name="Образовательная организация")
    email = models.CharField(null=False, max_length=150, verbose_name="email")
    target = models.CharField(null=False, max_length=10, default="Нет", verbose_name="Назначения")
    
    def __str__(self):
        return self.FIO

    objects = models.Manager()

    class Meta:
        verbose_name = "Уполномоченный"
        verbose_name_plural = "Уполномоченные"


class specialists(models.Model):
    period = models.ForeignKey(periods, on_delete=models.CASCADE, null=False, default=0, verbose_name="Период")
    MO = models.ForeignKey(MunObr, on_delete=models.CASCADE, null=False, related_name="specMO",
                           verbose_name="Муниципальное образование")
    FIO = models.CharField(null=False, max_length=100, verbose_name="ФИО")
    Organization = models.CharField(null=False, max_length=300, verbose_name="Образовательная организация")
    Position = models.ForeignKey(Position, on_delete=models.CASCADE, null=False,
                                 verbose_name="Должность")
    email = models.CharField(null=False, max_length=150, verbose_name="email")
    target = models.CharField(null=False, max_length=10, default="Нет", verbose_name="Назначения")
    
    def __str__(self):
        return self.FIO

    objects = models.Manager()

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"


class targets(models.Model):
    date_add = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания назначения")
    delegate = models.ForeignKey(delegates, on_delete=models.CASCADE, null=False, verbose_name="Уполномоченный")
    spec = models.ForeignKey(specialists, on_delete=models.CASCADE, null=False, verbose_name="Специалист")
    cert = models.ForeignKey(certified, on_delete=models.CASCADE, null=False, verbose_name="Аттестуемый")
    
    def __str__(self):
        return str(self.id)
    
    objects = models.Manager()
    
    class Meta:
        verbose_name = "Назначение"
        verbose_name_plural = "Назначения"


class targets_mo(models.Model):
    MO = models.ForeignKey('MunObr', on_delete=models.CASCADE, null=False, related_name="targetsMO",
                           verbose_name="Муниципальное образование")
    delegate = models.ForeignKey(delegates, on_delete=models.CASCADE, null=False, verbose_name="Уполномоченный")
    
    def __str__(self):
        return str(self.id)
    
    objects = models.Manager()
    
    class Meta:
        verbose_name = "Назначение МО"
        verbose_name_plural = "Назначения МО"


class intermediate(models.Model):
    date_add = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания карты")
    spec = models.ForeignKey(specialists, default='1', on_delete=models.CASCADE, null=False, verbose_name="Пользователь")
    operator_choice = models.CharField(null=False, default="Специалист", max_length=50,
                                       verbose_name="Тип карты оператора")
    cert = models.ForeignKey(certified, on_delete=models.CASCADE, null=False, verbose_name="Аттестуемый")
    level = models.ForeignKey(ExpLevel, on_delete=models.CASCADE, null=False, verbose_name="Этап анализа")
    result = models.CharField(null=False, max_length=30, verbose_name="Результат")

    def __str__(self):
        return self.result

    objects = models.Manager()

    class Meta:
        verbose_name = "Запись о карте"
        verbose_name_plural = "Записи о картах"


class cards_criteria(models.Model):
    inter = models.ForeignKey(intermediate, on_delete=models.CASCADE, default="1", null=False,
                              verbose_name="Результат")
    spec = models.ForeignKey(specialists, on_delete=models.CASCADE, null=False, verbose_name="Специалист")
    cert = models.ForeignKey(certified, on_delete=models.CASCADE, null=False, verbose_name="Аттестуемый")
    criteria = models.ForeignKey(criteria, on_delete=models.CASCADE, null=False, verbose_name="Критерий")
    info = models.TextField(null=False, max_length=1000, verbose_name="Замечание специалиста")
    to_deleg = models.BooleanField(null=False, default=False, verbose_name="Отправлено уполномоченному")
    from_operator = models.BooleanField(null=False, default=False, verbose_name="От оператора")
    
    def __str__(self):
        return str(self.id)

    objects = models.Manager()

    class Meta:
        verbose_name = "Запись о замечании специалиста"
        verbose_name_plural = "Записи о замечаниях специалистов"


class AttCategories(models.Model):
    type_cat = models.CharField(null=False, max_length=250, verbose_name="Категория")

    def __str__(self):
        return self.type_cat

    objects = models.Manager()

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class criteria_export(models.Model):
    period = models.ForeignKey(periods, on_delete=models.CASCADE, null=False, default=0, verbose_name="Период")
    id_cards_criteria = models.ForeignKey(cards_criteria, on_delete=models.CASCADE, default="1", null=False,
                                          verbose_name="ID записи")
    MO_spec = models.ForeignKey(MunObr, on_delete=models.CASCADE, default="1", null=False, related_name="MO_exp",
                               verbose_name="МО специалиста")
    FIO_spec = models.CharField(null=False, max_length=250, verbose_name="ФИО специалиста")
    Position_spec = models.ForeignKey(Position, on_delete=models.CASCADE, default="1", null=False, related_name="CritExpPos",
                                      verbose_name="Должность специалиста")
    MO_att = models.ForeignKey(MunObr, on_delete=models.CASCADE, default="1", null=False, related_name="MO_att",
                               verbose_name="МО аттестуемого")
    FIO_att = models.CharField(null=False, max_length=250, verbose_name="ФИО аттестуемого")
    Position_att = models.ForeignKey(Position, on_delete=models.CASCADE, default="1", null=False, related_name="CritAttPos",
                                      verbose_name="Должность специалиста")
    Category = models.ForeignKey(AttCategories, on_delete=models.CASCADE, default="1", null=False,
                                 verbose_name="Аттестационная категория")
    Result = models.CharField(null=False, max_length=30, default="Установить", verbose_name="Результат")
    criteria = models.ForeignKey(criteria, on_delete=models.CASCADE, default="1", null=False, verbose_name="Критерий")
    info = models.TextField(null=False, max_length=1000, verbose_name="Замечание специалиста")
    
    def __str__(self):
        return str(self.id)
    
    objects = models.Manager()
    
    class Meta:
        verbose_name="Замечание специалиста"
        verbose_name_plural="Замечания специалистов"


class ExpCards(models.Model):
    period = models.ForeignKey('periods', on_delete=models.CASCADE, null=False, default=0, verbose_name="Период")
    date_add = models.DateTimeField(verbose_name="Дата создания карты")
    type_MO = models.CharField(null=False, default="Муниципалитет", max_length=20,
                                verbose_name="Тип МО карты")
    type_emp = models.CharField(null=False, default="Специалист", max_length=20,
                                verbose_name="Тип сотрудника")
    MO_expert = models.ForeignKey('MunObr', on_delete=models.CASCADE, related_name="expMO",
                                  verbose_name="МО эксперта")
    FIO_expert = models.CharField(null=False, max_length=250, verbose_name="ФИО эксперта")
    Name_Org_expert = models.CharField(null=False, max_length=300, verbose_name="ОО эксперта")
    Position_expert = models.ForeignKey('Position', on_delete=models.CASCADE, null=False, related_name="ExpPos",
                                        verbose_name="Должность эксперта")
    Level_expert = models.ForeignKey('ExpLevel', on_delete=models.CASCADE, null=False, verbose_name="Уровень эксперта")
    MO_att = models.ForeignKey('MunObr', on_delete=models.CASCADE, null=False, related_name="attMO",
                               verbose_name="МО аттестуемого")
    FIO_att = models.CharField(null=False, max_length=250, verbose_name="ФИО аттестуемого")
    Name_Org_att = models.CharField(null=False, max_length=300, verbose_name="ОО аттестуемого")
    Position_att = models.ForeignKey('Position', on_delete=models.CASCADE, null=False, related_name="AttPos",
                                     verbose_name="Должность аттестуемого")
    Category = models.ForeignKey('AttCategories', on_delete=models.CASCADE, null=False,
                                 verbose_name="Заявленная категория")
    Result = models.CharField(null=False, max_length=30, verbose_name="Результат")
    inter = models.ForeignKey('intermediate', on_delete=models.CASCADE, default='1', null=False,
                                     verbose_name="Должность аттестуемого")

    objects = models.Manager()

    class Meta:
        verbose_name = "Экспертная карта"
        verbose_name_plural = "Экспертные карты"


class Summary_table(models.Model):
    period = models.ForeignKey('periods', on_delete=models.CASCADE, null=False, default=0, verbose_name="Период")
    type_MO = models.CharField(null=False, default="Муниципалитет", max_length=20,
                                verbose_name="Тип МО результата")
    FIO_expert = models.CharField(null=False, max_length=250, verbose_name="ФИО эксперта")
    Level_expert = models.ForeignKey('ExpLevel', on_delete=models.CASCADE, null=False, verbose_name="Уровень эксперта")
    MO_expert = models.ForeignKey('MunObr', on_delete=models.CASCADE, null=False, verbose_name="МО эксперта")
    Position_expert = models.ForeignKey('Position', on_delete=models.CASCADE, null=False,
                                        verbose_name="Должность эксперта")
    count = models.IntegerField(null=False, default=0, verbose_name="Количество экспертиз")
    coincidence_common = models.IntegerField(null=True, verbose_name="Совпадения на первом этапе")
    coincidence_general = models.IntegerField(null=True, verbose_name="Совпадения на втором этапе")
    coincidence_operator = models.IntegerField(null=True, verbose_name="Совпадения с оператором")
    Percent = models.DecimalField(null=False, default=0.0, verbose_name="%", max_digits=5, decimal_places=1)

    objects = models.Manager()

    class Meta:
        verbose_name = "Результат по эксперту"
        verbose_name_plural = "Результаты по экспертам"


class type_oo(models.Model):
    name = models.CharField(max_length=100, verbose_name='Тип ОО')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип ОО'
        verbose_name_plural = 'Типы ОО'


class oo(models.Model):
    full_name = models.CharField(max_length=500, verbose_name='Полное наименование ОО')
    short_name = models.CharField(max_length=100, verbose_name='Краткое наименование ОО')
    mo = models.ForeignKey('MunObr',
                           on_delete=models.PROTECT,
                           null=False,
                           default='1',
                           verbose_name='Муниципальное образование ОО'
                           )
    type = models.ForeignKey('type_oo',
                             on_delete=models.PROTECT,
                             null=False,
                             default='1',
                             verbose_name='Тип ОО')
    address = models.TextField(verbose_name='Адрес ОО')
    phone = models.PositiveIntegerField(null=True, blank=True, verbose_name='Телефон ОО')
    email = models.EmailField(max_length=254, verbose_name='Электронная почта ОО')
    url = models.URLField(max_length=254, verbose_name='Адрес сайта ОО')

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = 'Образовательная организация'
        verbose_name_plural = 'Образовательные организации'
