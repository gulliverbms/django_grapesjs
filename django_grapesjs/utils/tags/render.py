import re
from functools import reduce
from django.template import Template, Context
from django_grapesjs.settings import NAME_RENDER_TAG

__all__ = ('ApplyRenderTag', )


REGEX_RENDER_TAG = '<%s>(.*?)</%s>' % (NAME_RENDER_TAG, NAME_RENDER_TAG)


class ApplyRenderTag(object):
    def apply_tag_init(self, string):
        strings_to_render = re.findall(REGEX_RENDER_TAG, string)
        replace_to_strings = map(lambda t: t.render(Context({})), map(Template, strings_to_render))

        return reduce(lambda s, r: re.sub(REGEX_RENDER_TAG, r, s, 1), replace_to_strings, string)

    def apply_tag_save(self, string):
        return string
