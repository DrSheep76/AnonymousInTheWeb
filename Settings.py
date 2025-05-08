from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6 import uic

from faker import Faker

import sys
from pathlib import Path

class Settings(QDialog):
    """
    Settings dialog for configuring name generation preferences.
    
    Provides:
    - Region/locale selection from comprehensive list
    - Gender specification (Male/Female/None)
    - Apply button to confirm selections
    """
    
    # Comprehensive region/locale mapping for Faker
    # Format: {"Display Name": "locale_code"}
    # Put "★" anywhere you like, yes, manually. 
    REGION_DICT = {
        "Not selected": None,
        "Arabic (Generic)": "ar_AA",
        "Arabic (United Arab Emirates)": "ar_AE",
        "Arabic (Bahrain)": "ar_BH",
        "Arabic (Egypt)": "ar_EG",
        "Arabic (Jordan)": "ar_JO",
        "Arabic (Palestine)": "ar_PS",
        "Arabic (Saudi Arabia)": "ar_SA",
        "Azerbaijani (Azerbaijan)": "az_AZ",
        "Bulgarian (Bulgaria)": "bg_BG",
        "Bengali (Bangladesh)": "bn_BD",
        "Bosnian (Bosnia and Herzegovina)": "bs_BA",
        "Czech (Czech Republic)": "cs_CZ",
        "Danish (Denmark)": "da_DK",
        "German (Generic)": "de",
        "German (Austria)": "de_AT",
        "German (Switzerland)": "de_CH",
        "German (Germany)": "de_DE",
        "German (Liechtenstein)": "de_LI",
        "German (Luxembourg)": "de_LU",
        "Danish (Denmark) [Alternate]": "dk_DK",
        "Greek (Cyprus)": "el_CY",
        "Greek (Greece)": "el_GR",
        "English (Generic)": "en",
        "English (Australia)": "en_AU",
        "English (Bangladesh)": "en_BD",
        "English (Canada)": "en_CA",
        "English (United Kingdom)": "en_GB",
        "English (Ireland)": "en_IE",
        "English (India)": "en_IN",
        "English (Montserrat)": "en_MS",
        "English (New Zealand)": "en_NZ",
        "English (Philippines)": "en_PH",
        "English (Pakistan)": "en_PK",
        "English (Thailand)": "en_TH",
        "English (United States)": "en_US",
        "Spanish (Generic)": "es",
        "Spanish (Argentina)": "es_AR",
        "Spanish (Canada)": "es_CA",
        "Spanish (Chile)": "es_CL",
        "Spanish (Colombia)": "es_CO",
        "Spanish (Spain)": "es_ES",
        "Spanish (Mexico)": "es_MX",
        "Estonian (Estonia)": "et_EE",
        "Persian (Iran)": "fa_IR",
        "Finnish (Finland)": "fi_FI",
        "Filipino (Philippines)": "fil_PH",
        "French (Belgium)": "fr_BE",
        "French (Canada)": "fr_CA",
        "French (Switzerland)": "fr_CH",
        "French (France)": "fr_FR",
        "French (Quebec)": "fr_QC",
        "Irish (Ireland)": "ga_IE",
        "Gujarati (India)": "gu_IN",
        "Hebrew (Israel)": "he_IL",
        "Hindi (India)": "hi_IN",
        "Zulu (South Africa)": "zu_ZA",
        "Croatian (Croatia)": "hr_HR",
        "Hungarian (Hungary)": "hu_HU",
        "Armenian (Armenia)": "hy_AM",
        "Indonesian (Indonesia)": "id_ID",
        "Italian (Switzerland)": "it_CH",
        "Italian (Italy)": "it_IT",
        "Japanese (Japan)": "ja_JP",
        "Georgian (Georgia)": "ka_GE",
        "Korean (South Korea)": "ko_KR",
        "Latin (Generic)": "la",
        "Luxembourgish (Luxembourg)": "lb_LU",
        "Lithuanian (Lithuania)": "lt_LT",
        "Latvian (Latvia)": "lv_LV",
        "Maltese (Malta)": "mt_MT",
        "Nepali (Nepal)": "ne_NP",
        "Igbo (Nigeria)": "ng_NG",
        "Dutch (Belgium)": "nl_BE",
        "Dutch (Netherlands)": "nl_NL",
        "Norwegian (Norway)": "no_NO",
        "Odia (India)": "or_IN",
        "Polish (Poland)": "pl_PL",
        "Portuguese (Brazil)": "pt_BR",
        "Portuguese (Portugal)": "pt_PT",
        "Romanian (Romania)": "ro_RO",
        "Russian (Russia)": "ru_RU",
        "Slovak (Slovakia)": "sk_SK",
        "Slovenian (Slovenia)": "sl_SI",
        "Albanian (Albania)": "sq_AL",
        "Swedish (Sweden)": "sv_SE",
        "Swahili (Generic)": "sw",
        "Tamil (India)": "ta_IN",
        "Thai (Generic)": "th",
        "Thai (Thailand)": "th_TH",
        "Tagalog (Philippines)": "tl_PH",
        "Turkish (Turkey)": "tr_TR",
        "Twi (Ghana)": "tw_GH",
        "Ukrainian (Ukraine)": "uk_UA",
        "Uzbek (Uzbekistan)": "uz_UZ",
        "Vietnamese (Vietnam)": "vi_VN",
        "Yoruba (Nigeria)": "yo_NG",
        "Chinese (China)": "zh_CN",
        "Chinese (Taiwan)": "zh_TW"
        }  

    def __init__(self, parent=None, *args, **kwargs):
        """
        Initialize settings dialog.
        
        Args:
            parent: Parent widget (main application window)
        """
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Anonymous in the Web — Settings')
        uic.loadUi(Path(__file__).parent / 'Settings.ui', self)
        self.parent = parent  # Reference to main window

        # Connect apply button and give it focus
        self.Button.clicked.connect(self.accept)
        self.Button.setFocus()

        # Populate dropdown menus
        self.Gender.addItems(('Not selected', 'Male', 'Female'))
        self.Language.addItems(self.REGION_DICT.keys())

    def get_settings(self):
        """
        Retrieve current settings from dialog.
        
        Returns:
            tuple: (region_code, gender) where:
                - region_code: str or None
                - gender: 'male', 'female', or None
        """
        _gender = self.Gender.currentText().lower()
        if _gender == 'not selected':
            _gender = None
        return (self.REGION_DICT[self.Language.currentText()], _gender)


if __name__=='__main__':
    # For standalone testing of settings dialog
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    window = Settings()
    window.show()

    sys.exit(app.exec())