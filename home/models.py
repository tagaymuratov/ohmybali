from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import StreamField
from wagtail.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock

class HomePage(Page):
    subpage_types = ["AboutUsPage", "TourCategoryPage"]
    parent_page_types = ['wagtailcore.Page']
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    hero_title = models.CharField(max_length=64, blank=True, null=True)
    hero_subtitle = models.CharField(max_length=128, blank=True, null=True)

    advantage1_img = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    advantage1_title = models.CharField(max_length=64, blank=True, null=True)
    advantage1_text = models.CharField(max_length=128, blank=True, null=True)

    advantage2_img = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    advantage2_title = models.CharField(max_length=64, blank=True, null=True)
    advantage2_text = models.CharField(max_length=128, blank=True, null=True)

    advantage3_img = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    advantage3_title = models.CharField(max_length=64, blank=True, null=True)
    advantage3_text = models.CharField(max_length=128, blank=True, null=True)

    advantage4_img = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    advantage4_title = models.CharField(max_length=64, blank=True, null=True)
    advantage4_text = models.CharField(max_length=128, blank=True, null=True)

    istagram_link = models.URLField(blank=True, null=True)
    whatsapp_link = models.URLField(blank=True, null=True)
    telegram_link = models.URLField(blank=True, null=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("hero_image"),
            FieldPanel("hero_title"),
            FieldPanel("hero_subtitle"),
        ], heading="Hero Section"),
        MultiFieldPanel([
            FieldPanel("advantage1_img"),
            FieldPanel("advantage1_title"),
            FieldPanel("advantage1_text"),
            FieldPanel("advantage2_img"),
            FieldPanel("advantage2_title"),
            FieldPanel("advantage2_text"),
            FieldPanel("advantage3_img"),
            FieldPanel("advantage3_title"),
            FieldPanel("advantage3_text"),
            FieldPanel("advantage4_img"),
            FieldPanel("advantage4_title"),
            FieldPanel("advantage4_text"),
        ], heading="Преймущества"),
        MultiFieldPanel([
            FieldPanel("istagram_link"),
            FieldPanel("whatsapp_link"),
            FieldPanel("telegram_link"),
        ], heading="Социальные сети"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        
        categories_with_tours = []
        categories = TourCategoryPage.objects.live()
        for category in categories:
            tours = (
                category.get_children()
                .type(TourPage)
                .live()
                .specific()
                .order_by("-first_published_at")[:8]
            )

            categories_with_tours.append({
                "category": category,
                "tours": tours
            })
        context["categories_with_tours"] = categories_with_tours

        return context
    
class AboutUsPage(Page):
    subpage_types = []
    parent_page_types = ["HomePage"]
    max_count_per_parent = 1
    body = StreamField([
        ('rtfblock', RichTextBlock(features=[
            "h1","h2","h3","ol","ul","hr","blockquote","superscript","subscript","strikethrough","bold","italic","link"
        ], label="Текст")),
        ('imgblock', ImageChooserBlock(label="Изображение", template="blocks/image_block.html")),
    ], blank=True)
    content_panels = Page.content_panels + [FieldPanel("body")]

class TourPage(Page):
    subpage_types = []
    parent_page_types = ["TourCategoryPage"]

    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    price = models.IntegerField(blank=True, null=True, verbose_name="Цена")
    price_delta = models.IntegerField(blank=True, null=True, verbose_name="Дельта цены для умножения на количество человек")
    max_people = models.IntegerField(blank=True, null=True, verbose_name="Макс. кол-во человек")
    short_desc = models.CharField(max_length=255, blank=True, null=True, verbose_name="Краткое описание")

    text = StreamField([
        ('rtfblock', RichTextBlock(features=[
            "h1","h2","h3","ol","ul","hr","blockquote","superscript","subscript","strikethrough","bold","italic","link"
        ], label="Текст")),
        ('imgblock', ImageChooserBlock(label="Изображение", template="blocks/image_block.html")),
    ], blank=True, null=True, verbose_name="Описание тура")

    photos = StreamField([
        ('imgblock', ImageChooserBlock(label="Изображение", template="blocks/image_block.html")),
    ], blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("price"),
        FieldPanel("price_delta"),
        FieldPanel("max_people"),
        FieldPanel("short_desc"),
        FieldPanel("text"),
        FieldPanel("photos"),
    ]

class TourCategoryPage(Page):
    subpage_types = ["TourPage"]
    parent_page_types = ["HomePage"]

    content_panels = Page.content_panels

    def get_context(self, request):
        context = super().get_context(request)
        
        tours = (
            self.get_children()
            .type(TourPage)
            .live()
            .specific()
            .order_by("-first_published_at")
        )

        context["tours"] = tours
        return context