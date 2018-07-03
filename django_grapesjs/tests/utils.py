import os
from django import test
from django.template import TemplateDoesNotExist, TemplateSyntaxError
from django_grapesjs.utils import get_render_html_value
from django_grapesjs.utils import tags
from django_grapesjs.utils.tags.makeup import ApplyMakeupTag
from django_grapesjs.utils.tags.render import ApplyRenderTag
from django_grapesjs.settings import NAME_MAKEUP_TAG as m4p, NAME_RENDER_TAG as r4r

__all__ = (
    'GetRenderHtmlValueTestCase', 'ApplyStringHandlingTestCase',
    'ApplyMakeupTagTestCase', 'ApplyRenderTagTestCase',
)


class GetRenderHtmlValueTestCase(test.TestCase):
    template_name = 'django_grapesjs/tests/get_render_html_value.html'

    def test_get_render_html_value_correct(self):
        value = '{{ "TEST"|lower }}'
        result = 'test'

        self.assertEqual(value, get_render_html_value(self.template_name, apply_django_tag=False)())
        self.assertEqual(result, get_render_html_value(self.template_name, apply_django_tag=True)())

    def test_get_render_html_value_incorrect(self):
        with self.assertRaises(TemplateDoesNotExist):
            get_render_html_value('incorrect', apply_django_tag=False)()


class ApplyStringHandlingTestCase(test.TestCase):
    def test_apply_string_handling(self):
        class T1:
            def apply(self, value):
                return value + '1'

        class T2:
            def apply(self, value):
                return value + '2'

        string = ''
        result_string = '12'

        current_obj_init = tags.obj_init
        tags.obj_init = [T1, T2]

        self.assertEqual(result_string, tags.apply_string_handling(string, method='apply'))

        tags.obj_init = current_obj_init


class ApplyMakeupTagTestCase(test.TestCase):
    apply_tag_init_value = [
        '<%s>{{ "TEST"|lower }}</%s>' % (m4p, m4p),
        '<%s>{{ "TEST"|lower }}</%s><div hidden="">text</div>' % (m4p, m4p),
    ]
    apply_tag_init_result = [
        '<%s><div hidden="">{#{{ "TEST"|lower }}#}</div>test</%s>' % (m4p, m4p),
        '<%s><div hidden="">{#{{ "TEST"|lower }}#}</div>test</%s><div hidden="">text</div>' % (m4p, m4p),
    ]

    def test_apply_tag(self):
        handler = ApplyMakeupTag()

        for string, result in zip(self.apply_tag_init_value, self.apply_tag_init_result):
            self.assertEqual(handler.apply_tag_init(string), result)
            self.assertEqual(handler.apply_tag_save(result), string)

        for string, result in zip(self.apply_tag_init_value, self.apply_tag_init_result):
            self.assertEqual(handler.apply_tag_save(result.replace('test', 'text')), string)

        with self.assertRaises(TemplateSyntaxError):
            handler.apply_tag_init('<%s>' % m4p + '{% incorrect_value %}' + '</%s>' % m4p)


class ApplyRenderTagTestCase(test.TestCase):
    apply_tag_init_value = [
        '<%s>{{ "TEST"|lower }}</%s>' % (r4r, r4r),
    ]
    apply_tag_init_result = [
        'test'
    ]

    def test_apply_tag(self):
        handler = ApplyRenderTag()

        for string, result in zip(self.apply_tag_init_value, self.apply_tag_init_result):
            self.assertEqual(handler.apply_tag_init(string), result)
            self.assertEqual(handler.apply_tag_save(result), result)

        with self.assertRaises(TemplateSyntaxError):
            handler.apply_tag_init('<%s>' % r4r + '{% incorrect_value %}' + '</%s>' % r4r)

