from xero.models import BaseModel


class LeaveApplications(BaseModel):
    openapi_types = {"leave_applications": "list[LeaveApplication]"}
    attribute_map = {"leave_applications": "LeaveApplications"}

    def __init__(self, leave_applications=None):
        self._leave_applications = None
        self.discriminator = None
        if leave_applications is not None:
            self.leave_applications = leave_applications

    @property
    def leave_applications(self):
        return self._leave_applications

    @leave_applications.setter
    def leave_applications(self, leave_applications):
        self._leave_applications = leave_applications
