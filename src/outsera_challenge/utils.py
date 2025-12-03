import re


class Utils:
    @staticmethod
    def split_names(names: str) -> list[str]:
        return [name.strip() for name in re.split(r",|\sand\s", names) if name.strip()]
