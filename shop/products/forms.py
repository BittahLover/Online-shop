from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField, BooleanField, TextAreaField, validators, DecimalField

class Addproducts(Form):
    def __init__(
            self,
            formdata=None,
            obj=None,
            prefix="",
            data=None,
            meta=None,
    ):
        super().__init__(formdata, obj, prefix, data, meta)
        self.desc = None

    name = StringField('Name', [validators.DataRequired()])
    price = DecimalField('Price', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock', [validators.DataRequired()])
    description = TextAreaField('Description', [validators.DataRequired()])

    image_1 = FileField('Image 1', validators=[FileAllowed(['jpg','png','gif','jpeg'])])
    image_2 = FileField('Image 2', validators=[FileAllowed(['jpg','png','gif','jpeg'])])
    image_3 = FileField('Image 3', validators=[FileAllowed(['jpg','png','gif','jpeg'])])