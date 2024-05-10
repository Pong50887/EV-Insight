from dataclasses import dataclass


@dataclass
class Conversion:

    conversion_rates = {
        'EUR': 1,  # Germany
        'USD': 1.08,  # US Dollar
        'THB': 34.57,  # Thai Baht
        'JPY': 116.20,  # Japanese Yen
        'GBP': 0.88,  # British Pound Sterling
        'AUD': 1.56,  # Australian Dollar
        'CAD': 1.45,  # Canadian Dollar
        'CHF': 1.00,  # Swiss Franc
        'CNY': 7.02,  # Chinese Yuan Renminbi
        'SEK': 10.24,  # Swedish
        'NZD': 1.65,  # New Zealand Dollar
        'KRW': 1355.92,  # South Korean Won
        'SGD': 1.51,  # Singapore Dollar
        'NOK': 10.50,  # Norwegian Krone
        'MXN': 23.18,  # Mexican Peso
        'INR': 80.60,  # Indian Rupee
        'BRL': 6.33,  # Brazilian Real
        'RUB': 82.77,  # Russian Ruble
        'ZAR': 17.86,  # South African Rand
        'TRY': 11.57,  # Turkish Lira
        'AED': 3.97,  # UAE Dirham
        'HKD': 8.40,  # Hong Kong Dollar
        'DKK': 7.44,  # Danish Krone
        'PLN': 4.45,  # Polish Zloty
        'IDR': 15415.67,  # Indonesian Rupiah
        'HUF': 356.98,  # Hungarian Forint
        'CZK': 25.56,  # Czech Koruna
        'ILS': 3.55,  # Israeli Shekel
        'PHP': 57.72,  # Philippine Peso
        'MYR': 4.47,  # Malaysian Ringgit
        'ARS': 107.53,  # Argentine Peso
        'CLP': 812.37,  # Chilean Peso
        'PEN': 4.13,  # Peruvian Sol
        'COP': 4324.52,  # Colombian Peso
        'VND': 24988.13,  # Vietnamese Dong
        'UAH': 30.05,  # Ukrainian Hryvnia
        'KWD': 0.33,  # Kuwaiti Dinar
        'QAR': 3.92,  # Qatari Riyal
        'SAR': 4.07,  # Saudi Riyal
        'BDT': 91.10,  # Bangladeshi Taka
        'NGN': 461.83,  # Nigerian Naira
        'EGP': 18.05,  # Egyptian Pound
        'PKR': 192.95,  # Pakistani Rupee
        'IRR': 45789.42,  # Iranian Rial
        'IQD': 1577.45,  # Iraqi Dinar
        'KES': 122.47,  # Kenyan Shilling
        'LKR': 236.29,  # Sri Lankan Rupee
        'GHS': 7.18,  # Ghanaian Cedi
    }

    def get_currency_names(self):
        return list(self.conversion_rates.keys())

    def get_conversion(self, currency_name):
        return self.conversion_rates.get(currency_name.upper())
