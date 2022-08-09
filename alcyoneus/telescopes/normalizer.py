from datetime import datetime

import re
import json
import unicodedata

class NormalizeText:
    VI_ACCENTS_RULES = [("òa", "oà"), ("óa", "oá"), ("ỏa", "oả"), ("õa", "oã"), ("ọa", "oạ"), ("òe", "oè"),
                        ("óe", "oé"), ("ỏe", "oẻ"), ("õe", "oẽ"), ("ọe", "oẹ"), ("ùy", "uỳ"), ("úy", "uý"),
                        ("ủy", "uỷ"), ("ũy", "uỹ"), ("ụy", "uỵ"), ("Ủy", "Uỷ")]

    @staticmethod
    def remove_special_char(raw_value):
        norm_value = re.sub(u"\xad|\u200b|\ufeff", "", raw_value)
        norm_value = re.sub(u"\xc2|\xa0", " ", norm_value)
        norm_value = unicodedata.normalize("NFKD", norm_value)
        return norm_value

    def normalize_vi_accents(self, raw_value):
        for src, tgt in self.VI_ACCENTS_RULES:
            raw_value = re.sub(src, tgt, raw_value)
        return raw_value

    def __call__(self, raw_value, *args, **kwargs):
        if raw_value is None:
            return None
        norm_value = re.sub(' +', ' ', raw_value)
        return norm_value.strip()
class NormalizeAuthor:
    def __call__(self, raw_value, *args, **kwargs):
        if raw_value is None:
            return None
        norm_value = re.sub('Theo', '', raw_value)
        return norm_value.strip()
class ConvertToJsonString:
    def __call__(self, raw_value, *args, **kwargs):
        if isinstance(raw_value, str):
            return json.dumps([raw_value], ensure_ascii=False)
        else:
            return json.dumps(raw_value, ensure_ascii=False)

class ConvertToDatetime:
    # Regex pattern
    DATETIME_PATTERN_1 = re.compile(".*(\d+-\d+-\d+).*(\d+:\d+).*(PM|AM)")

    def __call__(self, raw_value, *args, **kwargs):
        if raw_value is None:
            return None
        if re.match(self.DATETIME_PATTERN_1, raw_value):
            m = re.match(self.DATETIME_PATTERN_1, raw_value)
            raw_datetime_str = f'{m.group(1)} {m.group(2)}'
            raw_datetime_str = datetime.strptime(raw_datetime_str, "%d-%m-%Y %H:%M")
            return raw_datetime_str.strftime("%Y-%m-%d %H:%M:%S")
        return None

