from rest_framework.response import Response


class ObjectMixin:
    """
        Object mixin
    """

    def get_object(self, queryset, pk):
        try:
            return queryset.get(pk=pk)
        except Exception as e:
            print(f"ERROR ObjectMixin.get_object: {e}")
            return None


class ResponseMixin:
    """
        Response mixin
    """

    def get_json_response(self, data, paginator=None):
        if paginator:
            return paginator.get_paginated_response(data)

        return Response({'result': data})


class ErrorMixin:
    """
        Error response mixin
    """

    def get_json_error(self, error_message, status):
        return Response({
            'error': error_message
        },
            status=status
        )
