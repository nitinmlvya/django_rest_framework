from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from get_started.models import User
from get_started.serializers import UserSerializer

# CSRF token is used to verify that request and response come from the same location. Verify that request is not
# a malicicous attack.
@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        # Get all the get_started objects
        users = User.objects.all()
        # serializer the list of get_started object. Pass "many=True" if type of objects is a list.
        serializer = UserSerializer(users, many=True)
        # use ".data" to get the serialized data.
        # In order to allow non-dict objects to be serialized set the safe parameter to False. Here,
        # serializer.data is a list.
        return JsonResponse(serializer.data, safe=False, status=200)

    elif request.method == 'POST':
        # "JSONParser()" is used to parse the json request into the object format.
        data = JSONParser().parse(request)
        # Serialize the "data" by passing into "data" attribute.
        serializer = UserSerializer(data=data)
        # Mandatory to validate the serialized data beforing saving the object.
        if serializer.is_valid():
            # To save the object using serializer into the database.
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        # use ".errors" to know the type of errors while calling the serializer.
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
# "pk" is the primary key which is received through the URL.
def user_detail(request, pk):
    if request.method == 'GET':
        try:
            user = User.objects.get(pk=pk)
        # "User.DoesNotExist" is the exception which is called when the given primary key ID user does not
        # exist in the table.
        except User.DoesNotExist:
            return HttpResponse(status=404)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, status=200)

    elif request.method == 'PUT':
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return HttpResponse(status=404)
        data = JSONParser().parse(request)
        # Serialize the "data" by passing into "data" attribute and pass the "user" object. So that the data get
        # serialized over the existing/given user. Allow "partial=True" to update only specify fields in the request
        # body even some fields of the model are mandatory to update.
        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return HttpResponse(status=404)
        # Delete the selected "user".
        user.delete()
        return HttpResponse(status=204)
