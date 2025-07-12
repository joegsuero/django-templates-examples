from django.shortcuts import render
from django.utils.html import mark_safe
from datetime import datetime


def home(request):
    """
    View for the home page, demonstrating basic variables, loops, and filters.
    """
    context = {
        'username': 'John Doe',
        'products': [
            {'name': 'Laptop', 'price': 1200, 'id': 1},
            {'name': 'Monitor', 'price': 300, 'id': 2},
            {'name': 'Keyboard', 'price': 75, 'id': 3},
        ],
        'now': datetime.now(),  # For the 'date' filter example
        'top_selling_products': [  # For the {% cache %} example
            {'name': 'Gaming Laptop'},
            {'name': 'Ergonomic Mouse'},
            {'name': 'HD Webcam'},
        ]
    }
    return render(request, 'home.html', context)


def products(request):
    """
    View for the products page, demonstrating template inheritance and inclusion.
    """
    context = {
        'products': [
            {'name': 'Laptop', 'price': 1200, 'id': 1},
            {'name': 'Monitor', 'price': 300, 'id': 2},
            {'name': 'Keyboard', 'price': 75, 'id': 3},
            {'name': 'Mouse', 'price': 25, 'id': 4},
        ]
    }
    return render(request, 'products.html', context)


def article_detail(request):
    """
    View for an article, demonstrating the use of mark_safe.
    """
    safe_html_content = "<p>This is <strong>safe HTML content</strong>, loaded from the view.</p>" \
        "<p>Normally, this would come from a database or a trusted source.</p>" \
        "<p>Remember to use `mark_safe` with extreme caution!</p>"
    # Only use mark_safe if you are 100% sure of the HTML source!
    return render(request, 'article.html', {'content': mark_safe(safe_html_content)})


def product_detail(request, product_id):
    """
    Example view for a product detail (used in {% url %}).
    Does not implement real logic, just a simple response.
    """
    return render(request, 'product_detail.html', {'product_id': product_id})  # You would need to create product_detail.html
