

from django.views.generic import FormView, TemplateView
from .forms import SignModelForm
from django.urls import reverse_lazy
from .models import Sign
from datetime import datetime


class SignFormView(FormView):
    template_name = 'index.html'
    form_class = SignModelForm
    success_url = reverse_lazy('index')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = Sign.objects.all()
        self.each_sign_first_month_days = (
            range(22, 32), range(21, 32), range(19, 32), range(21, 32), range(21, 32), range(21, 32),
            range(21, 32), range(23, 32), range(23, 32), range(23, 32), range(23, 32), range(22, 32)
        )

        self.each_sign_second_month_days = (
            range(1, 21), range(1, 19), range(1, 21), range(1, 21), range(1, 21), range(1, 21),
            range(1, 23), range(1, 23), range(1, 23), range(1, 23), range(1, 22), range(1, 22)
        )

        self.each_sign_first_month = (12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

        self.each_sign_second_month = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

        self.signs: tuple = (
            'Capricórnio', 'Aquário', 'Peixes', 'Aries', 'Touro', 'Gêmeos',
            'Câncer', 'Leão', 'Virgem', 'Libra', 'Escorpião', 'Sagitário'
        )

        if len(self.db) != 0:
            self.the_input = self.get_last_object_data()
            self.last_input_array = self.last_object_split_data()
            self.birthday_datetime = self.generate_birthday_datatime()
            self.person_age_in_days = self.calculate_lifetime()
            self.person_sign = self.find_sign()
        else:
            self.the_input = '01/01/2000'
            self.last_input_array = {'day': 1, 'month': 1, 'year': 2000}
            self.birthday_datetime = self.generate_birthday_datatime()
            self.person_age_in_days = self.calculate_lifetime()
            self.person_sign = self.find_sign()

        # print(dir(Sign.objects.get(birthday='16/07/1992').birthday))

    def form_valid(self, form):
        form.save()
        return super(SignFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(SignFormView, self).form_invalid(form)

    def get_last_object_data(self) -> str:
        db_size = len(self.db) - 1
        last_object_from_db = None

        for index, object_ in enumerate(self.db):
            # Se chegar no último índice do banco, pegar o atributo deste objeto neste índice
            if index == db_size:
                last_object_from_db = self.db[index].birthday

        # ANTES: .get(birthday=last_object_from_db).birthday (gera erro se há múltiplos objetos [repetidos])
        # SOLUÇÃO: trocar por "filter" e pegar o primeiro registro repitido encontrado
        last_input = Sign.objects.filter(birthday=last_object_from_db)[0].birthday
        return last_input

    def last_object_split_data(self) -> dict:
        last_object_array = [int(number) for number in self.the_input.split('/')]
        return {
            'day': last_object_array[0],
            'month': last_object_array[1],
            'year': last_object_array[2]
        }

    def generate_birthday_datatime(self):

        # Coletar o dado de data do aniversário p/ ser subtraído pela data de hoje na função "calculate_lifetime"
        the_birthday = datetime(
            day=self.last_input_array['day'],
            month=self.last_input_array['month'],
            year=self.last_input_array['year'])

        return the_birthday

    def calculate_lifetime(self):

        # P/ o cálculo, é preciso a data atual p/ subtrair com a data no aniversário do usuário
        right_now = datetime.today()
        today_datetime = datetime(year=right_now.year, month=right_now.month, day=right_now.day)

        # Subtração das datas p/ saber o tempo de vida do usuário
        person_existance = today_datetime - self.birthday_datetime

        # Formatar dados do cálculo p/ adquirir o dado numérico
        person_existance = f'{str(person_existance).split()[0]} dias'

        return person_existance

    def find_sign(self):

        # O signo é encontrado pela satisfação de 2 das 4 condições
        # O signo é achado caso: 2 primeiras condições satisfeitas, ou as 2 últimas
        for index in range(len(self.signs)):

            if self.last_input_array['day'] in tuple(self.each_sign_first_month_days)[index] \
               and self.last_input_array['month'] == tuple(self.each_sign_first_month)[index] \
               or self.last_input_array['day'] in tuple(self.each_sign_second_month_days)[index] \
               and self.last_input_array['month'] == tuple(self.each_sign_second_month)[index]:

                return self.signs[index]

    def get_context_data(self, **kwargs):
        context = super(SignFormView, self).get_context_data(**kwargs)
        context['db'] = self.db
        context['birthday'] = self.the_input
        context['age_in_days'] = self.person_age_in_days
        context['person_sign'] = self.person_sign
        return context


class SampleView(TemplateView):
    template_name = 'sample.html'
