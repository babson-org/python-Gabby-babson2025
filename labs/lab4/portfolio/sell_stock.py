
import time
import prices as _prices

def _find_position(self, sym):
    for p in self.positions:
        if p.get("sym") == sym:
            return p
    return None

def portfolio_sell_stock(self, sym: str, shares: float, price: float):
    """TODO:
    - Ensure symbol exists (use _find_position())
    - Ensure shares <= owned
    - Fetch last-close price via _prices.get_last_close_map([sym]) (use this price to sell shares)
    - Reduce position shares; adjust  'cost' proportionally by shares. (assumes average cost accounting)
    - Remove the position if shares drop to 0
    - Increase self.cash by proceeds
    - Hint: the amount you reduce cost is NOT the same as the amount you increase cash
    """
    pos = _find_position(self, sym)
    if pos is None:
        print("Position not found")
        return
    if shares <= 0 or shares > pos["shares"]:
        print("Not enough shares")
        return
    
        px = _prices.get_last_close_map([sym])[sym]

  # proportional cost reduction
    cost_reduction = pos["cost"] * (shares / pos["shares"])
    pos["shares"] -= shares
    pos["cost"] -= cost_reduction
    self.cash += shares * px 

    if pos["shares"] == 0:
        self.positions.remove(pos)

    return
       
