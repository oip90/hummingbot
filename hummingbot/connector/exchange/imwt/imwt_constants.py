import sys

from hummingbot.core.api_throttler.data_types import RateLimit
from hummingbot.core.data_type.common import TradeType
from hummingbot.core.data_type.in_flight_order import OrderState

MAX_ID_LEN = 32
SECONDS_TO_WAIT_TO_RECEIVE_MESSAGE = 600
PING_TIMEOUT = 20

DEFAULT_DOMAIN = ""

# URLs

IMWT_BASE_URL = "https://imwt.me/"

# Doesn't include base URL as the tail is required to generate the signature

IMWT_SERVER_TIME_PATH = '/api/public/v1/servertime'
IMWT_INSTRUMENTS_PATH = '/api/public/v1/pairs'
IMWT_FEES_AND_LIMITS_PATH = '/api/public/v1/limits'
IMWT_TICKER_PATH = '/api/public/v1/ticker'
IMWT_ORDER_BOOK_PATH = '/api/public/v1/orderbook/{pair}'

# Auth required
IMWT_PLACE_ORDER_PATH = '/api/public/v1/order'
IMWT_ORDER_DETAILS_PATH = '/api/public/v1/order/{order_id}'
IMWT_ORDER_CANCEL_PATH = '/api/public/v1/order/{order_id}'
IMWT_BALANCE_PATH = '/api/public/v1/balance'
IMWT_TRADE_FILLS_PATH = "/api/public/v1/matches"  # todo

# WS
IMWT_WS_BASE_DOMAIN = "imwt.me:8000"
IMWT_WS_URI_PUBLIC = f"ws://{IMWT_WS_BASE_DOMAIN}/wsapi/v1/live_notifications"
IMWT_WS_URI_PRIVATE = f"ws://{IMWT_WS_BASE_DOMAIN}/wsapi/v1/live_notifications"


IMWT_WS_ACCOUNT_CHANNEL = "balance"
IMWT_WS_OPENED_ORDERS_CHANNEL = "opened_orders"
IMWT_WS_CLOSED_ORDERS_CHANNEL = "closed_orders"
# IMWT_WS_USER_TRADES_CHANNEL = "user_trades"
IMWT_WS_PUBLIC_TRADES_CHANNEL = "trades"
IMWT_WS_PUBLIC_BOOKS_CHANNEL = "stack"


WS_CONNECTION_LIMIT_ID = "WSConnection"
WS_REQUEST_LIMIT_ID = "WSRequest"
WS_SUBSCRIPTION_LIMIT_ID = "WSSubscription"
WS_LOGIN_LIMIT_ID = "WSLogin"

ORDER_STATE = {
    "live": OrderState.OPEN,
    "filled": OrderState.FILLED,
    "partially_filled": OrderState.PARTIALLY_FILLED,
    "canceled": OrderState.CANCELED,
}

TRADE_TYPES_MAP = {
    TradeType.BUY: 0,
    TradeType.SELL: 1,
}


NO_LIMIT = sys.maxsize

RATE_LIMITS = [
    RateLimit(WS_CONNECTION_LIMIT_ID, limit=10, time_interval=1),
    RateLimit(WS_REQUEST_LIMIT_ID, limit=10, time_interval=1),
    RateLimit(WS_SUBSCRIPTION_LIMIT_ID, limit=10, time_interval=1),
    RateLimit(WS_LOGIN_LIMIT_ID, limit=10, time_interval=1),
    RateLimit(limit_id=IMWT_SERVER_TIME_PATH, limit=10, time_interval=1),
    RateLimit(limit_id=IMWT_INSTRUMENTS_PATH, limit=10, time_interval=1),
    RateLimit(limit_id=IMWT_TICKER_PATH, limit=10, time_interval=1),
    RateLimit(limit_id=IMWT_ORDER_BOOK_PATH, limit=10, time_interval=1),
    RateLimit(limit_id=IMWT_PLACE_ORDER_PATH, limit=10, time_interval=1),
    RateLimit(limit_id=IMWT_ORDER_DETAILS_PATH, limit=10, time_interval=1),
    RateLimit(limit_id=IMWT_ORDER_CANCEL_PATH, limit=10, time_interval=1),
    RateLimit(limit_id=IMWT_BALANCE_PATH, limit=10, time_interval=1),
    RateLimit(limit_id=IMWT_TRADE_FILLS_PATH, limit=10, time_interval=1),
    RateLimit(limit_id=IMWT_FEES_AND_LIMITS_PATH, limit=10, time_interval=1),
]
