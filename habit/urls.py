from rest_framework.routers import DefaultRouter

from habit.apps import HabitConfig
from habit.views import (ConditionViewSet, HabitReadOnlyViewSet, HabitViewSet,
                         RewardReadOnlyViewSet, RewardViewSet)

app_name = HabitConfig.name

router = DefaultRouter()
router.register(r"conditions", ConditionViewSet, basename="conditions")
router.register(r"rewards", RewardViewSet, basename="rewards")
router.register(r"public_rewards", RewardReadOnlyViewSet, basename="public_rewards")
router.register(r"habits", HabitViewSet, basename="habits")
router.register(r"public_habits", HabitReadOnlyViewSet, basename="public_habits")

urlpatterns = []

urlpatterns += router.urls
