from django.conf import settings
from drf_yasg.generators import OpenAPISchemaGenerator, EndpointEnumerator


class CustomEndpointEnumerator(EndpointEnumerator):
    """
    Дополнительно проверяем, находится ли url в списке запретов
    """

    def should_include_endpoint(
        self, path, callback, app_name="", namespace="", url_name=None
    ):
        if url_name in settings.SWAGGER_EXCLUDE_URLS:
            return False
        return super().should_include_endpoint(
            path, callback, app_name, namespace, url_name
        )


class OpenAPISchemaGenerator(OpenAPISchemaGenerator):
    endpoint_enumerator_class = CustomEndpointEnumerator
