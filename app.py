from flask import Flask, render_template, request
from api import api_blueprint
from utils import *
import logging

app = Flask(__name__)

app.register_blueprint(api_blueprint)

logging.basicConfig(filename="log.logs", level=logging.DEBUG, filemode="w",
                    format="%(asctime)s [%(levelname)s] %(message)s")


@app.route("/")
def page_main():
    schedule = get_schedule()
    logging.info('Запрос главной страницы ("/")')
    return render_template("index.html", schedule=schedule)


@app.route("/search/")
def page_search():
    query = request.args.get('query')
    schedule = get_schedule_by_word(query)
    logging.info('Запрос страницы поиска ("/search/")')
    return render_template("index.html", schedule=schedule)


@app.route("/schedule/<weekday>")
def page_weekday(weekday):
    schedule = get_schedule_by_day(weekday)
    logging.info(f'Запрос страницы по дню недели ("/schedule/{weekday}")')
    return render_template("index.html", schedule=schedule)


@app.route("/schedule/tomorrow/")
def page_tomorrow_schedule():
    schedule = get_schedule_for_tomorrow()
    logging.info('Запрос страницы с расписанием на завтра ("/schedule/tomorrow/")')
    return render_template("index.html", schedule=schedule)


@app.route("/schedule/today/")
def page_today_schedule():
    schedule = get_schedule_for_today()
    logging.info('Запрос страницы с расписанием на сегодня ("/schedule/today/")')
    return render_template("index.html", schedule=schedule)


@app.errorhandler(404)
def not_found_error(error):
    return "Error 404, такой страницы не существует"


@app.errorhandler(500)
def internal_error(error):
    return "Error 500, ошибка сервера"


if __name__ == '__main__':
    app.run()
