from rest_framework import viewsets

from apps.materials.models import Course
from apps.materials.pagination import MaterialsPagination
from apps.materials.serializers.course import CourseSerializer
from apps.materials.tasks import mailing_about_updates
from core.permissions import IsModerator, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = MaterialsPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [~IsModerator]
        elif self.action in ['retrieve', 'update', 'list']:
            self.permission_classes = [IsModerator | IsOwner]
        elif self.action == 'destroy':
            self.permission_classes = [IsOwner]
        return [permission() for permission in self.permission_classes]

    def perform_update(self, serializer):
        course = serializer.save()
        mailing_about_updates.delay(course.pk)
