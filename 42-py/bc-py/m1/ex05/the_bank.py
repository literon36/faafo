class Account(object):
    ID_COUNT = 1
    def __init__(self, name :str, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount :int):
        self.value += amount

class Bank(object):
    """The Bank"""
    def __init__(self):
        self.accounts = []

    def check_account_corr(self, acc :Account) -> bool:
        """check if Account is corrupted"""
        if (
            len(acc.__dict__) % 2 == 0
            or any(attr.startswith("b") for attr in acc.__dict__.keys())
            or not any(attr.startswith("zip") or attr.startswith("addr") for attr in acc.__dict__.keys())
            or not any(attr in ["name", "id", "value"] for attr in acc.__dict__.keys())
            ):
            return True
        return False

    def add(self, new_account :Account) -> bool:
        """Add an account to the bank"""
        if (
            new_account in self.accounts
            or new_account.name in [account.name for account in self.accounts]
            or self.check_account_corr(new_account)
            ):
            return False
        self.accounts.append(new_account)
        return True

    def transfer(self, origin :str, dest :str, amount: int):
        """Perform the fund transfer"""
        origin_account :Account = [account for account in self.accounts if account.name == origin][0]
        dest_account :Account = [account for account in self.accounts if account.name == dest][0]
        if (
            origin_account and dest_account not in self.accounts
            or self.check_account_corr(origin_account)
            or self.check_account_corr(dest_account)
            or amount < 0
            or origin_account.value < amount
            ):
            return False
        elif origin_account == dest_account:
            return True
        origin_account.transfer(-amount)
        dest_account.transfer(amount)
        return True
        
    def fix_account(self, name :str):
        """Fix corrupted account"""
        for account in self.accounts:
            if account.name == name:
                while self.check_account_corr(account):
                    #user input for address, id and value
                    account.__dict__.update({
                        "addr" : input("Enter address: "),
                        "id" : int(input("Enter id: ")),
                        "value" : int(input("Enter value: "))})
                return True
        return False