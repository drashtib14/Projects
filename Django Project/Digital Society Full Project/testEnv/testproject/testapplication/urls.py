"""
URL configuration for testproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,re_path
from testapplication import views

urlpatterns = [
    # path('aboutUs/', views.about, name='about'),
    # path('contactUs/', views.contact, name='contact'),
    # path('profile/',views.profile,name='profile')

    # chairman application
    path("index", views.index, name="index"),
    path("",views.login,name="login"),
    path("profile",views.profile,name="profile"),
    path("logout",views.logout,name="logout"),
    path("change-password",views.change_password,name="change-password"),
    path("update-profile",views.update_profile,name="update-profile"),
    path("add-member",views.add_member,name="add-member"),
    path("all-members",views.all_members,name="all_members"),
    path("add-notice",views.add_notice,name="add-notice"),
    path("view-notice",views.view_notice,name="view-notice"),
    path("del-notice/<int:pk>",views.del_notice,name="del-notice"),
    path("edit-notice/<int:pk>",views.edit_notice,name="edit-notice"),
    path("update-notice",views.update_notice,name="update-notice"),
    path("forgot-password",views.forgot_password,name="forgot-password"),
    path("reset-password",views.reset_password,name="reset-password"),
    path("add-event",views.add_event,name="add-event"),
    path("view-event",views.view_event,name="view-event"),
    path("all-complaints",views.view_complaints,name="all-complaints"),

    # member application
    path("member-index",views.member_index,name="member-index"),
    path("add-complaint",views.add_complaints,name="add-complaint"),
    # re_path(r'^.*$', views.notfound, name='notfound')
]