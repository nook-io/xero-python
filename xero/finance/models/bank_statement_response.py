from xero.models import BaseModel


class BankStatementResponse(BaseModel):
    openapi_types = {
        "statement_lines": "StatementLinesResponse",
        "current_statement": "CurrentStatementResponse",
    }
    attribute_map = {
        "statement_lines": "statementLines",
        "current_statement": "currentStatement",
    }

    def __init__(self, statement_lines=None, current_statement=None):
        self._statement_lines = None
        self._current_statement = None
        self.discriminator = None
        if statement_lines is not None:
            self.statement_lines = statement_lines
        if current_statement is not None:
            self.current_statement = current_statement

    @property
    def statement_lines(self):
        return self._statement_lines

    @statement_lines.setter
    def statement_lines(self, statement_lines):
        self._statement_lines = statement_lines

    @property
    def current_statement(self):
        return self._current_statement

    @current_statement.setter
    def current_statement(self, current_statement):
        self._current_statement = current_statement
