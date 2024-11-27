from django.shortcuts import render
def adout(req):
     return render(req, "about.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
]

