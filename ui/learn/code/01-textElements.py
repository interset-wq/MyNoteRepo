"""文本元素"""

from nicegui import ui, html

# 在HTML中解析为div
ui.label('some label')
# 在HTML解析为a
ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')
# 聊天气泡
ui.chat_message('Hello NiceGUI!',
                name='Robot',
                stamp='now',
                avatar='https://robohash.org/ui')
# 通用标签 使用这种方法可以指定HTML标签并且可以定义类名
with ui.element('div').classes('p-2 bg-blue-100'):
    ui.label('inside a colored div')
# 使用markdown解析为HTML
ui.markdown('This is **Markdown**.')
# 使用ReStructuredText解析为HTML
ui.restructured_text('This is **reStructuredText**.')
# 使用mermaid解析为HTML
ui.mermaid('''
graph LR;
    A --> B;
    A --> C;
''')
# 直接使用HTML语法
ui.html('This is <strong>HTML</strong>.')
# 更复杂的HTML 在section标签中嵌套多个标签
with html.section().style('font-size: 120%'):
    html.strong('This is bold.') \
        .classes('cursor-pointer') \
        .on('click', lambda: ui.notify('Bold!'))
    html.hr()
    html.em('This is italic.').tooltip('Nice!')
    with ui.row():
        html.img().props('src=https://placehold.co/60')
        html.img(src='https://placehold.co/60')
ui.run(native=True)