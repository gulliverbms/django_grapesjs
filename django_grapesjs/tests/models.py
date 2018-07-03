from django import test
from django.core.management.base import SystemCheckError

from django_grapesjs.models import GrapesJsHtmlField
from django_grapesjs.forms import GrapesJsField, GrapesJsWidget
from django_grapesjs.settings import REDACTOR_CONFIG

__all__ = ('GrapesJsHtmlFieldTestCase', )


TEMPLATE_CHOICES = (
    ('admin/500.html', '500 error', ),
    ('admin/404.html', '404 error', ),
)

class GrapesJsHtmlFieldTestCase(test.TestCase):
    def setUp(self):
        value_args = GrapesJsHtmlField.__init__.__defaults__

        self.default_params_for_formfield = {
            'default_html': value_args[0],
            'html_name_init_conf': REDACTOR_CONFIG[value_args[1]],
            'apply_django_tag': value_args[2],
            'validate_tags': value_args[3],
            'template_choices': value_args[4],
            'form_class': GrapesJsField,
            'widget': GrapesJsWidget,
        }

    def test_init(self):
        field = GrapesJsHtmlField()

        self.assertDictEqual(field.params_for_formfield, self.default_params_for_formfield)

    def test_init_incorrect_args(self):
        default_html_incorrect = 0
        apply_django_tag_incorrect = 'string'
        validate_tags_incorrect = 'string'

        with self.assertRaises(TypeError):
            GrapesJsHtmlField(any=0)

        field = GrapesJsHtmlField(
            default_html=default_html_incorrect,
            apply_django_tag=apply_django_tag_incorrect,
            validate_tags=validate_tags_incorrect
        )

        data = self.default_params_for_formfield.copy()
        data['default_html'] = default_html_incorrect
        data['apply_django_tag'] = apply_django_tag_incorrect
        data['validate_tags'] = validate_tags_incorrect

        self.assertDictEqual(field.params_for_formfield, data)

    def test_init_choices(self):
        with self.assertRaisesRegex(
            ValueError, "use 'template_choices' instead of 'choices' in the '\w+?'"
        ):
            GrapesJsHtmlField(choices=TEMPLATE_CHOICES)

    def test_init_template_choices_correct_value(self):
        field = GrapesJsHtmlField(template_choices=TEMPLATE_CHOICES)

        data = self.default_params_for_formfield.copy()
        data['default_html'] = TEMPLATE_CHOICES[0][0]
        data['template_choices'] = TEMPLATE_CHOICES

        self.assertDictEqual(field.params_for_formfield, data)

    def test_init_template_choices_incorrect_value(self):
        with self.assertRaisesRegex(
            SystemCheckError, "\nERROR:\n\w+?: '\w+?' must be an iterable \(e\.g\., a list or tuple\)\."
        ):
            GrapesJsHtmlField(template_choices='string')

        with self.assertRaisesRegex(
            SystemCheckError,
            "\nERROR:\n\w+?: '\w+?' must be an iterable containing \(actual value, human readable name\) tuples\."
        ):
            GrapesJsHtmlField(template_choices=(('value',),))

    def test_init_redactor_config_incorrect_value(self):
        with self.assertRaises(KeyError):
            GrapesJsHtmlField(redactor_config='incorrect_value')

    def test_formfield(self):
        with self.assertRaisesRegex(TypeError, "__init__\(\) got an unexpected keyword argument '\w+?'"):
            field = GrapesJsHtmlField()
            field.formfield(key='value')

        self.assertEqual(GrapesJsHtmlField().formfield().__class__, GrapesJsField)

    def test_check_template_choices(self):
        field = GrapesJsHtmlField()
        self.assertFalse(field.check_template_choices(False))

        with self.assertRaises(SystemCheckError):
            field.check_template_choices(True)

        self.assertTrue(field.check_template_choices(TEMPLATE_CHOICES))

