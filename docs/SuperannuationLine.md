# SuperannuationLine


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**super_membership_id** | **str** | Xero identifier for payroll super fund membership ID. | [optional] 
**contribution_type** | [**SuperannuationContributionType**](SuperannuationContributionType.md) |  | [optional] 
**calculation_type** | [**SuperannuationCalculationType**](SuperannuationCalculationType.md) |  | [optional] 
**minimum_monthly_earnings** | **float** | Superannuation minimum monthly earnings. | [optional] 
**expense_account_code** | **str** | Superannuation expense account code. | [optional] 
**liability_account_code** | **str** | Superannuation liability account code | [optional] 
**payment_date_for_this_period** | **str** | Superannuation payment date for the current period (YYYY-MM-DD) | [optional] 
**percentage** | **float** | Superannuation percentage | [optional] 
**amount** | **float** | Superannuation amount | [optional] 

## Example

```python
from xero_python.models.superannuation_line import SuperannuationLine

# TODO update the JSON string below
json = "{}"
# create an instance of SuperannuationLine from a JSON string
superannuation_line_instance = SuperannuationLine.from_json(json)
# print the JSON string representation of the object
print SuperannuationLine.to_json()

# convert the object into a dict
superannuation_line_dict = superannuation_line_instance.to_dict()
# create an instance of SuperannuationLine from a dict
superannuation_line_from_dict = SuperannuationLine.from_dict(superannuation_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


