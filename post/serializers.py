from rest_framework import serializers
from. models import Post
from vote.models import Vote
from vote.serializers import VoteSerializer

class PostSerializer(serializers.ModelSerializer):
    votes = serializers.ReadOnlyField(source='post.value')
    posted_by = serializers.ReadOnlyField(source = 'owner.username')
    votes = VoteSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ('posted_by','post_image', 'content', 'post_date','votes')
