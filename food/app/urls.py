from django.urls import path, include
from rest_framework import routers

from .views import FoodTypeAPIView, MeasurementAPIView, IngredientAPIView, FoodAPIView, CommentAPIView

router = routers.SimpleRouter()
router.register('food-type', FoodTypeAPIView)
router.register('measurement', MeasurementAPIView)
router.register('ingredient', IngredientAPIView)
router.register('food', FoodAPIView)
router.register('comment', CommentAPIView)


urlpatterns = [
    path('v1/', include(router.urls))
]
