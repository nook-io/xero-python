# Item


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | User defined item code (max length &#x3D; 30) | 
**inventory_asset_account_code** | **str** | The inventory asset account for the item. The account must be of type INVENTORY. The  COGSAccountCode in PurchaseDetails is also required to create a tracked item | [optional] 
**name** | **str** | The name of the item (max length &#x3D; 50) | [optional] 
**is_sold** | **bool** | Boolean value, defaults to true. When IsSold is true the item will be available on sales transactions in the Xero UI. If IsSold is updated to false then Description and SalesDetails values will be nulled. | [optional] 
**is_purchased** | **bool** | Boolean value, defaults to true. When IsPurchased is true the item is available for purchase transactions in the Xero UI. If IsPurchased is updated to false then PurchaseDescription and PurchaseDetails values will be nulled. | [optional] 
**description** | **str** | The sales description of the item (max length &#x3D; 4000) | [optional] 
**purchase_description** | **str** | The purchase description of the item (max length &#x3D; 4000) | [optional] 
**purchase_details** | [**Purchase**](Purchase.md) |  | [optional] 
**sales_details** | [**Purchase**](Purchase.md) |  | [optional] 
**is_tracked_as_inventory** | **bool** | True for items that are tracked as inventory. An item will be tracked as inventory if the InventoryAssetAccountCode and COGSAccountCode are set. | [optional] 
**total_cost_pool** | **float** | The value of the item on hand. Calculated using average cost accounting. | [optional] 
**quantity_on_hand** | **float** | The quantity of the item on hand | [optional] 
**updated_date_utc** | **str** | Last modified date in UTC format | [optional] [readonly] 
**item_id** | **str** | The Xero identifier for an Item | [optional] 
**status_attribute_string** | **str** | Status of object | [optional] 
**validation_errors** | [**List[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 

## Example

```python
from xero_python.models.item import Item

# TODO update the JSON string below
json = "{}"
# create an instance of Item from a JSON string
item_instance = Item.from_json(json)
# print the JSON string representation of the object
print Item.to_json()

# convert the object into a dict
item_dict = item_instance.to_dict()
# create an instance of Item from a dict
item_from_dict = Item.from_dict(item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


