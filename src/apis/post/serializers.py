from rest_framework import serializers

from models.post import models


class PublicPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ('id', 'title', 'content', 'author_nickname', 'created_at', 'updated_at',
                  'most_recent_comment')

    author_nickname = serializers.SerializerMethodField()
    most_recent_comment = serializers.SerializerMethodField()

    def get_most_recent_comment(self, obj) -> str | None:
        most_recent_comments = getattr(obj, 'most_recent_comments')
        if most_recent_comments:
            return most_recent_comments[0].content
        return None

    def get_author_nickname(self, obj) -> str | None:
        return getattr(obj, 'author_nickname', None)
