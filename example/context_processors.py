def global_app_info(request):
    """
    Adds company name and app version to the context.
    """
    return {
        'COMPANY_NAME': 'Django Templates Examples',
        'APP_VERSION': '1.0.2 Beta',
        'COPYRIGHT_YEAR': 2025  # Or datetime.now().year
    }
