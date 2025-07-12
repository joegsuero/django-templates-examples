---

## Django Templates: From Fundamentals to Advanced Tricks

This repository contains all the code examples discussed in the blog post "Django Templates: From Fundamentals to Advanced Tricks." It's designed for you to easily **explore, understand, and test** the concepts of Django's templating engine.

---

### This repository demonstrates:

- **Basic Syntax & Rendering**: How to display variables (`{{ variable }}`) and use control flow tags (`{% for %}`, `{% if %}`).
- **Template Reusability & Modularity**:
  - **Template Inheritance (`{% extends %}`)**: Creating a base template and extending it to reuse common structure.
  - **Component Inclusion (`{% include %}`)**: Reusing small, self-contained template fragments like product cards or navigation elements.
- **Customizing Template Logic**:
  - **Custom Filters**: How to create and use your own filters (e.g., `is_even`, `currency_format`) to transform data for display.
  - **Custom Tags (`@simple_tag`, `@inclusion_tag`)**: Implementing more complex logic directly within templates, including rendering other template fragments with `inclusion_tag`.
- **Real-World Optimization & Considerations**:
  - **Template Fragment Caching (`{% cache %}`)**: Caching specific, costly-to-render sections of your templates for performance.
  - **Using Static Files (`{% static %}`)**: Correctly linking CSS, JavaScript, and images.
  - **Safe HTML Rendering (`|safe filter`)**: Understanding when and how to render raw HTML from trusted sources (with a strong warning about security).

---

### How to Set Up and Run

Follow these steps to get the project running on your local machine:

1.  **Create and Activate a Virtual Environment (Recommended)**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # venv\Scripts\activate   # On Windows
    ```

2.  **Install Dependencies**:

    ```bash
    pip install Django django-htmlmin
    ```

    (`django-htmlmin` is included for the HTML compression example, configured in `settings.py`).

3.  **Prepare the Database (Optional for this example, but good practice)**:

    ```bash
    python manage.py migrate
    python manage.py createsuperuser # Optional, to access the admin and test staff user in navbar
    ```

4.  **Collect Static Files**:
    This command gathers static files from your apps into a single location, which is important for production environments.

    ```bash
    python manage.py collectstatic
    ```

    (Type `yes` if prompted to continue).

5.  **Run the Development Server**:

    ```bash
    python manage.py runserver
    ```

6.  **Explore the Application**:
    Open your web browser and visit the following URLs to interact with the examples:

    - **Home Page (Basic Syntax, Caching Example)**: `http://127.0.0.1:8000/`
    - **Products Page (Inheritance, Include Tag)**: `http://127.0.0.1:8000/products/`
    - **Article Page (`|safe` example)**: `http://127.0.0.1:8000/article/`
    - **Product Detail (Example for `{% url %}`)**: `http://127.0.0.1:8000/products/1/` (change `1` to any product ID)

    **Observe your server console** for any output related to template rendering or custom tag/filter execution.

---

### Conclusion

By interacting with these examples, you'll gain a **practical understanding of how to leverage Django's powerful templating system**. Mastering templates is crucial for building robust, maintainable, and user-friendly web applications.

I encourage you to **play with the code, modify the templates, and see the flexibility and efficiency of Django Templates for yourself**. For an even deeper dive into the definitive guide on Django templating, make sure to read the full blog post.
