import setuptools

setuptools.setup(
    name="baseball_news_picker",
    version="1.0",
    author="madoka takagi",
    author_email="mad106.t@gmail.com",
    description="baseball news picker. pick from yahoo sports news.",
    long_description="The game results will be acquired for the Japanese baseball teams such as Chunichi and Swarroese.",
    long_description_content_type="text/markdown",
    url="https://xmadoka.hatenablog.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6.0a3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)