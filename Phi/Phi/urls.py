import captcha.urls

from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', 'services.views.home'),
    url(r'^FAQ/$', 'services.views.answer'),
    url(r'^login/$', 'users.views.our_login'),
    url(r'^register/$', 'users.views.register'),
    url(r'^members/(?P<username>[\w|\d|_|@|+|.|-]+)/', include([
    	url(r'^$', 'services.views.get_user_profile'),
		url(r'^edit/$', 'services.views.edit_user_profile'),
		url(r'^follow_unfollow/$', 'services.views.follow_unfollow'),
		url(r'^following/$', 'services.views.get_followees'),
		url(r'^followers/$', 'services.views.get_followers'),
	])),
	url(r'^posts/(?P<post_id>[\d]+)/', include([
			url(r'^$', 'services.views.get_single_post'),
			url(r'^like_unlike/$', 'services.views.like_unlike'),
			url(r'^comment/$', 'services.views.comment'),
	])),
    url(r'^movies/(?P<movie_id>[\d]+)/', include([
    	url(r'^$', 'services.views.get_movie_profile'),
    	url(r'^rate_post/$', 'services.views.rate_post'),
    ])),
    url(r'^search/$', 'services.views.search'),
    url(r'^logout/$', 'users.views.our_logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include(captcha.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)