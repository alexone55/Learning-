import unittest
from quiz_maker_main import \
    get_questions, \
    get_answers_list, \
    get_given_amount_of_random_questions, \
    get_needed_answers, \
    count_points


class QuizMakerTest(unittest.TestCase):

    def test_get_questions_with_empty_file(self):
        with self.assertRaises(OSError) as context:
            get_questions('Документ Microsoft Word.docx')
        exception_message = str(context.exception)
        self.assertEqual('File is empty!', exception_message)

    def test_get_questions_with_right_paths(self):
        path = 'questions.txt'
        expected_questions = {0: 'Сколько лет длилась столетняя война?\na. 100\nб. 998\nв. 113\nг. 228',
                              1: 'Как звали Гитлера?\nа. Адольф\nб. Геннадий\nв. Васыль\nг. Григорий',
                              2: 'Кто пидумал современную архитектуру ЭВМ?\nа. Джон фон-Нейман\nб. Карл Цузе\nв. '
                                 'Бьярне Страусструп\nг. Илон Маск',
                              3: 'Какое пиво самое крепкое?\nа. Жиуглевское\nб. Тетерев\nв. Московское\nг. Опилля'}
        questions = get_questions(path)
        self.assertEqual(expected_questions, questions)

    def test_get_answer_list_with_right_paths(self):
        path = 'answers.txt'
        expected_answers = ['в', 'а', 'а', 'г']
        answers = get_answers_list(path)
        self.assertEqual(expected_answers, answers)

    def test_get_given_amount_of_random_questions_with_wrong_number_of_questions(self):
        number_of_questions = 6
        questions = {0: 'Сколько лет длилась столетняя война?\na. 100\nб. 998\nв. 113\nг. 228',
                     1: 'Как звали Гитлера?\nа. Адольф\nб. Геннадий\nв. Васыль\nг. Григорий',
                     2: 'Кто пидумал современную архитектуру ЭВМ?\nа. Джон фон-Нейман\nб. Карл Цузе\nв. '
                        'Бьярне Страусструп\nг. Илон Маск',
                     3: 'Какое пиво самое крепкое?\nа. Жиуглевское\nб. Тетерев\nв. Московское\nг. Опилля'}
        with self.assertRaises(ValueError) as context:
            get_given_amount_of_random_questions(number_of_questions, questions)
        exception_message = str(context.exception)
        self.assertEqual('Wrong number of questions was given', exception_message)

    def test_get_given_amount_of_random_questions_with_wrong_keys_of_questions(self):
        number_of_questions = 3
        questions = {228: 'Сколько лет длилась столетняя война?\na. 100\nб. 998\nв. 113\nг. 228',
                     "1": 'Как звали Гитлера?\nа. Адольф\nб. Геннадий\nв. Васыль\nг. Григорий',
                     '2': 'Кто пидумал современную архитектуру ЭВМ?\nа. Джон фон-Нейман\nб. Карл Цузе\nв. '
                          'Бьярне Страусструп\nг. Илон Маск',
                     1337: 'Какое пиво самое крепкое?\nа. Жиуглевское\nб. Тетерев\nв. Московское\nг. Опилля'}
        with self.assertRaises(ValueError) as context:
            get_given_amount_of_random_questions(number_of_questions, questions)
        exception_message = str(context.exception)
        self.assertEqual('Unexpected keys', exception_message)

    def test_get_given_amount_of_random_questions_with_right_input(self):
        number_of_questions = 3
        questions = {0: 'Сколько лет длилась столетняя война?\na. 100\nб. 998\nв. 113\nг. 228',
                     1: 'Как звали Гитлера?\nа. Адольф\nб. Геннадий\nв. Васыль\nг. Григорий',
                     2: 'Кто пидумал современную архитектуру ЭВМ?\nа. Джон фон-Нейман\nб. Карл Цузе\nв. '
                        'Бьярне Страусструп\nг. Илон Маск',
                     3: 'Какое пиво самое крепкое?\nа. Жиуглевское\nб. Тетерев\nв. Московское\nг. Опилля'}
        questions = get_given_amount_of_random_questions(number_of_questions, questions)
        self.assertEqual(number_of_questions, len(questions))

    def test_get_needed_answers_with_right_input(self):
        key_answers = ['в', 'а', 'а', 'г']
        questions_keys = [0, 1, 3]
        expected_needed_answers = {0: 'в', 1: 'а', 3: 'г'}
        needed_answers = get_needed_answers(key_answers, questions_keys)
        self.assertEqual(needed_answers, expected_needed_answers)

    def test_count_points_with_right_input(self):
        given_answers = {0: 'в', 1: 'б', 3: 'а'}
        key_answers = {0: 'в', 1: 'а', 2: 'а', 3: 'г'}  # {0: 'в', 1: 'а', 2: 'а', 3: 'г'} ->the same result
        successful, total = count_points(given_answers, key_answers)
        self.assertEqual(1, successful)


if __name__ == '__main__':
    unittest.main()
