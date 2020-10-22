import time
import random
import os


def get_questions(path):
    if not os.path.exists(path):
        raise FileNotFoundError('File not found')
    else:
        f = open(path, 'r', encoding='utf-8')
        text = ''
        for line in f:
            text += line
        f.close()
        questions = text.split('\n\n')
        questions_dict = {}
        for index in range(len(questions)):
            questions_dict[index] = questions[index]
        return questions_dict


def get_given_amount_of_random_questions(number_of_questions, questions):
    if number_of_questions > len(questions) or number_of_questions < 1:
        raise ValueError('Wrong number of questions was given')
    elif type(questions) != dict:
        raise TypeError('Given not dict')
    else:
        if number_of_questions == len(questions):
            return questions
        else:
            random.seed(time.time())
            number_of_questions_to_remove = len(questions) - number_of_questions
            for rand_value in range(number_of_questions_to_remove):
                rand_index = random.randint(0, number_of_questions_to_remove)
                try:
                    while questions.get(rand_index) is None:
                        rand_index = random.randint(-1, number_of_questions_to_remove)
                    questions.pop(rand_index)
                except KeyError:
                    raise KeyError
            return questions


def get_answers_list(path):
    if not os.path.exists(path):
        raise FileNotFoundError('File not found')
    else:
        f = open(path, 'r', encoding='utf-8')
        key_answers = ''
        for line in f:
            key_answers += line
        f.close()
        key_answers = key_answers.split('\n')
        return key_answers


def get_needed_answers(key_answers, questions_keys):
    if type(key_answers) != list or type(questions_keys) != list:
        raise TypeError('Given not list')
    else:
        needed_answers = {}
        for key in questions_keys:
            needed_answers[key] = key_answers[key]
        return needed_answers


def count_points(given_answers, key_answers):
    total = len(key_answers)
    successful = 0
    keys_of_given_answers = given_answers.keys()
    for key in keys_of_given_answers:
        if given_answers[key] == key_answers[key]:
            successful += 1
    return successful, total


def start_test(questions):
    questions_keys = questions.keys()
    given_answers = {}
    for key in questions_keys:
        print(questions[key])
        given_answers[key] = str(input('Ваш ответ: '))
        print('')
    return given_answers


def main():
    questions = get_questions('questions.txt')
    print(get_answers_list('answers.txt'))
    print(questions.keys())
    print('Всего вопросов:', len(questions))
    required_number_of_questions = int(input('Введите кол-во вопросов, на которые хотите ответить: '))
    questions = get_given_amount_of_random_questions(required_number_of_questions, questions)
    given_answers = start_test(questions)
    needed_answers_for_given_questions = get_needed_answers(get_answers_list('answers.txt'), questions.keys())
    successful, total = count_points(given_answers, needed_answers_for_given_questions)
    print('Total: '+str(total) + '\nSucceccful: '+str(successful))


if __name__ == "__main__":
    main()
