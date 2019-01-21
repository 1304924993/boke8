
from django import forms


class AddArtForm(forms.Form):
    title = forms.CharField(min_length=2, required=True,
                            error_messages={
                                'required': '文章标题必填',
                                'min_length': '文章标题不能少于2个字符'
                            })
    describe = forms.CharField(min_length=10, required=True,
                           error_messages={
                               'required': '文章简短描述必填',
                               'min_length': '文章简短描述不能少于10个字符'
                           })

    content = forms.CharField(required=True,
                              error_messages={
                                  'required': '文章内容必填',
                              })
    icon = forms.ImageField(required=True,
                            error_messages={
                            'request': '首图必填'
                        })


class EddArtForm(forms.Form):
    title = forms.CharField(min_length=2, required=True,
                            error_messages={
                                'required': '文章标题必填',
                                'min_length': '文章标题不能少于2个字符'
                            })
    describe = forms.CharField(min_length=10, required=True,
                           error_messages={
                               'required': '文章简短描述必填',
                               'min_length': '文章简短描述不能少于10个字符'
                           })

    content = forms.CharField(required=True,
                              error_messages={
                                  'required': '文章内容必填',
                              })
    icon = forms.ImageField(required=True,
                            error_messages={
                            'required': '首图必填'
                        })
