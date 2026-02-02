from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.popup import Popup
import re

class FuturesApp(App):
    def build(self):
        # 设置窗口大小和标题
        Window.size = (400, 800)
        self.title = '商品期货复盘'
        
        # 创建主布局
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # 创建滚动视图
        scroll_view = ScrollView()
        
        # 创建表单布局
        self.form_layout = GridLayout(cols=2, spacing=10, size_hint_y=None)
        self.form_layout.bind(minimum_height=self.form_layout.setter('height'))
        
        # 存储字段信息和输入控件
        self.fields = [
            ('品种', 'text'),
            ('交易方向', 'radio'),
            ('开仓时间', 'date'),
            ('开仓操作周期', 'integer'),
            ('开仓起始边界均线', 'integer'),
            ('预期目标边界均线', 'integer'),
            ('驱动策略', 'text'),
            ('入场模式', 'text'),
            ('入场信号', 'text'),
            ('止损规则', 'text'),
            ('止盈规则', 'text'),
            ('开仓情绪', 'text'),
            ('开仓价格', 'decimal'),
            ('回撤幅度', 'decimal'),
            ('增仓价格', 'decimal'),
            ('增仓价格1', 'decimal'),
            ('减仓价格', 'decimal'),
            ('减仓价格1', 'decimal'),
            ('平仓操作周期', 'integer'),
            ('平仓时间', 'date'),
            ('平仓边界均线', 'integer'),
            ('离场信号', 'text'),
            ('平仓情绪', 'text'),
            ('平仓价格', 'decimal')
        ]
        
        # 存储输入控件的引用
        self.inputs = {}
        
        for i, (field_name, field_type) in enumerate(self.fields):
            # 添加标签
            self.form_layout.add_widget(Label(text=field_name, size_hint_y=None, height=40))
            
            # 根据字段类型添加不同的输入控件
            if field_type == 'text':
                input_widget = TextInput(multiline=False, size_hint_y=None, height=40)
                self.form_layout.add_widget(input_widget)
                self.inputs[field_name] = input_widget
            elif field_type == 'integer':
                input_widget = TextInput(multiline=False, input_filter='int', size_hint_y=None, height=40)
                self.form_layout.add_widget(input_widget)
                self.inputs[field_name] = input_widget
            elif field_type == 'decimal':
                input_widget = TextInput(multiline=False, input_filter='float', size_hint_y=None, height=40)
                self.form_layout.add_widget(input_widget)
                self.inputs[field_name] = input_widget
            elif field_type == 'date':
                input_widget = TextInput(multiline=False, size_hint_y=None, height=40, hint_text='格式：XXXX年XX月XX日XX时XX分')
                self.form_layout.add_widget(input_widget)
                self.inputs[field_name] = input_widget
            elif field_type == 'radio':
                # 创建交易方向单选框
                direction_layout = BoxLayout(orientation='horizontal')
                direction_layout.add_widget(Label(text='多'))
                long_checkbox = CheckBox()
                direction_layout.add_widget(long_checkbox)
                direction_layout.add_widget(Label(text='空'))
                short_checkbox = CheckBox()
                direction_layout.add_widget(short_checkbox)
                self.form_layout.add_widget(direction_layout)
                self.inputs[field_name] = {'long': long_checkbox, 'short': short_checkbox}
        
        # 添加提交按钮
        submit_button = Button(text='提交', size_hint_y=None, height=50)
        submit_button.bind(on_press=self.validate_form)
        self.form_layout.add_widget(Widget())  # 占位
        self.form_layout.add_widget(submit_button)
        
        # 将表单布局添加到滚动视图
        scroll_view.add_widget(self.form_layout)
        
        # 将滚动视图添加到主布局
        main_layout.add_widget(scroll_view)
        
        return main_layout
    
    def validate_form(self, instance):
        """验证表单数据"""
        errors = []
        
        # 验证日期格式
        date_pattern = r'^\d{4}年\d{2}月\d{2}日\d{2}时\d{2}分$'
        for field_name in ['开仓时间', '平仓时间']:
            value = self.inputs[field_name].text.strip()
            if not value:
                errors.append(f'{field_name}不能为空')
            elif not re.match(date_pattern, value):
                errors.append(f'{field_name}格式错误，应为：XXXX年XX月XX日XX时XX分')
        
        # 验证小数位数
        decimal_fields = ['开仓价格', '回撤幅度', '增仓价格', '增仓价格1', '减仓价格', '减仓价格1', '平仓价格']
        for field_name in decimal_fields:
            value = self.inputs[field_name].text.strip()
            if value:
                try:
                    # 检查是否为数字
                    float_value = float(value)
                    # 检查小数位数
                    if '.' in value:
                        decimal_part = value.split('.')[1]
                        if len(decimal_part) > 2:
                            errors.append(f'{field_name}最多只能有两位小数')
                except ValueError:
                    errors.append(f'{field_name}必须是数字')
        
        # 验证整数
        integer_fields = ['开仓操作周期', '开仓起始边界均线', '预期目标边界均线', '平仓操作周期', '平仓边界均线']
        for field_name in integer_fields:
            value = self.inputs[field_name].text.strip()
            if value:
                try:
                    int(value)
                except ValueError:
                    errors.append(f'{field_name}必须是整数')
        
        # 验证交易方向
        direction_input = self.inputs['交易方向']
        if not direction_input['long'].active and not direction_input['short'].active:
            errors.append('请选择交易方向')
        
        # 验证必填字段
        required_fields = ['品种', '驱动策略', '入场模式', '入场信号', '止损规则', '止盈规则', '开仓情绪', '离场信号', '平仓情绪']
        for field_name in required_fields:
            if not self.inputs[field_name].text.strip():
                errors.append(f'{field_name}不能为空')
        
        # 显示错误信息或成功提示
        if errors:
            error_message = '\n'.join(errors)
            self.show_popup('验证错误', error_message)
        else:
            self.show_popup('成功', '表单提交成功！')
    
    def show_popup(self, title, message):
        """显示弹出窗口"""
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        popup_layout.add_widget(Label(text=message))
        close_button = Button(text='关闭', size_hint_y=None, height=50)
        popup_layout.add_widget(close_button)
        
        popup = Popup(title=title, content=popup_layout, size_hint=(0.8, 0.5))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == '__main__':
    FuturesApp().run()
