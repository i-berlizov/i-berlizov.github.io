from flask import Flask, request, jsonify
from datetime import datetime
import os
from flask_cors import CORS
from class_CreateSQL import _SQL
import asyncio
from Bot import send_notification

app = Flask(__name__)
CORS(app)

# Папка для сохранения данных
DATA_FOLDER = "form_data"
os.makedirs(DATA_FOLDER, exist_ok=True)


@app.route('/submit-form', methods=['POST'])
def submit_form():
    try:
        # Получаем данные из формы
        name = request.form.get('name', '')
        phone = request.form.get('phone', '')
        contact_method = request.form.get('contact-method', '')
        message = request.form.get('message', '')

        # Создаем строку с данными
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = f"""
===========================================
Время заявки: {timestamp}
Имя: {name}
Телефон: {phone}
Способ связи: {contact_method}
Сообщение: {message}
===========================================

"""
        asyncio.run(send_notification(data))
        # Сохраняем в файл
        sql = _SQL()
        sql.enter_data(timestamp, name, phone, contact_method, message)
        sql.read_data()
        sql.close_sql()


        return jsonify({
            'status': 'success',
            'message': 'Заявка принята, мы с вами свяжемся!'
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Ошибка: {str(e)}'
        }), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)