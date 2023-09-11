import detectlanguage
import unittest
import json

detectlanguage.configuration.api_key = "8df729e6c77caed3593ca12c940683ee"



# set up classe LangaugeCalls where our langauge functions will be located
class LanguageCalls():
    def __init__(self, uInput):
        self.uInput = uInput
        self.langList = [{'code': 'aa', 'name': 'AFAR'}, {'code': 'ab', 'name': 'ABKHAZIAN'}, {'code': 'af', 'name': 'AFRIKAANS'}, {'code': 'ak', 'name': 'AKAN'}, {'code': 'am', 'name': 'AMHARIC'}, {'code': 'ar', 'name': 'ARABIC'}, {'code': 'as', 'name': 'ASSAMESE'}, {'code': 'ay', 'name': 'AYMARA'}, {'code': 'az', 'name': 'AZERBAIJANI'}, {'code': 'ba', 'name': 'BASHKIR'}, {'code': 'be', 'name': 'BELARUSIAN'}, {'code': 'bg', 'name': 'BULGARIAN'}, {'code': 'bh', 'name': 'BIHARI'}, {'code': 'bi', 'name': 'BISLAMA'}, {'code': 'bn', 'name': 'BENGALI'}, {'code': 'bo', 'name': 'TIBETAN'}, {'code': 'br', 'name': 'BRETON'}, {'code': 'bs', 'name': 'BOSNIAN'}, {'code': 'bug', 'name': 'BUGINESE'}, {'code': 'ca', 'name': 'CATALAN'}, {'code': 'ceb', 'name': 'CEBUANO'}, {'code': 'chr', 'name': 'CHEROKEE'}, {'code': 'co', 'name': 'CORSICAN'}, {'code': 'crs', 'name': 'SESELWA'}, {'code': 'cs', 'name': 'CZECH'}, {'code': 'cy', 'name': 'WELSH'}, {'code': 'da', 'name': 'DANISH'}, {'code': 'de', 'name': 'GERMAN'}, {'code': 'dv', 'name': 'DHIVEHI'}, {'code': 'dz', 'name': 'DZONGKHA'}, {'code': 'egy', 'name': 'EGYPTIAN'}, {'code': 'el', 'name': 'GREEK'}, {'code': 'en', 'name': 'ENGLISH'}, {'code': 'eo', 'name': 'ESPERANTO'}, {'code': 'es', 'name': 'SPANISH'}, {'code': 'et', 'name': 'ESTONIAN'}, {'code': 'eu', 'name': 'BASQUE'}, {'code': 'fa', 'name': 'PERSIAN'}, {'code': 'fi', 'name': 'FINNISH'}, {'code': 'fj', 'name': 'FIJIAN'}, {'code': 'fo', 'name': 'FAROESE'}, {'code': 'fr', 'name': 'FRENCH'}, {'code': 'fy', 'name': 'FRISIAN'}, {'code': 'ga', 'name': 'IRISH'}, {'code': 'gd', 'name': 'SCOTS_GAELIC'}, {'code': 'gl', 'name': 'GALICIAN'}, {'code': 'gn', 'name': 'GUARANI'}, {'code': 'got', 'name': 'GOTHIC'}, {'code': 'gu', 'name': 'GUJARATI'}, {'code': 'gv', 'name': 'MANX'}, {'code': 'ha', 'name': 'HAUSA'}, {'code': 'haw', 'name': 'HAWAIIAN'}, {'code': 'hi', 'name': 'HINDI'}, {'code': 'hmn', 'name': 'HMONG'}, {'code': 'hr', 'name': 'CROATIAN'}, {'code': 'ht', 'name': 'HAITIAN_CREOLE'}, {'code': 'hu', 'name': 'HUNGARIAN'}, {'code': 'hy', 'name': 'ARMENIAN'}, {'code': 'ia', 'name': 'INTERLINGUA'}, {'code': 'id', 'name': 'INDONESIAN'}, {'code': 'ie', 'name': 'INTERLINGUE'}, {'code': 'ig', 'name': 'IGBO'}, {'code': 'ik', 'name': 'INUPIAK'}, {'code': 'is', 'name': 'ICELANDIC'}, {'code': 'it', 'name': 'ITALIAN'}, {'code': 'iu', 'name': 'INUKTITUT'}, {'code': 'iw', 'name': 'HEBREW'}, {'code': 'ja', 'name': 'JAPANESE'}, {'code': 'jw', 'name': 'JAVANESE'}, {'code': 'ka', 'name': 'GEORGIAN'}, {'code': 'kha', 'name': 'KHASI'}, {'code': 'kk', 'name': 'KAZAKH'}, {'code': 'kl', 'name': 'GREENLANDIC'}, {'code': 'km', 'name': 'KHMER'}, {'code': 'kn', 'name': 'KANNADA'}, {'code': 'ko', 'name': 'KOREAN'}, {'code': 'ks', 'name': 'KASHMIRI'}, {'code': 'ku', 'name': 'KURDISH'}, {'code': 'ky', 'name': 'KYRGYZ'}, {'code': 'la', 'name': 'LATIN'}, {'code': 'lb', 'name': 'LUXEMBOURGISH'}, {'code': 'lg', 'name': 'GANDA'}, {'code': 'lif', 'name': 'LIMBU'}, {'code': 'ln', 'name': 'LINGALA'}, {'code': 'lo', 'name': 'LAOTHIAN'}, {'code': 'lt', 'name': 'LITHUANIAN'}, {'code': 'lv', 'name': 'LATVIAN'}, {'code': 'mfe', 'name': 'MAURITIAN_CREOLE'}, {'code': 'mg', 'name': 'MALAGASY'}, {'code': 'mi', 'name': 'MAORI'}, {'code': 'mk', 'name': 'MACEDONIAN'}, {'code': 'ml', 'name': 'MALAYALAM'}, {'code': 'mn', 'name': 'MONGOLIAN'}, {'code': 'mr', 'name': 'MARATHI'}, {'code': 'ms', 'name': 'MALAY'}, {'code': 'mt', 'name': 'MALTESE'}, {'code': 'my', 'name': 'BURMESE'}, {'code': 'na', 'name': 'NAURU'}, {'code': 'ne', 'name': 'NEPALI'}, {'code': 'nl', 'name': 'DUTCH'}, {'code': 'no', 'name': 'NORWEGIAN'}, {'code': 'nr', 'name': 'NDEBELE'}, {'code': 'nso', 'name': 'PEDI'}, {'code': 'ny', 'name': 'NYANJA'}, {'code': 'oc', 'name': 'OCCITAN'}, {'code': 'om', 'name': 'OROMO'}, {'code': 'or', 'name': 'ORIYA'}, {'code': 'pa', 'name': 'PUNJABI'}, {'code': 'pl', 'name': 'POLISH'}, {'code': 'ps', 'name': 'PASHTO'}, {'code': 'pt', 'name': 'PORTUGUESE'}, {'code': 'qu', 'name': 'QUECHUA'}, {'code': 'rm', 'name': 'RHAETO_ROMANCE'}, {'code': 'rn', 'name': 'RUNDI'}, {'code': 'ro', 'name': 'ROMANIAN'}, {'code': 'ru', 'name': 'RUSSIAN'}, {'code': 'rw', 'name': 'KINYARWANDA'}, {'code': 'sa', 'name': 'SANSKRIT'}, {'code': 'sco', 'name': 'SCOTS'}, {'code': 'sd', 'name': 'SINDHI'}, {'code': 'sg', 'name': 'SANGO'}, {'code': 'si', 'name': 'SINHALESE'}, {'code': 'sk', 'name': 'SLOVAK'}, {'code': 'sl', 'name': 'SLOVENIAN'}, {'code': 'sm', 'name': 'SAMOAN'}, {'code': 'sn', 'name': 'SHONA'}, {'code': 'so', 'name': 'SOMALI'}, {'code': 'sq', 'name': 'ALBANIAN'}, {'code': 'sr', 'name': 'SERBIAN'}, {'code': 'ss', 'name': 'SISWANT'}, {'code': 'st', 'name': 'SESOTHO'}, {'code': 'su', 'name': 'SUNDANESE'}, {'code': 'sv', 'name': 'SWEDISH'}, {'code': 'sw', 'name': 'SWAHILI'}, {'code': 'syr', 'name': 'SYRIAC'}, {'code': 'ta', 'name': 'TAMIL'}, {'code': 'te', 'name': 'TELUGU'}, {'code': 'tg', 'name': 'TAJIK'}, {'code': 'th', 'name': 'THAI'}, {'code': 'ti', 'name': 'TIGRINYA'}, {'code': 'tk', 'name': 'TURKMEN'}, {'code': 'tl', 'name': 'TAGALOG'}, {'code': 'tlh', 'name': 'KLINGON'}, {'code': 'tn', 'name': 'TSWANA'}, {'code': 'to', 'name': 'TONGA'}, {'code': 'tr', 'name': 'TURKISH'}, {'code': 'ts', 'name': 'TSONGA'}, {'code': 'tt', 'name': 'TATAR'}, {'code': 'ug', 'name': 'UIGHUR'}, {'code': 'uk', 'name': 'UKRAINIAN'}, {'code': 'ur', 'name': 'URDU'}, {'code': 'uz', 'name': 'UZBEK'}, {'code': 've', 'name': 'VENDA'}, {'code': 'vi', 'name': 'VIETNAMESE'}, {'code': 'vo', 'name': 'VOLAPUK'}, {'code': 'war', 'name': 'WARAY_PHILIPPINES'}, {'code': 'wo', 'name': 'WOLOF'}, {'code': 'xh', 'name': 'XHOSA'}, {'code': 'yi', 'name': 'YIDDISH'}, {'code': 'yo', 'name': 'YORUBA'}, {'code': 'za', 'name': 'ZHUANG'}, {'code': 'zh', 'name': 'CHINESE_SIMPLIFIED'}, {'code': 'zh-Hant', 'name': 'CHINESE_TRADITIONAL'}, {'code': 'zu', 'name': 'ZULU'}]
        self.gibberish = []
    # outputs detailed info including whether the API considers its detection reliable, the confidence score, and the langauge code 
    def detailedOutput(self, word):
        return detectlanguage.detect(word)

    def simpleOutput(self, word):
        return detectlanguage.simple_detect(word)

    def languageDecetion(self):
        langCodeList = []
        langList = []
        words = self.uInput
        if words == '':
                return 'Blank'
        words = words.split()
        for word in words:
            try:
                langCode = self.simpleOutput(word)
            except IndexError:
                langCode = 'gibberish'
            if langCode not in langCodeList:
                langCodeList.append(langCode)
        for langCode in langCodeList:    
            for language in self.langList:
                if language['code'] == langCode:
                    langList.append(language['name'].lower())
        langList = [i.capitalize() for i in langList]
        return (', '.join(langList))
                    

class tests(unittest.TestCase):
    
    def test_spanish(self):
        esp = 'Buenos dias señor'
        self.assertEqual('spanish', LanguageCalls(esp).languageDecetion())

    def test_eng(self):
        en = 'Good morning sir'
        self.assertEqual('english', LanguageCalls(en).languageDecetion())


if __name__ == '__main__':
    unittest.main()
    tests.test_spanish()
    
