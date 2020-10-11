from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticViewSitemap(Sitemap):
    def items(self):
        return [
            "home",
            "about_us",
            "contact_us",
            "gallery",
            "menu_wedding",
            "menu_mitzvah",
            "menu_private",
            "menu_informal",
            "venues",
            "venue_loft_at_passyunk",
            "venue_platform_thirty",
            "venue_beat_street",
            "venue_or_ami",
            "venue_industry",
            "venue_appleford",
        ]

    def location(self, item):
        return reverse(item)
