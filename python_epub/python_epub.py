"""Converts all epub files in ressources folder to pdf."""

import os
import traceback

from enum import StrEnum
from epub2pdf import EpubPdfConverter


WORKDIR = os.getcwd()
RESSOURCES = os.path.join(WORKDIR, "ressources")
OUTPUT = os.path.join(WORKDIR, "output")


class PageLayout(StrEnum):
    SINGLE_PAGE = "SinglePage"
    ONE_COLUMN = "OneColumn"
    TWO_COLUMN_LEFT = "TwoColumnLeft"
    TWO_COLUMN_RIGHT = "TwoColumnRight"
    TWO_PAGE_LEFT = "TwoPageLeft"
    TWO_PAGE_RIGHT = "TwoPageRight"


class PageMode(StrEnum):
    USE_NONE = "UseNone"
    USE_OUTLINES = 'UseOutlines'
    USE_THUMBS = 'UseThumbs'
    USE_FULLSCREEN = 'FullScreen'
    USE_OC = 'UseOC'
    USE_ATTACHEMENTS = 'UseAttachments'


class Direction(StrEnum):
    L2R = "L2R"
    R2L = "R2L"


def main() -> None:
    ensure_ressources()
    for epub_path in find_ressources(".epub"):
        print(f"Converting {epub_path}...")
        converter = EpubPdfConverter(
            epub_path,
            OUTPUT,
            PageLayout.SINGLE_PAGE,
            PageMode.USE_FULLSCREEN,
            Direction.L2R,
        )

        try:
            converter.convert()
            print("Done.")

        except Exception:
            print("Error :", traceback.format_exc())


def ensure_ressources() -> None:
    if "ressources" not in os.listdir(WORKDIR):
        raise FileNotFoundError(f"{WORKDIR} does not contain any ressources")

    if "output" not in os.listdir(WORKDIR):
        os.mkdir(os.path.join(WORKDIR, "output"))


def find_ressources(ext: str = ".epub") -> list[str]:
    return [
        os.path.join(RESSOURCES, file)
        for file in os.listdir(RESSOURCES)
        if file.endswith(ext)
    ]


if __name__ == "__main__":
    main()
