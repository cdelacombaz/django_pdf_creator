# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template.loader import render_to_string
from rest_framework.generics import get_object_or_404
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

from project import settings
from .models import Post


def post_pdf(request, id):
    post = get_object_or_404(Post, pk=id)
    response = HttpResponse(content_type="application/pdf")

    # inline will open the pdf as preview in the browser. change it to attachement to have a downloadable file
    response['Content-Disposition'] = f"inline; filename={post.id}-{post.author}-post_{post.created.strftime('%Y-%m-%d')}.pdf"

    html = render_to_string(
        template_name="post_pdf.html",
        context={'post': post}
    )

    host_url = request.META.get('wsgi.url_scheme') + '://' + request.META['HTTP_HOST']

    css = CSS(host_url + settings.STATIC_ROOT + 'post_pdf.css')

    font_config = FontConfiguration()
    HTML(string=html).write_pdf(response, stylesheets=[css], font_config=font_config)
    return response


    # Following code is just to render a html as response - used it for testing
    # post = get_object_or_404(Post, pk=id)
    # template = loader.get_template('post_pdf.html')
    # context = {
    #     'post': post
    # }
    # return HttpResponse(template.render(context, request))
