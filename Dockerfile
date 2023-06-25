FROM python:3.11

RUN pip install poetry

WORKDIR /bot

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-root

COPY . /bot

CMD python bot/bot.py
