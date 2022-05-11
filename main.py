from binance.client import Client
import credentials
from web_socket import WebSocket

if __name__ == "__main__":
    client = Client(credentials.getBinanceKey(), credentials.getBinanceSecretKey())
    web_socket = WebSocket()
    web_socket.run_forever()
