# Payslip


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_slip_id** | **str** | The Xero identifier for a Payslip | [optional] 
**employee_id** | **str** | The Xero identifier for payroll employee | [optional] 
**pay_run_id** | **str** | The Xero identifier for the associated payrun | [optional] 
**last_edited** | **date** | The date payslip was last updated | [optional] 
**first_name** | **str** | Employee first name | [optional] 
**last_name** | **str** | Employee last name | [optional] 
**total_earnings** | **float** | Total earnings before any deductions. Same as gross earnings for UK. | [optional] 
**gross_earnings** | **float** | Total earnings before any deductions. Same as total earnings for UK. | [optional] 
**total_pay** | **float** | The employee net pay | [optional] 
**total_employer_taxes** | **float** | The employer&#39;s tax obligation | [optional] 
**total_employee_taxes** | **float** | The part of an employee&#39;s earnings that is deducted for tax purposes | [optional] 
**total_deductions** | **float** | Total amount subtracted from an employee&#39;s earnings to reach total pay | [optional] 
**total_reimbursements** | **float** | Total reimbursements are nontaxable payments to an employee used to repay out-of-pocket expenses when the person incurs those expenses through employment | [optional] 
**total_court_orders** | **float** | Total amounts required by law to subtract from the employee&#39;s earnings | [optional] 
**total_benefits** | **float** | Benefits (also called fringe benefits, perquisites or perks) are various non-earnings compensations provided to employees in addition to their normal earnings or salaries | [optional] 
**bacs_hash** | **str** | BACS Service User Number | [optional] 
**payment_method** | **str** | The payment method code | [optional] 
**earnings_lines** | [**List[EarningsLine]**](EarningsLine.md) |  | [optional] 
**leave_earnings_lines** | [**List[LeaveEarningsLine]**](LeaveEarningsLine.md) |  | [optional] 
**timesheet_earnings_lines** | [**List[TimesheetEarningsLine]**](TimesheetEarningsLine.md) |  | [optional] 
**deduction_lines** | [**List[DeductionLine]**](DeductionLine.md) |  | [optional] 
**reimbursement_lines** | [**List[ReimbursementLine]**](ReimbursementLine.md) |  | [optional] 
**leave_accrual_lines** | [**List[LeaveAccrualLine]**](LeaveAccrualLine.md) |  | [optional] 
**benefit_lines** | [**List[BenefitLine]**](BenefitLine.md) |  | [optional] 
**payment_lines** | [**List[PaymentLine]**](PaymentLine.md) |  | [optional] 
**employee_tax_lines** | [**List[TaxLine]**](TaxLine.md) |  | [optional] 
**employer_tax_lines** | [**List[TaxLine]**](TaxLine.md) |  | [optional] 
**court_order_lines** | [**List[CourtOrderLine]**](CourtOrderLine.md) |  | [optional] 

## Example

```python
from xero_python.models.payslip import Payslip

# TODO update the JSON string below
json = "{}"
# create an instance of Payslip from a JSON string
payslip_instance = Payslip.from_json(json)
# print the JSON string representation of the object
print Payslip.to_json()

# convert the object into a dict
payslip_dict = payslip_instance.to_dict()
# create an instance of Payslip from a dict
payslip_from_dict = Payslip.from_dict(payslip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


