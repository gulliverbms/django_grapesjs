from mock import mock
from django import test
from django.core.exceptions import ValidationError
from django_grapesjs.forms import GrapesJsField, GrapesJsWidget

__all__ = ('GrapesJsFieldTestCase', 'GrapesJsWidgetTestCase', )


class GrapesJsFieldTestCase(test.TestCase):
    list_args = {
        'default_html': lambda inst: inst.widget.default_html,
        'html_name_init_conf': lambda inst: inst.widget.html_name_init_conf,
        'apply_django_tag': lambda inst: inst.widget.apply_django_tag,
        'template_choices': lambda inst: inst.widget.template_choices,
        'validate_tags': lambda inst: inst.validate_tags
    }

    def get_check_dict_attr(self, values_default, dict_values, inst):
        data = {}

        for k, v in self.list_args.items():
            data[k] = values_default or dict_values.get(k) or v(inst)

        return data

    def test_init(self):
        incorrect_value = 'string'

        formfield = GrapesJsField()

        self.assertSetEqual(
            set(GrapesJsField.__init__.__defaults__),
            set(self.get_check_dict_attr(None, {}, formfield).values())
        )

        data = self.get_check_dict_attr(incorrect_value, {}, None)
        formfield = GrapesJsField(**data)

        self.assertSetEqual(
            set(data.values()),
            set(self.get_check_dict_attr(None, {}, formfield).values())
        )

    def test_validate(self):
        formfield = GrapesJsField()

        self.assertIsNone(formfield.validate('string'))

    def test_clean_correct_value(self):
        value = 'string'

        formfield = GrapesJsField()
        result = formfield.clean(value)

        self.assertEqual(value, result)

    def test_clean_incorrect_value(self):
        with self.assertRaises(ValidationError):
            formfield = GrapesJsField()
            formfield.clean('')

        with self.assertRaises(TypeError):
            formfield = GrapesJsField()
            formfield.clean(0)


class GrapesJsWidgetTestCase(test.TestCase):
    def test_get_formatted_id_value(self):
        value = 'value-id'
        correct_value = 'value_id'

        widget = GrapesJsWidget()
        result = widget.get_formatted_id_value(value)

        self.assertEqual(correct_value, result)

    @mock.patch('django.forms.widgets.Widget.get_context')
    def test_get_context(self, context_mock):
        value = 0
        attrs = [
            'apply_django_tag',
            'apply_django_tag',
            'template_choices',
            'html_name_init_conf',
        ]
        check_data = {'widget': {'attrs': {'id': 'test'}}}

        widget = GrapesJsWidget()
        context_mock.return_value = check_data

        data = check_data.copy()

        for attr in attrs:
            data['widget'][attr] = value

        attrs.append('default_html')

        for attr in attrs:
            setattr(widget, attr, value)

        self.assertDictEqual(data, widget.get_context('name', 'value', 'attrs'))

