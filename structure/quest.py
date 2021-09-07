from settings.data_loader import get_quest_df


class Quest:
    def __init__(self, name):
        self.name = name
        self.df = get_quest_df(name)

    def get_task(self, task_num):
        return self.df['task'][task_num]

    def get_hint(self, task_num):
        return self.df['hint'][task_num]

    def is_correct(self, task_num, answer):
        return str(answer).lower() == str(self.df['answer'][task_num]).lower()
