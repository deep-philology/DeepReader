import os
import shutil


COMMONS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))


def create_dir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)
        print(f"created {dirname}")


def copy_files(filenames, input_dir, output_dir):
    for filename in filenames:
        input_filename = os.path.join(input_dir, filename)
        output_filename = os.path.join(output_dir, filename)
        shutil.copy(input_filename, output_filename)
        print(f"copied {output_filename}")


def copy_css(filenames, output_dir):
    copy_files(filenames, os.path.join(COMMONS_DIR, "css"), output_dir)


def copy_js(filenames, output_dir):
    copy_files(filenames, os.path.join(COMMONS_DIR, "js"), output_dir)
