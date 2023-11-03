import time
class ControlPanel:
    def __init__(self):
        self.password = "1234"  # 设置的密码
        self.input_password = ""  # 输入的密码
        self.input_attempts = 0  # 输入密码错误次数
        self.is_locked = False  # 控制面板是否被锁定
        self.lock_time = 0  # 锁定开始时间

    def enter_password(self, key):
        if self.is_locked:
            current_time = time.time()
            if current_time - self.lock_time >= 120:
                self.is_locked = False
                print("解锁成功，请重新输入密码")
        elif len(self.input_password) < 4:
            self.input_password += key
            if len(self.input_password) == 4:
                self.check_password()
        else:
            print("密码已达到长度，正在验证，请稍等")

    def check_password(self):
        if self.input_password == self.password:
            self.input_attempts = 0
            self.input_password = ""
            print("密码正确，进入系统功能选择")
            # 在这里实现进入系统功能选择的相关操作
        else:
            self.input_attempts += 1
            self.input_password = ""
            print("密码错误")
            if self.input_attempts >= 3:
                self.is_locked = True
                self.lock_time = time.time()
                print("密码错误次数达到最大限制，已锁定控制面板，请等待解锁")

# 示例用法
control_panel = ControlPanel()

while True:
    key = input("请输入按键：")
    control_panel.enter_password(key)