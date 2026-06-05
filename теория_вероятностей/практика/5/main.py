import math

import matplotlib
import numpy as np
import matplotlib.pyplot as plt


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
    min_value = values[0] - h_interval / 2
    groups = []
    for num_group in range(class_num + 1):
        group = [value for value in values if
                 min_value + h_interval * num_group <= value < min_value + h_interval * (num_group + 1)]
        groups.append(group)
    return groups


def empirical_function_draw(values, n, min_value, max_value) -> None:
    """
    Формирование и отрисовка графика эмпирической функции распределения
    :param values: Значения вариационного ряда
    :param n: Объем выборки
    :return: None
    """
    x = np.arange(-1.8, 1.8, 0.001)
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
    x = [min_value + h_interval * i for i in range(class_num + 1)]
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
    plt.title(r"Гистограмма частот")
    x = ["{:.3f}".format(min_value + h_interval * i) for i in range(class_num + 1)]
    y = [len(i) / h_interval for i in variation_series_grouped]
    plt.bar(x, y)


def main() -> None:
    """
    Представленный вариационный ряд
    """
    values = sorted([
        -1.35, -0.42,
        0.38, 1.21,
        0.35, 1.56,
        0.80, 0.14,
        -1.49, 0.35,
        -0.34, -0.73,
        0.69, 0.55,
        1.11, 0.62,
        0.93, 0.42,
        1.00, -0.48
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
    class_num = formula_sturgess(n)  # количество классов для группированной выборки
    h_interval = (max_df - min_df) / formula_sturgess(n)  # значение интервала для группированной выборки
    variation_series_grouped = grouping_variation_series(values, class_num, h_interval)  # группированная выборка
    """
    Отрисовка графиков
    """
    empirical_function_draw(values, n, min_df, max_df)
    frequency_polygon_draw(variation_series_grouped, class_num, h_interval, min_df)
    bar_draw(variation_series_grouped, class_num, h_interval, min_df)
    plt.show()


if __name__ == '__main__':
    matplotlib.use('TkAgg')
    main()
