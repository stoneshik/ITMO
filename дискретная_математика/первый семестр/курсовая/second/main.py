from abc import ABC, abstractmethod
import itertools

import pandas as pd


class AbstractFirstStage(ABC):
    """
    Суперкласс для классов генерящих данные таблицы истинности.
    Для генерации данных своего варианта отнаследуйся от этого класса и
    переопредели метод make_table
    """
    def __init__(self, indexes: list, num_logic_var: int):
        """
        :param indexes: список с названиями столбцов,
        первое значение должно быть названием столбца для комбинаций перебираемых значений.
        Последнее значение дожно быть названием столбца конечных значений функции.
        :param num_logic_var: количество логических переменных (у всех вариантов вроде 5)
        """
        self.indexes = indexes
        self.num_logic_var = num_logic_var
        self.table = self.make_table()

    @abstractmethod
    def make_table(self):
        pass

    @staticmethod
    def make_df_from_table(indexes, columns):
        """
        Метод который юзается для получения DataFrame из списков
        Он используется в конце каждого метода где нужно получить таблицу.
        Без приведения данных к фрейму записать их в csv не получится
        :param indexes: Список со строками названий столбцов
        :param columns: Список со списками данных
        :return:
        """
        return pd.DataFrame(
            {
                index: value for index, value in
                zip(
                    indexes,
                    [pd.Series(value, dtype=str) for value in columns]
                )
            }
        )

    @staticmethod
    def kdnf(df, variants_index, result_index) -> str:
        """
        Метод который генерит КДНФ.
        В строке для математических символов юзается символы Латеха
        В последней версии ворда есть возможность их юзать в формулах, остальным соболезную.
        В примере выводит строку в консольку
        :param df:
        :param variants_index:
        :param result_index:
        :return:
        """
        result_for_kdnf = df.loc[df[result_index] == '1']
        result = ''
        for _, row in result_for_kdnf.iterrows():
            variant = row[variants_index]
            result += (
                ''.join(
                    [
                        str('\\bar x_' + str(i+1)) if v == '0' else str('x_' + str(i+1))
                        for i, v in enumerate(variant)
                    ]
                ) + ' \\vee '
            )
        return result

    @staticmethod
    def kknf(df, variants_index, result_index) -> str:
        """
        Метод который генерит ККНФ. Генерятся лишние значки перед закрывающей скобкой, просто удаляйте их,
        чинить эту недоработку мне пока лень
        :param df:
        :param variants_index:
        :param result_index:
        :return:
        """
        result_for_kknf = df.loc[df[result_index] == '0']
        result = ''
        for _, row in result_for_kknf.iterrows():
            variant = row[variants_index]
            res = '('
            res += str(
                ''.join(
                    [
                        str('\\bar x_' + str(i+1) + ' \\vee ') if v == '1' else str('x_' + str(i+1) + ' \\vee ')
                        for i, v in enumerate(variant)
                    ]
                )
            )
            res += ')'
            result += res
        return result

    def write(self, name_file):
        self.table.to_csv(name_file)


class FirstStage(AbstractFirstStage):
    """
    Класс для получения таблицы истинности.
    Данные таблицы юзается в остальных классах, очень важно чтобы генерируемые данные были верные.
    Если не знаешь как их правильно сгенерить, то посмотри референс в файле test
    """
    def make_table(self):
        """
        Этот метод генерит данные для 9 варианта
        :return:
        """
        variants = [''.join(i) for i in itertools.product('01', repeat=self.num_logic_var)]  # x1x2x3x4
        a1 = [i[0] for i in variants]
        a2 = [i[1] for i in variants]
        a3 = [i[2] for i in variants]
        a4 = [i[3] for i in variants]
        a5 = [i[4] for i in variants]

        c = [('0' * (self.num_logic_var - len(bin((int(i, 2)-1) % 29)[2:]))) + bin((int(i, 2)-1) % 29)[2:]
             if int(i, 2) != 0 else 'd' for i in variants]
        c0 = [i[0] if i != 'd' else '-' for i in c]
        c1 = [i[1] if i != 'd' else '-' for i in c]
        c2 = [i[2] if i != 'd' else '-' for i in c]
        c3 = [i[3] if i != 'd' else '-' for i in c]
        c4 = [i[4] if i != 'd' else '-' for i in c]
        table = AbstractFirstStage.make_df_from_table(self.indexes, [
            a1, a2, a3, a4, a5,
            c0, c1, c2, c3, c4
        ])
        return table


def main():
    first_stage = FirstStage(
        [
            'a1', 'a2', 'a3', 'a4', 'a5',
            'C0', 'C1', 'C2', 'C3', 'C4'
        ],
        5
    )
    first_stage.write('first.csv')


if __name__ == '__main__':
    main()