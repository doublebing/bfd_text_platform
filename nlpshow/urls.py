# coding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from nlpshow import views

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'nlpdemo.views.index', name='index'),
                       url(r'^show/', 'nlpdemo.views.show'),
                       url(r'^test/', 'nlpdemo.views.test'),

                       url(r'^developer/', 'nlpdemo.views.developer'),
                       url(r'^keywords', 'nlpdemo.views.keywords'),
                       url(r'^auto_summary', 'nlpdemo.views.auto_summary'),
                       url(r'^media_label', 'nlpdemo.label.media_label'),
                        url(r'^item_label', 'nlpdemo.label.item_label'),
                       url(r'^sentiment_weibo', 'nlpdemo.sentiment.sentiment_weibo'),
                       url(r'^sentiment_auto', 'nlpdemo.sentiment.sentiment_auto'),
                       url(r'^sentiment_news', 'nlpdemo.sentiment.sentiment_news'),
                       url(r'^sentiment_finance', 'nlpdemo.sentiment.sentiment_finance'),
                       url(r'^reputation', 'nlpdemo.reputation.reputation'),
                       # 微博抓取
                       url(r'^crawle_weibo', 'nlpdemo.views.crawle_weibo'),
                       url(r'^crawle_media', 'nlpdemo.label.crawle_news'),

                       url(r'^admin/', include(admin.site.urls)),
                        url(r'^login/$', 'account.views.login'),
                        url(r'^logout/$', 'account.views.logout'),

                        url(r'^register/$', 'account.views.register'),
                        url(r'^password/$','account.views.find_password'),
                        url(r'^user/tel$','account.views.update_tel'),
                        url(r'^user/$','account.views.show_user'),
                        url(r'^user/detail/$','account.views.show_detail'),
                        url(r'^test', 'nlpdemo.views.testapi')

                       )
