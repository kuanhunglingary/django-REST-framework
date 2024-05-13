from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshSlidingView

from Api import views as Api_views

from .views import (
    BookInfoViewSet,
    BookNameViewSet,
    BooksellerViewSet,
    BookstoreViewSet,
    PictureTimeViewSet,
    PlaceViewSet,
    PrintingManagerViewSet,
    PrintingManufacturerViewSet,
    PublishingHouseManagerViewSet,
    PublishingHouseViewSet,
    SignatureViewSet,
    StampViewSet,
    Task5ViewSet,
    Task7ViewSet,
)

app_name = "Api"

TokenUrl = [
    path("token/", TokenObtainPairView.as_view(), name="tokem-login"),
    path("token/refresh/", TokenRefreshSlidingView.as_view(), name="token-refresh"),
]

# BookstoreUrl = [
#     path(
#         "bookstore/",
#         Api_views.BookstoreViewSet.as_view({"get": "list", "post": "create"}),
#         name="bookstore",
#     ),
#     path(
#         "bookstore/<int:pk>",
#         Api_views.BookstoreViewSet.as_view(
#             {"get": "retrieve", "patch": "update", "delete": "destroy"}
#         ),
#         name="bookstore-pk",
#     ),
# ]
BookstoreUrl = [
    path(
        "bookstore/",
        BookstoreViewSet.as_view({"get": "list", "post": "create"}),
        name="bookstore",
    ),
    path(
        "bookstore/<int:pk>",
        BookstoreViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="bookstore-pk",
    ),
]

# BookNameUrl = [
#     path(
#         "booklName/",
#         Api_views.BookNameViewSet.as_view({"get": "list", "post": "create"}),
#         name="booklName",
#     ),
#     path(
#         "booklName/<int:pk>",
#         Api_views.BookNameViewSet.as_view(
#             {"get": "retrieve", "patch": "update", "delete": "destroy"}
#         ),
#         name="booklName-pk",
#     ),
# ]
BookNameUrl = [
    path(
        "booklName/",
        BookNameViewSet.as_view({"get": "list", "post": "create"}),
        name="booklName",
    ),
    path(
        "booklName/<int:pk>",
        BookNameViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="booklName-pk",
    ),
]


# BooksellerUrl = [
#     path(
#         "bookseller/",
#         Api_views.BooksellerViewSet.as_view({"get": "list", "post": "create"}),
#         name="bookseller",
#     ),
#     path(
#         "bookseller/<int:pk>",
#         Api_views.BooksellerViewSet.as_view(
#             {"get": "retrieve", "patch": "update", "delete": "destroy"}
#         ),
#         name="bookseller-pk",
#     ),
# ]
BooksellerUrl = [
    path(
        "bookseller/",
        BooksellerViewSet.as_view({"get": "list", "post": "create"}),
        name="bookseller",
    ),
    path(
        "bookseller/<int:pk>",
        BooksellerViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="bookseller-pk",
    ),
]


# PictureTimeUrl = [
#     path(
#         "pictureTime/",
#         Api_views.PictureTimeViewSet.as_view({"get": "list", "post": "create"}),
#         name="pictureTime",
#     ),
#     path(
#         "pictureTime/<int:pk>",
#         Api_views.PictureTimeViewSet.as_view(
#             {"get": "retrieve", "patch": "update", "delete": "destroy"}
#         ),
#         name="pictureTime-pk",
#     ),
# ]
PictureTimeUrl = [
    path(
        "pictureTime/",
        PictureTimeViewSet.as_view({"get": "list", "post": "create"}),
        name="pictureTime",
    ),
    path(
        "pictureTime/<int:pk>",
        PictureTimeViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="pictureTime-pk",
    ),
]


# Task5Url = [
#     path(
#         "task5/",
#         Api_views.Task5ViewSet.as_view({"get": "list", "post": "create"}),
#         name="task5",
#     ),
#     path(
#         "task5/<int:pk>",
#         Api_views.Task5ViewSet.as_view(
#             {"get": "retrieve", "patch": "update", "delete": "destroy"}
#         ),
#         name="task5-pk",
#     ),
# ]
Task5Url = [
    path(
        "task5/",
        Task5ViewSet.as_view({"get": "list", "post": "create"}),
        name="task5",
    ),
    path(
        "task5/<int:pk>",
        Task5ViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="task5-pk",
    ),
]

# PlaceUrl = [
#     path(
#         "place/",
#         Api_views.PlaceViewSet.as_view({"get": "list", "post": "create"}),
#         name="place",
#     ),
#     path(
#         "place/<int:pk>",
#         Api_views.PlaceViewSet.as_view(
#             {"get": "retrieve", "patch": "update", "delete": "destroy"}
#         ),
#         name="place-pk",
#     ),
# ]
PlaceUrl = [
    path(
        "place/",
        PlaceViewSet.as_view({"get": "list", "post": "create"}),
        name="place",
    ),
    path(
        "place/<int:pk>",
        PlaceViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="place-pk",
    ),
]

# PrintingManufacturerUrl = [
#     path(
#         "printingManufacturer/",
#         Api_views.PrintingManufacturerViewSet.as_view(
#             {"get": "list", "post": "create"}
#         ),
#         name="printingManufacturer",
#     ),
#     path(
#         "printingManufacturer/<int:pk>",
#         Api_views.PrintingManufacturerViewSet.as_view(
#             {"get": "retrieve", "patch": "update", "delete": "destroy"}
#         ),
#         name="printingManufacturer-pk",
#     ),
# ]
PrintingManufacturerUrl = [
    path(
        "printingManufacturer/",
        PrintingManufacturerViewSet.as_view({"get": "list", "post": "create"}),
        name="printingManufacturer",
    ),
    path(
        "printingManufacturer/<int:pk>",
        PrintingManufacturerViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="printingManufacturer-pk",
    ),
]


# PrintingManagerUrl = [
#     path(
#         "printingManager/",
#         Api_views.PrintingManagerViewSet.as_view({"get": "list", "post": "create"}),
#         name="printingManager",
#     ),
#     path(
#         "printingManager/<int:pk>",
#         Api_views.PrintingManagerViewSet.as_view(
#             {"get": "retrieve", "patch": "update", "delete": "destroy"}
#         ),
#         name="printingManager-pk",
#     ),
# ]
PrintingManagerUrl = [
    path(
        "printingManager/",
        PrintingManagerViewSet.as_view({"get": "list", "post": "create"}),
        name="printingManager",
    ),
    path(
        "printingManager/<int:pk>",
        PrintingManagerViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="printingManager-pk",
    ),
]


# PublishingHouseUrl = [
#     path(
#         "publishingHouse/",
#         Api_views.PublishingHouseViewSet.as_view({"get": "list", "post": "create"}),
#         name="publishingHouse",
#     ),
#     path(
#         "publishingHouse/<int:pk>",
#         Api_views.PublishingHouseViewSet.as_view(
#             {"get": "retrieve", "patch": "update", "delete": "destroy"}
#         ),
#         name="publishingHouse-pk",
#     ),
# ]
PublishingHouseUrl = [
    path(
        "publishingHouse/",
        PublishingHouseViewSet.as_view({"get": "list", "post": "create"}),
        name="publishingHouse",
    ),
    path(
        "publishingHouse/<int:pk>",
        PublishingHouseViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="publishingHouse-pk",
    ),
]


# PublishingHouseManagerUrl = [
#     path(
#         "publishingHouseManager/",
#         Api_views.PublishingHouseManagerViewSet.as_view(
#             {"get": "list", "post": "create"}
#         ),
#         name="publishingHouseManager",
#     ),
#     path(
#         "publishingHouseManager/<int:pk>",
#         Api_views.PublishingHouseManagerViewSet.as_view(
#             {"get": "retrieve", "patch": "update", "delete": "destroy"}
#         ),
#         name="publishingHouseManager-pk",
#     ),
# ]
PublishingHouseManagerUrl = [
    path(
        "publishingHouseManager/",
        PublishingHouseManagerViewSet.as_view({"get": "list", "post": "create"}),
        name="publishingHouseManager",
    ),
    path(
        "publishingHouseManager/<int:pk>",
        PublishingHouseManagerViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="publishingHouseManager-pk",
    ),
]


# Task7Url = [
#     path(
#         "task7/",
#         Api_views.Task7ViewSet.as_view({"get": "list", "post": "create"}),
#         name="task7",
#     ),
#     path(
#         "task7/<int:pk>",
#         Api_views.Task7ViewSet.as_view(
#             {"get": "retrieve", "patch": "update", "delete": "destroy"}
#         ),
#         name="task7-pk",
#     ),
# ]
Task7Url = [
    path(
        "task7/",
        Task7ViewSet.as_view({"get": "list", "post": "create"}),
        name="task7",
    ),
    path(
        "task7/<int:pk>",
        Task7ViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="task7-pk",
    ),
]


# SignatureUrl = [
#     path(
#         "signature/",
#         Api_views.SignatureViewSet.as_view({"get": "list", "post": "create"}),
#         name="signature",
#     ),
#     path(
#         "signature/<int:pk>",
#         Api_views.SignatureViewSet.as_view(
#             {"get": "retrieve", "patch": "update", "delete": "destroy"}
#         ),
#         name="signature-pk",
#     ),
# ]
SignatureUrl = [
    path(
        "signature/",
        SignatureViewSet.as_view({"get": "list", "post": "create"}),
        name="signature",
    ),
    path(
        "signature/<int:pk>",
        SignatureViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="signature-pk",
    ),
]


# StampUrl = [
#     path(
#         "stamp/",
#         Api_views.StampViewSet.as_view({"get": "list", "post": "create"}),
#         name="stamp",
#     ),
#     path(
#         "stamp/<int:pk>",
#         Api_views.StampViewSet.as_view(
#             {"get": "retrieve", "patch": "update", "delete": "destroy"}
#         ),
#         name="stamp-pk",
#     ),
# ]
StampUrl = [
    path(
        "stamp/",
        StampViewSet.as_view({"get": "list", "post": "create"}),
        name="stamp",
    ),
    path(
        "stamp/<int:pk>",
        StampViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="stamp-pk",
    ),
]

# BookInfoUrl = [
#     path(
#         "bookInfo/",
#         Api_views.BookInfoViewSet.as_view({"get": "list", "post": "create"}),
#         name="bookInfo",
#     ),
#     path(
#         "bookInfo/<int:pk>",
#         Api_views.BookInfoViewSet.as_view(
#             {"get": "retrieve", "patch": "update", "delete": "destroy"}
#         ),
#         name="bookInfo-pk",
#     ),
# ]
BookInfoUrl = [
    path(
        "bookInfo/",
        BookInfoViewSet.as_view({"get": "list", "post": "create"}),
        name="bookInfo",
    ),
    path(
        "bookInfo/<int:pk>",
        BookInfoViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="bookInfo-pk",
    ),
]

urlpatterns = (
    TokenUrl
    + BookstoreUrl
    + BookNameUrl
    + BooksellerUrl
    + PictureTimeUrl
    + Task5Url
    + PlaceUrl
    + PrintingManufacturerUrl
    + PrintingManagerUrl
    + PublishingHouseUrl
    + PublishingHouseManagerUrl
    + Task7Url
    + SignatureUrl
    + StampUrl
    + BookInfoUrl
)
