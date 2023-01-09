from django.urls import path
from .import views
urlpatterns=[
    path('',views.set,name='set'),
    # path('detail',views.details,name='details')
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('clbased/',views.Task_list.as_view(),name='clb'),
    path('cldetail/<int:pk>/',views.Task_detail.as_view(),name='cld'),
    path('clupdate/<int:pk>/',views.Task_update.as_view(),name='clu'),
    path('cldelete/<int:pk>/',views.Taskdelete.as_view(),name='cldelete'),

]
