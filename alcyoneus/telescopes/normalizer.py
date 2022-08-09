from datetime import datetime
import re


class ConvertToDatetime:
    # Regex pattern
    DATE_PATTERN = re.compile("(\d+)[/-](\d+)[/-](\d+)")
    TIME_PATTERN = re.compile("(\d+:\d+)")

    def __call__(self, raw_value, *args, **kwargs):
        if raw_value is None:
            return None
        date_match = re.match(self.DATE_PATTERN, raw_value)
        time_match = re.match(self.TIME_PATTERN, raw_value)
        if date_match and time_match:
            raw_datetime_str = time_match.group(1)
            if len(date_match.group(3)) == 4:
                raw_datetime_str += f' {date_match.group(1)}/{date_match.group(2)}/{date_match.group(3)}'
            else:
                raw_datetime_str += f' {date_match.group(3)}/{date_match.group(2)}/{date_match.group(1)}'
            raw_datetime_str = datetime.strptime(raw_datetime_str, "%d-%m-%Y %H:%M")
            return raw_datetime_str.strftime("%Y-%m-%d %H:%M:%S")

