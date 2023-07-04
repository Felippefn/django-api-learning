from django.urls import path, include
from django.contrib import admin
from car.views import hello2_world, insert_driver, add_car
from blog.views import hello1_world, post_list, post_create
from questions.views import hello3_world, create_question
from userMain.views import hello_world, create_user


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world, name='hello_world'),
    path('bye/', hello1_world, name='hello1_world'),
    path('good/', hello2_world, name='hello2_world'),
    path('bad/', hello3_world, name='hello3_world'),
    path('users/create/', create_user, name='create_user'),
    path('users/', include("userMain.urls")),
    path('blog/', post_list, name='post_list'),
    path('blog/post/', post_create, name='post_create'),
    path("cars/", include("car.urls")),
    path("cars/create/", insert_driver, name='insert_driver'),
    path("cars/create/car", add_car, name="add_car"),
    path("question/create/", create_question, name='create_question'),
]
