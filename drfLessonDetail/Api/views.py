import os
import zipfile
from datetime import date

from django.conf import settings
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from Api import models as Api_models
from Api import serializers as Api_serializers

from .models import (
    BookInfo,
    BookName,
    Bookseller,
    Bookstore,
    Log,
    PictureTime,
    Place,
    PrintingManager,
    PrintingManufacturer,
    PublishingHouse,
    PublishingHouseManager,
    Signature,
    Stamp,
    Task5,
    Task7,
)
from .serializers import (
    BookInfoSerializer,
    BookNameSerializer,
    BooksellerSerializer,
    BookstoreSerializer,
    PictureTimeSerializer,
    PlaceSerializer,
    PrintingManagerSerializer,
    PrintingManufacturerSerializer,
    PublishingHouseManagerSerializer,
    PublishingHouseSerializer,
    SignatureSerializer,
    StampSerializer,
    Task5Serializer,
    Task7Serializer,
)


class BookstoreViewSet(viewsets.ModelViewSet):
    # queryset = Api_models.Bookstore.objects.all()
    queryset = Bookstore.objects.all()
    # serializer_class = Api_serializers.BookstoreSerializer
    serializer_class = BookstoreSerializer


class BookNameViewSet(viewsets.ModelViewSet):
    # queryset = Api_models.BookName.objects.all()
    queryset = BookName.objects.all()
    # serializer_class = Api_serializers.BookNameSerializer
    serializer_class = BookNameSerializer


class BooksellerViewSet(viewsets.ModelViewSet):
    # queryset = Api_models.Bookseller.objects.all()
    queryset = Bookseller.objects.all()
    # serializer_class = Api_serializers.BooksellerSerializer
    serializer_class = BooksellerSerializer


class PictureTimeViewSet(viewsets.ModelViewSet):
    # queryset = Api_models.PictureTime.objects.all()
    queryset = PictureTime.objects.all()
    # serializer_class = Api_serializers.PictureTimeSerializer
    serializer_class = PictureTimeSerializer


class Task5ViewSet(viewsets.ModelViewSet):
    # queryset = Api_models.Task5.objects.all()
    queryset = Task5.objects.all()
    # serializer_class = Api_serializers.Task5Serializer
    serializer_class = Task5Serializer


class PlaceViewSet(viewsets.ModelViewSet):
    # queryset = Api_models.Place.objects.all()
    queryset = Place.objects.all()
    # serializer_class = Api_serializers.PlaceSerializer
    serializer_class = PlaceSerializer


class PrintingManufacturerViewSet(viewsets.ModelViewSet):
    # queryset = Api_models.PrintingManufacturer.objects.all()
    queryset = PrintingManufacturer.objects.all()
    # serializer_class = Api_serializers.PrintingManufacturerSerializer
    serializer_class = PrintingManufacturerSerializer


class PrintingManagerViewSet(viewsets.ModelViewSet):
    # queryset = Api_models.PrintingManufacturer.objects.all()
    queryset = PrintingManufacturer.objects.all()
    # serializer_class = Api_serializers.PrintingManufacturerSerializer
    serializer_class = PrintingManufacturerSerializer


class PublishingHouseViewSet(viewsets.ModelViewSet):
    # queryset = Api_models.PublishingHouse.objects.all()
    queryset = PublishingHouse.objects.all()
    # serializer_class = Api_serializers.PublishingHouseSerializer
    serializer_class = PublishingHouseSerializer


class PublishingHouseManagerViewSet(viewsets.ModelViewSet):
    # queryset = Api_models.PublishingHouseManager.objects.all()
    queryset = PublishingHouseManager.objects.all()
    # serializer_class = Api_serializers.PublishingHouseManagerSerializer
    serializer_class = PublishingHouseManagerSerializer


class Task7ViewSet(viewsets.ModelViewSet):
    # queryset = Api_models.Task7.objects.all()
    queryset = Task7.objects.all()
    # serializer_class = Api_serializers.Task7Serializer
    serializer_class = Task7Serializer


class SignatureViewSet(viewsets.ModelViewSet):
    # queryset = Api_models.Signature.objects.all()
    queryset = Signature.objects.all()
    # serializer_class = Api_serializers.SignatureSerializer
    serializer_class = SignatureSerializer


class StampViewSet(viewsets.ModelViewSet):
    # queryset = Api_models.Stamp.objects.all()
    queryset = Stamp.objects.all()
    # serializer_class = Api_serializers.StampSerializer
    serializer_class = StampSerializer


class BookInfoViewSet(viewsets.ModelViewSet):
    # queryset = Api_models.BookInfo.objects.all()
    queryset = BookInfo.objects.all()
    # serializer_class = Api_serializers.BookInfoSerializer
    serializer_class = BookInfoSerializer
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        # 解壓縮前端上傳的 6 種 ZIP 檔案
        for file_type in [
            "picture_time_all",
            "task_8",
            "signature_saler",
            "signature_manager",
            "signature_owener",
            "stamp",
        ]:
            uploaded_file = request.FILES.get(file_type)
            if uploaded_file:
                try:
                    with zipfile.ZipFile(uploaded_file, "r") as zip_ref:
                        # 創建解壓縮目錄
                        extract_dir = os.path.join(settings.MEDIA_ROOT, file_type)
                        os.makedirs(extract_dir, exist_ok=True)

                        # 解壓縮到指定目錄
                        zip_ref.extractall(extract_dir)
                except Exception as e:
                    # 處理解壓縮錯誤
                    print(f"Error extracting {file_type} ZIP file: {e}")
            bookInfo_serializer = self.serializer_class(data=request.data)
            bookInfo_serializer.is_valid(raise_exception=True)
            task = bookInfo_serializer.save()
            # Api_models.Log.objects.create(action=1, task=task)
            Log.objects.create(action=1, task=task)
            return Response(bookInfo_serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        # queryset = Api_models.BookInfo.objects.all()
        queryset = BookInfo.objects.all()
        # 過濾出建立時間早於指定時間的任務
        #    queryset = self.get_queryset().filter(toolbox_6_time__lt=date(2024, 5, 8))
        # 過濾出建立時間晚於指定時間的任務
        # queryset = self.get_queryset().filter(toolbox_6_time__gt=date(2024, 5, 3))
        # # 過濾指定時間的任務
        #    queryset = self.get_queryset().filter(toolbox_6_time__range=(date(2024, 5, 3),date(2024, 5, 9)))

        # serializer = Api_serializers.BookInfoSerializer(queryset, many=True)
        serializer = BookInfoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        task = self.get_object()
        # task_serializer = Api_serializers.BookInfoSerializer(task)
        task_serializer = BookInfoSerializer(task)
        # Api_models.Log.create_log(action=4, task=task)
        Log.create_log(action=4, task=task)
        return Response(task_serializer.data, status=status.HTTP_202_ACCEPTED)

    def update(self, request, pk, *args, **kwargs):
        # bookInfo_objects = Api_serializers.BookInfoSerializer.objects.get(
        #     pk=self.kwargs["pk"]
        # )
        bookInfo_objects = BookInfoSerializer.objects.get(pk=self.kwargs["pk"])
        bookInfo_serializer = self.get_serializer(
            bookInfo_objects, data=request.data, partial=True
        )  # set partial=True to update a data partially
        bookInfo_serializer.is_valid(raise_exception=True)
        task = bookInfo_serializer.save()
        # Api_models.Log.objects.create(action=3, task=task)
        Log.objects.create(action=3, task=task)
        return Response(bookInfo_serializer.data, status=status.HTTP_205_RESET_CONTENT)

    def destroy(self, request, *args, **kwargs):
        task = self.get_object()
        # Api_models.Log.create_log(action=2, task=task)
        Log.create_log(action=2, task=task)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
