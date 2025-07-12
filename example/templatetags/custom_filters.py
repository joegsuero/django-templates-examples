from django import template

# Register a template.Library instance for your filters and tags.
register = template.Library()


@register.filter
def is_even(value):
    """
    Returns True if the number is even.
    Usage: {{ number|is_even }}
    """
    try:
        return int(value) % 2 == 0
    except (ValueError, TypeError):
        # Handles cases where the value is not a valid number.
        return False


@register.filter(name='currency_format')
def currency_format(value, currency_symbol='$'):
    """
    Formats a number as currency.
    Usage: {{ price|currency_format:"€" }} or {{ price|currency_format }}
    """
    try:
        # Converts to float and formats with 2 decimal places and thousands separator.
        # Note: The thousands separator (,) may vary depending on regional settings.
        return f"{currency_symbol}{float(value):,.2f}"
    except (ValueError, TypeError):
        # If the value is not numeric, returns the original value.
        return value
