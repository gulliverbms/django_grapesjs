import re
from functools import reduce
from django.template import Template, Context
from django_grapesjs.settings import NAME_MAKEUP_TAG

__all__ = ('ApplyMakeupTag', )


REGEX_MAKEUP_TAG = '<%s>(.*?)</%s>' % (NAME_MAKEUP_TAG, NAME_MAKEUP_TAG)
REGEX_MAKEUP_INIT = '<%s>(?!<div hidden="">{#).*?(?!#}</div>)</%s>' % (NAME_MAKEUP_TAG, NAME_MAKEUP_TAG)
REGEX_MAKEUP_SAVE = '<%s.*?><div hidden="">{#(.*?)#}</div>.*?</%s>' % (NAME_MAKEUP_TAG, NAME_MAKEUP_TAG)


class ApplyMakeupTag(object):
    def apply_tag_init(self, string):
        strings_to_render = re.findall(REGEX_MAKEUP_TAG, string)

        replace_to_strings = map(
            lambda t:
                '<%s><div hidden="">{#%s#}</div>%s</%s>' % (
                    NAME_MAKEUP_TAG, t.source, t.render(Context({})), NAME_MAKEUP_TAG
                ),
                    map(Template, strings_to_render)
        )

        return reduce(lambda s, r: re.sub(REGEX_MAKEUP_INIT, r, s, 1), replace_to_strings, string)

    def apply_tag_save(self, string):
        substrings_to_save = [
            '<%s>%s</%s>' % (NAME_MAKEUP_TAG, sub, NAME_MAKEUP_TAG)
                for sub in re.findall(REGEX_MAKEUP_SAVE, string)
        ]

        return reduce(lambda s, r: re.sub(REGEX_MAKEUP_SAVE, r, s, 1), substrings_to_save, string)

