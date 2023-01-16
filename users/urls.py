from rest_framework.routers import DefaultRouter
from . views import UserViewSet, ProfileViewSet
from post.views import PostViewSet
from vote.views import VoteViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'profiles', ProfileViewSet)
router.register(r'Posts', PostViewSet)
router.register(r'Votes', VoteViewSet)






urlpatterns = router.urls
