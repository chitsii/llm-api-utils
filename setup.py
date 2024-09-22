from setuptools import setup

setup(
    name="llm-api-utils",
    version="0.1.0",
    install_requires=[
        "openai",
        "google-generativeai",
        "anthropic",
        "tenacity",
    ],
    extras_require={
        "develop": []
    },
    entry_points={}
)
