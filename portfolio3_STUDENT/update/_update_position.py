def _update_position(active_client, transaction):
    # helper function to only be used inside create_transaction    

# Yes, cash position is adjusted
# No, we do not have to add to the transaction list, as it should be in the "buy" section
    if transaction['type'] == 'CONTRIBUTION':
        if active_client['positions']:
            for position in active_client['positions']:                
                if position['symbol'] == transaction['symbol']:
                    position['shares'] += transaction['shares']
        else:
            position = {'id': transaction['id'],            
            'shares': round(transaction['shares'], 2),
            'symbol': transaction['symbol'],
            'name': transaction['name'],
            'avg_cost': transaction['trn_price']}

            active_client['positions'].append(position)    # or client['positions].append(position)
    elif transaction['type'] == 'BUY':
        pass
    elif transaction['type'] == 'SELL':
        pass
    elif transaction['type'] == 'WITHDRAWAL':
        pass
    else:
        print('FATAL ERROR: we should never get here _update_postion')
        exit()
    return