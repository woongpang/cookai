import re
from django.core.exceptions import ValidationError


def validate_password(self, password):
    """비밀번호 유효성 검사"""
    if len(password) < 8:
        raise ValidationError({"password": "비밀번호는 8자리 이상이어야 합니다."})
    if not re.search(r"[a-zA-Z]", password):
        raise ValidationError({"password": "비밀번호는 하나 이상의 영문이 포함되어야 합니다."})
    if not re.search(r"\d", password):
        raise ValidationError({"password": "비밀번호는 하나 이상의 숫자가 포함되어야 합니다."})
    if not re.search(r"[!@#$%^&*()]", password):
        raise ValidationError(
            {"password": "비밀번호는 적어도 하나 이상의 특수문자(!@#$%^&*())가 포함되어야 합니다."}
        )
    return password
