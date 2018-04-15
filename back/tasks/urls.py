from rest_framework import routers
from tasks.views import TaskViewSet

router = routers.SimpleRouter()
router.register(u'tasks', TaskViewSet)

urlpatterns = router.urls
