from django.conf.urls import patterns, url

urlpatterns = patterns('web.views',
    url(r'^upload/form$', 'web_upload_public_form'),
    url(r'^upload/submit$', 'web_upload_public_submit', name='upload_public')
)