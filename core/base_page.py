import flet as ft
from abc import ABC, abstractmethod
from typing import Callable
from flet import Container, Column, Text, padding, margin, Page, border, border_radius
from .theme import ThemeColors


class BasePage(ABC):
    def __init__(self, on_theme_changed: Callable = None, theme_colors: ThemeColors = None, theme_mode: str = "dark", title: str = "", page: ft.Page = None):
        self.on_theme_changed = on_theme_changed
        self.theme_colors = theme_colors or ThemeColors()
        self.theme_mode = theme_mode
        self.title = title
        self.page = page
        self.content = self.build()

    def did_mount(self):
        """
        组件挂载后的生命周期方法
        子类可以重写此方法以在组件挂载后执行操作
        """
        pass

    def will_unmount(self):
        """
        组件卸载前的生命周期方法
        子类可以重写此方法以在组件卸载前执行清理操作
        """
        pass

    def build_title(self) -> Container:
        """构建统一的标题栏"""
        container = Container(
            content=Text(
                self.title,
                size=23,
                color=self.theme_colors.text_color,
            ),
            padding=padding.only(top=10, bottom=10, left=30),
            bgcolor=self.theme_colors.nav_color,
            margin=margin.only(left=-10, bottom=20),
            width=5000,                                             # 设置标题栏宽度,填充整行
        )

        return container

    @abstractmethod
    def build_content(self) -> Column:
        """子类实现此方法来构建页面主要内容"""
        pass

    def build(self) -> Container:
        """构建完整的页面布局"""
        container = Container(
            content=Column(
                controls=[
                    self.build_title(),  # 标题部分
                    Container(  # 内容部分
                        content=self.build_content(),
                        expand=True,
                        bgcolor=self.theme_colors.bg_color,
                    ),
                ],
                spacing=0,
                scroll="none",
            ),
            expand=True,
            bgcolor=self.theme_colors.bg_color,
        )
        return container

    def update_theme(self, theme_colors: ThemeColors, theme_mode: str):
        self.theme_colors = theme_colors
        self.theme_mode = theme_mode
        self.content = self.build()

    def build_section(self, title: str = None, content: Container = None) -> Container:
        """构建一个带标题的部分"""
        controls = []

        if title:
            title_text = Text(title, size=22, weight="bold", color=self.theme_colors.text_color)
            controls.append(title_text)

        if content:
            controls.append(content)

        section_content = Column(
            controls=controls,
            spacing=10,  # 减少标题和内容之间的间距
        )

        container = Container(
            content=section_content,
            bgcolor=self.theme_colors.card_color,
            padding=30 if title else 10,  # 根据是否有标题调整内边距
            border_radius=border_radius.all(10),  # 更圆的边角
            border=border.all(1, self.theme_colors.divider_color),  # 添加轮廓线
            margin=padding.symmetric(horizontal=20, vertical=10),  # 增加上下边距
        )
        
        return container
