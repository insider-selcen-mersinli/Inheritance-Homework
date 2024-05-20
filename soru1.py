class WebPush(object):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
        self.platform = platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type

    def send_push(self):
        print("\n**********************************************")
        if self.push_type == "TriggerPush":
            print(self.push_type, "gönderildi!")
        elif self.push_type == "BulkPush":
            print(self.push_type, "gönderildi!")
        elif self.push_type == "PriceAlertPush":
            print(self.push_type, "gönderildi!")
        elif self.push_type == "InStockPush":
            print(self.push_type, "gönderildi!")
        else:
            print("Tanımlanamayan Push türü.")


class TriggerPush(WebPush):
    def __init__(self, trigger_page, platform, optin, global_frequency_capping, start_date, end_date, language,
                 push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.trigger_page = trigger_page


class BulkPush(WebPush):
    def __init__(self, send_date, platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.send_date = send_date


class PriceAlertPush(WebPush):
    def __init__(self, price_info, discount_rate, platform, optin, global_frequency_capping, start_date, end_date,
                 language, push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.price_info = price_info
        self.discount_rate = discount_rate

    def discountPrice(self, price_info, discount_rate):
        discount_price = price_info - ((price_info / 100) * discount_rate)
        return discount_price


class InStockPush(WebPush):
    def __init__(self, stock_info, platform, optin, global_frequency_capping, start_date, end_date, language,
                 push_type):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.stock_info = stock_info

    def stockUpdate(self, stock_info):
        self.stock_info = stock_info
        return self.stock_info


web_push = WebPush("web", True, 3, "2024-04-11",
                   "2024-04-18", "en", "WebPush")

trigger_push = TriggerPush("home", "web", True, 3, "2024-04-11",
                           "2024-04-18", "en", "TriggerPush")
trigger_push.send_push()

bulk_push = BulkPush(20240611, "web", True, 3, "2024-04-11",
                     "2024-04-18", "en", "BulkPush")
bulk_push.send_push()

price_alert_push = PriceAlertPush(500, 20.0, "web", True, 3, "2024-04-11",
                                  "2024-04-18", "en", "PriceAlertPush")
discount_rate = price_alert_push.discountPrice(price_alert_push.price_info, price_alert_push.discount_rate)
price_alert_push.send_push()
print("\nDiscount Price: ", discount_rate)


inStock_push = InStockPush(True, "web", True, 3, "2024-04-11",
                           "2024-04-18", "en", "InStockPush")
inStock_push.send_push()
print("\nStock Info: ", inStock_push.stockUpdate(False))
