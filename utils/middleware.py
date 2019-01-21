import re

from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect

from backweb.models import User


class TestMiddlware(MiddlewareMixin):

    def process_request(self, request):
        not_need_check = [
                    '/backweb/register/',
                    '/backweb/login/',
                    '/web/index/',
                    '/web/about/',
                    '/web/infopic/',
                    '/web/list/',
                    '/web/share/',
                    '/media/*'
                                        ]
        path = request.path
        for not_check in not_need_check:
            if re.match(not_check, path):
                return None
        user_id = request.session.get('user_id')
        if user_id:
            user = User.objects.get(pk=user_id)
            request.session['user_id'] = user.id
            request.user = user
            return None
        else:
            return HttpResponseRedirect(reverse('backweb:login'))

    def process_response(self, request, response):
        return response