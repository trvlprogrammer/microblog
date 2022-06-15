def inidecorator(fungsinama):
    def halo(*args, **kwargs):
        print('Halo')
        fungsinama(*args,**kwargs)
        print('Apa kabar?')

    return halo

@inidecorator
def person2(nama):
    print(nama)

person2('Nyaasyu')