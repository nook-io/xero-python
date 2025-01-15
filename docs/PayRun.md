# PayRun


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_run_id** | **str** | Xero unique identifier for the pay run | [optional] 
**payroll_calendar_id** | **str** | Xero unique identifier for the payroll calendar | [optional] 
**period_start_date** | **date** | Period start date of the payroll calendar | [optional] 
**period_end_date** | **date** | Period end date of the payroll calendar | [optional] 
**payment_date** | **date** | Payment date of the pay run | [optional] 
**total_cost** | **float** | Total cost of the pay run | [optional] 
**total_pay** | **float** | Total pay of the pay run | [optional] 
**pay_run_status** | **str** | Pay run status | [optional] 
**pay_run_type** | **str** | Pay run type | [optional] 
**calendar_type** | **str** | Calendar type of the pay run | [optional] 
**posted_date_time** | **date** | Posted date time of the pay run | [optional] 
**pay_slips** | [**List[Payslip]**](Payslip.md) |  | [optional] 

## Example

```python
from xero_python.models.pay_run import PayRun

# TODO update the JSON string below
json = "{}"
# create an instance of PayRun from a JSON string
pay_run_instance = PayRun.from_json(json)
# print the JSON string representation of the object
print PayRun.to_json()

# convert the object into a dict
pay_run_dict = pay_run_instance.to_dict()
# create an instance of PayRun from a dict
pay_run_from_dict = PayRun.from_dict(pay_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


