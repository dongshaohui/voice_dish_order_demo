from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weixin_dish_order_recognition_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','voice_dish_order.views.do'),
    url(r'^admin/', include(admin.site.urls)),
)
