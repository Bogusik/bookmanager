from rest_framework import viewsets
from .serializer import BookSerializer
from .permissions import IsOwnerAndAuthenticated


class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [
        IsOwnerAndAuthenticated
    ]

    def get_queryset(self):
        return self.request.user.books.all()
