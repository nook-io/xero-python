# BookDepreciationDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_capital_gain** | **float** | When an asset is disposed, this will be the sell price minus the purchase price if a profit was made. | [optional] 
**current_gain_loss** | **float** | When an asset is disposed, this will be the lowest one of sell price or purchase price, minus the current book value. | [optional] 
**depreciation_start_date** | **date** | YYYY-MM-DD | [optional] 
**cost_limit** | **float** | The value of the asset you want to depreciate, if this is less than the cost of the asset. | [optional] 
**residual_value** | **float** | The value of the asset remaining when you&#39;ve fully depreciated it. | [optional] 
**prior_accum_depreciation_amount** | **float** | All depreciation prior to the current financial year. | [optional] 
**current_accum_depreciation_amount** | **float** | All depreciation occurring in the current financial year. | [optional] 

## Example

```python
from xero_python.models.book_depreciation_detail import BookDepreciationDetail

# TODO update the JSON string below
json = "{}"
# create an instance of BookDepreciationDetail from a JSON string
book_depreciation_detail_instance = BookDepreciationDetail.from_json(json)
# print the JSON string representation of the object
print BookDepreciationDetail.to_json()

# convert the object into a dict
book_depreciation_detail_dict = book_depreciation_detail_instance.to_dict()
# create an instance of BookDepreciationDetail from a dict
book_depreciation_detail_from_dict = BookDepreciationDetail.from_dict(book_depreciation_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


