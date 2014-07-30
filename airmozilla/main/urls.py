from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView
from django.views.decorators.cache import cache_page

from . import views


urlpatterns = patterns(
    '',
    url(r'^__debugger__', views.debugger__),
    url(r'^$', views.home, name='home'),
    url(r'^channels/(?P<channel_slug>[-\w]+)/$', views.home,
        name='home_channels'),
    url(r'^page/1/$', RedirectView.as_view(url='/'), name='first_page'),
    url(r'^page/(?P<page>\d+)/$', views.home, name='home'),
    url(r'^channels/(?P<channel_slug>[-\w]+)/page/(?P<page>\d+)/$',
        views.home, name='home_channels'),
    url(r'^channels/$', views.channels, name='channels'),
    url(r'^presenter/(?P<slug>[-\w]+)/$', views.participant,
        name='participant'),
    url(r'^presenter-clear/(?P<clear_token>[-\w]+)/$', views.participant_clear,
        name='participant_clear'),
    url(r'^login/$', views.page, name='login',
        kwargs={'template': 'main/login.html'}),
    url(r'^login-failure/$', views.page, name='login_failure',
        kwargs={'template': 'main/login_failure.html'}),
    url(r'^calendar/$', views.calendar, name='calendar'),
    url(r'^calendar/data.json$', views.calendar_data, name='calendar_data'),
    url(r'^calendars/$', views.calendars, name='calendars'),
    url(r'^calendar/(company|contributors|public).ics$',
        views.events_calendar_ical, name='calendar_ical'),
    url(r'^feed/(?P<private_or_public>'
        'company|public|private|contributors)?/?$',
        cache_page(60 * 60)(views.EventsFeed()),
        name='feed'),
    url(r'^feed/(?P<private_or_public>company|public|private|contributors)'
        r'/(?P<format_type>webm)/?$',
        cache_page(60 * 60)(views.EventsFeed()),
        name='feed_format_type'),
    url(r'^feed/(?P<channel_slug>[-\w]+)/$',
        cache_page(60 * 60)(views.EventsFeed()),
        name='channel_feed_default'),
    url(r'^feed/(?P<channel_slug>[-\w]+)/'
        r'(?P<private_or_public>company|public|private|contributors)/?$',
        cache_page(60 * 60)(views.EventsFeed()),
        name='channel_feed'),
    url(r'^feed/(?P<channel_slug>[-\w]+)/'
        r'(?P<private_or_public>company|public|private|contributors)/'
        r'(?P<format_type>webm)/?$',
        cache_page(60 * 60)(views.EventsFeed()),
        name='channel_feed_format_type'),
    url(r'^tagcloud/$', views.tag_cloud, name='tag_cloud'),
    url(r'^all-tags/$', views.all_tags, name='all_tags'),
    url(r'^(?P<slug>[-\w]+)/$', views.EventView.as_view(),
        name='event'),
    url(r'^(?P<slug>[-\w]+)/video/$', views.EventVideoView.as_view(),
        name='event_video'),
    url(r'^(?P<slug>[-\w]+)/permission-denied/$', views.permission_denied,
        name='permission_denied'),
    url(r'^(?P<slug>[-\w]+)/edit/$', views.EventEditView.as_view(),
        name='event_edit'),
    url(r'^(?P<slug>[-\w]+)/(?P<id>\d+)/change/$',
        views.EventRevisionView.as_view(),
        name='event_change'),
    url(r'^(?P<slug>[-\w]+)/(?P<id>\d+)/difference/$',
        views.EventRevisionView.as_view(difference=True),
        name='event_difference'),
    url(r'^edgecast.smil$',
        views.edgecast_smil,
        name='edgecast_smil'),




)
