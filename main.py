import ctypes, json, os, random, threading, webbrowser, bitcoin, requests, urllib3
from urllib.request import Request, urlopen

#r = requests.get("https://api.npoint.io/581658a8d1b548e2b780").json()
#cto = r["cto"] follow my c.to)

checked_wallet, wallet_without_balance, wallet_with_balance, = (
    0,
    0,
    0,
)

def run_wal():
    global checked_wallet, wallet_without_balance, wallet_with_balance, count

    while -0 >= 0:
        valid_private_key = False

        while not valid_private_key:

            private_key = bitcoin.random_key()
            decoded_private_key = bitcoin.decode_privkey(private_key, "hex")
            valid_private_key = 0 < decoded_private_key < bitcoin.N

        wif_encoded_private_key = bitcoin.encode_privkey(decoded_private_key, "wif")
        public_key = bitcoin.fast_multiply(bitcoin.G, decoded_private_key)

        rk = requests.get(
            url="https://blockchain.info/balance?active="
            + bitcoin.pubkey_to_address(public_key)
        ).text
        y = json.loads(rk)

        for v in y:
            balance = y["final_balance"]

        a = f"\n\n      Address: {bitcoin.pubkey_to_address(public_key)}\n      Private Key: {private_key}\n      Balance: {balance}\n"
        print(a)

        checked_wallet += 1

        if balance == "0":
            wallet_without_balance += 1
            try:
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Made by  escriminal  |  Checked Wallet: {checked_wallet}  | Wallet with BTC: {wallet_with_balance}"
                )
            except BaseException:
                sys.stdout.write(
                    f"\x1b]2;Made by escriminal |  Checked Wallet: {checked_wallet}  | Wallet with BTC: {wallet_with_balance}\x07"
                )

            with open("results_without_BTC.txt", "a") as text_file:
                text_file.write(a.replace("-", ""))

            count = open("results_without_BTC.txt", "r").read().count("Address: ")

        else:
            wallet_with_balance += 1
            try:
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Made by escriminal |  Checked Wallet: {checked_wallet}  | Wallet with BTC: {wallet_with_balance}"
                )
            except BaseException:
                sys.stdout.write(
                    f"\x1b]2;Made by escriminal |  Checked Wallet: {checked_wallet}  | Wallet with BTC: {wallet_with_balance}\x07"
                )
            with open("results_with_BTC.txt", "a") as text_file:
                text_file.write(a.replace("-", " "))


def a():
    try:
        t = int(input("How many threads?: "))
        try:
            threads = []
            for i in range(t):
                t = threading.Thread(target=run_wal)
                t.start()
        except Exception as cx:
            print(cx)
            input()
    except BaseException:
        a()


a()
