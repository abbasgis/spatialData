import datetime
import logging
import os
import time
import traceback
import uuid


class CommonUtils:

    @classmethod
    def make_dirs(cls, file_path_name: str):
        file_dir, file_name = cls.separate_file_path_name(file_path_name)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

    @classmethod
    def separate_file_path_name(cls, file_path_name: str):
        file_dir = os.path.dirname(file_path_name)
        file_name = os.path.basename(file_path_name)
        return file_dir, file_name

    @classmethod
    def get_file_name_extension(cls, file_name: str) -> (str, str):
        split = file_name.split(".")
        if len(split) == 2:
            return split[0], split[1]
        return file_name, None


class DataLogger:
    @classmethod
    def log_view_error_message(cls, e, request=None, redirect_path=None):
        error_message = str(e)
        cls.log_error_message(e)
        if request:
            if redirect_path is None:
                redirect_path = request.META.get('HTTP_REFERER', '')
                if redirect_path == '':
                    redirect_path = "/"
            return redirect_path

        # response.write(error_message)

    @classmethod
    def log_error_message(cls, e, message_type="error", user_id=None):
        error_message = str(e)
        logger = logging.getLogger()

        logger.error(traceback.format_exc())
        print("error_message: ", error_message)
        # log_data = get_log_data()
        #
        # ActivityLog().log_message(log_data,LogType.Err)
        return error_message  # , act_log.id
