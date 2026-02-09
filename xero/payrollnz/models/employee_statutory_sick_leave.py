from xero.models import BaseModel


class EmployeeStatutorySickLeave(BaseModel):
    openapi_types = {
        "statutory_leave_id": "str",
        "employee_id": "str",
        "leave_type_id": "str",
        "start_date": "date",
        "end_date": "date",
        "type": "str",
        "status": "str",
        "work_pattern": "list[str]",
        "is_pregnancy_related": "bool",
        "sufficient_notice": "bool",
        "is_entitled": "bool",
        "entitlement_weeks_requested": "float",
        "entitlement_weeks_qualified": "float",
        "entitlement_weeks_remaining": "float",
        "overlaps_with_other_leave": "bool",
        "entitlement_failure_reasons": "list[str]",
    }
    attribute_map = {
        "statutory_leave_id": "statutoryLeaveID",
        "employee_id": "employeeID",
        "leave_type_id": "leaveTypeID",
        "start_date": "startDate",
        "end_date": "endDate",
        "type": "type",
        "status": "status",
        "work_pattern": "workPattern",
        "is_pregnancy_related": "isPregnancyRelated",
        "sufficient_notice": "sufficientNotice",
        "is_entitled": "isEntitled",
        "entitlement_weeks_requested": "entitlementWeeksRequested",
        "entitlement_weeks_qualified": "entitlementWeeksQualified",
        "entitlement_weeks_remaining": "entitlementWeeksRemaining",
        "overlaps_with_other_leave": "overlapsWithOtherLeave",
        "entitlement_failure_reasons": "entitlementFailureReasons",
    }

    def __init__(
        self,
        statutory_leave_id=None,
        employee_id=None,
        leave_type_id=None,
        start_date=None,
        end_date=None,
        type=None,
        status=None,
        work_pattern=None,
        is_pregnancy_related=None,
        sufficient_notice=None,
        is_entitled=None,
        entitlement_weeks_requested=None,
        entitlement_weeks_qualified=None,
        entitlement_weeks_remaining=None,
        overlaps_with_other_leave=None,
        entitlement_failure_reasons=None,
    ):
        self._statutory_leave_id = None
        self._employee_id = None
        self._leave_type_id = None
        self._start_date = None
        self._end_date = None
        self._type = None
        self._status = None
        self._work_pattern = None
        self._is_pregnancy_related = None
        self._sufficient_notice = None
        self._is_entitled = None
        self._entitlement_weeks_requested = None
        self._entitlement_weeks_qualified = None
        self._entitlement_weeks_remaining = None
        self._overlaps_with_other_leave = None
        self._entitlement_failure_reasons = None
        self.discriminator = None
        if statutory_leave_id is not None:
            self.statutory_leave_id = statutory_leave_id
        self.employee_id = employee_id
        self.leave_type_id = leave_type_id
        self.start_date = start_date
        self.end_date = end_date
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        self.work_pattern = work_pattern
        self.is_pregnancy_related = is_pregnancy_related
        self.sufficient_notice = sufficient_notice
        if is_entitled is not None:
            self.is_entitled = is_entitled
        if entitlement_weeks_requested is not None:
            self.entitlement_weeks_requested = entitlement_weeks_requested
        if entitlement_weeks_qualified is not None:
            self.entitlement_weeks_qualified = entitlement_weeks_qualified
        if entitlement_weeks_remaining is not None:
            self.entitlement_weeks_remaining = entitlement_weeks_remaining
        if overlaps_with_other_leave is not None:
            self.overlaps_with_other_leave = overlaps_with_other_leave
        if entitlement_failure_reasons is not None:
            self.entitlement_failure_reasons = entitlement_failure_reasons

    @property
    def statutory_leave_id(self):
        return self._statutory_leave_id

    @statutory_leave_id.setter
    def statutory_leave_id(self, statutory_leave_id):
        self._statutory_leave_id = statutory_leave_id

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        if employee_id is None:
            raise ValueError("Invalid value for `employee_id`, must not be `None`")
        self._employee_id = employee_id

    @property
    def leave_type_id(self):
        return self._leave_type_id

    @leave_type_id.setter
    def leave_type_id(self, leave_type_id):
        if leave_type_id is None:
            raise ValueError("Invalid value for `leave_type_id`, must not be `None`")
        self._leave_type_id = leave_type_id

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")
        self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")
        self._end_date = end_date

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def work_pattern(self):
        return self._work_pattern

    @work_pattern.setter
    def work_pattern(self, work_pattern):
        if work_pattern is None:
            raise ValueError("Invalid value for `work_pattern`, must not be `None`")
        self._work_pattern = work_pattern

    @property
    def is_pregnancy_related(self):
        return self._is_pregnancy_related

    @is_pregnancy_related.setter
    def is_pregnancy_related(self, is_pregnancy_related):
        if is_pregnancy_related is None:
            raise ValueError(
                "Invalid value for `is_pregnancy_related`, must not be `None`"
            )
        self._is_pregnancy_related = is_pregnancy_related

    @property
    def sufficient_notice(self):
        return self._sufficient_notice

    @sufficient_notice.setter
    def sufficient_notice(self, sufficient_notice):
        if sufficient_notice is None:
            raise ValueError(
                "Invalid value for `sufficient_notice`, must not be `None`"
            )
        self._sufficient_notice = sufficient_notice

    @property
    def is_entitled(self):
        return self._is_entitled

    @is_entitled.setter
    def is_entitled(self, is_entitled):
        self._is_entitled = is_entitled

    @property
    def entitlement_weeks_requested(self):
        return self._entitlement_weeks_requested

    @entitlement_weeks_requested.setter
    def entitlement_weeks_requested(self, entitlement_weeks_requested):
        self._entitlement_weeks_requested = entitlement_weeks_requested

    @property
    def entitlement_weeks_qualified(self):
        return self._entitlement_weeks_qualified

    @entitlement_weeks_qualified.setter
    def entitlement_weeks_qualified(self, entitlement_weeks_qualified):
        self._entitlement_weeks_qualified = entitlement_weeks_qualified

    @property
    def entitlement_weeks_remaining(self):
        return self._entitlement_weeks_remaining

    @entitlement_weeks_remaining.setter
    def entitlement_weeks_remaining(self, entitlement_weeks_remaining):
        self._entitlement_weeks_remaining = entitlement_weeks_remaining

    @property
    def overlaps_with_other_leave(self):
        return self._overlaps_with_other_leave

    @overlaps_with_other_leave.setter
    def overlaps_with_other_leave(self, overlaps_with_other_leave):
        self._overlaps_with_other_leave = overlaps_with_other_leave

    @property
    def entitlement_failure_reasons(self):
        return self._entitlement_failure_reasons

    @entitlement_failure_reasons.setter
    def entitlement_failure_reasons(self, entitlement_failure_reasons):
        allowed_values = [
            "UnableToCalculateAwe",
            "AweLowerThanLel",
            "NotQualifiedInPreviousPiw",
            "ExceededMaximumEntitlementWeeksOfSsp",
            "ExceededMaximumDurationOfPiw",
            "SufficientNoticeNotGiven",
            "None",
        ]
        if not set(entitlement_failure_reasons).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `entitlement_failure_reasons` [{0}], must be a subset of [{1}]".format(
                    ", ".join(
                        map(str, set(entitlement_failure_reasons) - set(allowed_values))
                    ),
                    ", ".join(map(str, allowed_values)),
                )
            )
        self._entitlement_failure_reasons = entitlement_failure_reasons
