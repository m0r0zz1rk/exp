from django.contrib import admin
from import_export import resources, widgets
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from .models import *


class PositionResource(resources.ModelResource):
    class Meta:
        model = Position
        list_display = ("name_pos", "type_pos")


class PeriodsResource(resources.ModelResource):
    class Meta:
        model = periods
        list_display = ("name_period", "date_start, date_end")


class MOResource(resources.ModelResource):
    class Meta:
        model = MunObr
        list_display = ("name_MO", "type_MO")


class IntermediateAdmin(admin.ModelAdmin):
    list_display = ('date_add', 'spec', 'operator_choice', 'cert', 'level', 'result')

    class Meta:
        model = intermediate
        fields = ('date_add', 'spec', 'operator_choice', 'cert', 'level', 'result')


class CriteriaExportResource(resources.ModelResource):
    MO_spec = Field(attribute="MO_spec", column_name="МО специалиста",
                        widget=ForeignKeyWidget(MunObr, "name_MO"))
    FIO_spec = Field(attribute="FIO_spec", column_name="ФИО специалиста")
    Position_spec = Field(attribute="Position_spec", column_name="Должность специалиста",
                        widget=ForeignKeyWidget(Position, "name_pos"))
    MO_att = Field(attribute="MO_att", column_name="МО аттестуемого",
                        widget=ForeignKeyWidget(MunObr, "name_MO"))
    FIO_att = Field(attribute="FIO_att", column_name="ФИО аттестуемого")
    Position_att = Field(attribute="Position_att", column_name="Должность аттестуемого",
                        widget=ForeignKeyWidget(Position, "name_pos"))
    Category = Field(attribute="Category", column_name="Аттестационная категория",
                        widget=ForeignKeyWidget(AttCategories, "type_cat"))
    Result = Field(attribute="Result", column_name="Результат аттестации")
    criteria = Field(attribute="criteria", column_name="Критерий",
                     widget=ForeignKeyWidget(criteria, "name_criteria"))
    info = Field(attribute="info", column_name="Замечание")

    list_display = ("MO_spec", "FIO_spec", "Position_spec", "MO_att", "FIO_att", "Position_att", "Category",
                    "Result", "criteria", "info")

    class Meta:
        fields = ("MO_spec", "FIO_spec", "Position_spec", "MO_att", "FIO_att", "Position_att", "Category",
                    "Result", "criteria", "info")
        model = criteria_export


class CriteriaResource(resources.ModelResource):
    spec__FIO = Field(attribute="spec", column_name="ФИО специалиста",
                        widget=ForeignKeyWidget(specialists, "FIO"))
    cert__FIO = Field(attribute="cert", column_name="ФИО аттестуемого",
                     widget=ForeignKeyWidget(certified, "FIO"))
    inter__result = Field(attribute="inter", column_name="Результат аттестации",
                     widget=ForeignKeyWidget(intermediate, "result"))
    criteria__name_criteria = Field(attribute="criteria", column_name="Критерий",
                     widget=ForeignKeyWidget(criteria, "name_criteria"))
    info = Field(attribute="info", column_name="Замечание")

    list_display = ("spec__FIO", "cert__FIO", "inter__result", "criteria__name_criteria", "info")

    class Meta:
        fields = ("spec__FIO", "cert__FIO", "inter__result", "criteria__name_criteria", "info")
        model = criteria_export



class CertifiedResource(resources.ModelResource):
    period__name_period = Field(attribute="period", column_name="Период",
                                widget=ForeignKeyWidget(periods, "name_period"))
    att_code = Field(attribute="att_code", column_name="Код аттестуемого")
    MO__name_MO = Field(attribute="MO", column_name="Муниципальное образование",
                        widget=ForeignKeyWidget(MunObr, "name_MO"))
    FIO = Field(attribute="FIO", column_name="ФИО")
    Organization = Field(attribute="Organization", column_name="ОО")
    att_form__name = Field(attribute="att_form", column_name="Форма аттестации",
                                    widget=ForeignKeyWidget(AttForm, "name"))
    Position__name_pos = Field(attribute="Position", column_name="Должность",
                                   widget=ForeignKeyWidget(Position, "name_pos"))
    Category__type_cat = Field(attribute="Category", column_name="Заявленная категория",
                               widget=ForeignKeyWidget(AttCategories, "type_cat"))

    list_display = ("att_code", "MO__name_MO", "FIO", "Organization",
                    "Position__name_pos", "att_form__name", "Category__type_cat")
    class Meta:
        model = certified
        fields = ("period__name_period", "att_code", "MO__name_MO", "FIO", "Organization",
                    "Position__name_pos", "att_form__name", "Category__type_cat")


class SpecialistsResource(resources.ModelResource):
    period__name_period = Field(attribute="period", column_name="Период",
                                widget=ForeignKeyWidget(periods, "name_period"))
    MO__name_MO = Field(attribute="MO", column_name="Муниципальное образование",
                               widget=ForeignKeyWidget(MunObr, "name_MO"))
    Position__name_pos = Field(attribute="Position", column_name="Должность",
                                   widget=ForeignKeyWidget(Position, "name_pos"))               
    list_display = ("period__name_period", "MO__name_MO", "FIO", "Organization",
                    "Position__name_pos", "email")

    class Meta:
        model = specialists
        fields = ("period__name_period", "MO__name_MO", "FIO", "Organization",
                    "Position__name_pos", "email")


class DelegatesResource(resources.ModelResource):
    period__name_period = Field(attribute="period", column_name="Период",
                                widget=ForeignKeyWidget(periods, "name_period"))
    MO__name_MO = Field(attribute="MO", column_name="Муниципальное образование",
                               widget=ForeignKeyWidget(MunObr, "name_MO"))
    list_display = ("period__name_period", "MO__name_MO", "FIO", "Organization",
                    "Position__name_pos", "email")

    class Meta:
        model = delegates
        fields = ("period__name_period", "MO__name_MO", "FIO", "Organization", "email")


class SummaryResource(resources.ModelResource):
    FIO_expert = Field(attribute="FIO_expert", column_name="ФИО эксперта")
    Level_expert__name_level = Field(attribute="Level_expert", column_name="Уровень эксперта")
    MO_expert__name_MO = Field(attribute="MO_expert", column_name="МО эксперта")
    Position_expert__name_pos = Field(attribute="Position_expert", column_name="Должность эксперта")
    count = Field(attribute="count", column_name="Количество экспертиз")
    coincidence_common = Field(attribute="coincidence_common", column_name="Совпадения на первом этапе")
    coincidence_general = Field(attribute="coincidence_general", column_name="Совпадения на втором этапе")
    coincidence_operator = Field(attribute="coincidence_operator", column_name="Совпадения с оператором")
    Percent = Field(attribute="Percent", column_name="Результативность (%)")
    
    class Meta:
        model = Summary_table
        fields = ("FIO_expert", "Level_expert__name_level", "MO_expert__name_MO", "Position_expert__name_pos", "count",
                  "coincidence_common", "coincidence_general", "coincidence_operator", "Percent")


class ExpCardResources(resources.ModelResource):
    MO_expert__name_MO = Field(attribute="MO_expert", column_name="МО эксперта",
                               widget=ForeignKeyWidget(MunObr, "name_MO"))
    FIO_expert = Field(attribute="FIO_expert", column_name="ФИО эксперта")
    Name_Org_expert = Field(attribute="Name_Org_expert", column_name="ОО эксперта")
    Position_expert__name_pos = Field(attribute="Position_expert", column_name="Должность эксперта",
                                      widget=ForeignKeyWidget(Position, "name_pos"))
    Level_expert__name_level = Field(attribute="Level_expert", column_name="Уровень эксперта",
                                     widget=ForeignKeyWidget(ExpLevel, "name_level"))
    MO_att__name_MO = Field(attribute="MO_att", column_name="МО аттестуемого",
                            widget=ForeignKeyWidget(MunObr, "name_MO"))
    FIO_att = Field(attribute="FIO_att", column_name="ФИО аттестуемого")
    Name_Org_att = Field(attribute="Name_Org_att", column_name="ОО аттестуемого")
    Position_att__name_pos = Field(attribute="Position_att", column_name="Должность аттестуемого",
                                   widget=ForeignKeyWidget(Position, "name_pos"))
    Category__type_cat = Field(attribute="Category", column_name="Заявленная категория",
                               widget=ForeignKeyWidget(AttCategories, "type_cat"))
    Result = Field(attribute="Result", column_name="Результат аттестации")

    class Meta:
        model = ExpCards
        fields = ("MO_expert__name_MO", "FIO_expert", "Name_Org_expert", "Position_expert__name_pos",
                  "Level_expert__name_level", "MO_att__name_MO", "FIO_att", "Name_Org_att",
                  "Position_att__name_pos", "Category__type_cat", "Result")
        import_id_fields = ()



class ExpCardsAdmin(ImportExportModelAdmin):
    list_display = ("date_add", "type_MO", "type_emp", "MO_expert", "FIO_expert", "Name_Org_expert", "Position_expert", "Level_expert",
                    "MO_att", "FIO_att", "Name_Org_att", "Position_att", "Category", "Result")
    list_filter = ("MO_expert", "FIO_expert", "FIO_att", "type_MO", "type_emp")
    search_fields = ("FIO_expert", "FIO_att", "MO_expert__name_MO", "MO_att__name_MO", "Position_att__name_pos")
    ordering = ("FIO_expert", "MO_expert", "MO_att", "FIO_att", "Position_att")
    resource_class = ExpCardResources


class SummaryAdmin(ImportExportModelAdmin):
    list_display = (
        "type_MO", "FIO_expert", "Level_expert", "MO_expert", "Position_expert", "count", "coincidence_common",
        "coincidence_general", "coincidence_operator",
        "Percent")
    list_filter = ("type_MO", )
    search_fields = ["FIO_expert", "MO_expert__name_MO"]
    resource_class = SummaryResource


class CardsCriteriaAdmin(ImportExportModelAdmin):
    list_display = ("spec", "cert", "inter", "criteria", "info")
    resource_class = CriteriaResource


class CriteriaExportAdmin(ImportExportModelAdmin):
    list_display = ("MO_spec", "FIO_spec", "Position_spec", "MO_att", "FIO_att", "Position_att", "Category",
                    "Result", "criteria", "info")
    resource_class = CriteriaExportResource


class CertifiedAdmin(ImportExportModelAdmin):
    list_display = ("att_code", "MO", "FIO", "Organization",
                    "Position", "att_form", "Category")
    list_filter = ("period",)
    resource_class = CertifiedResource


class PositionAdmin(ImportExportModelAdmin):
    list_display = ("name_pos", "type_pos")
    resource_class = PositionResource


class SpecialistsAdmin(admin.ModelAdmin):
    list_display = ("period", "MO", "FIO", "Organization",
                    "Position", "email")
    list_filter = ("period",)
    resource_class = SpecialistsResource


class DelegatesAdmin(admin.ModelAdmin):
    list_display = ("period", "MO", "FIO", "Organization", "email")
    list_filter = ("period",)
    resource_class = DelegatesResource


class MOAdmin(ImportExportModelAdmin):
    list_display = ('name_MO', 'type_MO')
    resource_class = MOResource


class PeriodsAdmin(ImportExportModelAdmin):
    list_display = ('name_period', 'date_start', 'date_end')
    resource_class = PeriodsResource


admin.site.register(AttCategories)
admin.site.register(MunObr, MOAdmin)
#admin.site.register(periods, PeriodsAdmin)
admin.site.register(AttForm)
admin.site.register(Position, PositionAdmin)
admin.site.register(ExpLevel)
admin.site.register(criteria)
#admin.site.register(intermediate, IntermediateAdmin)
#admin.site.register(cards_criteria, CardsCriteriaAdmin)
admin.site.register(criteria_export, CriteriaExportAdmin)
#admin.site.register(certified, CertifiedAdmin)
#admin.site.register(specialists, SpecialistsAdmin)
#admin.site.register(delegates, DelegatesAdmin)
admin.site.register(ExpCards, ExpCardsAdmin)
admin.site.register(Summary_table, SummaryAdmin)
