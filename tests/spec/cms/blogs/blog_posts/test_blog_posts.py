from hubspot import HubSpot
from hubspot.cms.blogs.blog_posts import BlogPostApi


def test_is_discoverable():
    apis = HubSpot().cms.blogs.blog_posts
    assert isinstance(apis.blog_post_api, BlogPostApi)
