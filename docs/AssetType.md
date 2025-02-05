# AssetType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_type_id** | **str** | Xero generated unique identifier for asset types | [optional] 
**asset_type_name** | **str** | The name of the asset type | 
**fixed_asset_account_id** | **str** | The asset account for fixed assets of this type | [optional] 
**depreciation_expense_account_id** | **str** | The expense account for the depreciation of fixed assets of this type | [optional] 
**accumulated_depreciation_account_id** | **str** | The account for accumulated depreciation of fixed assets of this type | [optional] 
**book_depreciation_setting** | [**BookDepreciationSetting**](BookDepreciationSetting.md) |  | 
**locks** | **int** | All asset types that have accumulated depreciation for any assets that use them are deemed ‘locked’ and cannot be removed. | [optional] 

## Example

```python
from xero_python.models.asset_type import AssetType

# TODO update the JSON string below
json = "{}"
# create an instance of AssetType from a JSON string
asset_type_instance = AssetType.from_json(json)
# print the JSON string representation of the object
print AssetType.to_json()

# convert the object into a dict
asset_type_dict = asset_type_instance.to_dict()
# create an instance of AssetType from a dict
asset_type_from_dict = AssetType.from_dict(asset_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


