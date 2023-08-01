import logging
import os
import tempfile
from datetime import datetime
from dateutil import parser
from io import BytesIO
from typing import Final, Literal, TextIO
from .datetime_pomes import DATETIME_FORMAT_INV
from .env_pomes import APP_PREFIX, env_get_str


def __get_logging_level(level: Literal["debug", "info", "warning", "error", "critical"]) -> int:
    """
    Translate the log severity string *level* into the *logging*'s internal logging severity value.

    :param level: the string log severity
    :return: the internal logging severity value
    """
    result: int | None
    match level:
        case "debug":
            result = logging.DEBUG          # 10
        case "info":
            result = logging.INFO           # 20
        case "warning":
            result = logging.WARN           # 30
        case "error":
            result = logging.ERROR          # 40
        case "critical":
            result = logging.CRITICAL       # 50
        case _:
            result = logging.NOTSET         # 0

    return result


LOGGING_ID: Final[str] = env_get_str(f"{APP_PREFIX}_LOGGING_ID", f"{APP_PREFIX}")
LOGGING_FORMAT: Final[str] = env_get_str(f"{APP_PREFIX}_LOGGING_FORMAT",
                                         "{asctime} {levelname:1.1} {thread:5d} "
                                         "{module:20.20} {funcName:20.20} {lineno:3d} {message}")
LOGGING_STYLE: Final[str] = env_get_str(f"{APP_PREFIX}_LOGGING_STYLE", "{")

LOGGING_FILE_PATH: Final[str] = env_get_str(f"{APP_PREFIX}_LOGGING_FILE_PATH",
                                            os.path.join(tempfile.gettempdir(),
                                                         f"{APP_PREFIX}.log"))
LOGGING_FILE_MODE: Final[str] = env_get_str(f"{APP_PREFIX}_LOGGING_FILE_MODE", "a")

# define and configure the logger
PYPOMES_LOGGER: Final[logging.Logger] = logging.getLogger(LOGGING_ID)

# define the logging severity level
# noinspection PyTypeChecker
LOGGING_LEVEL: Final[int] = __get_logging_level(env_get_str(f"{APP_PREFIX}_LOGGING_LEVEL"))

# configure the logger
# noinspection PyTypeChecker
logging.basicConfig(filename=LOGGING_FILE_PATH,
                    filemode=LOGGING_FILE_MODE,
                    format=LOGGING_FORMAT,
                    datefmt=DATETIME_FORMAT_INV,
                    style=LOGGING_STYLE,
                    level=LOGGING_LEVEL)
for _handler in logging.root.handlers:
    _handler.addFilter(logging.Filter(LOGGING_ID))


def logging_get_entries(errors: list[str],
                        log_level:  Literal["debug", "info", "warning", "error", "critical"] = None,
                        log_from: str = None, log_to: str = None,
                        file_path: str = LOGGING_FILE_PATH) -> BytesIO:
    """
    Extract and return all entries in *PYPOMES_LOGGER*'s logging file.

    The extraction meets the criteria specified by *log_level* and by the inclusive interval *[log_from, log_to]*.

    :param errors: errors eventually generated during execution
    :param log_level: the logging level (defaults to all levels)
    :param log_from: the initial timestamp (defaults to unspecified)
    :param log_to: the finaL timestamp (defaults to unspecified)
    :param file_path: the path of the log file
    :return: the logging entries meeting the specified criteria
    """
    # inicializa variável de retorno
    result: BytesIO | None = None

    # obtain the logging level
    # noinspection PyTypeChecker
    logging_level: int = __get_logging_level(log_level)

    # obtain the initial timestamp
    from_stamp: datetime | None = None
    if log_from is not None:
        from_stamp = parser.parse(log_from)
        if from_stamp is None:
            errors.append(f"Value '{from_stamp}' of 'from' attribute invalid")

    # obtaind the final timestamp
    to_stamp: datetime | None = None
    if log_to is not None:
        to_stamp = parser.parse(log_to)
        if to_stamp is None or \
           (from_stamp is not None and from_stamp > to_stamp):
            errors.append(f"Value '{to_stamp}' of 'to' attribute invalid")

    # does the log file exist ?
    if not os.path.exists(file_path):
        # no, report the error
        errors.append(f"File '{file_path}' not found")

    # any error ?
    if len(errors) == 0:
        # no, proceed
        result = BytesIO()
        with open(file_path) as f:
            line: str = f.readline()
            while line:
                items: list[str] = line.split(maxsplit=3)
                # noinspection PyTypeChecker
                msg_level: int = __get_logging_level(items[2])
                if msg_level >= logging_level:
                    timestamp: datetime = parser.parse(f"{items[0]} {items[1]}")
                    if (from_stamp is None or timestamp >= from_stamp) and \
                       (to_stamp is None or timestamp <= to_stamp):
                        result.write(line.encode())
                line = f.readline()

    return result


def logging_log_msgs(msgs: list[str], output_dev: TextIO = None,
                     log_level: Literal["debug", "info", "warning",
                                        "error", "critical"] = "error",
                     logger: logging.Logger = PYPOMES_LOGGER):
    """
    Write all messages in *msgs* to *PYPOMES_LOGGER*'s logging file, and to *output_dev*.

    The output device is tipically *sys.stdout* ou *sys.stderr*.

    :param msgs: the messages list
    :param output_dev: output device where the message is to be printed (None for no device printing)
    :param log_level: the logging level, defaults to 'error' (None for no logging)
    :param logger: the logger to use
    """
    # define the log writer
    log_writer: callable = None
    match log_level:
        case "debug":
            log_writer = logger.debug
        case "info":
            log_writer = logger.info
        case "warning":
            log_writer = logger.warning
        case "error":
            log_writer = logger.error
        case "critical":
            log_writer = logger.critical

    # traverse the messages list
    for msg in msgs:
        # has the log writer been defined ?
        if log_writer is not None:
            # yes, log the message
            log_writer(msg)

        # the output device has been defined ?
        if output_dev is not None:
            # yes, write the message to it
            output_dev.write(msg)

            # the output device is 'stderr' ou 'stdout' ?
            if output_dev.name.startswith("<std"):
                # yes, skip to the next line
                output_dev.write("\n")