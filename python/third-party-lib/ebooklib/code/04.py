# coding=utf-8

from ebooklib import epub
from ebooklib.plugins import standard
from ebooklib.utils import create_pagebreak
from uuid import uuid4


book = epub.EpubBook()

"""元数据 epub必须具备的书籍信息"""
# epub唯一识别码
book.set_identifier(str(uuid4()))
# 书名
book.set_title('样书')
# 语言
book.set_language('zh-CN')

"""其他元数据 可有可无"""
# 书籍作者
book.add_author('ebooklib')

"""章节"""
# Introduction章节
c1 = epub.EpubHtml(
    title='Introduction', 
    file_name='intro.xhtml', lang='zh-CN',
    content='<h2>简介</h2>\
        <p>简介章节就是简单的介绍一下主要内容。</p>\
        <p>如果你不擅长写简介，那就把随便写几句吧。</p>'
)
c2 = epub.EpubHtml(title='第二章', 
    file_name='chap02.xhtml', lang='zh-CN',
    content='<html><body><h1>第二章</h1>\
        <p>This chapter has two page breaks, \
        both with invisible page numbers.</p>'
)

# Add invisible page numbers that match the printed text, 
# for accessibility
c2.content += create_pagebreak("2")

# You can add more content  after the page break
c2.content += '<p>This is the second page in the second chapter, \
    after the invisible page break.</p>'

# Add invisible page numbers that match the printed text, for accessibility
c2.content += create_pagebreak("3", label="Page 3")

# close the chapter
c2.content += '</body></html>'

"""将章节添加到epub"""
book.add_item(c1)
book.add_item(c2)

"""创建目录"""
book.toc = ((c1, c2, ))

"""添加导航文件"""
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

"""添加书脊"""
book.spine = ['nav', c1, c2, ]

"""制作epub"""
opts = {'plugins': [standard.SyntaxPlugin()]}
epub.write_epub('test.epub', book, opts)
