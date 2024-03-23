

class Sign:

    def get_name(self):

        allowed = [
            ' ',
            *'a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z'.split('.'),
            *'a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z'.upper().split('.')
        ]

        print(self.msg['shut_down'])
        if self.arbitrary:
            self.person_name = self.mock_name
            for letter in self.person_name:
                if letter not in allowed:
                    self.error = True
        else:
            person_name = input(self.msg['type_your_name'])

            # Impedir que o usuário digite nomes com caracteres especiais
            [self.not_allowed.append(True) if letter not in allowed else None for letter in person_name]
            if person_name == '0':
                exit(0)

            # Havendo caracter especial, impedir e relançar o input pedindo o nome
            if True in self.not_allowed:
                self.not_allowed.clear()
                print(self.msg['invalid_char'])
                self.get_name()

            # Continuar
            else:
                print(self.msg['next_step'].format(align=self.align, person_name=person_name))
                self.person_name = person_name

    def get_born_date(self):

        if self.arbitrary:
            person_birthday = self.mock_birth
        else:
            # Pedir a data de aniversário
            person_birthday = input(self.msg['type_birth_day'])

        # Aniversário convertido em array p/ verificar se o usuário fornecerá todos os dados (3 no total)
        person_birthday_array = person_birthday.split('/')

        # Não forneceu todos os dados, repete a função
        if len(person_birthday_array) < 3:
            print(self.msg['incomplete_data_set'])
            self.get_born_date()

        # Dados corretamente inseridos: converter dados da data de aniversário
        else:
            # Aniversário convertido em dicionário p/ uso na função "find_sign" p/ haver mais legibilidade nos dados
            self.person_birthday_string = {
                'day': person_birthday_array[0],
                'month': person_birthday_array[1],
                'year': person_birthday_array[2],
            }

    def generate_birthday_datatime(self):

        from datetime import datetime

        # Coletar o dado de data do aniversário p/ ser subtraído pela data de hoje na função "calculate_lifetime"
        the_birthday = datetime(
            year=int(self.person_birthday_string['year']),
            month=int(self.person_birthday_string['month']),
            day=int(self.person_birthday_string['day']))

        return the_birthday

    def calculate_lifetime(self):
        from datetime import datetime

        # P/ o cálculo, é preciso a data atual p/ subtrair com a data no aniversário do usuário
        right_now = datetime.today()
        today_datetime = datetime(year=right_now.year, month=right_now.month, day=right_now.day)

        # Subtração das datas p/ saber o tempo de vida do usuário
        person_existance = today_datetime - self.person_birthday_datetime

        # Formatar dados do cálculo p/ adquirir o dado numérico
        person_existance = f'{str(person_existance).split()[0]} dias'

        return person_existance

    def find_sign(self):

        # É convertido p/ tupla na condição da função
        each_sign_first_month_days = (
            range(22, 32), range(21, 32), range(19, 32), range(21, 32), range(21, 32), range(21, 32),
            range(21, 32), range(23, 32), range(23, 32), range(23, 32), range(23, 32), range(22, 32)
        )

        # É convertido p/ tupla na condição da função
        each_sign_second_month_days = (
            range(1, 21), range(1, 19), range(1, 21), range(1, 21), range(1, 21), range(1, 21),
            range(1, 23), range(1, 23), range(1, 23), range(1, 23), range(1, 22), range(1, 22)
        )

        # Onde começa e termina a duração do mês de cada signo (segue a ordem e tamanho em "signs")
        each_sign_first_month = (12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
        each_sign_second_month = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

        signs: tuple = (
            'Capricorn', 'Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini',
            'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Saggitarius'
        )

        # O signo é encontrado pela satisfação de 2 das 4 condições
        # O signo é achado caso: 2 primeiras condições satisfeitas, ou as 2 últimas
        for index in range(len(signs)):

            if int(self.person_birthday_string['day']) in tuple(each_sign_first_month_days)[index] and int(self.person_birthday_string['month']) == tuple(each_sign_first_month)[index] \
             or int(self.person_birthday_string['day']) in tuple(each_sign_second_month_days)[index] and int(self.person_birthday_string['month']) == tuple(each_sign_second_month)[index]:

                return signs[index]

    def display_result(self):
        # Usado apenas p/ o código do nascimento caber em apenas uma linha
        data = self.person_birthday_string

        # Usar todos os dados coletados e exibi-los em forma de menu
        print(f"""
        ========== PESSOA: {self.person_name} ==========
        Nascimento    || {data['day']}/{data['month']}/{data['year']}
        Tempo de vida || {self.person_days_alive}
        Signo         || {self.person_sign}
        """)

    def print_data(self):
        print(f'{self.person_name = }')
        print(f'{self.person_birthday_string = }')
        print(f'{self.person_birthday_datetime = }')
        print(f'{self.person_days_alive = }')
        print(f'{self.person_sign = }')

    def __init__(self, mock_name: str = 'Maria', mock_birth: str = '01/01/2000', arbitrary: bool = False):
        self.br = '\n'
        self.indent = ' ' * 7
        self.align = self.br + self.indent
        self.arrow = f'{self.align}----------> '
        self.warning = f'{self.align}========== AVISO =========={self.align}'

        self.mock_name = mock_name
        self.mock_birth = mock_birth
        self.arbitrary = arbitrary
        self.error = False

        self.msg = {
            'shut_down': f'{self.align}ENCERRAR SESSÃO: digite 0',
            'type_your_name': f'{self.align}Digite seu nome após a seta{self.arrow}',
            'next_step': '{align}Certo, {person_name}, vamos a próxima etapa!',
            'invalid_char': f'{self.warning}Não use qualquer caracter especial, apenas letras comuns!',

            'type_birth_day': f'{self.align}Por favor, informe seu nascimento em formato dd/mm/aaaa (Ex: 27/11/1970){self.arrow}',
            'incomplete_data_set': f'{self.warning}Dados incompletos! Por favor, informar "dia/mês/ano"'
        }

        self.main_numbers = tuple(str(number) for number in range(1, 10))
        self.main_numbers_with_zero = tuple('0' + str_number for str_number in self.main_numbers)
        self.not_allowed = []

        # Quem for receber dados do input, é anteriormente configurado como "None"
        self.person_name = None

        # Função de input não deve ter retorno, apenas uma atribuição ao final
        self.get_name()

        self.person_birthday_string = None

        self.get_born_date()

        # Dados do aniversário convertidos em um dado do tipo (datetime)
        self.person_birthday_datetime = self.generate_birthday_datatime()

        # Resultado do cálculo do tempo de vida
        self.person_days_alive = self.calculate_lifetime()

        # Resultado da consulta que atribui o signo
        self.person_sign = self.find_sign()

        # Exibir resultado final
        self.display_result()

        # self.print_data()


if __name__ == '__main__':
    algorithm = Sign()
