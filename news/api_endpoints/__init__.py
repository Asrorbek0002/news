from comments.api_endpoints import (CommentCreateAPIView,
                                    CommentListAPIView,
                                    CommentUpdateAPIView,
                                    CommentDeleteAPIView,
                                    )
from .NewsCreate import NewsCreateAPIView
from .NewsDetail import NewsRetrieveAPIView
from .NewsList import NewsListAPIView
from .NewsUpdate import NewsUpdateAPIView
from .NewsDelete import NewsDeleteAPIView

from .MediaFileCreate import MediaFileCreateAPIView
from .MediaFileList import MediaFileListAPIView
from .MediaFileRetrieve import MediaFileRetrieveAPIView
from .MediaFileUpdate import MediaFileUpdateAPIView
from .MediaFileDelete import MediaFileDeleteAPIView

__all__ = [
    "NewsCreateAPIView",
    "NewsListAPIView",
    "NewsRetrieveAPIView",
    "NewsDeleteAPIView",

    "CommentCreateAPIView",
    "CommentListAPIView",
    "CommentUpdateAPIView",
    "CommentDeleteAPIView",

    "MediaFileCreateAPIView",
    "MediaFileListAPIView",
    "MediaFileRetrieveAPIView",
    "MediaFileUpdateAPIView",
    "MediaFileDeleteAPIView",
]