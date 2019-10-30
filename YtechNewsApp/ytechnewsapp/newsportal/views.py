from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import News

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'newsportal/index.html'
    context_object_name = 'latest_news_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return News.objects.order_by('-date_published')[:5]


class DetailView(generic.DetailView):
    model = News
    template_name = 'newsportal/detail.html'


#This is for backend form
'''
@login_required
@transaction.atomic
def update_profile(request):
    if request.method='POST':
        user_form=UserForm(request.POST, instance=request.user)
        profile_form=ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            message.success(request, _('Your profile was successfully updated'))
            return redirect('settings:profile')
        else:
            message.error(request, _('Please correct the error below'))
    else:
        user_form=UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'profiles/profile.html',
    {
        'user_form': user_form,
        'profile_form':profile_form
    }) '''