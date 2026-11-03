import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("Aplikasi")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

file_handler = RotatingFileHandler(
    "aplikasi.log",
    maxBytes=1024,
    backupCount=3,
)

file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


def jalankan_aplikasi():
    logger.debug("Aplikasi sedang dimulai.")
    logger.info("Pengguna berhasil masuk.")
    logger.warning("Percobaan login mencurigakan.")
    logger.error("Terjadi kesalahan pada aplikasi.")
    logger.critical("Kesalahan kritis pada sistem.")


if __name__ == "__main__":
    jalankan_aplikasi()
