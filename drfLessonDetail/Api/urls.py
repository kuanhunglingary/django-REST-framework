from Api import views as Api_views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshSlidingView

app_name = "Api"

TokenUrl = [
    path("token/", TokenObtainPairView.as_view(), name="tokem-login"),
    path("token/refresh/", TokenRefreshSlidingView.as_view(), name="token-refresh"),
]

BookstoreUrl = [
    path(
        "bookstore/",
        Api_views.BookstoreViewSet.as_view({"get": "list", "post": "create"}),
        name="bookstore",
    ),
    path(
        "bookstore/<int:pk>",
        Api_views.BookstoreViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="bookstore-pk",
    ),
]

BookNameUrl = [
    path(
        "booklName/",
        Api_views.BookNameViewSet.as_view({"get": "list", "post": "create"}),
        name="booklName",
    ),
    path(
        "booklName/<int:pk>",
        Api_views.BookNameViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="booklName-pk",
    ),
]


BooksellerUrl = [
    path(
        "bookstore/",
        Api_views.BooksellerViewSet.as_view({"get": "list", "post": "create"}),
        name="bookstore",
    ),
    path(
        "bookstore/<int:pk>",
        Api_views.BooksellerViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="bookstore-pk",
    ),
]


PictureTimeUrl = [
    path(
        "bookstore/",
        Api_views.PictureTimeViewSet.as_view({"get": "list", "post": "create"}),
        name="bookstore",
    ),
    path(
        "bookstore/<int:pk>",
        Api_views.PictureTimeViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="bookstore-pk",
    ),
]


Task5Url = [
    path(
        "bookstore/",
        Api_views.Task5ViewSet.as_view({"get": "list", "post": "create"}),
        name="bookstore",
    ),
    path(
        "bookstore/<int:pk>",
        Api_views.Task5ViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="bookstore-pk",
    ),
]


PlaceUrl = [
    path(
        "bookstore/",
        Api_views.PlaceViewSet.as_view({"get": "list", "post": "create"}),
        name="bookstore",
    ),
    path(
        "bookstore/<int:pk>",
        Api_views.PlaceViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="bookstore-pk",
    ),
]


PrintingManufacturerUrl = [
    path(
        "bookstore/",
        Api_views.PrintingManufacturerViewSet.as_view(
            {"get": "list", "post": "create"}
        ),
        name="bookstore",
    ),
    path(
        "bookstore/<int:pk>",
        Api_views.PrintingManufacturerViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="bookstore-pk",
    ),
]


PrintingManagerUrl = [
    path(
        "bookstore/",
        Api_views.PrintingManagerViewSet.as_view({"get": "list", "post": "create"}),
        name="bookstore",
    ),
    path(
        "bookstore/<int:pk>",
        Api_views.PrintingManagerViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="bookstore-pk",
    ),
]


PublishingHouseUrl = [
    path(
        "bookstore/",
        Api_views.PublishingHouseViewSet.as_view({"get": "list", "post": "create"}),
        name="bookstore",
    ),
    path(
        "bookstore/<int:pk>",
        Api_views.PublishingHouseViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="bookstore-pk",
    ),
]


PublishingHouseManagerUrl = [
    path(
        "bookstore/",
        Api_views.PublishingHouseManagerViewSet.as_view(
            {"get": "list", "post": "create"}
        ),
        name="bookstore",
    ),
    path(
        "bookstore/<int:pk>",
        Api_views.PublishingHouseManagerViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="bookstore-pk",
    ),
]


Task7Url = [
    path(
        "bookstore/",
        Api_views.Task7ViewSet.as_view({"get": "list", "post": "create"}),
        name="bookstore",
    ),
    path(
        "bookstore/<int:pk>",
        Api_views.Task7ViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="bookstore-pk",
    ),
]


SignatureUrl = [
    path(
        "bookstore/",
        Api_views.SignatureViewSet.as_view({"get": "list", "post": "create"}),
        name="bookstore",
    ),
    path(
        "bookstore/<int:pk>",
        Api_views.SignatureViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="bookstore-pk",
    ),
]


StampUrl = [
    path(
        "bookstore/",
        Api_views.StampViewSet.as_view({"get": "list", "post": "create"}),
        name="bookstore",
    ),
    path(
        "bookstore/<int:pk>",
        Api_views.StampViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="bookstore-pk",
    ),
]

BookInfoUrl = [
    path(
        "bookstore/",
        Api_views.BookInfoViewSet.as_view({"get": "list", "post": "create"}),
        name="bookstore",
    ),
    path(
        "bookstore/<int:pk>",
        Api_views.BookInfoViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="bookstore-pk",
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
