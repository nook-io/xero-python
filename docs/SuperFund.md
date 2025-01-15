# SuperFund


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**super_fund_id** | **str** | Xero identifier for a super fund | [optional] 
**type** | [**SuperFundType**](SuperFundType.md) |  | 
**name** | **str** | Name of the super fund | [optional] 
**abn** | **str** | ABN of the self managed super fund | [optional] 
**bsb** | **str** | BSB of the self managed super fund | [optional] 
**account_number** | **str** | The account number for the self managed super fund. | [optional] 
**account_name** | **str** | The account name for the self managed super fund. | [optional] 
**electronic_service_address** | **str** | The electronic service address for the self managed super fund. | [optional] 
**employer_number** | **str** | Some funds assign a unique number to each employer | [optional] 
**spin** | **str** | The SPIN of the Regulated SuperFund. This field has been deprecated. It will only be present for legacy superfunds. New superfunds will not have a SPIN value. The USI field should be used instead of SPIN. | [optional] 
**usi** | **str** | The USI of the Regulated SuperFund | [optional] 
**updated_date_utc** | **str** | Last modified timestamp | [optional] [readonly] 
**validation_errors** | [**List[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 

## Example

```python
from xero_python.models.super_fund import SuperFund

# TODO update the JSON string below
json = "{}"
# create an instance of SuperFund from a JSON string
super_fund_instance = SuperFund.from_json(json)
# print the JSON string representation of the object
print SuperFund.to_json()

# convert the object into a dict
super_fund_dict = super_fund_instance.to_dict()
# create an instance of SuperFund from a dict
super_fund_from_dict = SuperFund.from_dict(super_fund_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


