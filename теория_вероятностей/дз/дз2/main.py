import math

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable


def formula_sturgess(n) -> int:
    """
    Формула Стерджиса
    :param n: Объем выборки
    :return: Количества классов
    """
    return 1 + int(math.log2(n))


def create_map_values(values) -> dict:
    """
    Создание словаря со значениями в качестве ключей и частотами вариант в качестве значений
    :param values: значения вариационного ряда
    :return: map_values: dict
    """
    map_values = {}
    for key in values:
        if map_values.get(key, None) is not None:
            map_values[key] += 1
        else:
            map_values[key] = 1
    return map_values


def grouping_variation_series(values, class_num, h_interval) -> list:
    """
    Группировка вариационного ряда
    :param values: значения вариационного ряда
    :param class_num: количество классов для группированной выборки
    :param h_interval: значение интервала для группированной выборки
    :return: Сгруппированный ряд
    """
    min_value = values[0]
    groups = []
    for num_group in range(class_num):
        group = [value for value in values if
                 min_value + h_interval * num_group <= value < min_value + h_interval * (num_group + 1)]
        groups.append(group)
    # корректировка последнего значения
    if groups[-1][-1] != values[-1]:
        groups[-1].extend([value for value in values if value == values[-1]])
    return groups


def empirical_function_draw(values, n, min_value, max_value) -> None:
    """
    Формирование и отрисовка графика эмпирической функции распределения
    :param values: Значения вариационного ряда
    :param n: Объем выборки
    :return: None
    """
    x = np.arange(min_value - 5, max_value + 5, 0.001)
    # добавляем разрывы на графике
    for value in values:
        x[(x > value - 0.001) & (x < value + 0.001)] = np.nan
    f_n = np.array([
        sum((1 if value < x_iter else 0 for value in values)) / n for x_iter in x
    ])
    plt.figure()
    plt.xlabel(r'$x$', fontsize=14)
    plt.ylabel(r'$F_n^*(x)$', fontsize=14)
    plt.title(r"Эмпирическая функция распределения $F_n^*(x)$")
    plt.plot(x, f_n)

    print("Выведенная эмпирическая функция")
    print(f"0; x <= {min_value}")
    previous_value: float = min_value
    for value in sorted(set(values[1:])):
        print(
            f"{sum((1 if value_iter < value else 0 for value_iter in values))}/{n}; {previous_value} < x <= {value}")
        previous_value = value
    print(f"1; x > {max_value}")


def frequency_polygon_draw(variation_series_grouped, class_num, h_interval, min_value) -> None:
    """
    Формирование и отрисовка полигона частот
    :param variation_series_grouped: значения группиррованной выборки
    :param class_num: количество классов для группированной выборки
    :param h_interval: значение интервала для группированной выборки
    :param min_value: минимальное значение выборки
    :return: None
    """
    plt.figure()
    plt.xlabel(r'$x$', fontsize=14)
    plt.ylabel(r'$n_i$', fontsize=14)
    plt.title(r"Полигон частот")
    x = [min_value + h_interval / 2 + h_interval * i for i in range(class_num)]
    y = [len(i) for i in variation_series_grouped]
    plt.plot(x, y, marker='o')


def bar_draw(variation_series_grouped, class_num, h_interval, min_value) -> None:
    """
    Формирование и отрисовка гистограммы
    :param variation_series_grouped: значения группиррованной выборки
    :param class_num: количество классов для группированной выборки
    :param h_interval: значение интервала для группированной выборки
    :param min_value: минимальное значение выборки
    :return: None
    """
    plt.figure()
    plt.xlabel(r'$x$', fontsize=14)
    plt.ylabel(r'$n_i/h$', fontsize=14)
    plt.title(r"Гистограмма относительных частот")
    x = ["{:.1f}".format(min_value + h_interval / 2 + h_interval * i) for i in range(class_num)]
    y = [len(i) / class_num / h_interval for i in variation_series_grouped]
    plt.bar(x, y)


def create_table(variation_series_grouped, h_interval, min_value, n):
    table = PrettyTable()
    table.field_names = ['номер частичного интервала', 'границы интервала', 'середина интервала', 'частота интервала',
                         'относительная частота', 'плотность относительной частоты']
    for i, group in enumerate(variation_series_grouped):
        table.add_row([
            i + 1,
            f"{min_value + h_interval * i}-{min_value + h_interval * (i + 1)}",
            min_value + h_interval / 2 + h_interval * i,
            len(group),
            len(group) / n,
            len(group) / n / h_interval
        ])
    print(table)


def main() -> None:
    """
    Представленный вариационный ряд
    """
    values = sorted([
        76,   28, 151,  91,  60, 204, 177, 102, 128, 217,
        120,  66, 207, 126, 124, 152,  27, 221, 131,  51,
        241,  77, 250, 134, 123, 147, 184, 195,  47, 160,
        159,  74, 169, 178,  79, 129, 250, 223, 182,  96,
        135, 199,  56,  25,  82, 116,  44, 229, 145, 203,
        88,  209, 146, 224, 239, 103, 201, 245, 130, 163,
        71,  165, 176, 194,  78, 154,  99,  78, 127,  69,
        171, 173,  31, 181, 117,  84,  73, 161, 240, 149,
        247, 107, 140,  53, 205, 155,  29, 132, 185, 179,
        180, 128,  42, 114,  93, 191, 174, 210, 133, 226
    ])
    map_values = create_map_values(values)
    """
    Вычисления значений
    """
    n = len(values)  # n - объем выборки
    min_df = values[0]  # X1 - минимальное значение выборки
    max_df = values[n - 1]  # Xn - максимальное значение выборки
    mean_value = sum((i * map_values[i] for i in frozenset(values))) / n  # M - выборочное математическое ожидание
    # S^2 - исправленная выборочная дисперсия
    dispersion = sum([math.pow(i - mean_value, 2) * map_values[i] for i in frozenset(values)]) / (n - 1)
    std = math.sqrt(dispersion)  # среднеквадратическое отклонение выборки
    """
    Вывод полученных значений в консоль
    """
    print("Вариационный ряд:")
    print(f"{' '.join([str(i) for i in values])}\n")
    print("Экстремальные значения вариацинного ряда")
    print(f"|Минимальное значение: {min_df}")
    print(f"|Максимальное значение: {max_df}")
    print(f"|Размах выборки: {max_df - min_df}\n")
    print("Оценки математического ожидания и среднеквадратического отклонения")
    print(f"|Математическое ожидание: {mean_value}")
    print(f"|Дисперсия: {dispersion}")
    print(f"|Среднеквадратическое отклонение: {std}\n")
    """
    Формирование группированной выборки
    """
    class_num = 9  # количество классов для группированной выборки
    h_interval = (max_df - min_df) / class_num  # значение интервала для группированной выборки
    variation_series_grouped = grouping_variation_series(values, class_num, h_interval)  # группированная выборка
    """
    Отрисовка графиков
    """
    create_table(variation_series_grouped, h_interval, min_df, n)
    empirical_function_draw(values, n, min_df, max_df)
    frequency_polygon_draw(variation_series_grouped, class_num, h_interval, min_df)
    bar_draw(variation_series_grouped, class_num, h_interval, min_df)
    plt.show()


if __name__ == '__main__':
    matplotlib.use('TkAgg')
    main()
