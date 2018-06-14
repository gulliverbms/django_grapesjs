from django_grapesjs.settings import STRING_HANDLERS as s_h
from importlib import import_module as i_m
from functools import reduce

__all__ = ('apply_string_handling', )


obj_init = [getattr(i_m(s[:s.rfind('.')]), s[s.rfind('.')+1:]) for s in set(s_h)]


def apply_string_handling(string, method='apply_tag_init'):
    return reduce(lambda s, C: getattr(C(), method)(s), obj_init, string)

