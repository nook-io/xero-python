# ExpenseClaim


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expense_claim_id** | **str** | Xero generated unique identifier for an expense claim | [optional] 
**status** | **str** | Current status of an expense claim – see status types | [optional] 
**payments** | [**List[Payment]**](Payment.md) | See Payments | [optional] 
**user** | [**User**](User.md) |  | [optional] 
**receipts** | [**List[Receipt]**](Receipt.md) |  | [optional] 
**updated_date_utc** | **str** | Last modified date UTC format | [optional] [readonly] 
**total** | **float** | The total of an expense claim being paid | [optional] [readonly] 
**amount_due** | **float** | The amount due to be paid for an expense claim | [optional] [readonly] 
**amount_paid** | **float** | The amount still to pay for an expense claim | [optional] [readonly] 
**payment_due_date** | **str** | The date when the expense claim is due to be paid YYYY-MM-DD | [optional] [readonly] 
**reporting_date** | **str** | The date the expense claim will be reported in Xero YYYY-MM-DD | [optional] [readonly] 
**receipt_id** | **str** | The Xero identifier for the Receipt e.g. e59a2c7f-1306-4078-a0f3-73537afcbba9 | [optional] 

## Example

```python
from xero_python.models.expense_claim import ExpenseClaim

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseClaim from a JSON string
expense_claim_instance = ExpenseClaim.from_json(json)
# print the JSON string representation of the object
print ExpenseClaim.to_json()

# convert the object into a dict
expense_claim_dict = expense_claim_instance.to_dict()
# create an instance of ExpenseClaim from a dict
expense_claim_from_dict = ExpenseClaim.from_dict(expense_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


