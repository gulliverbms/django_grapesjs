from django.http import HttpResponse
from django.template import TemplateDoesNotExist
from mock import mock
from django import test
from django_grapesjs.views import GetTemplate

__all__ = ('GetTemplateTestCase', )


class GetTemplateTestCase(test.TestCase):
    def test_get(self):
        m = mock.Mock()
        m.GET = {}

        with self.assertRaises(KeyError):
            GetTemplate.get(mock.Mock(), m)

        with self.assertRaisesRegex(ValueError, "invalid literal for int\(\) with base 10: 'num'"):
            m.GET = {'template_name': 'value', 'apply_django_tag': 'num'}
            GetTemplate.get(mock.Mock(), m)

        with self.assertRaises(TemplateDoesNotExist):
            m.GET = {'template_name': 'value', 'apply_django_tag': '0'}
            GetTemplate.get(mock.Mock(), m)

        m.GET = {'template_name': 'django_grapesjs/default.html', 'apply_django_tag': '0'}
        self.assertTrue(isinstance(GetTemplate.get(mock.Mock(), m), HttpResponse))

