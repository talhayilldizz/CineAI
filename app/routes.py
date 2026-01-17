from flask import Blueprint, render_template, request, jsonify
from app.ml_manager import MovieReccomender

main=Blueprint('main',__name__)

recommender=MovieReccomender()

@main.route('/', methods=['GET','POST'])
def index():
    movie_list=recommender.movies['original_title'].values

    if request.method == 'POST':
        #kullanıcının yazdığı film
        selected_movie=request.form.get('movie_name')

        #yazdığımız öneri fonksiyonunu çağırdık
        recommendations=recommender.recommend(selected_movie)

        return render_template('result.html',
                               selected_movie=selected_movie,
                               movies=recommendations)
    
    return render_template('index.html', movie_list=movie_list)

@main.route('/get_ai_comment',methods=['POST'])
def get_ai_comment():
    data=request.get_json()
    user_movie=data.get("user_movie")
    target_movie=data.get("target_movie")

    comment=recommender.get_gpt_response(user_movie,target_movie)

    return jsonify({'comment':comment})