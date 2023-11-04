from dwk_hugo.hugo_tools import (
    HugoToolkit,
    GALLERY_TEMPLATE,
    GALLERY_ITEM_TEMPLATE,
    MINI_PORTFOLIO_TEMPLATE,
    MINI_PORTFOLIO_ITEM_TEMPLATE,
)


def test_generate_gallery_from_wasabi():
    hugo = HugoToolkit()
    result = hugo.generate_gallery_from_wasabi(
        bucket_name="api-upload", folder_name="_steps_", caption="Steps"
    )
    print(result)


def test_generate_mini_portfolio_from_wasabi():
    hugo = HugoToolkit()
    result = hugo.generate_mini_portfolio_from_wasabi(
        bucket_name="api-upload",
        folder_name="makerstoolkit",
        caption="Some random samples from Makers Toolkit",
    )
    print(result)


def test_generate_mini_portfolio_galler001_from_wasabi():
    hugo = HugoToolkit()
    result = hugo.generate_mini_portfolio_from_wasabi(
        bucket_name="api-upload",
        folder_name="gallery001",
        caption="Some random samples from Makers Toolkit",
    )
    print(result)


def test_generate_mini_portfolio_from_wasabi_nine_catastrophes():
    hugo = HugoToolkit()
    result = hugo.generate_mini_portfolio_from_wasabi(
        bucket_name="api-upload",
        folder_name="nine-catastrophes",
        caption="Nine Catastrophes - 4 more to go",
    )
    print(result)


def test_template_gallery_template():
    assert len(GALLERY_TEMPLATE) == 116


def test_template_gallery_item_template():
    assert len(GALLERY_ITEM_TEMPLATE) == 21


def test_template_mini_portfolio_template_template():
    assert len(MINI_PORTFOLIO_TEMPLATE) == 740


def test_template_mini_portfolio_item_template():
    assert len(MINI_PORTFOLIO_ITEM_TEMPLATE) == 422


def test_generate_youtube_embed():
    hugo = HugoToolkit()
    result = hugo.generate_youtube_embed("TaoXJUPTS0w")
    assert (
        result
        == '<p><iframe src="https://www.youtube.com/embed/TaoXJUPTS0w" loading="lazy" frameborder="0" allowfullscreen></iframe></p>'
    )


def test_generate_single_image():
    hugo = HugoToolkit()
    result = hugo.generate_single_image_gallery(
        "https://s3.eu-west-1.wasabisys.com/api-upload/smok/Memories%20of%20the%20Forest.jpg",
        "Step 1",
    )
    assert (
        result
        == """<div class="gallery-box">
  <div class="gallery">
    <img src="https://s3.eu-west-1.wasabisys.com/api-upload/smok/Memories%20of%20the%20Forest.jpg">    
  </div>
  <em>Step 1</em>
</div>"""
    )


def test_generate_gallery_from_list_of_files():
    hugo = HugoToolkit()
    file_url = "https://s3.eu-west-1.wasabisys.com/api-upload/smok/Memories%20of%20the%20Forest.jpg"
    result = hugo.generate_gallery_from_list_of_files(
        [file_url, file_url, file_url], "Step 2"
    )
    print(result)
    found_count = result.count(file_url)
    assert found_count == 3
    assert file_url in result
    assert "Step 2" in result
    assert len(result) == 377


def test_generate_gallery_from_list_of_files_from_local_folder():
    hugo = HugoToolkit()
    file_url = "/images/Bruegel_copy_pencils-1024x685.jpg"
    result = hugo.generate_gallery_from_list_of_files(
        [file_url, file_url, file_url], "Bruegel"
    )
    print(result)
    found_count = result.count(file_url)
    assert found_count == 3
    assert file_url in result
    assert "Bruegel" in result
    assert len(result) == 252
