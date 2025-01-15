# BookDepreciationSetting


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**depreciation_method** | **str** | The method of depreciation applied to this asset. See Depreciation Methods | [optional] 
**averaging_method** | **str** | The method of averaging applied to this asset. See Averaging Methods | [optional] 
**depreciation_rate** | **float** | The rate of depreciation (e.g. 0.05) | [optional] 
**effective_life_years** | **int** | Effective life of the asset in years (e.g. 5) | [optional] 
**depreciation_calculation_method** | **str** | See Depreciation Calculation Methods | [optional] 
**depreciable_object_id** | **str** | Unique Xero identifier for the depreciable object | [optional] 
**depreciable_object_type** | **str** | The type of asset object | [optional] 
**book_effective_date_of_change_id** | **str** | Unique Xero identifier for the effective date change | [optional] 

## Example

```python
from xero_python.models.book_depreciation_setting import BookDepreciationSetting

# TODO update the JSON string below
json = "{}"
# create an instance of BookDepreciationSetting from a JSON string
book_depreciation_setting_instance = BookDepreciationSetting.from_json(json)
# print the JSON string representation of the object
print BookDepreciationSetting.to_json()

# convert the object into a dict
book_depreciation_setting_dict = book_depreciation_setting_instance.to_dict()
# create an instance of BookDepreciationSetting from a dict
book_depreciation_setting_from_dict = BookDepreciationSetting.from_dict(book_depreciation_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


