# Payslip1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** | The Xero identifier for an employee | [optional] 
**payslip_id** | **str** | Xero identifier for the payslip | [optional] 
**first_name** | **str** | First name of employee | [optional] 
**last_name** | **str** | Last name of employee | [optional] 
**wages** | **float** | The Wages for the Payslip | [optional] 
**deductions** | **float** | The Deductions for the Payslip | [optional] 
**tax** | **float** | The Tax for the Payslip | [optional] 
**super** | **float** | The Super for the Payslip | [optional] 
**reimbursements** | **float** | The Reimbursements for the Payslip | [optional] 
**net_pay** | **float** | The NetPay for the Payslip | [optional] 
**earnings_lines** | [**List[EarningsLine1]**](EarningsLine1.md) |  | [optional] 
**leave_earnings_lines** | [**List[LeaveEarningsLine1]**](LeaveEarningsLine1.md) |  | [optional] 
**timesheet_earnings_lines** | [**List[EarningsLine1]**](EarningsLine1.md) |  | [optional] 
**deduction_lines** | [**List[DeductionLine1]**](DeductionLine1.md) |  | [optional] 
**leave_accrual_lines** | [**List[LeaveAccrualLine1]**](LeaveAccrualLine1.md) |  | [optional] 
**reimbursement_lines** | [**List[ReimbursementLine1]**](ReimbursementLine1.md) |  | [optional] 
**superannuation_lines** | [**List[SuperannuationLine]**](SuperannuationLine.md) |  | [optional] 
**tax_lines** | [**List[TaxLine1]**](TaxLine1.md) |  | [optional] 
**updated_date_utc** | **str** | Last modified timestamp | [optional] [readonly] 

## Example

```python
from xero_python.models.payslip1 import Payslip1

# TODO update the JSON string below
json = "{}"
# create an instance of Payslip1 from a JSON string
payslip1_instance = Payslip1.from_json(json)
# print the JSON string representation of the object
print Payslip1.to_json()

# convert the object into a dict
payslip1_dict = payslip1_instance.to_dict()
# create an instance of Payslip1 from a dict
payslip1_from_dict = Payslip1.from_dict(payslip1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


