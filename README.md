# jandi

```
from jandi import *

if __name__ == "__main__":
    url: str = <Jandi Connect Incomming Webhook URL>
    jandi = Jandi(url)
    headline = "[[PizzaHouse]](http://url_to_text) You have a new Pizza order."
    jandi.push_info(title="Topping", description="Pepperoni")
    jandi.push_info("Location", "Empire State Building, 5th Ave, New York")
    resp = jandi.send(headline=headline, color=jandi.Colors.RED)
    print(resp)

```
