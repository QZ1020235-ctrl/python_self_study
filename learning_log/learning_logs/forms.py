"""用于添加主题的表单，类似于models.py，即用于管理添加页面的数据"""
# 在Diango中，创建表单的最简单方式是使用ModelForm 

from django import forms

from .models import Topic, Entry

# 最简单的ModelForm版本只包含一个内嵌的Meta类，
# 让Django根据哪个模型创建表单以及在表单中包含哪些字段
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        lables = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        lables = {'text': ' '}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}