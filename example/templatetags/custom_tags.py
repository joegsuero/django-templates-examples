from django import template
from datetime import datetime

# Registra una instancia de template.Library para tus filtros y tags.
register = template.Library()


@register.simple_tag
def get_current_time(format_string):
    """
    Tag simple que retorna la hora actual formateada.
    Uso: {% get_current_time "%H:%M:%S" %}
    """
    return datetime.now().strftime(format_string)


@register.inclusion_tag('componentes/navbar.html', takes_context=True)
def show_navbar(context):
    """
    Tag de inclusión que renderiza un componente de navegación.
    Toma el contexto de la plantilla padre para acceder a request.user.
    Uso: {% show_navbar %}
    """
    # Accede al objeto request del contexto para obtener el usuario.
    request = context.get('request')
    user = request.user if request else None  # Asegura que request exista

    # Prepara las variables para la plantilla 'navbar.html'
    return {
        'user': user,
        'is_staff': user.is_staff if user and user.is_authenticated else False
    }
