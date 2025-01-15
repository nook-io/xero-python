# BatchPaymentDetails

Bank details for use on a batch payment stored with each contact

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_account_number** | **str** | Bank account number for use with Batch Payments | [optional] 
**bank_account_name** | **str** | Name of bank for use with Batch Payments | [optional] 
**details** | **str** | (Non-NZ Only) These details are sent to the org’s bank as a reference for the batch payment transaction. They will also show with the batch payment transaction in the bank reconciliation Find &amp; Match screen. Depending on your individual bank, the detail may also show on the bank statement imported into Xero. Maximum field length &#x3D; 18 | [optional] 
**code** | **str** | (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find &amp; Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero. | [optional] 
**reference** | **str** | (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find &amp; Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero. | [optional] 

## Example

```python
from xero_python.models.batch_payment_details import BatchPaymentDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BatchPaymentDetails from a JSON string
batch_payment_details_instance = BatchPaymentDetails.from_json(json)
# print the JSON string representation of the object
print BatchPaymentDetails.to_json()

# convert the object into a dict
batch_payment_details_dict = batch_payment_details_instance.to_dict()
# create an instance of BatchPaymentDetails from a dict
batch_payment_details_from_dict = BatchPaymentDetails.from_dict(batch_payment_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


