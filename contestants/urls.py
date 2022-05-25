from django.urls import path
from contestants.views import RegPurchView,VerifyTransaction


urlpatterns = [
    path("form-purchase/",RegPurchView.as_view()),
    path("verify/<str:ref>/",VerifyTransaction.as_view()),
]
