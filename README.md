# Icebreaker

A simple implementation of OpenAI and Langchain's ability to easily use third parties to produce internet aware outputs.

In this project, Linkedin is used to produce the summary of a person.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OPENAI_API_KEY`

`PROXYCURL_API_KEY`

`SERPAPI_API_KEY`

## Installation

```bash
pipenv install
```

Use the `.env.example` to create a new `.env` file with your own API keys and secrets.

```bash
pipenv run app.py
```

If you asked for `Soonkwon Hwang` for example, you would get the following output:

```json

```
