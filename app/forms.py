from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember_me')
    submit = SubmitField('Sign In')

    
class reviewForm(FlaskForm):
    reviewname = StringField('제목', validators=[DataRequired()])
    like_score = SelectField('선호도 점수', validators=[DataRequired('별점을 선택해주세요.')],
                    choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]
                    )
    crowded_score =  SelectField('혼잡도 점수', validators=[DataRequired('별점을 선택해주세요.')],
                    choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]
                    )   
    content = TextAreaField('내용', validators=[DataRequired('내용을 입력해주세요.')],
                description={'placeholder': '내용을 20자 이내로 입력해주세요.'}
                )
    submit = SubmitField('제출')


