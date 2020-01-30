# Example code to create pdf's with Django

- WeasyPrint package: https://weasyprint.org/
- Guide on how to use it: https://dev.to/djangotricks/how-to-create-pdf-documents-with-django-in-2019-5gb9

## Content

This is a dummy project for reference. There is 1 endpoint which can be called. Based on a post id it creates a html, 
converts it to a pdf document and return it.

## How to use it (Terminal commands)

- Open your terminal and cd into DjangoPlayground

- Create a conda environment to install Django, Weasyprint and all other dependencies
`conda env create -f requirements.yml`

- Create database tables (sqlite3)
`python manage.py migrate`

- Create a superuser
`python manage.py createsuperuser`

- Run the Django development server
`python manage.py runserver 0:8000`

- Visit http://localhost:8000/admin/ and create at least 1 new post

- Visit http://localhost:8000/api/posts/1/ to see the PDF preview in your browser (you can replace 1 with any post id)

## How it works

- The endpoint .../api/posts/1/ is calling the function post_pdf.
- Information about the post with ID 1 (or whichever you passed in the url) will be taken from the database
- With the post information and the template 'post_pdf.html', a html string is created
- After that, the pdf is created based on that html string. CSS can be add at that point.

## Options

If you want to have a download window instead of the PDF preview as response, you can change "inline" to "attachment"
in post/views/ on line 18.

## Good to know

If you get error messages after the installation, you can check the docs of Weasyprint. There might be differences 
depending on your OS system. https://weasyprint.readthedocs.io/en/latest/install.html
