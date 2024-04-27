from django import template

register = template.Library()

@register.filter(name='html_to_real')
def html_to_real(value):
    # Lógica para converter HTML em texto real
    pass
