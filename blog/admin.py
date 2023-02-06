from django.contrib import admin
from .models import Post # blog폴더 안의 models.py에서 정의한 Post 모델을 가져온다.

admin.site.register(Post) # 관리자 페이지에서 만든 모델을 보려면 register해야한다.