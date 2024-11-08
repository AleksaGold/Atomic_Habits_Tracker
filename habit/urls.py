
from rest_framework.routers import DefaultRouter

from habit.apps import HabitConfig
from habit.views import ConditionViewSet, RewardViewSet, HabitViewSet

app_name = HabitConfig.name

router = DefaultRouter()
router.register(r"conditions", ConditionViewSet, basename="conditions")
router.register(r"rewards", RewardViewSet, basename="rewards")
router.register(r"habits", HabitViewSet, basename="habits")

urlpatterns = []

urlpatterns += router.urls
