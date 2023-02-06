from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): # Post라는 이름의 모델을 정의한다.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 다른 모델에 대한 링크를 의미
    title = models.CharField(max_length=200) # 글자수가 max_lenght로 제한된 텍스트 정의
    text = models.TextField() # 글자 수에 제한이 없는 긴 텍스트 정의
    created_date = models.DateTimeField(
            default=timezone.now) # 날짜와 시간을 의미
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): # publish라는 이름의 메서드 정의
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
