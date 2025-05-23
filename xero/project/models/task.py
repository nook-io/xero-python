# coding: utf-8

"""
    Xero Projects API

    This is the Xero Projects API  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero.models import BaseModel


class Task(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "task_id": "str",
        "name": "str",
        "rate": "Amount",
        "charge_type": "ChargeType",
        "estimate_minutes": "int",
        "project_id": "str",
        "total_minutes": "int",
        "total_amount": "Amount",
        "minutes_invoiced": "int",
        "minutes_to_be_invoiced": "int",
        "fixed_minutes": "int",
        "non_chargeable_minutes": "int",
        "amount_to_be_invoiced": "Amount",
        "amount_invoiced": "Amount",
        "status": "str",
    }

    attribute_map = {
        "task_id": "taskId",
        "name": "name",
        "rate": "rate",
        "charge_type": "chargeType",
        "estimate_minutes": "estimateMinutes",
        "project_id": "projectId",
        "total_minutes": "totalMinutes",
        "total_amount": "totalAmount",
        "minutes_invoiced": "minutesInvoiced",
        "minutes_to_be_invoiced": "minutesToBeInvoiced",
        "fixed_minutes": "fixedMinutes",
        "non_chargeable_minutes": "nonChargeableMinutes",
        "amount_to_be_invoiced": "amountToBeInvoiced",
        "amount_invoiced": "amountInvoiced",
        "status": "status",
    }

    def __init__(
        self,
        task_id=None,
        name=None,
        rate=None,
        charge_type=None,
        estimate_minutes=None,
        project_id=None,
        total_minutes=None,
        total_amount=None,
        minutes_invoiced=None,
        minutes_to_be_invoiced=None,
        fixed_minutes=None,
        non_chargeable_minutes=None,
        amount_to_be_invoiced=None,
        amount_invoiced=None,
        status=None,
    ):  # noqa: E501
        """Task - a model defined in OpenAPI"""  # noqa: E501

        self._task_id = None
        self._name = None
        self._rate = None
        self._charge_type = None
        self._estimate_minutes = None
        self._project_id = None
        self._total_minutes = None
        self._total_amount = None
        self._minutes_invoiced = None
        self._minutes_to_be_invoiced = None
        self._fixed_minutes = None
        self._non_chargeable_minutes = None
        self._amount_to_be_invoiced = None
        self._amount_invoiced = None
        self._status = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if name is not None:
            self.name = name
        if rate is not None:
            self.rate = rate
        if charge_type is not None:
            self.charge_type = charge_type
        if estimate_minutes is not None:
            self.estimate_minutes = estimate_minutes
        if project_id is not None:
            self.project_id = project_id
        if total_minutes is not None:
            self.total_minutes = total_minutes
        if total_amount is not None:
            self.total_amount = total_amount
        if minutes_invoiced is not None:
            self.minutes_invoiced = minutes_invoiced
        if minutes_to_be_invoiced is not None:
            self.minutes_to_be_invoiced = minutes_to_be_invoiced
        if fixed_minutes is not None:
            self.fixed_minutes = fixed_minutes
        if non_chargeable_minutes is not None:
            self.non_chargeable_minutes = non_chargeable_minutes
        if amount_to_be_invoiced is not None:
            self.amount_to_be_invoiced = amount_to_be_invoiced
        if amount_invoiced is not None:
            self.amount_invoiced = amount_invoiced
        if status is not None:
            self.status = status

    @property
    def task_id(self):
        """Gets the task_id of this Task.  # noqa: E501

        Identifier of the task.  # noqa: E501

        :return: The task_id of this Task.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this Task.

        Identifier of the task.  # noqa: E501

        :param task_id: The task_id of this Task.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def name(self):
        """Gets the name of this Task.  # noqa: E501

        Name of the task.  # noqa: E501

        :return: The name of this Task.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Task.

        Name of the task.  # noqa: E501

        :param name: The name of this Task.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def rate(self):
        """Gets the rate of this Task.  # noqa: E501


        :return: The rate of this Task.  # noqa: E501
        :rtype: Amount
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this Task.


        :param rate: The rate of this Task.  # noqa: E501
        :type: Amount
        """

        self._rate = rate

    @property
    def charge_type(self):
        """Gets the charge_type of this Task.  # noqa: E501


        :return: The charge_type of this Task.  # noqa: E501
        :rtype: ChargeType
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this Task.


        :param charge_type: The charge_type of this Task.  # noqa: E501
        :type: ChargeType
        """

        self._charge_type = charge_type

    @property
    def estimate_minutes(self):
        """Gets the estimate_minutes of this Task.  # noqa: E501

        An estimated time to perform the task  # noqa: E501

        :return: The estimate_minutes of this Task.  # noqa: E501
        :rtype: int
        """
        return self._estimate_minutes

    @estimate_minutes.setter
    def estimate_minutes(self, estimate_minutes):
        """Sets the estimate_minutes of this Task.

        An estimated time to perform the task  # noqa: E501

        :param estimate_minutes: The estimate_minutes of this Task.  # noqa: E501
        :type: int
        """

        self._estimate_minutes = estimate_minutes

    @property
    def project_id(self):
        """Gets the project_id of this Task.  # noqa: E501

        Identifier of the project task belongs to.  # noqa: E501

        :return: The project_id of this Task.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Task.

        Identifier of the project task belongs to.  # noqa: E501

        :param project_id: The project_id of this Task.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def total_minutes(self):
        """Gets the total_minutes of this Task.  # noqa: E501

        Total minutes which have been logged against the task. Logged by assigning a time entry to a task  # noqa: E501

        :return: The total_minutes of this Task.  # noqa: E501
        :rtype: int
        """
        return self._total_minutes

    @total_minutes.setter
    def total_minutes(self, total_minutes):
        """Sets the total_minutes of this Task.

        Total minutes which have been logged against the task. Logged by assigning a time entry to a task  # noqa: E501

        :param total_minutes: The total_minutes of this Task.  # noqa: E501
        :type: int
        """

        self._total_minutes = total_minutes

    @property
    def total_amount(self):
        """Gets the total_amount of this Task.  # noqa: E501


        :return: The total_amount of this Task.  # noqa: E501
        :rtype: Amount
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this Task.


        :param total_amount: The total_amount of this Task.  # noqa: E501
        :type: Amount
        """

        self._total_amount = total_amount

    @property
    def minutes_invoiced(self):
        """Gets the minutes_invoiced of this Task.  # noqa: E501

        Minutes on this task which have been invoiced.  # noqa: E501

        :return: The minutes_invoiced of this Task.  # noqa: E501
        :rtype: int
        """
        return self._minutes_invoiced

    @minutes_invoiced.setter
    def minutes_invoiced(self, minutes_invoiced):
        """Sets the minutes_invoiced of this Task.

        Minutes on this task which have been invoiced.  # noqa: E501

        :param minutes_invoiced: The minutes_invoiced of this Task.  # noqa: E501
        :type: int
        """

        self._minutes_invoiced = minutes_invoiced

    @property
    def minutes_to_be_invoiced(self):
        """Gets the minutes_to_be_invoiced of this Task.  # noqa: E501

        Minutes on this task which have not been invoiced.  # noqa: E501

        :return: The minutes_to_be_invoiced of this Task.  # noqa: E501
        :rtype: int
        """
        return self._minutes_to_be_invoiced

    @minutes_to_be_invoiced.setter
    def minutes_to_be_invoiced(self, minutes_to_be_invoiced):
        """Sets the minutes_to_be_invoiced of this Task.

        Minutes on this task which have not been invoiced.  # noqa: E501

        :param minutes_to_be_invoiced: The minutes_to_be_invoiced of this Task.  # noqa: E501
        :type: int
        """

        self._minutes_to_be_invoiced = minutes_to_be_invoiced

    @property
    def fixed_minutes(self):
        """Gets the fixed_minutes of this Task.  # noqa: E501

        Minutes logged against this task if its charge type is `FIXED`.  # noqa: E501

        :return: The fixed_minutes of this Task.  # noqa: E501
        :rtype: int
        """
        return self._fixed_minutes

    @fixed_minutes.setter
    def fixed_minutes(self, fixed_minutes):
        """Sets the fixed_minutes of this Task.

        Minutes logged against this task if its charge type is `FIXED`.  # noqa: E501

        :param fixed_minutes: The fixed_minutes of this Task.  # noqa: E501
        :type: int
        """

        self._fixed_minutes = fixed_minutes

    @property
    def non_chargeable_minutes(self):
        """Gets the non_chargeable_minutes of this Task.  # noqa: E501

        Minutes logged against this task if its charge type is `NON_CHARGEABLE`.  # noqa: E501

        :return: The non_chargeable_minutes of this Task.  # noqa: E501
        :rtype: int
        """
        return self._non_chargeable_minutes

    @non_chargeable_minutes.setter
    def non_chargeable_minutes(self, non_chargeable_minutes):
        """Sets the non_chargeable_minutes of this Task.

        Minutes logged against this task if its charge type is `NON_CHARGEABLE`.  # noqa: E501

        :param non_chargeable_minutes: The non_chargeable_minutes of this Task.  # noqa: E501
        :type: int
        """

        self._non_chargeable_minutes = non_chargeable_minutes

    @property
    def amount_to_be_invoiced(self):
        """Gets the amount_to_be_invoiced of this Task.  # noqa: E501


        :return: The amount_to_be_invoiced of this Task.  # noqa: E501
        :rtype: Amount
        """
        return self._amount_to_be_invoiced

    @amount_to_be_invoiced.setter
    def amount_to_be_invoiced(self, amount_to_be_invoiced):
        """Sets the amount_to_be_invoiced of this Task.


        :param amount_to_be_invoiced: The amount_to_be_invoiced of this Task.  # noqa: E501
        :type: Amount
        """

        self._amount_to_be_invoiced = amount_to_be_invoiced

    @property
    def amount_invoiced(self):
        """Gets the amount_invoiced of this Task.  # noqa: E501


        :return: The amount_invoiced of this Task.  # noqa: E501
        :rtype: Amount
        """
        return self._amount_invoiced

    @amount_invoiced.setter
    def amount_invoiced(self, amount_invoiced):
        """Sets the amount_invoiced of this Task.


        :param amount_invoiced: The amount_invoiced of this Task.  # noqa: E501
        :type: Amount
        """

        self._amount_invoiced = amount_invoiced

    @property
    def status(self):
        """Gets the status of this Task.  # noqa: E501

        Status of the task. When a task of ChargeType is `FIXED` and the rate amount is invoiced the status will be set to `INVOICED` and can't be modified. A task with ChargeType of `TIME` or `NON_CHARGEABLE` cannot have a status of `INVOICED`. A `LOCKED` state indicates that the task is currently changing state (for example being invoiced) and can't be modified.  # noqa: E501

        :return: The status of this Task.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Task.

        Status of the task. When a task of ChargeType is `FIXED` and the rate amount is invoiced the status will be set to `INVOICED` and can't be modified. A task with ChargeType of `TIME` or `NON_CHARGEABLE` cannot have a status of `INVOICED`. A `LOCKED` state indicates that the task is currently changing state (for example being invoiced) and can't be modified.  # noqa: E501

        :param status: The status of this Task.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "INVOICED", "LOCKED", "None"]  # noqa: E501

        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                        status, allowed_values
                    )
                )

        self._status = status
