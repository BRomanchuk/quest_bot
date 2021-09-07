from settings.data_loader import get_quest_df


class Quest:
    def __init__(self):
        self.df = get_quest_df()

    def get_task(self, task_num):
        pass

    def get_hint(self, task_num):
        pass

    def is_correct(self, task_num, answer):
        pass
