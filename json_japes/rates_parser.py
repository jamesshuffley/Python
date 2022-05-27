import json


class RatesParser:
    def __init__(self, file_path):
        rates = self._open_json_file(file_path)
        self.base_rate = rates["base"]
        self.date = rates["date"]
        self.gbp = rates["rates"]["GBP"]
        self.usd = rates["rates"]["USD"]
        self.jpy = rates["rates"]["JPY"]

    def _open_json_file(self, file_path: str) -> dict:
        with open(file_path) as json_file:
            return json.load(json_file)


if __name__ == "__main__":
    rp = RatesParser("exchange_rates.json")
    print(rp.gbp)
    print(rp.base_rate)
    print(rp.date)
