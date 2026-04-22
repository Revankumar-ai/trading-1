from bot.exceptions import ValidationError

VALID_SIDES = {"BUY", "SELL"}
VALID_TYPES = {"MARKET", "LIMIT"}

def validate(symbol, side, order_type, quantity, price):
    if not symbol.endswith("USDT"):
        raise ValidationError("Only USDT pairs supported")

    if side not in VALID_SIDES:
        raise ValidationError("Side must be BUY or SELL")

    if order_type not in VALID_TYPES:
        raise ValidationError("Type must be MARKET or LIMIT")

    if quantity <= 0:
        raise ValidationError("Quantity must be > 0")

    if order_type == "LIMIT" and not price:
        raise ValidationError("LIMIT order requires price")