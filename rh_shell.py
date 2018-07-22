import requests
from six.moves.urllib.request import getproxies
import getpass

class RobinHood:

    endpoints = {
        "login": "https://api.robinhood.com/api-token-auth/",
        "logout": "https://api.robinhood.com/api-token-logout/",
        "account": "https://api.robinhood.com/accounts/",
        "user": "https://api.robinhood.com/user/",
        "investment_profile": "https://api.robinhood.com/user/",
        "accounts": "https://api.robinhood.com/accounts/",
        "ach_iav_auth": "https://api.robinhood.com/ach/iav/auth/",
        "ach_relationships": "https://api.robinhood.com/ach/relationships/",
        "ach_transfers": "https://api.robinhood.com/ach/transfers/",
        "applications": "https://api.robinhood.com/applications/",
        "dividends": "https://api.robinhood.com/dividends/",
        "edocuments": "https://api.robinhood.com/documents/",
        "instruments": "https://api.robinhood.com/instruments/",
        "instruments_popularity": "https://api.robinhood.com/instruments/popularity/",
        "margin_upgrades": "https://api.robinhood.com/margin/upgrades/",
        "markets": "https://api.robinhood.com/markets/",
        "notifications": "https://api.robinhood.com/notifications/",
        "options_positions": "https://api.robinhood.com/options/positions/",
        "orders": "https://api.robinhood.com/orders/",
        "password_reset": "https://api.robinhood.com/password_reset/request/",
        "portfolios": "https://api.robinhood.com/portfolios/",
        "positions": "https://api.robinhood.com/positions/",
        "quotes": "https://api.robinhood.com/quotes/",
        "historicals": "https://api.robinhood.com/quotes/historicals/",
        "document_requests": "https://api.robinhood.com/upload/document_requests/",
        "user": "https://api.robinhood.com/user/",
        "watchlists": "https://api.robinhood.com/watchlists/",
        "news": "https://api.robinhood.com/midlands/news/",
        "ratings": "https://api.robinhood.com/midlands/ratings/",
        "fundamentals": "https://api.robinhood.com/fundamentals/",
        "options": "https://api.robinhood.com/options/",
        "marketdata": "https://api.robinhood.com/marketdata/"
    }

    session = None
    headers = None
    token = None

    def __init__(self):
        self.session = requests.session()
        self.session.proxies = getproxies()
        self.headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en;q=1, fr;q=0.9, de;q=0.8, ja;q=0.7, nl;q=0.6, it;q=0.5",
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            "X-Robinhood-API-Version": "1.0.0",
            "Connection": "keep-alive",
            "User-Agent": "Robinhood/823 (iPhone; iOS 7.1.2; Scale/2.00)",
            "Origin": "https://robinhood.com"
        }
        self.session.headers = self.headers

    def display_options(self):
        print("|****************************************|")
        print("|* p: displays current portfolio        *|")
        print("|* b <symbol> <quantity> <order>: buy   *|")
        print("|* s <symbol> <quantity> <order>: sell  *|")
        print("|* o: shows all open orders             *|")
        print("|* c: cancel an order                   *|")
        print("|* h: display help menu                 *|")
        print("|* e: exit                              *|")
        print("|****************************************|")

    def main_menu(self):
        self.display_options()
        while(1):
            command_string = input("> ")
            command_options = command_string.split(" ")
            command = command_options[0]
            if command=="e":
                self.logout()
                print("thank you for using the shell.")
                print("goodbye.")
                exit(0)
            elif command=="h":
                self.display_options()
            elif command=="p":
                self.show_portfolio()
            elif command=="b":
                if len(command_options) != 4:
                    print("invalid buy options.")
                    print("usage: b <symbol> <quantity> <order>")
                else:
                    self.buy()
            elif command=="s":
                if len(command_options) != 4:
                    print("invalid sell options.")
                    print("usage: s <symbol> <quantity> <order>")
                else:
                    self.sell()
            elif command=="o":
                self.show_open_orders()
            elif command=="c":
                self.cancel_order()
            elif command=="":
                continue
            else:
                print("invalid command.")


    def login(self):
        user = input("username: ")
        password = getpass.getpass('password:')

        payload = {
            'password': password,
            'username': user,
        }

        try:
            resp = self.session.post(self.endpoints['login'], data=payload)
            data = resp.json()
        except requests.exceptions.HTTPError:
            print("login failed. goodbye.")
            print(resp)
            exit(1)

        if 'token' in data.keys():
            self.token = data['token']
            self.headers['Authorization'] = 'Token ' + self.token
            print("successfully logged in")


    def logout(self):
        try:
            resp = self.session.post(self.endpoints['logout'])
        except requests.exceptions.HTTPError:
            print("couldn't log out.")

        print("succesfully logged out")
        self.headers['Authorization'] = None
        self.token = None


    def show_portfolio(self):
        print("curent portfolio: ")
        try:
            resp = self.session.get(self.endpoints['account'])
        except requests.exceptions.HTTPError:
            print("couldn't get portfolio.")

        results = resp.json()['results'][0]
        port = results['portfolio']
        self.endpoints['portfolio'] = port
        resp = self.session.get(self.endpoints['portfolio'])
        print(resp.json())

    def buy(self):
        print("NEED TO IMPLEMENT BUY")

    def sell(self):
        print("NEED TO IMPLEMENT SELL")

    def show_open_orders(self):
        print("NEED TO IMPLEMENT OPEN ORDERS")

    def cancel_order(self):
        print("NEED TO IMPLEMENT CANCEL ORDER")


if __name__ == "__main__":
    print("welcome to the Robinhood shell.")
    trader = RobinHood()
    trader.login()
    trader.main_menu()


