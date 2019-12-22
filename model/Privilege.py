import json


class Privilege(object):

    def __init__(self):
        self.id = None
        self.fee = None
        self.payed = None
        self.st = None
        self.pl = None
        self.dl = None
        self.sp = None
        self.cp = None
        self.subp = None
        self.cs = None
        self.maxbr = None
        self.fl = None
        self.toast = None
        self.flag = None

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_fee(self, fee):
        self.fee = fee

    def get_fee(self):
        return self.fee

    def set_payed(self, payed):
        self.payed = payed

    def get_payed(self):
        return self.payed

    def set_st(self, st):
        self.st = st

    def get_st(self):
        return self.st

    def set_pl(self, pl):
        self.pl = pl

    def get_pl(self):
        return self.pl

    def set_dl(self, dl):
        self.dl = dl

    def get_dl(self):
        return self.dl

    def set_sp(self, sp):
        self.sp = sp

    def get_sp(self):
        return self.sp

    def set_cp(self, cp):
        self.cp = cp

    def get_cp(self):
        return self.cp

    def set_subp(self, subp):
        self.subp = subp

    def get_subp(self):
        return self.subp

    def set_cs(self, cs):
        self.cs = cs

    def get_cs(self):
        return self.cs

    def set_maxbr(self, maxbr):
        self.maxbr = maxbr

    def get_maxbr(self):
        return self.maxbr

    def set_fl(self, fl):
        self.fl = fl

    def get_fl(self):
        return self.fl

    def set_toast(self, toast):
        self.toast = toast

    def get_toast(self):
        return self.toast

    def set_flag(self, flag):
        self.flag = flag

    def get_flag(self):
        return self.flag

    def dict_to_object(dictObject: dict, object):
        for k, v in dictObject.items():
            object.__dict__[k] = v
        return object

    def to_string(self):
        return json.dumps({
            'id': self.get_id(),
            'fee': self.get_fee(),
            'payed': self.get_payed(),
            'st': self.get_st(),
            'pl': self.get_pl(),
            'dl': self.get_dl(),
            'sp': self.get_sp(),
            'cp': self.get_cp(),
            'subp': self.get_subp(),
            'cs': self.get_cs(),
            'maxbr': self.get_maxbr(),
            'fl': self.get_fl(),
            'toast': self.get_toast(),
            'flag': self.get_flag(),
        }, ensure_ascii=False)

    def to_json(self):
        return {
            'id': self.get_id(),
            'fee': self.get_fee(),
            'payed': self.get_payed(),
            'st': self.get_st(),
            'pl': self.get_pl(),
            'dl': self.get_dl(),
            'sp': self.get_sp(),
            'cp': self.get_cp(),
            'subp': self.get_subp(),
            'cs': self.get_cs(),
            'maxbr': self.get_maxbr(),
            'fl': self.get_fl(),
            'toast': self.get_toast(),
            'flag': self.get_flag(),
        }


def generate_setter_getter():
    privilege = Privilege()
    print(privilege.__dict__)
    for k in privilege.__dict__:
        print("def set_" + k + "(self," + k + "):")
        print("\tself." + k, "=" + k)
        print("def get_" + k + "(self):")
        print("\treturn self." + k)


def generate_to_string():
    privilege = Privilege()
    print(privilege.__dict__)
    result = 'def to_string(self):\n'
    result += '\treturn json.dumps({\n'
    for k in privilege.__dict__:
        result += "\t\t'" + k + "'" + ":" + " self.get_" + k + "(),\n"
    result += "\t}, ensure_ascii=False)"
    print(result)


def generate_to_json():
    privilege = Privilege()
    print(privilege.__dict__)
    result = 'def to_json(self):\n'
    result += '\treturn {\n'
    for k in privilege.__dict__:
        result += "\t\t'" + k + "'" + ":" + " self.get_" + k + "(),\n"
    result += "\t}"
    print(result)


def test_dict_to_object():
    privilege_dict = {'id': 514235010, 'fee': 4, 'payed': 5, 'st': 0, 'pl': 999000, 'dl': 999000, 'sp': 7, 'cp': 1,
                      'subp': 1, 'cs': False, 'maxbr': 999000, 'fl': 0, 'toast': False, 'flag': 0}
    privilege = Privilege.dict_to_object(privilege_dict, Privilege())
    print(privilege.to_json())
    print(privilege.to_string())


if __name__ == '__main__':
    # generate_setter_getter()
    # generate_to_string()
    # generate_to_json()
    test_dict_to_object()
