# Assuming pytest and mock are already installed

import os
import sys
import pytest
from unittest.mock import patch, MagicMock

sys.path.append(
    "dwk_hugo"
)  # change this with the path where the module dwk_hugo is stored
from dwk_hugo import hugo_tools

# Given mock values
mock_bucket_name = "bucket_name"
mock_folder_name = "folder_name"
mock_caption = "caption"

mock_wasabi_handler = MagicMock()
mock_wasabi_handler.get_all_objects_with_extensions.return_value = {
    "test.jpg": "image1",
    "test.png": "image2",
}

mock_hugo_toolkit = hugo_tools.HugoToolkit()
mock_hugo_toolkit.handler = mock_wasabi_handler


# Tests start here
class TestHugoToolkit:
    def test_generate_mini_portfolio_from_wasabi(self):
        response = mock_hugo_toolkit.generate_mini_portfolio_from_wasabi(
            mock_bucket_name, mock_folder_name, mock_caption
        )
        assert type(response) == str

    def test_generate_gallery_from_wasabi(self):
        response = mock_hugo_toolkit.generate_gallery_from_wasabi(
            mock_bucket_name, mock_folder_name, mock_caption
        )
        assert type(response) == str

    def test_generate_youtube_embed(self):
        mock_video_id = "123abc"
        response = mock_hugo_toolkit.generate_youtube_embed(mock_video_id)
        assert type(response) == str
        assert mock_video_id in response

    def test_generate_single_image_gallery(self):
        mock_image_file = "image.jpg"
        mock_image_caption = "image_caption"
        response = mock_hugo_toolkit.generate_single_image_gallery(
            mock_image_file, mock_image_caption
        )
        assert type(response) == str
        assert mock_image_file in response
        assert mock_image_caption in response

    def test_generate_gallery_from_list_of_files(self):
        mock_files = ["file1", "file2"]
        response = mock_hugo_toolkit.generate_gallery_from_list_of_files(
            mock_files, mock_caption
        )
        assert type(response) == str
