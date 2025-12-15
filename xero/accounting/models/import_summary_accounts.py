from xero.models import BaseModel


class ImportSummaryAccounts(BaseModel):
    openapi_types = {
        "total": "int",
        "new": "int",
        "updated": "int",
        "deleted": "int",
        "locked": "int",
        "system": "int",
        "errored": "int",
        "present": "bool",
        "new_or_updated": "int",
    }
    attribute_map = {
        "total": "Total",
        "new": "New",
        "updated": "Updated",
        "deleted": "Deleted",
        "locked": "Locked",
        "system": "System",
        "errored": "Errored",
        "present": "Present",
        "new_or_updated": "NewOrUpdated",
    }

    def __init__(
        self,
        total=None,
        new=None,
        updated=None,
        deleted=None,
        locked=None,
        system=None,
        errored=None,
        present=None,
        new_or_updated=None,
    ):
        self._total = None
        self._new = None
        self._updated = None
        self._deleted = None
        self._locked = None
        self._system = None
        self._errored = None
        self._present = None
        self._new_or_updated = None
        self.discriminator = None
        if total is not None:
            self.total = total
        if new is not None:
            self.new = new
        if updated is not None:
            self.updated = updated
        if deleted is not None:
            self.deleted = deleted
        if locked is not None:
            self.locked = locked
        if system is not None:
            self.system = system
        if errored is not None:
            self.errored = errored
        if present is not None:
            self.present = present
        if new_or_updated is not None:
            self.new_or_updated = new_or_updated

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total

    @property
    def new(self):
        return self._new

    @new.setter
    def new(self, new):
        self._new = new

    @property
    def updated(self):
        return self._updated

    @updated.setter
    def updated(self, updated):
        self._updated = updated

    @property
    def deleted(self):
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        self._deleted = deleted

    @property
    def locked(self):
        return self._locked

    @locked.setter
    def locked(self, locked):
        self._locked = locked

    @property
    def system(self):
        return self._system

    @system.setter
    def system(self, system):
        self._system = system

    @property
    def errored(self):
        return self._errored

    @errored.setter
    def errored(self, errored):
        self._errored = errored

    @property
    def present(self):
        return self._present

    @present.setter
    def present(self, present):
        self._present = present

    @property
    def new_or_updated(self):
        return self._new_or_updated

    @new_or_updated.setter
    def new_or_updated(self, new_or_updated):
        self._new_or_updated = new_or_updated
