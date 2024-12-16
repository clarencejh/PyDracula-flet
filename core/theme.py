from dataclasses import dataclass

@dataclass
class ThemeColors:
    def __init__(self, is_dark: bool = True):
        if is_dark:
            self.title_bar_color = "#393E46"
            self.bg_color = "#222831"
            self.nav_color = "#393E46"
            self.card_color = "#393E46"
            self.divider_color = "#9AA6B2"
            self.text_color = "#EEEEEE"
        else:
            self.title_bar_color = "#E0E0E0" # 标题栏背景色 
            self.bg_color = "#FAFAFA"  # 更柔和的背景色
            self.nav_color = "#FFFFFF"  # 更清淡的导航背景色
            self.card_color = "#FFFFFF"  # 使用纯白色卡片，增加对比
            self.divider_color = "#9AA6B2"  # 稍微深一点的分隔线颜色
            self.text_color = "#333333"  # 更深的文本颜色，增加可读性