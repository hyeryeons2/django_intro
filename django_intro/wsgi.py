"""
WSGI config for django_intro project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

# Web Server Gateway Interface(구축한 환경을 배포할 때 사용함)
# 배포에 필요한 파일이기 때문에 지금은 사용할 필요가 없음
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_intro.settings')

application = get_wsgi_application()
