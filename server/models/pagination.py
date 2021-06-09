# pagination.py
# @Author : Anderson Rocha (anderson.rocha@dextra-sw.com)
# @Date   : 01/10/18, 22:01

from server import ma


class PaginationSchema(ma.ModelSchema):
    class Meta:
        fields = (
            "page",
            "per_page",
            "total",
            "pages",
            "has_prev",
            "has_next",
            "prev_num",
            "next_num",
        )
