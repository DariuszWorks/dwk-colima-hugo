import os

from dotenv import load_dotenv
from dwk_wasabi.wasabi_handler import WasabiHandler

CAPTION_MARKER = "###CAPTION###"

URL_MARKER = "###URL###"

YOUTUBE_TEMPLATE = """<p><iframe src="https://www.youtube.com/embed/###YOUTUBE_VIDEO_ID###" loading="lazy" frameborder="0" allowfullscreen></iframe></p>"""

SINGLE_IMAGE_GALLERY_TEMPLATE = """<div class="gallery-box">
  <div class="gallery">
    <img src="###IMAGE_FILE###">    
  </div>
  <em>###IMAGE_CAPTION###</em>
</div>"""

GALLERY_TEMPLATE = """
<div class="gallery-box">
  <div class="gallery">
    ###GALLERY_ITEMS###
  </div>
  <em>###CAPTION###</em>
</div>
"""

GALLERY_ITEM_TEMPLATE = """<img src="###URL###">"""

MINI_PORTFOLIO_ITEM_TEMPLATE = """<div class="col col-4 col-d-6 col-t-12">
          <div class="portfolio__item">
            <a href="###URL###" class="portfolio__link glightbox" data-glightbox='title: ; description: ; descPosition: bottom;'>
              <span class="portfolio__icon"><i class="ion ion-ios-eye"></i></span>
              <img data-src="###URL###" class="portfolio__image lazy" alt="">
            </a>
            </div>
        </div>"""

MINI_PORTFOLIO_TEMPLATE = """

<section class="section portfolio">
  <div class="container">
    <div class="row">
      <div class="col col-12">
        <div class="section__head">
          <h2 class="section__title">###CAPTION###</h2>
          <div class="portfolio__view">
            <div class="portfolio__toggle">
              <div class="icon">
                <div class="icon-bar"></div>
                <div class="icon-bar"></div>
                <div class="icon-bar"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="portfolio__gallery animate">
    <div class="container">
      <div class="row">
        ###MINI_PORTFOLIO_ITEMS###
      </div>
    </div>
  </div>
</section>
"""

load_dotenv()


class HugoToolkit:
    """

    HugoToolkit
    ===========

    This class provides a set of methods for generating various types of content using the WasabiHandler.

    Methods
    -------
    __init__()
        Initializes an instance of HugoToolkit with AWS credentials.

    generate_mini_portfolio_from_wasabi(bucket_name, folder_name, caption)
        Generates a mini portfolio HTML snippet using images from the Wasabi bucket.

    Parameters:
        - bucket_name: str
            The name of the Wasabi bucket.
        - folder_name: str
            The name of the folder containing the images.
        - caption: str
            The caption for the mini portfolio.

    Returns:
        str
            The HTML snippet for the mini portfolio.

    generate_gallery_from_wasabi(bucket_name, folder_name, caption)
        Generates a gallery HTML snippet using images from the Wasabi bucket.

    Parameters:
        - bucket_name: str
            The name of the Wasabi bucket.
        - folder_name: str
            The name of the folder containing the images.
        - caption: str
            The caption for the gallery.

    Returns:
        str
            The HTML snippet for the gallery.

    generate_youtube_embed(youtube_video_id)
        Generates an HTML snippet for embedding a YouTube video.

    Parameters:
        - youtube_video_id: str
            The YouTube video ID.

    Returns:
        str
            The HTML snippet for embedding the YouTube video.

    generate_single_image_gallery(image_file, image_caption)
        Generates an HTML snippet for a single image gallery.

    Parameters:
        - image_file: str
            The URL or file path of the image.
        - image_caption: str
            The caption for the image.

    Returns:
        str
            The HTML snippet for the single image gallery.

    generate_gallery_from_list_of_files(files, caption)
        Generates a gallery HTML snippet using a list of image files.

    Parameters:
        - files: list[str]
            A list of URLs or file paths of the images.
        - caption: str
            The caption for the gallery.

    Returns:
        str
            The HTML snippet for the gallery.

    """

    def __init__(self):
        """
        Method to initialize the class object.

        This method sets up the necessary credentials for the AWS service. It retrieves the
        AWS access key ID and secret access key from the environment variables and uses them
        to create an instance of the WasabiHandler class.

        Parameters:
            None

        Returns:
            None
        """
        aws_access_key_id = os.environ.get("ACCESS_KEY_ID")
        aws_secret_access_key = os.environ.get("SECRET_ACCESS_KEY")
        self.handler = WasabiHandler(
            access_key_id=aws_access_key_id, secret_access_key=aws_secret_access_key
        )

    def generate_mini_portfolio_from_wasabi(self, bucket_name, folder_name, caption):
        """
        Generate a mini portfolio from images stored in Wasabi.

        :param bucket_name: The name of the bucket in Wasabi.
        :param folder_name: The name of the folder within the bucket.
        :param caption: The caption to be displayed in the portfolio.
        :return: A string representing the generated mini portfolio.
        """
        result = []
        images_dict_1 = self.handler.get_all_objects_with_extensions(
            bucket_name=bucket_name, extension=".jpg"
        )
        images_dict_2 = self.handler.get_all_objects_with_extensions(
            bucket_name=bucket_name, extension=".png"
        )
        images_dict = {**images_dict_1, **images_dict_2}
        for key, value in images_dict.items():
            if f"/{folder_name}/" in key:
                result.append(MINI_PORTFOLIO_ITEM_TEMPLATE.replace(URL_MARKER, key))
        return MINI_PORTFOLIO_TEMPLATE.replace(
            "###MINI_PORTFOLIO_ITEMS###", "".join(result)
        ).replace(CAPTION_MARKER, caption)

    def generate_gallery_from_wasabi(self, bucket_name, folder_name, caption):
        """
        Generate a gallery from images stored in Wasabi.

        :param bucket_name: The name of the bucket in Wasabi.
        :param folder_name: The name of the folder within the bucket containing the images.
        :param caption: The caption to be displayed for the gallery.
        :return: The generated gallery as a string.

        Example usage:
            gallery = generate_gallery_from_wasabi("mybucket", "images", "My Image Gallery")
        """
        result = []
        images_dict_1 = self.handler.get_all_objects_with_extensions(
            bucket_name=bucket_name, extension=".jpg"
        )
        images_dict_2 = self.handler.get_all_objects_with_extensions(
            bucket_name=bucket_name, extension=".png"
        )
        images_dict = {**images_dict_1, **images_dict_2}
        for key, value in images_dict.items():
            if f"/{folder_name}/" in key:
                result.append(GALLERY_ITEM_TEMPLATE.replace("###URL###", key))
        return GALLERY_TEMPLATE.replace(
            "###GALLERY_ITEMS###", "\n".join(result)
        ).replace("###CAPTION###", caption)

    def generate_youtube_embed(self, youtube_video_id):
        """
        Generates a YouTube embed HTML code for the given video id.

        :param youtube_video_id: The YouTube video id.
        :return: The YouTube embed HTML code.
        """
        return YOUTUBE_TEMPLATE.replace("###YOUTUBE_VIDEO_ID###", youtube_video_id)

    def generate_single_image_gallery(self, image_file, image_caption):
        """
        Generates a single image gallery.

        :param image_file: The file path of the image.
        :type image_file: str
        :param image_caption: The caption to be displayed for the image.
        :type image_caption: str
        :return: The generated single image gallery.
        :rtype: str
        """
        return SINGLE_IMAGE_GALLERY_TEMPLATE.replace(
            "###IMAGE_FILE###", image_file
        ).replace("###IMAGE_CAPTION###", image_caption)

    def generate_gallery_from_list_of_files(self, files, caption):
        """
        Generate a gallery from a list of file URLs.

        :param files: A list of file URLs.
        :param caption: Caption for the gallery.
        :return: Generated gallery HTML as a string.
        """
        result = []
        for file in files:
            result.append(GALLERY_ITEM_TEMPLATE.replace("###URL###", file))
        return GALLERY_TEMPLATE.replace(
            "###GALLERY_ITEMS###", "\n".join(result)
        ).replace("###CAPTION###", caption)
