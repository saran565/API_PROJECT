import jwt
from demoproject import settings
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework_jwt.utils import jwt_payload_handler
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json
@csrf_exempt
@api_view(['GET'])
def authenticate_user(request):


        # user1 = User.objects.create_user("john1", email, password)
        # print(user1)
        username= request.GET.get("username")
        try:
            user = User.objects.get(username=username)
            print(user)
            if user:
                # try:
                    payload = jwt_payload_handler(user)
                    token = jwt.encode(payload, settings.SECRET_KEY)
                    print()
                    user_details = {}
                    # user_details['name'] = "%s %s" % (
                    #     user.first_name, user.last_name)
                    user_details['token'] = str(token)
                    print(user_details)
                    # user_logged_in.send(sender=user.__class__,
                    #                     request=request, user=user)
                    return HttpResponse(json.dumps(user_details),content_type="application/json")
                # except Exception as e:
                #     raise e
        except:
            res = {
                'error': 'can not authenticate with the given credentials or the account has been deactivated'}
            return HttpResponse(json.dumps(res),content_type="application/json")
@csrf_exempt
@api_view(['GET'])
def get_employeedata(request):
    employee_data={
        "Name":"Santhosh",
        "Code":"EMP001",
        "Status":"Active",
        "Department":"Developing"

    }
    return HttpResponse(json.dumps(employee_data), content_type="application/json")