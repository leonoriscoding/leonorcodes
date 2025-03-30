
class tarefa():
    def __init__(self):
        lista_tarefas = []

    def add_task(self):
        task_text = self.task_input.text().strip()
        if task_text:
            self.task_count += 1
            self.task_list.addItem(f"{self.task_count}. {task_text}")
            self.task_input.clear()
            
    def remove_task(self):
        selected_items = self.task_list.selectedItems()
        if selected_items:
            for item in selected_items:
                self.task_list.takeItem(self.task_list.row(item))