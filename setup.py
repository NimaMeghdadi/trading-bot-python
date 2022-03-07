import asyncio
if msg['topic'] == '/market/ticker:ETH-USDT':
            print(f'got ETH-USDT tick:{msg["data"]}')
# await ksm.subscribe('/market/ticker:ETH-USDT')