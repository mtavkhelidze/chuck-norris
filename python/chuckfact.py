from _chuck_fact import lib, ffi


class ChuckFact:
    def __init__(self):
        self.cf = lib.chuck_fact_init()

    def get(self):
        c_fact = lib.chuck_fact_get(self.cf)
        fact_as_bytes = ffi.string(c_fact)
        return fact_as_bytes.decode("UTF-8")

    def __del__(self):
        lib.chuck_fact_destroy(self.cf)


def main():
    chuck = ChuckFact()
    print(chuck.get())


if __name__ == '__main__':
    main()
