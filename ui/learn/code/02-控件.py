"""控件"""

from nicegui import ui

"""按钮Button"""
ui.markdown('## Button按钮')
ui.button('Click me!', on_click=lambda: ui.notify('You clicked me!'))

"""按钮组合Button Group"""
ui.markdown('## 按钮组合Button Group')
with ui.button_group():
    ui.button('One', on_click=lambda: ui.notify('You clicked Button 1!'))
    ui.button('Two', on_click=lambda: ui.notify('You clicked Button 2!'))
    ui.button('Three', on_click=lambda: ui.notify('You clicked Button 3!'))

"""下拉列表Dropdown Button"""
ui.markdown('## 下拉列表Dropdown Button')
with ui.dropdown_button('Open me!', auto_close=True):
    ui.item('Item 1', on_click=lambda: ui.notify('You clicked item 1'))
    ui.item('Item 2', on_click=lambda: ui.notify('You clicked item 2'))

"""动作按钮Floating Action Button (FAB)"""
ui.markdown('## 动作按钮Floating Action Button (FAB)')
with ui.fab('navigation', label='Transport'):
    ui.fab_action('train', on_click=lambda: ui.notify('Train'))
    ui.fab_action('sailing', on_click=lambda: ui.notify('Boat'))
    ui.fab_action('rocket', on_click=lambda: ui.notify('Rocket'))

"""计数器"""
ui.markdown('## 计数器Badge')
with ui.button('Click me!', on_click=lambda: badge.set_text(int(badge.text) + 1)):
    badge = ui.badge('0', color='red').props('floating')

"""Chip"""
ui.markdown('## Chip')
with ui.row().classes('gap-1'):
    ui.chip('Click me', icon='ads_click', on_click=lambda: ui.notify('Clicked'))
    ui.chip('Selectable', selectable=True, icon='bookmark', color='orange')
    ui.chip('Removable', removable=True, icon='label', color='indigo-3')
    ui.chip('Styled', icon='star', color='green').props('outline square')
    ui.chip('Disabled', icon='block', color='red').set_enabled(False)

"""切换按钮Toggle"""
ui.markdown('## 切换按钮Toggle')
toggle1 = ui.toggle([1, 2, 3], value=1)
toggle2 = ui.toggle({1: 'A', 2: 'B', 3: 'C'}).bind_value(toggle1, 'value')

ui.run()