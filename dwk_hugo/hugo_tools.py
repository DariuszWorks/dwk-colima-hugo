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
    def __init__(self):
        aws_access_key_id = os.environ.get("ACCESS_KEY_ID")
        aws_secret_access_key = os.environ.get("SECRET_ACCESS_KEY")
        self.handler = WasabiHandler(
            access_key_id=aws_access_key_id, secret_access_key=aws_secret_access_key
        )

    def generate_mini_portfolio_from_wasabi(self, bucket_name, folder_name, caption):
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
        return YOUTUBE_TEMPLATE.replace("###YOUTUBE_VIDEO_ID###", youtube_video_id)

    def generate_single_image_gallery(self, image_file, image_caption):
        return SINGLE_IMAGE_GALLERY_TEMPLATE.replace(
            "###IMAGE_FILE###", image_file
        ).replace("###IMAGE_CAPTION###", image_caption)

    def generate_gallery_from_list_of_files(self, files, caption):
        result = []
        for file in files:
            result.append(GALLERY_ITEM_TEMPLATE.replace("###URL###", file))
        return GALLERY_TEMPLATE.replace(
            "###GALLERY_ITEMS###", "\n".join(result)
        ).replace("###CAPTION###", caption)
