import re

from django.core.validators import _lazy_re_compile


class AsteriskRestrictedEmailValidator:
    user_regex = _lazy_re_compile(
        r"(^[-!#$%&'+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'+/=?^_`{}|~0-9A-Z]+)*\Z"  # dot-atom
        r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-\011\013\014\016-\177])*"\Z)',  # quoted-string
        re.IGNORECASE)
