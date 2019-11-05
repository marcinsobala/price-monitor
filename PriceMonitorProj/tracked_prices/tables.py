import django_tables2 as tables
from django.utils.html import format_html

from .models import TrackedPrice


class PriceTable(tables.Table):
    class Meta:
        model = TrackedPrice
        template_name = 'tracked_prices/table.html'
        fields = ('name',
                  'when_inform',
                  'current',
                  'last_checked_date')
        attrs = {'class': 'table table-hover table-responsive'}

    name = tables.Column("Nazwa", attrs={'th': {'class': "col_header"}})

    @staticmethod
    def render_name(record):
        return format_html(
            f"<a href=\"{record.url}\" class=\"price_name\">{record.name}</a>")

    when_inform = tables.Column("Wyślij powiadomienie",
                                attrs={'td': {'style': 'width: 17%'},
                                       'th': {'class': "col_header"}})

    @staticmethod
    def render_when_inform(record):
        if record.when_inform == "A":
            message = f'gdy cena spadnie'
        elif record.when_inform == "B":
            message = f'gdy cena spadnie o {record.percent_drop}%'
        else:
            message = f'gdy cena spadnie do {record.current} {record.currency}'

        return message

    current = tables.Column('Obecna cena',
                            attrs={'td': {'style': 'width: 10%'},
                                   'th': {'class': "col_header"}})

    @staticmethod
    def render_current(record):
        return f"{record.current} {record.currency}"

    last_checked_date = tables.Column("Ostatnio sprawdzono",
                                      attrs={'th': {'class': "col_header"}})

    @staticmethod
    def render_last_checked_date(value):
        return value.strftime("%d.%m.%y")

    edit = tables.Column('Edytuj',
                         linkify=('price_edit', (tables.A("id"),)),
                         orderable=False,
                         empty_values=(),
                         attrs={'th': {'class': "col_header"}})

    @staticmethod
    def render_edit():
        return format_html("<i id = \"ihover\" class=\"fas fa-edit text-muted\"></i>")

    delete = tables.Column('Usuń',
                           linkify=('price_remove', (tables.A("id"),)),
                           orderable=False,
                           empty_values=(),
                           attrs={'th': {'class': "col_header"}})

    @staticmethod
    def render_delete():
        return format_html("<i id=\"ihover\" class=\"fas fa-trash-alt text-danger\"></i>")
