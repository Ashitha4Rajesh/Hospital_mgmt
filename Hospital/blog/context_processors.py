from blog.models import post
def category_links(request):
    c = post.objects.all()
    return {'links':c}