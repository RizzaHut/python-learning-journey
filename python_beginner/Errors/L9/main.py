def purchase_item(price, gold_available):
    if gold_available < price:
        raise Exception("not enough gold")
    return gold_available - price
