import os
import zipfile
from datetime import date

from Api import models as Api_models
from Api import serializers as Api_serializers
from django.conf import settings
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response


class BookstoreViewSet(viewsets.ModelViewSet):
    queryset = Api_models.Bookstore.objects.all()
    serializer_class = Api_serializers.BookstoreSerializer


class BookNameViewSet(viewsets.ModelViewSet):
    queryset = Api_models.BookName.objects.all()
    serializer_class = Api_serializers.BookNameSerializer


class BooksellerViewSet(viewsets.ModelViewSet):
    queryset = Api_models.Bookseller.objects.all()
    serializer_class = Api_serializers.BooksellerSerializer


class PictureTimeViewSet(viewsets.ModelViewSet):
    queryset = Api_models.PictureTime.objects.all()
    serializer_class = Api_serializers.PictureTimeSerializer


class Task5ViewSet(viewsets.ModelViewSet):
    queryset = Api_models.Task5.objects.all()
    serializer_class = Api_serializers.Task5Serializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Api_models.Place.objects.all()
    serializer_class = Api_serializers.PlaceSerializer


class PrintingManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Api_models.PrintingManufacturer.objects.all()
    serializer_class = Api_serializers.PrintingManufacturerSerializer


class PrintingManagerViewSet(viewsets.ModelViewSet):
    queryset = Api_models.PrintingManufacturer.objects.all()
    serializer_class = Api_serializers.PrintingManufacturerSerializer


class PublishingHouseViewSet(viewsets.ModelViewSet):
    queryset = Api_models.PublishingHouse.objects.all()
    serializer_class = Api_serializers.PublishingHouseSerializer


class PublishingHouseManagerViewSet(viewsets.ModelViewSet):
    queryset = Api_models.PublishingHouseManager.objects.all()
    serializer_class = Api_serializers.PublishingHouseManagerSerializer


class Task7ViewSet(viewsets.ModelViewSet):
    queryset = Api_models.Task7.objects.all()
    serializer_class = Api_serializers.Task7Serializer


class SignatureViewSet(viewsets.ModelViewSet):
    queryset = Api_models.Signature.objects.all()
    serializer_class = Api_serializers.SignatureSerializer


class StampViewSet(viewsets.ModelViewSet):
    queryset = Api_models.Stamp.objects.all()
    serializer_class = Api_serializers.StampSerializer


class BookInfoViewSet(viewsets.ModelViewSet):
    queryset = Api_models.BookInfo.objects.all()
    serializer_class = Api_serializers.BookInfoSerializer
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
            Api_models.Log.objects.create(action=1, task=task)
            return Response(bookInfo_serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        # 過濾出建立時間早於指定時間的任務
        #    queryset = self.get_queryset().filter(toolbox_6_time__lt=date(2024, 5, 8))
        # 過濾出建立時間晚於指定時間的任務
        queryset = self.get_queryset().filter(toolbox_6_time__gt=date(2024, 5, 3))
        # # 過濾指定時間的任務
        #    queryset = self.get_queryset().filter(toolbox_6_time__range=(date(2024, 5, 3),date(2024, 5, 9)))

        serializer = Api_serializers.BookInfoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        task = self.get_object()
        task_serializer = Api_serializers.BookInfoSerializer(task)
        Api_models.Log.create_log(action=4, task=task)
        return Response(task_serializer.data, status=status.HTTP_202_ACCEPTED)

    def update(self, request, pk, *args, **kwargs):
        bookInfo_objects = Api_serializers.BookInfoSerializer.objects.get(
            pk=self.kwargs["pk"]
        )
        bookInfo_serializer = self.get_serializer(
            bookInfo_objects, data=request.data, partial=True
        )  # set partial=True to update a data partially
        bookInfo_serializer.is_valid(raise_exception=True)
        task = bookInfo_serializer.save()
        Api_models.Log.objects.create(action=3, task=task)
        return Response(bookInfo_serializer.data, status=status.HTTP_205_RESET_CONTENT)

    def destroy(self, request, *args, **kwargs):
        task = self.get_object()
        Api_models.Log.create_log(action=2, task=task)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
