import json
import websocket
from datetime import datetime
from configuration import CANDLE_INTERVAL, TRADE_SYMBOL
from csv_handler import CsvHandler

class WebSocket():
    def __init__(self) -> None:
        self.csv_handler = CsvHandler()
    
    def run_forever(self):
        SOCKET = ("wss://fstream.binance.com/ws/{}@kline_{}").format(TRADE_SYMBOL.lower(),CANDLE_INTERVAL)
        ws=websocket.WebSocketApp(SOCKET, 
            on_open = lambda ws: self.__on_open(ws), 
            on_message = lambda ws,msg: self.__on_message(ws, msg),
            on_error = lambda ws,error: self.__on_error(ws, error),
            on_close = lambda ws,close_status_code,close_msg: self.__on_close(ws, close_status_code, close_msg),
        )
        ws.run_forever()

    def __print_time(self):
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    def __on_open(self,ws):
        self.__print_time()
        print("Connection Opened")

    def __on_close(self, ws, close_status_code, close_msg):
        self.__print_time()
        print("Connection Closed:" + "\n" + str(close_status_code) + "\n" + str(close_msg))

    def __on_error(self, ws, error):
        self.__print_time()
        print("Connection Error:" + "\n" + str(error))

    def __on_message(self, ws, message):
        json_message = json.loads(message)
        price_message = json_message["k"]
        self.csv_handler.on_message(price_message)
