# board.urls.py
from django.urls import path
from . import views
urlpatterns = [
    # path('list/', views.board_list, name='board_list'), # 👈 name 지정
    # path('write/', views.board_write, name='board_write'), # 👈 name 지정
    path('detail/<int:pk>', views.board_detail), # 👈 도메인/board/detail/정수/ 로 진입
]