import typer
from rich import print
from rich.panel import Panel

from bot.orders import place_order
from bot.validators import validate
from bot.exceptions import ValidationError, OrderError
from bot.logger import setup_logging

# ✅ Initialize logging (file only)
setup_logging()

app = typer.Typer()
trade_app = typer.Typer()
app.add_typer(trade_app, name="trade")


@trade_app.command()
def place(
    symbol: str = typer.Option(...),
    side: str = typer.Option(...),
    order_type: str = typer.Option(...),
    quantity: float = typer.Option(...),
    price: float = typer.Option(None)
):
    try:
        # ✅ Validate input
        validate(symbol, side, order_type, quantity, price)

        # ✅ Order summary panel
        print(Panel.fit(f"Placing {order_type} order for {symbol}"))

        # ✅ Call order function
        result = place_order(symbol, side, order_type, quantity, price)

        # ✅ Clean CLI output (as required)
        print("\n[bold]Order Request:[/bold]")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        if order_type.upper() == "LIMIT":
            print(f"Price: {price}")

        print("\n[bold]Order Response:[/bold]")
        print(f"Order ID: {result['orderId']}")
        print(f"Status: {result['status']}")
        print(f"Executed Quantity: {result['executedQty']}")
        print(f"Average Price: {result['avgPrice']}")

        print("\n[green]✅ Order executed successfully[/green]")

    except ValidationError as ve:
        print(f"[red]Validation Error: {ve}[/red]")

    except OrderError as oe:
        print(f"[red]Order Error: {oe}[/red]")

    except Exception as e:
        print(f"[red]Unexpected Error: {e}[/red]")


if __name__ == "__main__":
    app()