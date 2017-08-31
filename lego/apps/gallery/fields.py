from rest_framework import fields

from lego.apps.permissions.constants import EDIT


class PictureListField(fields.Field):
    """
    List pictures.
    Only users with can_edit perms on the gallery can see all pictures.
    """

    def __init__(self):
        return super().__init__(read_only=True, source='*')

    def to_representation(self, gallery):
        from .serializers import GalleryPictureSerializer
        user = self.context['request'].user

        images = gallery.pictures.all().select_related('file')
        if not user.has_perm(EDIT, gallery):
            images = images.filter(active=True)

        serializer = GalleryPictureSerializer(images, many=True)
        return serializer.data
