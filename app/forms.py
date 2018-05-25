from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField, TextAreaField, PasswordField, RadioField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Optional, Length
from app.models import *


class LoginForm(FlaskForm):
    userid = StringField('ID', validators=[DataRequired('ID를 입력해주세요.')])
    password = PasswordField('Password', validators=[DataRequired('비밀번호를 입력해주세요.')])
    remember_me = BooleanField('Remember_me')
    submit = SubmitField('Sign In')

    
class registerForm(FlaskForm):
    userid = StringField('ID', validators=[DataRequired('ID를 입력해주세요.')])
    password = PasswordField('비밀번호', validators=[DataRequired('비밀 번호는 필수 항목입니다.')])
    password_confirm = PasswordField('비밀번호 확인', validators=[DataRequired('비밀번호를 다시 입력해주세요.'), EqualTo('password', message='비밀번호가 일치하지 않습니다.')])
    username = StringField('Username', validators=[DataRequired('이름을 입력해주세요.')])
    terms = BooleanField('이용 약관에 동의합니다.', validators=[DataRequired('약관에 동의해주세요.')])
    submit = SubmitField('가입')

    def validate_userid(self, userid):
        user = User.query.filter_by(user_id = userid.data).first()
        if user is not None:
            raise ValidationError('이미 이 아이디를 가진 사용자가 존재합니다.')


class LocationListFilterForm(FlaskForm):
    """공부 장소 목록을 보여주는 페이지에서, 공부 장소 목록을 분류하는 방법을 선택하는 폼"""
    filter_type = SelectField('별로 보기', default = 'building', choices = [('building', '건물'), ('location-type', '종류')])


class ReviewForm(FlaskForm):
    from app.models import Review
    like_score = RadioField('만족도', validators = [DataRequired('만족도를 선택하세요')],
                    choices = [(i, text) for i, text in enumerate(Review.like_score_to_text)],
                    default = '0'
                )
    crowded_score = RadioField('혼잡도', validators = [DataRequired('혼잡도를 선택하세요')],
                    choices = [(i, text) for i, text in enumerate(Review.crowded_score_to_text)],
                    default = '0'
                )
    comment = TextAreaField('평가', validators = [Optional(), Length(max = 300)])
    submit_save   = SubmitField('저장')
    submit_delete = SubmitField('삭제')

class ReservationForm(FlaskForm):
    group_number = SelectField('사용 인원을 입력해주세요.', coerce = int)
    purpose = TextAreaField('사용 목적을 입력해주세요.', validators = [Optional(), Length(max = 300)])