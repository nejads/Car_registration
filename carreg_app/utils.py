
def validate_phone():
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Not allowed telephone number")
