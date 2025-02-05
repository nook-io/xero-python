# coding: utf-8

"""
    merged spec

    merged spec

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xero_python.models.asset_type import AssetType  # noqa: E501


class TestAssetType(unittest.TestCase):
    """AssetType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AssetType:
        """Test AssetType
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AssetType`
        """
        model = AssetType()  # noqa: E501
        if include_optional:
            return AssetType(
                asset_type_id = '5da209c5-5e19-4a43-b925-71b776c49ced',
                asset_type_name = 'Computer Equipment',
                fixed_asset_account_id = '24e260f1-bfc4-4766-ad7f-8a8ce01de879',
                depreciation_expense_account_id = 'b23fc79b-d66b-44b0-a240-e138e086fcbc',
                accumulated_depreciation_account_id = 'ca4c6b39-4f4f-43e8-98da-5e1f350a6694',
                book_depreciation_setting = xero_python.models.book_depreciation_setting.BookDepreciationSetting(
                    depreciation_method = 'StraightLine', 
                    averaging_method = 'ActualDays', 
                    depreciation_rate = 0.05, 
                    effective_life_years = 5, 
                    depreciation_calculation_method = 'None', 
                    depreciable_object_id = '68f17094-af97-4f1b-b36b-013b45b6ad3c', 
                    depreciable_object_type = 'Asset', 
                    book_effective_date_of_change_id = '68f17094-af97-4f1b-b36b-013b45b6ad3c', ),
                locks = 33
            )
        else:
            return AssetType(
                asset_type_name = 'Computer Equipment',
                book_depreciation_setting = xero_python.models.book_depreciation_setting.BookDepreciationSetting(
                    depreciation_method = 'StraightLine', 
                    averaging_method = 'ActualDays', 
                    depreciation_rate = 0.05, 
                    effective_life_years = 5, 
                    depreciation_calculation_method = 'None', 
                    depreciable_object_id = '68f17094-af97-4f1b-b36b-013b45b6ad3c', 
                    depreciable_object_type = 'Asset', 
                    book_effective_date_of_change_id = '68f17094-af97-4f1b-b36b-013b45b6ad3c', ),
        )
        """

    def testAssetType(self):
        """Test AssetType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
