from tenacity import retry, stop_after_attempt, wait_fixed
import logging

from bot.client import get_client
from bot.exceptions import OrderError

# ✅ Use global logger (configured in cli.py)
logger = logging.getLogger("trading_bot")

client = get_client()


@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def place_order(symbol, side, order_type, quantity, price=None):
    try:
        # ✅ Log request
        logger.info(f"Request -> {symbol} {side} {order_type} qty={quantity} price={price}")

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type.upper() == "LIMIT":
            params.update({
                "price": price,
                "timeInForce": "GTC"
            })

        # ✅ Place order
        response = client.futures_create_order(**params)
        logger.info(f"Response -> {response}")

        # ✅ Fetch updated status (important for MARKET orders)
        order_status = client.futures_get_order(
            symbol=symbol,
            orderId=response["orderId"]
        )
        logger.info(f"Updated Status -> {order_status}")

        # ✅ Return only required fields (assignment requirement)
        return {
            "orderId": order_status.get("orderId"),
            "status": order_status.get("status"),
            "executedQty": order_status.get("executedQty"),
            "avgPrice": order_status.get("avgPrice"),
        }

    except Exception as e:
        logger.error(f"Order failed: {e}")
        raise OrderError(str(e))