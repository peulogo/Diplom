from .models import Entry

def entries_count(request):
    if request.user.is_authenticated:
        count = Entry.objects.filter(user=request.user).count()
        return {'entries_count': count}
    return {'entries_count': 0}