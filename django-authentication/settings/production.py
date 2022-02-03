from .base import *


# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================

EMAIL_HOST = config("EMAIL_HOST", default='')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
DEFAULT_FROM_MAIL = EMAIL_HOST_USER