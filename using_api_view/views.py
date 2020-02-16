from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from using_api_view.models import CategoryAV, SubCategoryAV, VendorAV, DeliveryAV, Member, Group, Membership
from using_api_view.serializers import CategoryAVSerializer, SubCategoryAVSerializer, VendorAVSerializer, \
    DeliveryAVSerializer, MemberSerializer, GroupSerializer, GroupMemberSerializer


@api_view(['GET', 'POST'])
def catgory_av_list(request):
    if request.method == 'GET':
        category_av = CategoryAV.objects.all()
        category_av_serializer = CategoryAVSerializer(category_av, many=True)
        return Response(category_av_serializer.data)

    elif request.method == 'POST':
        category_av_serializer = CategoryAVSerializer(data=request.data)
        if category_av_serializer.is_valid():
            category_av_serializer.save()
            return Response(category_av_serializer.data, status=status.HTTP_201_CREATED)
        return Response(category_av_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def catgory_av_detail(request, pk):
    try:
        category_av = CategoryAV.objects.get(pk=pk)
    except CategoryAV.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        category_av_serializer = CategoryAVSerializer(category_av)
        return Response(category_av_serializer.data)

    elif request.method == 'PUT':
        category_av_serializer = CategoryAVSerializer(category_av, data=request.data)
        if category_av_serializer.is_valid():
            category_av_serializer.save()
            return Response(category_av_serializer.data)
        return Response(category_av_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category_av.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# For Sub Category


@api_view(['GET', 'POST'])
def sub_category_av_list(request):
    if request.method == 'GET':
        sub_category_av = SubCategoryAV.objects.all()
        sub_category_av_serializer = SubCategoryAVSerializer(sub_category_av, many=True)
        return Response(sub_category_av_serializer.data)

    elif request.method == 'POST':
        sub_category_av_serializer = SubCategoryAVSerializer(data=request.data)
        if sub_category_av_serializer.is_valid():
            sub_category_av_serializer.save()
            return Response(sub_category_av_serializer.data, status=status.HTTP_201_CREATED)
        return Response(sub_category_av_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def sub_category_av_detail(request, pk):
    try:
        sub_category_av = SubCategoryAV.objects.get(pk=pk)
    except SubCategoryAV.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        sub_category_av_serializer = SubCategoryAVSerializer(sub_category_av)
        return Response(sub_category_av_serializer.data)

    elif request.method == 'PUT':
        sub_category_av_serializer = SubCategoryAVSerializer(sub_category_av, data=request.data)
        if sub_category_av_serializer.is_valid():
            sub_category_av_serializer.save()
            return Response(sub_category_av_serializer.data)
        return Response(sub_category_av_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        sub_category_av.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# For Vendors
@api_view(['GET', 'POST'])
def vendor_av_list(request):
    if request.method == 'GET':
        vendor_av = VendorAV.objects.all()
        vendor_av_serializer = VendorAVSerializer(vendor_av, many=True)
        return Response(vendor_av_serializer.data)

    elif request.method == 'POST':
        vendor_av_serializer = VendorAVSerializer(data=request.data)
        if vendor_av_serializer.is_valid():
            vendor_av_serializer.save()
            return Response(vendor_av_serializer.data, status=status.HTTP_201_CREATED)
        return Response(vendor_av_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# For Delivery
@api_view(['GET', 'POST'])
def delivery_av_list(request):
    if request.method == 'GET':
        delivery_av = DeliveryAV.objects.all()
        delivery_av_serializer = DeliveryAVSerializer(delivery_av, many=True)
        return Response(delivery_av_serializer.data)

    elif request.method == 'POST':
        delivery_av_serializer = DeliveryAVSerializer(data=request.data)
        if delivery_av_serializer.is_valid():
            delivery_av_serializer.save()
            return Response(delivery_av_serializer.data, status=status.HTTP_201_CREATED)
        return Response(delivery_av_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
Many to Many View set
"""

class MemberViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet is a class that provides the functionality of a set of views which are closely related.
    It’s one class but provides a set of views and methods such as list, create, retreive, update,
    and destory and also ask for the serializer class and the queryset.
    """
    queryset = Member.objects.all()
    """
    queryset basically a collection of (sql) queries and will show you
    the sql query generated from your django filter calls.
    """
    serializer_class = MemberSerializer
    """
    The serializer class that should be used for validating and
    deserializing input, and for serializing output.
    """

    def get_queryset(self):
        """
        Returns the queryset that will be used to retrieve the object
        that this view will display. By default, get_queryset()
        returns the value of the queryset attribute
        """
        print('Executing get_queryset...')
        return self.queryset.all() # OR Member.objects.all()

    def filter_queryset(self, queryset):
        """
        Given a queryset, filter it with whichever filter backends are in use,
        returning a new queryset.

        queryset parameter contains the value returned from the
        self.get_queryset() or from queryset class variable
        """
        print('Executing filter_queryset...')
        if 'alias_name' in self.request.query_params:
            alias_name = self.request.query_params.get('alias_name')
            return queryset.filter(alias_name=alias_name) # OR Member.objects.filter(alias_name=alias_name)
        return queryset.all() # OR queryset

    def get_object(self):
        """
        get_object works for single instance of the model.
        """
        print("Executing get_object...")
        queryset = self.get_queryset()
        obj = queryset.get(pk=self.kwargs['pk'])
        return obj

    def list(self, request):
        """
        list is used for "get" request method and supersede get_queryset() and get_filterqueryset()
        """
        print('Executing list...')
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Overrides the get_object()
        """
        print("Executing retrieve...")
        member = Member.objects.get(pk=pk)
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    def update(self, request, pk=None):
        member = Member.objects.get(pk=pk)
        serializer = MemberSerializer(member, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        print("Executing delete...")
        Member.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    """
    '^' Starts-with search.
    '=' Exact matches.
    '@' Full-text search. (Currently only supported Django's MySQL backend.)
    '$' Regex search.
    """
    ordering_fields = ['name']
    """
    Ordering is supported on all the fields by default. If you want to restrict ordering to only specific 
    fields. Put in the ordering_fields. 
    ?ordering=name ==> Ascending order
    ?ordering=-name ==> Descending order
    """

class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = GroupMemberSerializer


"""
Class based API View
"""

class MemberListAPIView(APIView):

    def get(self, request):
        print('Executing APIView get list...')
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)

    def post(self, request):
        print('Executing APIView post ...')
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

class MemberDetailAPIView(APIView):

    def get(self, request, pk):
        print("Executing APIView get object...")
        member = Member.objects.get(pk=pk)
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    def put(self, request, pk):
        print("Executing APIView put object...")
        member = Member.objects.get(pk=pk)
        serializer = MemberSerializer(member, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        print("Executing APIView delete...")
        Member.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
Using Mixins
"""
class MemberListCreateMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    List of available mixins:
    ListModelMixin: provides a .list() method to the view/viewset
    RetrieveModelMixin: provides a .retrieve() method to the view/viewset
    CreateModelMixin: provides a .create() method to the view/viewset
    UpdateModelMixin: provides a .update() method to the view/viewset
    DestroyModelMixin: provides a .destroy() method to the view/viewset
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def list(self, request, *args, **kwargs):
        print("Mixins list...")
        members = self.get_queryset()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


"""
Using Generic Views
"""
class MemberListCreateView(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = MemberSerializer(queryset, many=True)
        return Response(serializer.data)


"""
ListCreateAPIView:
Used for read-write endpoints to represent a collection of model instances.
Provides get and post method handlers.
Extends: GenericAPIView, ListModelMixin, CreateModelMixin


RetrieveUpdateDestroyAPIView:
Provides get, put, patch and delete method handlers.
Extends: GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


GenericViewSet:
The GenericViewSet class inherits from GenericAPIView, and provides the default set of 
get_object, get_queryset methods and other generic view base behavior, but does not 
include any actions by default.


ModelViewSet:
The ModelViewSet class inherits from GenericAPIView and includes implementations for 
various actions, by mixing in the behavior of the various mixin classes.
The actions provided by the ModelViewSet class are .list(), .retrieve(), .create(), 
.update(), and .destroy().
"""

"""
APIView is the base class for all API views.
This is the class we use when not dealing with internal django models. 
In most cases it is used with external APIs.


GenericAPIView is used when you want to have custom URL endpoints or hook into 
the request method (get, post, put, delete, patch) before getting into the action 
(retrieve, list, create, update, destroy). Most of the time you can use ViewSet, 
but there will be some situations where you need more flexibility.

ViewSet provides you everything you need for default actions with Django data.
 It is built off of GenericAPIView and performs default actions based off of 
 the type of method received. To add into your urls, you just need to add it into a router.
"""