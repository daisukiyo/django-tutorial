"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# import the automatic admin interface
from django.contrib import admin

# include allows referencing of other URL configurations
# path returns an element for inclusion in urlpatterns
from django.urls import include, path

urlpatterns = [
    # EXAMPLE ARGUMENT: path(route, view, kwargs*, name*)
    # you should always use include() when you include other URL patterns. 
    path('polls/', include('polls.urls')),
    # admin.site.urls is the only exception to this.
    path('admin/', admin.site.urls),
]