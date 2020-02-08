from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from using_api_view.models import CategoryAV, SubCategoryAV, VendorAV, DeliveryAV
from using_api_view.serializers import CategoryAVSerializer, SubCategoryAVSerializer, VendorAVSerializer, \
    DeliveryAVSerializer


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