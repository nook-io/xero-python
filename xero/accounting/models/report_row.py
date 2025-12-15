from xero.models import BaseModel


class ReportRow(BaseModel):
    openapi_types = {"row_type": "RowType", "title": "str", "cells": "list[ReportCell]"}
    attribute_map = {"row_type": "RowType", "title": "Title", "cells": "Cells"}

    def __init__(self, row_type=None, title=None, cells=None):
        self._row_type = None
        self._title = None
        self._cells = None
        self.discriminator = None
        if row_type is not None:
            self.row_type = row_type
        if title is not None:
            self.title = title
        if cells is not None:
            self.cells = cells

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
