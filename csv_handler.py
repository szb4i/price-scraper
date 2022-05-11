from enum import Enum
from typing import List, TypedDict
import pandas as pd

class PriceInfoMessage(Enum):
    IS_CLOSING_CANDLE = "x"
    OPEN_TIME = "t"
    OPEN = "o"
    HIGH = "h"
    LOW = "l"
    CLOSE = "c"
    VOLUME = "v"

class CsvHandler():
    def __init__(self) -> None:
        df = pd.DataFrame(columns = [PriceInfoMessage.IS_CLOSING_CANDLE.value, PriceInfoMessage.OPEN_TIME.value, PriceInfoMessage.OPEN.value, PriceInfoMessage.HIGH.value, PriceInfoMessage.LOW.value, PriceInfoMessage.CLOSE.value, PriceInfoMessage.VOLUME.value])
        df.to_csv("data.csv", index = False)
        self.is_closing_candle = []
        self.open_time = []
        self.open = []
        self.high = []
        self.low = []
        self.close = []
        self.volume = []

    def on_message(self, message):
        self.is_closing_candle.append(message[PriceInfoMessage.IS_CLOSING_CANDLE.value])
        self.open_time.append(message[PriceInfoMessage.OPEN_TIME.value])
        self.open.append(message[PriceInfoMessage.OPEN.value])
        self.high.append(message[PriceInfoMessage.HIGH.value])
        self.low.append(message[PriceInfoMessage.LOW.value])
        self.close.append(message[PriceInfoMessage.CLOSE.value])
        self.volume.append(message[PriceInfoMessage.VOLUME.value])
        if len(self.is_closing_candle) == 50:
            self.__append_to_csv()
            self.is_closing_candle = []
            self.open_time = []
            self.open = []
            self.high = []
            self.low = []
            self.close = []
            self.volume = []

    def __append_to_csv(self):
        data = {
            PriceInfoMessage.IS_CLOSING_CANDLE.value: self.is_closing_candle,
            PriceInfoMessage.OPEN_TIME.value: self.open_time,
            PriceInfoMessage.OPEN.value: self.open,
            PriceInfoMessage.HIGH.value: self.high,
            PriceInfoMessage.LOW.value: self.low,
            PriceInfoMessage.CLOSE.value: self.close,
            PriceInfoMessage.VOLUME.value: self.volume
        }
        df = pd.DataFrame(data)
        df.to_csv('data.csv', mode = 'a', index = False, header = False)
