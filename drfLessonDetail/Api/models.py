import os

from django.db import models


def picture_upload_path(instance, filename):
    return os.path.join("lesson2_picture", filename)


def signature_upload_path(instance, filename):
    return os.path.join("studentSignature", filename)


def stamp_upload_path(instance, filename):
    return os.path.join("stamp", filename)


class Bookstore(models.Model):
    bookstore = models.TextField(null=True, blank=True, verbose_name="書店")

    class Meta:
        db_table = "Bookstore"

    def __str__(self):
        return self.bookstore


class BookName(models.Model):
    booklName = models.TextField(null=True, blank=True, verbose_name="書名")

    class Meta:
        db_table = "BookName"

    def __str__(self):
        return self.booklName


class Bookseller(models.Model):
    bookseller = models.TextField(null=True, blank=True, verbose_name="書商")

    class Meta:
        db_table = "Bookseller"

    def __str__(self):
        return self.bookseller


class PictureTime(models.Model):
    picture = models.ImageField(
        upload_to=picture_upload_path, null=True, blank=True, verbose_name="圖"
    )
    picture_time = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, verbose_name="上傳圖的時間"
    )

    class Meta:
        db_table = "PictureTime"

    def __str__(self):
        return self.picture


class Task5(models.Model):
    task5 = models.TextField(null=True, blank=True, verbose_name="第 5 個 任務")

    class Meta:
        db_table = "Task5"

    def __str__(self):
        return self.task5


class Place(models.Model):
    place = models.TextField(null=True, blank=True, verbose_name="地點")  # 地點

    class Meta:
        db_table = "Place"

    def __str__(self):
        return self.place


class PrintingManufacturer(models.Model):
    printingManufacturer = models.TextField(
        null=True, blank=True, verbose_name="印刷廠商"
    )

    class Meta:
        db_table = "PrintingManufacturerr"

    def __str__(self):
        return self.printingManufacturer


class PrintingManager(models.Model):
    printingManager = models.TextField(
        null=True, blank=True, verbose_name="印刷廠商經理"
    )

    class Meta:
        db_table = "MachineryManager"

    def __str__(self):
        return self.machineryManager


class PublishingHouse(models.Model):
    publishingHouse = models.TextField(null=True, blank=True, verbose_name="出版社")

    class Meta:
        db_table = "ElectricalCoOrganizer"

    def __str__(self):
        return self.electricalCoOrganizer


class PublishingHouseManager(models.Model):
    publishingHouseManager = models.TextField(
        null=True, blank=True, verbose_name="出版社經理"
    )

    class Meta:
        db_table = "ElectricalManager"

    def __str__(self):
        return self.electricalManager


class Task7(models.Model):
    task7 = models.TextField(null=True, blank=True, verbose_name="第7個任務")

    class Meta:
        db_table = "Task7"

    def __str__(self):
        return self.task7


class Signature(models.Model):
    signature = models.ImageField(
        upload_to=signature_upload_path, null=True, blank=True, verbose_name="簽名"
    )

    class Meta:
        db_table = "Signature"

    def __str__(self):
        return self.signature


class Stamp(models.Model):
    stamp = models.ImageField(
        upload_to=signature_upload_path, null=True, blank=True, verbose_name="書局大章"
    )

    class Meta:
        db_table = "Stamp"

    def __str__(self):
        return self.stamp


class BookInfo(models.Model):
    bookName_all = models.ForeignKey(BookName, on_delete=models.SET_NULL, null=True)
    bookseller_all = models.ForeignKey(Bookseller, on_delete=models.SET_NULL, null=True)
    picture_time_all = models.ImageField(
        upload_to=picture_upload_path,
        null=True,
        blank=True,
        verbose_name="圖_時間(全部)",
    )
    task_1_1_1 = models.BooleanField(default=False, verbose_name="第 1.1.1 個 任務")
    task_1_1_2 = models.BooleanField(default=False, verbose_name="第 1.1.2 個 任務")
    task_1_1_3 = models.BooleanField(default=False, verbose_name="第 1.1.3 個 任務")
    task_1_1_4 = models.BooleanField(default=False, verbose_name="第 1.1.4 個 任務")
    task_1_1_5 = models.BooleanField(default=False, verbose_name="第 1.1.5 個 任務")
    task_1_1_6 = models.BooleanField(default=False, verbose_name="第 1.1.6 個 任務")
    task_1_1_7 = models.BooleanField(default=False, verbose_name="第 1.1.7 個 任務")
    task_1_1_8 = models.BooleanField(default=False, verbose_name="第 1.1.8 個 任務")
    task_1_1_9 = models.BooleanField(default=False, verbose_name="第 1.1.9 個 任務")
    task_1_1_10 = models.BooleanField(default=False, verbose_name="第 1.1.10 個 任務")
    task_1_1_11 = models.BooleanField(default=False, verbose_name="第 1.1.11 個 任務")
    task_1_1_12 = models.BooleanField(default=False, verbose_name="第 1.1.12 個 任務")
    task_1_1_13 = models.BooleanField(default=False, verbose_name="第 1.1.13 個 任務")
    task_1_1_14 = models.BooleanField(default=False, verbose_name="第 1.1.14 個 任務")
    task_1_1_15 = models.BooleanField(default=False, verbose_name="第 1.1.15 個 任務")
    task_1_2_1_1 = models.BooleanField(default=False, verbose_name="第 1.2.1.1 個 任務")
    task_1_2_1_2 = models.BooleanField(default=False, verbose_name="第 1.2.1.2 個 任務")
    task_1_2_1_3 = models.BooleanField(default=False, verbose_name="第 1.2.1.3 個 任務")
    task_1_2_1_4 = models.BooleanField(default=False, verbose_name="第 1.2.1.4 個 任務")
    task_1_2_1_5 = models.BooleanField(default=False, verbose_name="第 1.2.1.5 個 任務")
    task_1_2_1_6 = models.BooleanField(default=False, verbose_name="第 1.2.1.6 個 任務")
    task_1_2_1_7 = models.BooleanField(default=False, verbose_name="第 1.2.1.7 個 任務")
    task_1_2_2_1 = models.BooleanField(default=False, verbose_name="第 1.2.2.1 個 任務")
    task_1_2_2_2 = models.BooleanField(default=False, verbose_name="第 1.2.2.2 個 任務")
    task_1_2_2_3 = models.BooleanField(default=False, verbose_name="第 1.2.2.3 個 任務")
    task_1_2_2_4 = models.BooleanField(default=False, verbose_name="第 1.2.2.4 個 任務")
    task_1_2_2_5 = models.BooleanField(default=False, verbose_name="第 1.2.2.5 個 任務")
    task_1_2_2_6 = models.BooleanField(default=False, verbose_name="第 1.2.2.6 個 任務")
    task_1_2_2_7 = models.BooleanField(default=False, verbose_name="第 1.2.2.7 個 任務")
    task_1_2_2_8 = models.BooleanField(default=False, verbose_name="第 1.2.2.8 個 任務")
    task_1_2_3_1 = models.BooleanField(default=False, verbose_name="第 1.2.3.1 個 任務")
    task_1_2_3_2 = models.BooleanField(default=False, verbose_name="第 1.2.3.2 個 任務")
    task_1_2_3_3 = models.BooleanField(default=False, verbose_name="第 1.2.3.3 個 任務")
    task_1_2_3_4 = models.BooleanField(default=False, verbose_name="第 1.2.3.4 個 任務")
    task_1_2_3_5 = models.BooleanField(default=False, verbose_name="第 1.2.3.5 個 任務")
    task_1_2_4_1 = models.BooleanField(default=False, verbose_name="第 1.2.4.1 個 任務")
    task_1_2_4_2 = models.BooleanField(default=False, verbose_name="第 1.2.4.2 個 任務")
    task_1_2_4_3 = models.BooleanField(default=False, verbose_name="第 1.2.4.3 個 任務")
    task_1_2_4_4 = models.BooleanField(default=False, verbose_name="第 1.2.4.4 個 任務")
    task_1_2_4_5 = models.BooleanField(default=False, verbose_name="第 1.2.4.5 個 任務")
    task_1_2_4_6 = models.BooleanField(default=False, verbose_name="第 1.2.4.6 個 任務")
    task_1_2_4_7 = models.BooleanField(default=False, verbose_name="第 1.2.4.7 個 任務")
    task_1_2_4_8 = models.BooleanField(default=False, verbose_name="第 1.2.4.8 個 任務")
    task_1_2_4_9 = models.BooleanField(default=False, verbose_name="第 1.2.4.9 個 任務")
    task_1_2_4_10 = models.BooleanField(
        default=False, verbose_name="第 1.2.4.10 個 任務"
    )
    task_1_2_4_11 = models.BooleanField(
        default=False, verbose_name="第 1.2.4.11 個 任務"
    )
    task_1_2_5_1 = models.BooleanField(default=False, verbose_name="第 1.2.5.1 個 任務")
    task_1_2_5_2 = models.BooleanField(default=False, verbose_name="第 1.2.5.2 個 任務")
    task_1_2_5_3 = models.BooleanField(default=False, verbose_name="第 1.2.5.3 個 任務")
    task_1_2_5_4 = models.BooleanField(default=False, verbose_name="第 1.2.5.4 個 任務")
    task_1_2_5_5 = models.BooleanField(default=False, verbose_name="第 1.2.5.5 個 任務")
    task_1_2_5_6 = models.BooleanField(default=False, verbose_name="第 1.2.5.6 個 任務")
    task_1_2_5_7 = models.BooleanField(default=False, verbose_name="第 1.2.5.7 個 任務")
    task_2_1 = models.BooleanField(default=False, verbose_name="第 2.1 個 任務")
    task_2_2 = models.BooleanField(default=False, verbose_name="第 2.2 個 任務")
    task_3_1 = models.BooleanField(default=False, verbose_name="第 3.1 個 任務")
    task_3_2 = models.BooleanField(default=False, verbose_name="第 3.2 個 任務")
    task_3_3 = models.BooleanField(default=False, verbose_name="第 3.3 個 任務")
    task_3_4 = models.BooleanField(default=False, verbose_name="第 3.4 個 任務")
    task_3_5 = models.BooleanField(default=False, verbose_name="第 3.5 個 任務")
    task_3_6 = models.BooleanField(default=False, verbose_name="第 3.6 個 任務")
    task_3_7 = models.BooleanField(default=False, verbose_name="第 3.7 個 任務")
    task_5 = models.ForeignKey(Task5, on_delete=models.SET_NULL, null=True)
    task_6_time = models.DateField(verbose_name="時間")
    task_6_place = models.ForeignKey(
        Place, on_delete=models.SET_NULL, null=True
    )  # 第 6 個 任務  地點
    task_6_printingManufacturer = models.ForeignKey(
        PrintingManufacturer, on_delete=models.SET_NULL, null=True
    )  # 第 6 個 任務 印刷廠商
    task_6_printingManager = models.ForeignKey(
        PrintingManager, on_delete=models.SET_NULL, null=True
    )  # 第 6 個 任務 印刷廠商經理
    task_6_publishingHouse = models.ForeignKey(
        PublishingHouse, on_delete=models.SET_NULL, null=True
    )  # 第 6 個 任務 出版社
    task_6_publishingHouseManager = models.ForeignKey(
        PublishingHouseManager, on_delete=models.SET_NULL, null=True
    )  # 第 6 個 任務 出版社經理
    task_6_other = models.TextField(
        null=True, blank=True, verbose_name="第 6 個任務其他"
    )
    task_7 = models.ForeignKey(Task7, on_delete=models.SET_NULL, null=True)
    task_8 = models.ImageField(upload_to=stamp_upload_path, null=True, blank=True)
    signature_saler = models.ImageField(
        upload_to="sign_saler", null=True, blank=True, verbose_name="店員簽名"
    )
    signature_manager = models.ImageField(
        upload_to="sign_manager", null=True, blank=True, verbose_name="經理簽名"
    )
    signature_owener = models.ImageField(
        upload_to="sign_owener", null=True, blank=True, verbose_name="經營者簽名"
    )
    stamp = models.ImageField(upload_to=stamp_upload_path, null=True, blank=True)

    class Meta:
        db_table = "BookInfo"


class Log(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    action = models.IntegerField(
        choices=((1, "新增"), (2, "刪除"), (3, "修改"), (4, "查詢"))
    )
    task = models.ForeignKey(BookInfo, on_delete=models.SET_NULL, null=True)

    @classmethod
    def create_log(cls, action, task=None):
        log = cls(action=action, task=task)
        log.save()
        return log

    class Meta:
        db_table = "Log"
