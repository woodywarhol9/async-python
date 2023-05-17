from odmantic import Model


class BookModel(Model):
    keyword: str
    publisher: str
    discount: int
    image: str

    # MongoDB의 구조 : Database -> collections -> Documents
    class Config:
        collection = "book-collector"
