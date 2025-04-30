import sys


def generate_task_tree(t, level=0):
    result = []
    indent = "  " * level
    prefix = indent + "- " if level >= 0 else ""
    result.append(f"{prefix}**Task {t.id}**: {t.content}")

    for sub in t.subtasks:
        sub_tree = generate_task_tree(sub, level + 1)
        result.append(sub_tree)

    return "\n".join(result)


class StreamlitStdout:
    def __init__(self, title, placeholder):
        self.title = title
        self.placeholder = placeholder
        self.full_log = ""
        self._buf = ""
        self.max_lines = 10
        self.log_tail = ""
        self.original_stdout = sys.__stdout__

    def write(self, text):
        self.original_stdout.write(text)

        self._buf += text
        if "\n" in self._buf:
            lines = self._buf.split("\n")
            for line in lines[:-1]:
                self.full_log += line + "\n"
            self._buf = lines[-1]

            self.log_tail = "\n".join(self.full_log.split("\n")[-self.max_lines :])
            self.placeholder.text_area(
                self.title, self.log_tail, height=300, disabled=True
            )

    def flush(self):
        self.original_stdout.flush()
        if self._buf:
            self.full_log += self._buf
            self._buf = ""
            self.log_tail = "\n".join(self.full_log.split("\n")[-self.max_lines :])
            self.placeholder.text_area(
                self.title, self.log_tail, height=300, disabled=True
            )
