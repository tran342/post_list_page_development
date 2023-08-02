from django.db.models import Prefetch, Subquery, OuterRef, F
from rest_framework.viewsets import ReadOnlyModelViewSet

from apis.post.serializers import PublicPostSerializer
from models.comment.models import Comment
from models.post.models import Post


class PublicPostViewSet(ReadOnlyModelViewSet):
    serializer_class = PublicPostSerializer
    queryset = Post.valid_objects.none()

    def get_queryset(self):
        # This is a sample of prefetch_related
        #
        # I think to make the query more efficient,
        # partial of content of the most recently comment should be stored into the Post
        # There will be async work to update every a new comment is created
        sub_query = Subquery(
            Comment.valid_objects.filter(post_id=OuterRef('post_id')).order_by('-id').values_list('id', flat=True)[:1]
        )

        # If the query become more complex, I think it should be moved to the DAO classes
        qs = Post.valid_objects.all().prefetch_related(
            Prefetch('post_comments', to_attr='most_recent_comments',
                     queryset=Comment.valid_objects.filter(id__in=sub_query))
        ).annotate(author_nickname=F('author__nickname')).order_by('-id')

        return qs
