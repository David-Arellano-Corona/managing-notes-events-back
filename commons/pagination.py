from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class Pagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page=1
    page_size = 50
    max_page_size = 50

    def get_paginated_response(self, data):
        return Response({
            "count":self.page.paginator.count,
            "next":self.get_next_link(),
            "previous":self.get_previous_link(),
            "items":data
        })