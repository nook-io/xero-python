from xero.models import BaseModel


class ReportRows(BaseModel):
    openapi_types = {
        "row_type": "RowType",
        "title": "str",
        "cells": "list[ReportCell]",
        "rows": "list[ReportRow]",
    }
    attribute_map = {
        "row_type": "RowType",
        "title": "Title",
        "cells": "Cells",
        "rows": "Rows",
    }

    def __init__(self, row_type=None, title=None, cells=None, rows=None):
        self._row_type = None
        self._title = None
        self._cells = None
        self._rows = None
        self.discriminator = None
        if row_type is not None:
            self.row_type = row_type
        if title is not None:
            self.title = title
        if cells is not None:
            self.cells = cells
        if rows is not None:
            self.rows = rows

    @property
    def row_type(self):
        return self._row_type

    @row_type.setter
    def row_type(self, row_type):
        self._row_type = row_type

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def cells(self):
        return self._cells

    @cells.setter
    def cells(self, cells):
        self._cells = cells

    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, rows):
        self._rows = rows
