from django.urls import path
from . import views

urlpatterns = [
    # مسارات الصفحات الرئيسية
    path('', views.dashboard, name='dashboard'),
    
    path('circles/', views.circle_list, name='circle_list'),
    path('circles/<int:circle_id>/', views.circle_detail, name='circle_detail'),
    path('circle_update/<int:id>', views.circle_update, name='circle_update'),
    path('circle_delete/<int:id>', views.circle_delete, name='circle_delete'),
    path('create_circle/', views.create_circle, name='create_circle'),
    
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/<int:teacher_id>/', views.teacher_detail, name='teacher_detail'),
    path('teacher_update/<int:id>', views.teacher_update, name='teacher_update'),
    path('teacher_delete/<int:id>', views.teacher_delete, name='teacher_delete'),
    path('create_teacher/', views.create_teacher, name='create_teacher'),
    
    path('students/', views.student_list, name='student_list'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('create_student/', views.create_student, name='create_student'),
    
    path('tests/', views.test_list, name='test_list'),
    path('tests/<int:test_id>/', views.test_detail, name='test_detail'),
    path('test_update/<int:id>', views.test_update, name='test_update'),
    path('test_delete/<int:id>', views.test_delete, name='test_delete'),
    path('create_test/', views.create_test, name='create_test'),
    
    path('daily_saving/', views.daily_saving_list, name='daily_saving_list'),
    # path('tests/<int:test_id>/', views.test_detail, name='test_detail'),
    path('daily_saving/update/<int:id>/', views.update_daily_saving, name='daily_saving_update'),
    path('daily_saving_delete/<int:id>', views.daily_saving_delete, name='daily_saving_delete'),
    path('create_daily_saving/', views.create_daily_saving, name='create_daily_saving'),
    
    
    # path('achievements/', views.achievement_list, name='achievement_list'),
    # path('achievements/<int:achievement_id>/', views.achievement_detail, name='achievement_detail'),
    # path('recitations/', views.recitation_list, name='recitation_list'),
    # path('recitations/<int:recitation_id>/', views.recitation_detail, name='recitation_detail'),
    # path('honor_roll/', views.honor_roll, name='honor_roll'),


    # مسارات إضافة سجلات جديدة




    # path('create_achievement/', views.create_achievement, name='create_achievement'),
    # path('create_recitation/', views.create_recitation, name='create_recitation'),
    
]
