from Api import models as Api_models
from rest_framework import serializers


class BookstoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api_models.Bookstore
        fields = "__all__"


class BookNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api_models.BookName
        fields = "__all__"


class BooksellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api_models.Bookseller
        fields = "__all__"


class PictureTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api_models.PictureTime
        fields = "__all__"


class Task5Serializer(serializers.ModelSerializer):
    class Meta:
        model = Api_models.Task5
        fields = "__all__"


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api_models.Place
        fields = "__all__"


class PrintingManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api_models.PrintingManufacturer
        fields = "__all__"


class PrintingManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api_models.PrintingManager
        fields = "__all__"


class PublishingHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api_models.PublishingHouse
        fields = "__all__"


class PublishingHouseManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api_models.PublishingHouseManager
        fields = "__all__"


class Task7Serializer(serializers.ModelSerializer):
    class Meta:
        model = Api_models.Task7
        fields = "__all__"


class SignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api_models.Signature
        fields = "__all__"


class StampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api_models.Stamp
        fields = "__all__"


class BookInfoSerializer(serializers.ModelSerializer):
    bookName_all = BookNameSerializer()
    bookseller_all = BooksellerSerializer()
    task5 = Task5Serializer()
    task6_place = PlaceSerializer()
    task6_printingManufacturer = PrintingManufacturerSerializer()
    task6_printingManager = PrintingManagerSerializer()
    task6_publishingHouse = PublishingHouseSerializer()
    task6_publishingHouseManager = PublishingHouseManagerSerializer()

    class Meta:
        model = Api_models.BookInfo
        fields = "__all__"

    def create(self, validated_data):
        bookName_data = validated_data.pop("bookName_all")
        bookseller_data = validated_data.pop("bookseller_all")
        task_5_data = validated_data.pop("task5")
        task_6_place_data = validated_data.pop("task6_place")
        task_6_printingManufacturer_data = validated_data.pop(
            " task6_printingManufacturer"
        )
        task_6_printingManager_data = validated_data.pop("task6_printingManager")
        task_6_publishingHouse_data = validated_data.pop("task6_publishingHouse")
        task_6_publishingHouseManager_data = validated_data.pop(
            "task6_publishingHouseManager"
        )

        if bookName_data is None:
            bookName = None
        else:
            bookName = Api_models.BookName.objects.create(**bookName_data)

        if bookseller_data is None:
            bookseller = None
        else:
            bookseller = Api_models.Bookseller.objects.create(**bookseller_data)

        if task_5_data is None:
            task5 = None
        else:
            task5 = Api_models.Task5.objects.create(**task_5_data)

        if task_6_place_data is None:
            task6_place = None
        else:
            task6_place = Api_models.Place.objects.create(**task_6_place_data)

        if task_6_printingManufacturer_data is None:
            task6_printingManufacturer = None
        else:
            task6_printingManufacturer = Api_models.PrintingManufacturer.objects.create(
                **task_6_printingManufacturer_data
            )

        if task_6_printingManager_data is None:
            task6_printingManager = None
        else:
            task6_printingManager = Api_models.PrintingManager.objects.create(
                **task_6_printingManager_data
            )

        if task_6_publishingHouse_data is None:
            task6_publishingHouse = None
        else:
            task6_publishingHouse = Api_models.PublishingHouse.objects.create(
                **task_6_publishingHouse_data
            )

        bookInfo = Api_models.BookInfo.objects.create(
            bookName_all=bookName,
            bookseller_all=bookseller,
            task_5=task5,
            task_6_place=task6_place,
            task_6_printingManufacturer=task6_printingManufacturer,
            task_6_printingManager=task6_printingManager,
            task_6_publishingHouse=task6_publishingHouse,
            **validated_data
        )
        return bookInfo

    def update(self, instance, validated_data):
        bookName_data = validated_data.pop("bookName_all")
        bookseller_data = validated_data.pop("bookseller_all")
        task_5_data = validated_data.pop("task5")
        task_6_place_data = validated_data.pop("task6_place")
        task_6_printingManufacturer_data = validated_data.pop(
            " task6_printingManufacturer"
        )
        task_6_printingManager_data = validated_data.pop("task6_printingManager")
        task_6_publishingHouse_data = validated_data.pop("task6_publishingHouse")
        task_6_publishingHouseManager_data = validated_data.pop(
            "task6_publishingHouseManager"
        )

        if bookName_data:
            bookName_instance = instance.bookName_all
            bookName__serializer = BookNameSerializer(bookName_instance, bookName_data)
            bookName__serializer.is_valide(raise_exception=True)
            bookName__serializer.save()

        if bookseller_data:
            bookseller_instance = instance.bookseller_all
            bookseller_serializer = BooksellerSerializer(
                bookseller_instance, bookseller_data
            )
            bookseller_serializer.is_valide(raise_exception=True)
            bookseller_serializer.save()

        if task_5_data:
            task_5_instance = instance.task_5
            task_5_serializer = Task5Serializer(task_5_instance, task_5_data)
            task_5_serializer.is_valide(raise_exception=True)
            task_5_serializer.save()

        if task_6_place_data:
            task_6_place_instance = instance.task_6_place
            task6_serializer = PlaceSerializer(task_6_place_instance, task_6_place_data)
            task6_serializer.is_valide(raise_exception=True)
            task6_serializer.save()

        if task_6_printingManufacturer_data:
            task_6_printingManufacturer_instance = instance.task_6_printingManufacturer
            task_6_printingManufacturer_serializer = PrintingManufacturerSerializer(
                task_6_printingManufacturer_instance, task_6_printingManufacturer_data
            )
            task_6_printingManufacturer_serializer.is_valide(raise_exception=True)
            task_6_printingManufacturer_serializer.save()

        if task_6_printingManager_data:
            task_6_printingManager_instance = instance.task_6_printingManager
            task_6_printingManager_serializer = PrintingManagerSerializer(
                task_6_printingManager_instance, task_6_printingManager_data
            )
            task_6_printingManager_serializer.is_valide(raise_exception=True)
            task_6_printingManager_serializer.save()

        if task_6_publishingHouse_data:
            task_6_publishingHouse_instance = instance.task_6_publishingHouse
            task_6_publishingHouse_serializer = PublishingHouseSerializer(
                task_6_publishingHouse_instance, task_6_publishingHouse_data
            )
            task_6_publishingHouse_serializer.is_valide(raise_exception=True)
            task_6_publishingHouse_serializer.save()

        if task_6_publishingHouseManager_data:
            task_6_publishingHouseManager_instance = (
                instance.task_6_publishingHouseManager
            )
            task_6_publishingHouseManager_serializer = PublishingHouseManagerSerializer(
                task_6_publishingHouseManager_instance,
                task_6_publishingHouseManager_data,
            )
            task_6_publishingHouseManager_serializer.is_valide(raise_exception=True)
            task_6_publishingHouseManager_serializer.save()

        instance = super().update(instance, validated_data)
        return instance
