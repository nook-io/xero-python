# BatchPayment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**Account**](Account.md) |  | [optional] 
**reference** | **str** | (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find &amp; Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero. | [optional] 
**particulars** | **str** | (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find &amp; Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero. | [optional] 
**code** | **str** | (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find &amp; Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero. | [optional] 
**details** | **str** | (Non-NZ Only) These details are sent to the org’s bank as a reference for the batch payment transaction. They will also show with the batch payment transaction in the bank reconciliation Find &amp; Match screen. Depending on your individual bank, the detail may also show on the bank statement imported into Xero. Maximum field length &#x3D; 18 | [optional] 
**narrative** | **str** | (UK Only) Only shows on the statement line in Xero. Max length &#x3D;18 | [optional] 
**batch_payment_id** | **str** | The Xero generated unique identifier for the bank transaction (read-only) | [optional] [readonly] 
**date_string** | **str** | Date the payment is being made (YYYY-MM-DD) e.g. 2009-09-06 | [optional] 
**var_date** | **str** | Date the payment is being made (YYYY-MM-DD) e.g. 2009-09-06 | [optional] 
**amount** | **float** | The amount of the payment. Must be less than or equal to the outstanding amount owing on the invoice e.g. 200.00 | [optional] 
**payments** | [**List[Payment]**](Payment.md) | An array of payments | [optional] 
**type** | **str** | PAYBATCH for bill payments or RECBATCH for sales invoice payments (read-only) | [optional] [readonly] 
**status** | **str** | AUTHORISED or DELETED (read-only). New batch payments will have a status of AUTHORISED. It is not possible to delete batch payments via the API. | [optional] [readonly] 
**total_amount** | **float** | The total of the payments that make up the batch (read-only) | [optional] [readonly] 
**updated_date_utc** | **str** | UTC timestamp of last update to the payment | [optional] [readonly] 
**is_reconciled** | **bool** | Booelan that tells you if the batch payment has been reconciled (read-only) | [optional] [readonly] 
**validation_errors** | [**List[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 

## Example

```python
from xero_python.models.batch_payment import BatchPayment

# TODO update the JSON string below
json = "{}"
# create an instance of BatchPayment from a JSON string
batch_payment_instance = BatchPayment.from_json(json)
# print the JSON string representation of the object
print BatchPayment.to_json()

# convert the object into a dict
batch_payment_dict = batch_payment_instance.to_dict()
# create an instance of BatchPayment from a dict
batch_payment_from_dict = BatchPayment.from_dict(batch_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


