import pytest


class Links:
    FAVORITES_PRODUCT_PAGE = "https://my.prom.ua/cabinet/user/favorites"
    PRODUCT_LINKS = [
        "https://prom.ua/p712545800-pokrishka-schwalbe-marathon.html",
        "https://prom.ua/ua/p712545800-pokrishka-schwalbe-marathon.html",
        pytest.param("https://prom.ua/ua/p712398427927349545800-pokrishka"
                     "-schwjfjdsbjfkbdjkfbadalbe-marathon.html",
                     marks=pytest.mark.with_error),
    ]
