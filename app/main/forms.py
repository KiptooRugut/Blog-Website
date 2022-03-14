from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,RadioField, FileField,TextAreaField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import Required, Length, EqualTo
from ..models import User,Blogs,Comment
from flask_mde import Mde, MdeField

# from flask_ckeditor import CKEditor 
# from flask_ckeditor import CKEditorField


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class FormBlog(FlaskForm):
    title = StringField('Blog Title', validators=[Required(), Length(1, 64)])
    author = StringField('Author : ',)
    category = RadioField('Blog Category :', choices = [('Life, Health & Fitness', 'Life, Health & Fitness'),  ('Fashion', ' Fashion'), ('Sports', 'Sports'),('Tech' , 'Tech')], validators = [Required()])
    content = MdeField() 
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    content = TextAreaField('Leave a comment ...', validators=[Required()])

    submit = SubmitField('Submit')
