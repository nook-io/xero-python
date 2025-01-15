# PayslipLines


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**earnings_lines** | [**List[EarningsLine1]**](EarningsLine1.md) |  | [optional] 
**leave_earnings_lines** | [**List[LeaveEarningsLine1]**](LeaveEarningsLine1.md) |  | [optional] 
**timesheet_earnings_lines** | [**List[EarningsLine1]**](EarningsLine1.md) |  | [optional] 
**deduction_lines** | [**List[DeductionLine1]**](DeductionLine1.md) |  | [optional] 
**leave_accrual_lines** | [**List[LeaveAccrualLine1]**](LeaveAccrualLine1.md) |  | [optional] 
**reimbursement_lines** | [**List[ReimbursementLine1]**](ReimbursementLine1.md) |  | [optional] 
**superannuation_lines** | [**List[SuperannuationLine]**](SuperannuationLine.md) |  | [optional] 
**tax_lines** | [**List[TaxLine1]**](TaxLine1.md) |  | [optional] 

## Example

```python
from xero_python.models.payslip_lines import PayslipLines

# TODO update the JSON string below
json = "{}"
# create an instance of PayslipLines from a JSON string
payslip_lines_instance = PayslipLines.from_json(json)
# print the JSON string representation of the object
print PayslipLines.to_json()

# convert the object into a dict
payslip_lines_dict = payslip_lines_instance.to_dict()
# create an instance of PayslipLines from a dict
payslip_lines_from_dict = PayslipLines.from_dict(payslip_lines_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


