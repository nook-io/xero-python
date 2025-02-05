"""
merged spec

merged spec

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import json
import re  # noqa: F401

from aenum import Enum


class TimeZone(str, Enum):
    """
    Timezone specifications
    """

    """
    allowed enum values
    """
    AFGHANISTANSTANDARDTIME = "AFGHANISTANSTANDARDTIME"
    ALASKANSTANDARDTIME = "ALASKANSTANDARDTIME"
    ALEUTIANSTANDARDTIME = "ALEUTIANSTANDARDTIME"
    ALTAISTANDARDTIME = "ALTAISTANDARDTIME"
    ARABIANSTANDARDTIME = "ARABIANSTANDARDTIME"
    ARABICSTANDARDTIME = "ARABICSTANDARDTIME"
    ARABSTANDARDTIME = "ARABSTANDARDTIME"
    ARGENTINASTANDARDTIME = "ARGENTINASTANDARDTIME"
    ASTRAKHANSTANDARDTIME = "ASTRAKHANSTANDARDTIME"
    ATLANTICSTANDARDTIME = "ATLANTICSTANDARDTIME"
    AUSCENTRALSTANDARDTIME = "AUSCENTRALSTANDARDTIME"
    AUSCENTRALWSTANDARDTIME = "AUSCENTRALWSTANDARDTIME"
    AUSEASTERNSTANDARDTIME = "AUSEASTERNSTANDARDTIME"
    AZERBAIJANSTANDARDTIME = "AZERBAIJANSTANDARDTIME"
    AZORESSTANDARDTIME = "AZORESSTANDARDTIME"
    BAHIASTANDARDTIME = "BAHIASTANDARDTIME"
    BANGLADESHSTANDARDTIME = "BANGLADESHSTANDARDTIME"
    BELARUSSTANDARDTIME = "BELARUSSTANDARDTIME"
    BOUGAINVILLESTANDARDTIME = "BOUGAINVILLESTANDARDTIME"
    CANADACENTRALSTANDARDTIME = "CANADACENTRALSTANDARDTIME"
    CAPEVERDESTANDARDTIME = "CAPEVERDESTANDARDTIME"
    CAUCASUSSTANDARDTIME = "CAUCASUSSTANDARDTIME"
    CENAUSTRALIASTANDARDTIME = "CENAUSTRALIASTANDARDTIME"
    CENTRALAMERICASTANDARDTIME = "CENTRALAMERICASTANDARDTIME"
    CENTRALASIASTANDARDTIME = "CENTRALASIASTANDARDTIME"
    CENTRALBRAZILIANSTANDARDTIME = "CENTRALBRAZILIANSTANDARDTIME"
    CENTRALEUROPEANSTANDARDTIME = "CENTRALEUROPEANSTANDARDTIME"
    CENTRALEUROPESTANDARDTIME = "CENTRALEUROPESTANDARDTIME"
    CENTRALPACIFICSTANDARDTIME = "CENTRALPACIFICSTANDARDTIME"
    CENTRALSTANDARDTIME = "CENTRALSTANDARDTIME"
    CENTRALSTANDARDTIME_LEFT_PARENTHESIS_MEXICO_RIGHT_PARENTHESIS = "CENTRALSTANDARDTIME(MEXICO)"
    CHATHAMISLANDSSTANDARDTIME = "CHATHAMISLANDSSTANDARDTIME"
    CHINASTANDARDTIME = "CHINASTANDARDTIME"
    CUBASTANDARDTIME = "CUBASTANDARDTIME"
    DATELINESTANDARDTIME = "DATELINESTANDARDTIME"
    EAFRICASTANDARDTIME = "EAFRICASTANDARDTIME"
    EASTERISLANDSTANDARDTIME = "EASTERISLANDSTANDARDTIME"
    EASTERNSTANDARDTIME = "EASTERNSTANDARDTIME"
    EASTERNSTANDARDTIME_LEFT_PARENTHESIS_MEXICO_RIGHT_PARENTHESIS = "EASTERNSTANDARDTIME(MEXICO)"
    EAUSTRALIASTANDARDTIME = "EAUSTRALIASTANDARDTIME"
    EEUROPESTANDARDTIME = "EEUROPESTANDARDTIME"
    EGYPTSTANDARDTIME = "EGYPTSTANDARDTIME"
    EKATERINBURGSTANDARDTIME = "EKATERINBURGSTANDARDTIME"
    ESOUTHAMERICASTANDARDTIME = "ESOUTHAMERICASTANDARDTIME"
    FIJISTANDARDTIME = "FIJISTANDARDTIME"
    FLESTANDARDTIME = "FLESTANDARDTIME"
    GEORGIANSTANDARDTIME = "GEORGIANSTANDARDTIME"
    GMTSTANDARDTIME = "GMTSTANDARDTIME"
    GREENLANDSTANDARDTIME = "GREENLANDSTANDARDTIME"
    GREENWICHSTANDARDTIME = "GREENWICHSTANDARDTIME"
    GTBSTANDARDTIME = "GTBSTANDARDTIME"
    HAITISTANDARDTIME = "HAITISTANDARDTIME"
    HAWAIIANSTANDARDTIME = "HAWAIIANSTANDARDTIME"
    INDIASTANDARDTIME = "INDIASTANDARDTIME"
    IRANSTANDARDTIME = "IRANSTANDARDTIME"
    ISRAELSTANDARDTIME = "ISRAELSTANDARDTIME"
    JORDANSTANDARDTIME = "JORDANSTANDARDTIME"
    KALININGRADSTANDARDTIME = "KALININGRADSTANDARDTIME"
    KAMCHATKASTANDARDTIME = "KAMCHATKASTANDARDTIME"
    KOREASTANDARDTIME = "KOREASTANDARDTIME"
    LIBYASTANDARDTIME = "LIBYASTANDARDTIME"
    LINEISLANDSSTANDARDTIME = "LINEISLANDSSTANDARDTIME"
    LORDHOWESTANDARDTIME = "LORDHOWESTANDARDTIME"
    MAGADANSTANDARDTIME = "MAGADANSTANDARDTIME"
    MAGALLANESSTANDARDTIME = "MAGALLANESSTANDARDTIME"
    MARQUESASSTANDARDTIME = "MARQUESASSTANDARDTIME"
    MAURITIUSSTANDARDTIME = "MAURITIUSSTANDARDTIME"
    MIDATLANTICSTANDARDTIME = "MIDATLANTICSTANDARDTIME"
    MIDDLEEASTSTANDARDTIME = "MIDDLEEASTSTANDARDTIME"
    MONTEVIDEOSTANDARDTIME = "MONTEVIDEOSTANDARDTIME"
    MOROCCOSTANDARDTIME = "MOROCCOSTANDARDTIME"
    MOUNTAINSTANDARDTIME = "MOUNTAINSTANDARDTIME"
    MOUNTAINSTANDARDTIME_LEFT_PARENTHESIS_MEXICO_RIGHT_PARENTHESIS = "MOUNTAINSTANDARDTIME(MEXICO)"
    MYANMARSTANDARDTIME = "MYANMARSTANDARDTIME"
    NAMIBIASTANDARDTIME = "NAMIBIASTANDARDTIME"
    NCENTRALASIASTANDARDTIME = "NCENTRALASIASTANDARDTIME"
    NEPALSTANDARDTIME = "NEPALSTANDARDTIME"
    NEWFOUNDLANDSTANDARDTIME = "NEWFOUNDLANDSTANDARDTIME"
    NEWZEALANDSTANDARDTIME = "NEWZEALANDSTANDARDTIME"
    NORFOLKSTANDARDTIME = "NORFOLKSTANDARDTIME"
    NORTHASIAEASTSTANDARDTIME = "NORTHASIAEASTSTANDARDTIME"
    NORTHASIASTANDARDTIME = "NORTHASIASTANDARDTIME"
    NORTHKOREASTANDARDTIME = "NORTHKOREASTANDARDTIME"
    OMSKSTANDARDTIME = "OMSKSTANDARDTIME"
    PACIFICSASTANDARDTIME = "PACIFICSASTANDARDTIME"
    PACIFICSTANDARDTIME = "PACIFICSTANDARDTIME"
    PACIFICSTANDARDTIME_LEFT_PARENTHESIS_MEXICO_RIGHT_PARENTHESIS = "PACIFICSTANDARDTIME(MEXICO)"
    PAKISTANSTANDARDTIME = "PAKISTANSTANDARDTIME"
    PARAGUAYSTANDARDTIME = "PARAGUAYSTANDARDTIME"
    QYZYLORDASTANDARDTIME = "QYZYLORDASTANDARDTIME"
    ROMANCESTANDARDTIME = "ROMANCESTANDARDTIME"
    RUSSIANSTANDARDTIME = "RUSSIANSTANDARDTIME"
    RUSSIATIMEZONE10 = "RUSSIATIMEZONE10"
    RUSSIATIMEZONE11 = "RUSSIATIMEZONE11"
    RUSSIATIMEZONE3 = "RUSSIATIMEZONE3"
    SAEASTERNSTANDARDTIME = "SAEASTERNSTANDARDTIME"
    SAINTPIERRESTANDARDTIME = "SAINTPIERRESTANDARDTIME"
    SAKHALINSTANDARDTIME = "SAKHALINSTANDARDTIME"
    SAMOASTANDARDTIME = "SAMOASTANDARDTIME"
    SAOTOMESTANDARDTIME = "SAOTOMESTANDARDTIME"
    SAPACIFICSTANDARDTIME = "SAPACIFICSTANDARDTIME"
    SARATOVSTANDARDTIME = "SARATOVSTANDARDTIME"
    SAWESTERNSTANDARDTIME = "SAWESTERNSTANDARDTIME"
    SEASIASTANDARDTIME = "SEASIASTANDARDTIME"
    SINGAPORESTANDARDTIME = "SINGAPORESTANDARDTIME"
    SOUTHAFRICASTANDARDTIME = "SOUTHAFRICASTANDARDTIME"
    SOUTHSUDANSTANDARDTIME = "SOUTHSUDANSTANDARDTIME"
    SRILANKASTANDARDTIME = "SRILANKASTANDARDTIME"
    SUDANSTANDARDTIME = "SUDANSTANDARDTIME"
    SYRIASTANDARDTIME = "SYRIASTANDARDTIME"
    TAIPEISTANDARDTIME = "TAIPEISTANDARDTIME"
    TASMANIASTANDARDTIME = "TASMANIASTANDARDTIME"
    TOCANTINSSTANDARDTIME = "TOCANTINSSTANDARDTIME"
    TOKYOSTANDARDTIME = "TOKYOSTANDARDTIME"
    TOMSKSTANDARDTIME = "TOMSKSTANDARDTIME"
    TONGASTANDARDTIME = "TONGASTANDARDTIME"
    TRANSBAIKALSTANDARDTIME = "TRANSBAIKALSTANDARDTIME"
    TURKEYSTANDARDTIME = "TURKEYSTANDARDTIME"
    TURKSANDCAICOSSTANDARDTIME = "TURKSANDCAICOSSTANDARDTIME"
    ULAANBAATARSTANDARDTIME = "ULAANBAATARSTANDARDTIME"
    USEASTERNSTANDARDTIME = "USEASTERNSTANDARDTIME"
    USMOUNTAINSTANDARDTIME = "USMOUNTAINSTANDARDTIME"
    UTC = "UTC"
    UTC_PLUS_12 = "UTC+12"
    UTC_PLUS_13 = "UTC+13"
    UTC02 = "UTC02"
    UTC08 = "UTC08"
    UTC09 = "UTC09"
    UTC11 = "UTC11"
    VENEZUELASTANDARDTIME = "VENEZUELASTANDARDTIME"
    VLADIVOSTOKSTANDARDTIME = "VLADIVOSTOKSTANDARDTIME"
    VOLGOGRADSTANDARDTIME = "VOLGOGRADSTANDARDTIME"
    WAUSTRALIASTANDARDTIME = "WAUSTRALIASTANDARDTIME"
    WCENTRALAFRICASTANDARDTIME = "WCENTRALAFRICASTANDARDTIME"
    WESTASIASTANDARDTIME = "WESTASIASTANDARDTIME"
    WESTBANKSTANDARDTIME = "WESTBANKSTANDARDTIME"
    WESTPACIFICSTANDARDTIME = "WESTPACIFICSTANDARDTIME"
    WEUROPESTANDARDTIME = "WEUROPESTANDARDTIME"
    WMONGOLIASTANDARDTIME = "WMONGOLIASTANDARDTIME"
    YAKUTSKSTANDARDTIME = "YAKUTSKSTANDARDTIME"
    YUKONSTANDARDTIME = "YUKONSTANDARDTIME"

    @classmethod
    def from_json(cls, json_str: str) -> "TimeZone":
        """Create an instance of TimeZone from a JSON string"""
        return TimeZone(json.loads(json_str))
