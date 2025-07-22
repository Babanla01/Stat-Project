from django.urls import path
from . import views

urlpatterns = [
    path('', views.stats_home, name='stats_home'),
]
# This file defines the URL patterns for the statsweb application.
#     {
#         "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
#     },
# ]
#
# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/
# LANGUAGE_CODE = "en-us"
# TIME_ZONE = "UTC"
# USE_I18N = True
# USE_L10N = True
# USE_TZ = True
# This file defines the URL patterns for the statsweb application.
# It maps the root URL to the `stats_home` view function.
#
# The `urlpatterns` list routes URLs to views. For more information please see:
# https://docs.djangoproject.com/en/5.2/topics/http/urls/
#
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# The `urlpatterns` list routes URLs to views. For more information please see:
# https://docs.djangoproject.com/en/5.2/topics/http/urls/
#
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# The `urlpatterns` list routes URLs to views. For more information please see:
# https://docs.djangoproject.com/en/5.2/topics/http/urls/
# Examples:
# Function views