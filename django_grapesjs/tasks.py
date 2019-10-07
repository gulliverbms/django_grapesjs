from django_grapesjs import get_grapesjs_model


def clear_empty_templates():
    model_class = get_grapesjs_model()
    empty_template_qs = model_class.objects.filter(
        gjs_assets='',
        gjs_css='',
        gjs_styles='',
        gjs_html='',
        gjs_components=''
    )
    for row in empty_template_qs:
        row.delete()
